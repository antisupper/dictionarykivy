from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

age = ''
name = ''

class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lbl1 = Label(text= 'Enter the name:', halign='right')
        self.in_name =TextInput(multiline=False)
        lbl2 = Label(text='Enter the age:', halign='right')
        self.in_age = TextInput(multiline=False)
        self.btn = Button(text= 'Start', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line1)
        outer.add_widget(line2)
        self.add_widget(outer)



class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr(name='home'))
        return sm
    
app = MyApp()
app.run()