import os

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

import solutions
from solutions import *

# Set the app size
# Window.size = (500, 700)
# Window.clearcolor = (255/255, 255/255, 255/255, 1)
# Designate Our .kv design file 
Builder.load_file('calc.kv')


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

    def show_load_list(self):
        content = LoadDialog(load=self.load_list, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load a file list", content=content, size_hint=(0.5, 0.5))
        self._popup.open()

    def load_list(self, path, filename):
        pass

    def dismiss_popup(self):
        self._popup.dismiss()
    pass


class CustomDropDown(BoxLayout):
    state = False
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

    def selection(self, text):
        if text == 'Bisection':
            self.ids.x2.opacity = 1
            self.ids.x2TextArea.opacity = 1
            self.ids.gxInputField.opacity = 0
            self.ids.gx.opacity = 0
        elif text == 'Regula falsi':
            self.ids.x2.opacity = 1
            self.ids.x2TextArea.opacity = 1
            self.ids.gxInputField.opacity = 0
            self.ids.gx.opacity = 0
        elif text == 'Fixed point':
            self.ids.x2.opacity = 0
            self.ids.x2TextArea.opacity = 0
            self.ids.gxInputField.opacity = 1
            self.ids.gx.opacity = 1
        elif text == 'Newton Raphhsen':
            self.ids.x2.opacity = 0
            self.ids.x2TextArea.opacity = 0
            self.ids.gxInputField.opacity = 0
            self.ids.gx.opacity = 0
        else:
            self.ids.x2.opacity = 1
            self.ids.x2TextArea.opacity = 1
            self.ids.gxInputField.opacity = 0
            self.ids.gx.opacity = 0
        self.ids.dropdown.select(text)

    def evaluate(self, inputText, selection, x1, x2, gx, maxIteration, precision):
        if selection is 'Bisection':
            self.ids.answerField.text = str(solutions.bisection(inputText,int(x2),int(x1)))
        elif selection is 'Regula falsi':
            self.ids.answerField = str(solutions.falsi(inputText, int(x2), int(x1)))
        elif selection is 'Fixed point':
            self.ids.answerField = str(solutions.fixed(inputText,int(gx), int(x2)))
        elif selection is 'Newton Raphhsen':
            self.ids.answerField = str(solutions.Newton(inputText,int(x1)))
        else:
            self.ids.answerField = str(solutions.secant(inputText,int(x1),int(x2)))
    def upload(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def dismiss_popup(self):
        self._popup.dismiss()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])):
            print(path,filename)
        self.dismiss_popup()


class CalculatorApp(App):
    def build(self):
        return CustomDropDown()


if __name__ == '__main__':
    app = CalculatorApp()
    app.run()