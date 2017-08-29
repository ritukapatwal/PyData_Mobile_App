from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.factory import Factory
from functools import partial

import webbrowser


class ScreenAbout(Screen):
    Builder.load_string('''
<ScreenAbout>
    spacing: dp(9)
    name: 'ScreenAbout'
    ScrollView
        id: scroll
        ScrollGrid
            AsyncImage
                id: imgbt
                allow_stretch: True
                size_hint_y: None
                height: dp(200)
            BackLabel
                backcolor: app.base_active_color[:3] + [.5]
                id: comm_desc
            FloatLayout
                size_hint_y: None
                height: dp(45)
                ActiveButton
                    id: but
                    text: "Visit our website"
                    size_hint: None, None
                    width: dp(200)
                    center_x: comm_desc.center_x
                    top: comm_desc.y - dp(10)
                ActiveButton
                    size_hint: None, None
                    width: dp(200)
                    center_x: comm_desc.center_x
                    top: but.y - dp(10)
                    text: 'Fork me on Github.'
                    on_release: import webbrowser; webbrowser.open('https://github.com/pydata/PyData_Mobile_App/')
    ActiveButton
        text: 'An OpenSource initiative by Quanon Tech'
        font_size: dp(27)
        bold: True
        on_release:
            import webbrowser; webbrowser.open('http://quanontech.com')
        ''')

    def on_pre_enter(self):
        self.ids.scroll.opacity = 0

    def on_enter(self, onsuccess=False):
        from network import get_data
        about = get_data('about', onsuccess=onsuccess)

        if not about:
            return

        about = about.get('0.0.1')[0]
        imbt = self.ids.imgbt
        imbt.source = about['logo']
        self.ids.but.on_released = partial(webbrowser.open, about['website'])

        self.ids.comm_desc.text = about['about']

        Factory.Animation(opacity=1, d=.5).start(self.ids.scroll)