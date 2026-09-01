from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label

class CarApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        self.car_image=Image(source='Bmw.png')
        self.add_widget(self.car_image)
        self.label=Label(text='BMW', size_hint=(1,0.2))
        self.add_widget(self.label)
        btns=BoxLayout(size_hint=(1,0.3))
        for name,file in [('BMW','Bmw.png'),('Bugatti','Bugatti.png'),('Koenigs','Koenigs.png'),('Thar','Thar.png')]:
            b=Button(text=name)
            b.bind(on_press=lambda x,f=file,n=name: self.change(f,n))
            btns.add_widget(b)
        self.add_widget(btns)
    def change(self,f,n):
        self.car_image.source=f
        self.label.text=n

class KonfigaarApp(App):
    def build(self):
        return CarApp()
KonfigaarApp().run()
