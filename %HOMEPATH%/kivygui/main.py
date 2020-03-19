import kivy

 
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.image import Image


Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '791')

# load file from kv file
Builder.load_file('./kivycss.kv')
# The Properties classes are used 
# when you create an EventDispatcher. 
from kivy.properties import NumericProperty
from kivy.garden.graph import MeshLinePlot
  
# BoxLayout arranges children in a vertical or horizontal box.  
# or help to put the children at the desired location.  
  
# he Clock object allows you to 
# schedule a function call in the future 
from kivy.clock import Clock 
class ScreenHOME(Screen):
    pass

 
class ScreenDATA(Screen):
    def update(self):
        # plot graph
        pass
    


class ScreenREPAIR(Screen):
    number = NumericProperty()
    def start(self): 
          
        Clock.unschedule(self.increment_time)
        # increament tiem every num seconds now is one second for test purpose
        Clock.schedule_interval(self.increment_time, 1)
    def increment_time(self, interval): 
        self.number += 1


  


# class ScreenButton(Button):
#     screenmanager = ObjectProperty()
#     def on_press(self, *args):
#         super(ScreenButton, self).on_press(*args)
#         self.screenmanager.current = 'whatever'
 
# The ScreenManager controls moving between screens
screen_manager = ScreenManager()
 
# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(ScreenHOME(name="screen_home"))
screen_manager.add_widget(ScreenDATA(name="screen_data"))
screen_manager.add_widget(ScreenREPAIR(name="screen_repair"))
 
class KivyTut2App(App):
 
    def build(self):
        return screen_manager
    
 
sample_app = KivyTut2App()
sample_app.run()
