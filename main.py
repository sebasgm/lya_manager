import os

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
from KivyCalendar import CalendarWidget

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models_db import User, Base, engine # Import created objects for connecting
                                         #with existing DB

# Sessions handling by attaching each session to an existing engine
DBSession = sessionmaker(bind=engine) # once engine is available
DBSession.configure()

# For start communicating with the database each time it is required
session = DBSession()

# EXAMPLE: Adding and updating objects
test_user = User(name='sebasgm', fullname='Sebastian Garcia Marra', password='pass')
session.add(test_user)
our_user = session.query(User).filter_by(name='sebasgm').first()

print "Hello 2017!!!!"
print our_user.fullname

# ==============================================================================

#class MainView(BoxLayout):
class LyaApp(App):

    def build(self):

        def new_patient_callback(instance, value):
            print('My button <%s> state is <%s>' % (instance, value))

        main_win = BoxLayout(orientation='vertical') # Kind of layout that
                                              #automatically places its
                                              #children in a row

        search_field = TextInput(font_size=30, size_hint_y=None, height=48, text='Buscar')

        #f = FloatLayout()
        #s = Scatter()
        calendar = CalendarWidget()
        new_patient_button = Button(text='Nuevo paciente', font_size=18)
        treatment_button = Button(text='tratamientos', font_size=18)

        new_patient_button.bind(on_press=new_patient_callback)

        #l = Label(text='default',font_size=150)

        #search_field.bind(text=l.setter('text')) # By binding any function to TextInput
                                       #one could add special behavior on many
                                       #aspects to test inputs

        #f.add_widget(s)
        #s.add_widget(l)

        main_win.add_widget(search_field)
        main_win.add_widget(calendar)
        main_win.add_widget(new_patient_button)
        main_win.add_widget(treatment_button)



        return main_win

#class LyaApp(App):
#    def build(self):
#        main_view = MainView()
#        resized_view = ModalView(size=(320, 640))
#        resized_view.add_widget(main_view)
#        return resized_view.open()

if __name__ == '__main__':
    LyaApp().run()
