from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class MilesToKilometres(App):
    output_file = StringProperty
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kms.kv')
        return self.root

    def handle_convert(self, text):
        """handle calculation """
        print("handle calculation")
        miles = self.convert_to_number(text)
        self.update_results(miles)

    def handle_add(self, text, change):
        """handle button press up and down"""
        print("handle adding")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles = str(miles)

    def update_result(self, miles):
        print("update")
        self.output_km = str(miles * 1.60934)

    @staticmethod
    def convert_to_number(text):
        try:
            value = float(text)
            return value
        except ValueError:
            return 0.0


MilesToKilometres().run()
