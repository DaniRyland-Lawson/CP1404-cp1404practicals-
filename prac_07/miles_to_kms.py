from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty


class MilesToKlms(App):
    def build(self):
        Window.size = (200, 400)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kms.kv')
        return self.root

    def handle_convert(self, value):
        """ handle calculation """
        result = value ** 2
        self.root.ids.output_label.text = str(result)


MilesToKlms().run()
