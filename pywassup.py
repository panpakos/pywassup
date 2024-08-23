import sys
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
gi.require_version("WebKit", "6.0")
from gi.repository import Gtk, Adw, WebKit


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_title("whatsapp")
        self.set_default_size(800, 600)
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box)
        self.webview = WebKit.WebView()
        self.webview.load_uri("https://web.whatsapp.com/")
        self.webview.set_vexpand(True)
        self.box.append(self.webview)


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
