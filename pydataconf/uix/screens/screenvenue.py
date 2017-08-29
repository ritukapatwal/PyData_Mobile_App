'''ScreenSponsor:
Display all the information about venue.
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.garden.mapview import MapView
from kivy.garden.mapview import MapMarker

class ScreenVenue(Screen):
    
    Builder.load_string('''
<ScreenVenue>
    name: 'ScreenVenue'
    BoxLayout
        spacing: dp(13)
        orientation: 'vertical'
        padding: dp(4)
        BoxLayout
            orientation: 'vertical'
            SingleLineLabel:
                text: app.venue_name
                halign: 'center'
                size_hint_y: None
                height: dp(25)
            AsyncImage:
                id: img_venue
                source: 'atlas://data/default/venue'
                allow_stretch: True
                keep_ratio: True
        Splitter
            sizable_from: 'top'
            MapView:
                zoom: 11
                lat: 28.5456282
                lon: 77.2731505 
                MapMarker
                    lat: 28.5456282
                    lon: 77.2731505
        BoxLayout:
            size_hint: 1, None
            height: dp(45)
            spacing: dp(13)
            padding: dp(4)
            Widget
                # this is a space holder
            # ActiveButton:
            #     text: 'Open Street View'
            ActiveButton:
                text: 'Get Directions'
                on_release:
                    import webbrowser
                    webbrowser.open("https://www.google.co.in/maps/dir/''/IIIT+Delhi/@28.5456102,77.2031102,12z/data=!3m1!4b1!4m8!4m7!1m0!1m5!1m1!1s0x390ce3e564daac1d:0x2c582e340e7bc556!2m2!1d77.2731505!2d28.5456282") 
''')

