import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas, NavigationToolbar2Kivy
# ignore the above warning... it is stated in the libary that this would happen... kivy...
from kivy.uix.button import Button

import kivy.properties as props
from bargraph import fig, fig2
from kivy.clock import Clock 
from kivy.uix.boxlayout import BoxLayout

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '791')

# load file from kv file
Builder.load_file('./kivycss.kv')

fig, ax = plt.subplots()
fig2, ax2 = plt.subplots()
canvas = fig.canvas
canvas2 = fig2.canvas

class ScreenHOME(Screen):
    pass
 
class ScreenData(Screen):
    bar = props.ObjectProperty(None)
    def __init__(self, name, *args, **kwargs):
        super(ScreenData, self).__init__(*args, **kwargs)
        self.name = name
        self.build()
        
    def build(self):
        f1 = BoxLayout(orientation="vertical")
        nav1 = NavigationToolbar2Kivy(canvas)
        nav2 = NavigationToolbar2Kivy(canvas2)
        f1.add_widget(nav1.actionbar)
        f1.add_widget(canvas)
        f1.add_widget(nav2.actionbar)
        f1.add_widget(canvas2)
        self.add_widget(f1)
        # plot graph

class ScreenREPAIR(Screen):
    number = props.NumericProperty()
    def start(self): 
        Clock.unschedule(self.increment_time)
        # increament time every num seconds now is one second for test purpose
        Clock.schedule_interval(self.increment_time, 1)
    def increment_time(self, interval): 
        self.number += 1

screen_manager = ScreenManager()
screen_manager.add_widget(ScreenHOME(name="screen_home"))
screen_manager.add_widget(ScreenData(name="screen_data"))
screen_manager.add_widget(ScreenREPAIR(name="screen_repair"))
 
class KivyTut2App(App):
    def build(self):
        return screen_manager

sample_app = KivyTut2App()
sample_app.run() 