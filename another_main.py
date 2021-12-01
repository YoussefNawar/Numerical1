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
        """
            useless function
            shows how to get variables from the calc.kv 'you can consider it somehow an html file
        """
        print(text)
        self.ids.dropdown.select(text)

    def evaluate(self, inputText, selection):
        # TODO: do something useful
        print(inputText, selection)
        self.ids.answerField.text = inputText + " " + selection

    def upload(self):
        pass


class CalculatorApp(App):
    def build(self):
        return CustomDropDown()


if __name__ == '__main__':
    CalculatorApp().run()
