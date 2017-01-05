import kivy
kivy.require('1.9.1') # keep current kivy version up to date!

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView

import os

class LyaTreatmentsApp(App):
    def build(self):
#        main_view = MainView()
#        resized_view = ModalView(size=(320, 640))
#        resized_view.add_widget(main_view)
#        return resized_view.open()

if __name__ == '__main__':
    LyaTreatments().run()
