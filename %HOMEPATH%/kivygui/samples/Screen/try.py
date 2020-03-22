import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('mykv.kv')

class Home(Screen):
    pass

class tryapp(App):
    def build(self):
        return Home()
tryapp().run()
