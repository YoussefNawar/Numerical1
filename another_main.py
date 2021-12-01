from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

# Set the app size
# Window.size = (500, 700)
# Window.clearcolor = (255/255, 255/255, 255/255, 1)
# Designate Our .kv design file 
Builder.load_file('calc.kv')


class CustomDropDown(BoxLayout):
    state = False

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

    def evaluate(self, inputText, selection):
        print(inputText, selection)
        self.ids.answerField.text = inputText + " " + selection

    def upload(self):
        pass


class CalculatorApp(App):
    def build(self):
        return CustomDropDown()


if __name__ == '__main__':
    CalculatorApp().run()
