from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder


class TicTacToeKivyView(App):
    """The tic-tac-toe Kivy view"""

    def build(self):
        self.error_text = ""
        self.input_text = ""
        self.footer_text = ""
        self.root = ""
        self.title = 'TicTacToe'
        self.root = root = RootWidget()
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size





Builder.load_string('''
<BoxLayout>
    orientation: 'vertical'

<RootWidget>
    Label:
        text: self.input_text
        halign: 'center'
        valign: 'top'
    GridLayout:
        size_hint: .9, .9
        pos_hint: {'center_x': .5, 'center_y': .5}
        rows:3
        Button:
            text: " "

        Button:
            text: " "
    
        Button:
            text: " "
            
        Button:
            text: " "

        Button:
            text: " "
    
        Button:
            text: " "

        Button:
            text: " "

        Button:
            text: " "
    
        Button:
            text: " "
    Label:
        text: self.footer_text
        valign: 'middle'
        halign: 'center'
''')


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)


if __name__ == '__main__':
    TicTacToeKivyView().run()


#        self.add_widget(Label(text="This is a title", valign: 'centre'))
#
#        cb = CustomBtn()
#        cb.bind(pressed=self.btn_pressed)
#        self.add_widget(cb)
#
#        self.add_widget(Button(text='btn 2'))
#
#    def btn_pressed(self, instance, pos):
#        print('pos: printed from root widget: {pos}'.format(pos=pos))


# class CustomBtn(Widget):
#    pressed = ListProperty([0, 0])
#
#    def on_touch_down(self, touch):
#        if self.collide_point(*touch.pos):
#            self.pressed = touch.pos
#            # we consumed the touch. return False here to propagate
#            # the touch further to the children.
#            return True
#        return super(CustomBtn, self).on_touch_down(touch)
#
#    def on_pressed(self, instance, pos):
#        print('pressed at {pos}'.format(pos=pos))