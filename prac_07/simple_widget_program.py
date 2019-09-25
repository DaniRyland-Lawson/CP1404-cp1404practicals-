"""CP1404 - Programming II Simple Widget program - from scratch"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class SimpleWidget(App):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_of_names = ["Dani", "Tyler", "Ashlee", "Luna", "Dobby", "Justin"]

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Simple Widget"
        self.root = Builder.load_file("simple_widgets.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.list_of_names:
            temp_button = Button(text=name, id=name)
            # temp_button.bind(on_release=self.update_result)
            self.root.ids.entries_box.add_widget(temp_button)


SimpleWidget().run()
