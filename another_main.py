import os
import json
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

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

    def printAnswer(self, iterationList, x):
        pass

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
        if selection == 'Bisection':
            iterations, x = solutions.bisection(inputText, int(x1), int(x2))
        elif selection == 'Regula falsi':
            iterations, x = solutions.falsi(inputText, int(x1),int(x2))
        elif selection == 'Fixed point':
            iterations, x = solutions.fixed(inputText, gx, int(x1))
        elif selection == 'Newton Raphhsen':
            iterations, x = solutions.Newton(inputText, int(x1))
        else:
            iterations, x = solutions.secant(inputText, int(x1),int(x2))
        self.ids.answerField.text = str(iterations) + str(x)

    def upload(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def dismiss_popup(self):
        self._popup.dismiss()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])):
            f = open(filename[0])
            data = json.load(f)
            for i in data["Problem_Details"]:
                print(i)
                fx = i.get('f(x)')
                Selection = i.get("Selection")
                x1 = i.get("x1")
                x2 = i.get("x2")
                gx = i.get("g(x)")
                maxIteration = i.get("MaxIteration")
                precision = i.get("precision")
                self.evaluate(fx, Selection, x1, x2, gx, maxIteration, precision)
        self.dismiss_popup()


class CalculatorApp(App):
    def build(self):
        return CustomDropDown()


if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
