import kivy
kivy.require('1.9.0')
 
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

class ScreenHOME(Screen):
    pass
 
class ScreenDATA(Screen):
    pass

class ScreenREPAIR(Screen):
    pass

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