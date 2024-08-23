import sys
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
gi.require_version("WebKit", "6.0")
from gi.repository import Gtk, Adw, Gio, GLib, WebKit


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_default_size(800, 600)
        self.set_title("pywassup")

        # Main layout
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box1)
        self.webview = WebKit.WebView()
        self.webview.load_uri("https://web.whatsapp.com/")
        self.webview.set_vexpand(True)
        self.box1.append(self.webview)

        # Create headerbar
        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)

        # Create a new menu
        menu = Gio.Menu.new()

        # Create a popover
        self.popover = Gtk.PopoverMenu()
        self.popover.set_menu_model(menu)

        # Create a menu button
        self.button = Gtk.MenuButton()
        self.button.set_popover(self.popover)
        self.button.set_icon_name("open-menu-symbolic")

        # Add menu button to the header bar
        self.header.pack_end(self.button)

        # set app name
        GLib.set_application_name("pywassup")

        # Add an about dialog
        action = Gio.SimpleAction.new("about", None)
        action.connect("activate", self.show_about)
        self.add_action(action)
        menu.append("About", "win.about")

        app = self.get_application()
        sm = app.get_style_manager()
        sm.set_color_scheme(Adw.ColorScheme.PREFER_DARK)

    def show_about(self, action, param):
        self.about = Gtk.AboutDialog()
        self.about.set_transient_for(self)
        self.about.set_modal(self)

        self.about.set_authors(["Pakos"])
        self.about.set_copyright("Copyright 2024 Pakos")
        self.about.set_license_type(Gtk.License.GPL_3_0)
        self.about.set_website("https://github.com/panpakos/pywassup")
        self.about.set_website_label("pywassup")
        self.about.set_version("0.1")
        self.about.set_logo_icon_name("help-about")

        self.about.show()


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
