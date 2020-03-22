from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.core.text import Label as CoreLabel
from kivy.lang.builder import Builder
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
import serial
from tkinter import *


class CircularProgressBar(ProgressBar):

    def __init__(self, **kwargs):
        super(CircularProgressBar, self).__init__(**kwargs)

        # Set constant for the bar thickness
        self.thickness = 50

        # Create a direct text representation
        self.label = CoreLabel(text="0%", font_size=self.thickness)

        # Initialise the texture_size variable
        self.texture_size = None

        # Refresh the text
        self.refresh_text()

        # Redraw on innit
        self.draw()

    def draw(self):

        with self.canvas:

            # Empty canvas instructions
            self.canvas.clear()

            # Draw no-progress circle
            Color(0.26, 0.26, 0.26)
            Ellipse(pos=self.pos, size=self.size)

            # Draw progress circle, small hack if there is no progress (angle_end = 0 results in full progress)
            Color(1, 0, 0)
            Ellipse(pos=self.pos, size=self.size,
                    angle_end=(0.001 if self.value_normalized == 0 else self.value_normalized*360))

            # Draw the inner circle (colour should be equal to the background)
            Color(0, 0, 0)
            Ellipse(pos=(self.pos[0] + self.thickness / 2, self.pos[1] + self.thickness / 2),
                    size=(self.size[0] - self.thickness, self.size[1] - self.thickness))

            # Center and draw the progress text
            Color(1, 1, 1, 1)
            Rectangle(texture=self.label.texture, size=self.texture_size,
                      pos=(self.size[0]/2 - self.texture_size[0]/2, self.size[1]/2 - self.texture_size[1]/2))

    def refresh_text(self):
        # Render the label
        self.label.refresh()

        # Set the texture size each refresh
        self.texture_size = list(self.label.texture.size)

    def set_value(self, value):
        # Update the progress bar value
        self.value = value

        # Update textual value and refresh the texture
        self.label.text = str(int(self.value_normalized*100)) + "%"
        self.refresh_text()

        # Draw all the elements
        self.draw()


class ProxApp(App):

    
    # Update with values
    def update(self, dt):
       global filter, eps
       #
       # idle routine
       #
       WINDOW = 600 # window size
       eps = 0.9 # filter time constant
       filter = 0.0 # filtered value
       nloop = 100.0 # number of loops accumulated
       amp = 25.0 # difference amplitude
       port = sys.argv[1]
       maximum = 10
        #
        # open serial port
        #
       ser = serial.Serial(port,9600)
       ser.setDTR()

       byte2 = 0
       byte3 = 0
       byte4 = 0
       ser.flush()
       while 1:
          #
          # find framing 
          #
          byte1 = byte2
          byte2 = byte3
          byte3 = byte4
          byte4 = ord(ser.read())
          if ((byte1 == 1) & (byte2 == 2) & (byte3 == 3) & (byte4 == 4)):
             break
       on_low = ord(ser.read())
       on_high = ord(ser.read())
       on_value = (256*on_high + on_low)/nloop
       off_low = ord(ser.read())
       off_high = ord(ser.read())
       off_value = (256*off_high + off_low)/nloop
       filter = (1-eps)*filter + eps*amp*(on_value-off_value)
       self.root.set_value(filter/maximum)
    
    def build(self):
        container = Builder.load_string(
                '''CircularProgressBar:
        size_hint: (None, None)
        pos_hint: {'center_y': 0.5, 'center_x': 0.5}
        height: 500
        width: 500
        max: 80''')

        # Update the progress bar
        Clock.schedule_interval(self.update, 0.1)
        return container


if __name__ == '__main__':
    ProxApp().run()