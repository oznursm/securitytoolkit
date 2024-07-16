import gi
import functions as func

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="AĞ GÜVENLİĞİ ARAÇ KİTİ")
        self.set_border_width(10)

        grid = Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button(label="Mac Adresi Değiştir")
        button1.connect("clicked", self.on_mac_change_clicked)
        grid.attach(button1, 0, 0, 1, 1)

        button2 = Gtk.Button(label="Bilgi Toplama")
        button2.connect("clicked", self.on_info_gathering_clicked)
        grid.attach(button2, 1, 0, 1, 1)

        button3 = Gtk.Button(label="Ağ Taramaları")
        button3.connect("clicked", self.on_nmap_scan_clicked)
        grid.attach(button3, 2, 0, 1, 1)

        button4 = Gtk.Button(label="SearchSploit")
        button4.connect("clicked", self.on_searchsploit_clicked)
        grid.attach(button4, 0, 1, 1, 1)

        button5 = Gtk.Button(label="Nikto Tarama")
        button5.connect("clicked", self.on_niktoscan_clicked)
        grid.attach(button5, 1, 1, 1, 1)

        button6 = Gtk.Button(label="Görsel Analiz(Exiftool)")
        button6.connect("clicked", self.on_exiftool_clicked)
        grid.attach(button6, 2, 1, 1, 1)

        button7 = Gtk.Button(label="Wordpress Tarama")
        button7.connect("clicked", self.on_wordpress_clicked)
        grid.attach(button7, 0, 2, 1, 1)

        button8 = Gtk.Button(label="Wordlist Oluşturma")
        button8.connect("clicked", self.on_wordlist_clicked)
        grid.attach(button8, 1, 2, 1, 1)

        button9 = Gtk.Button(label="Rustscan")
        button9.connect("clicked", self.on_rustscan_clicked)
        grid.attach(button9, 2, 2, 1, 1)

        button10 = Gtk.Button(label="TCPDump")
        button10.connect("clicked", self.on_tcpdump_clicked)
        grid.attach(button10, 0, 3, 1, 1)

        button11 = Gtk.Button(label="Docker ile OpenVAS")
        button11.connect("clicked", self.on_docker_openvas_clicked)
        grid.attach(button11, 1, 3, 1, 1)

        button12 = Gtk.Button(label="Docker ile Ollama")
        button12.connect("clicked", self.on_docker_ollama_clicked)
        grid.attach(button12, 2, 3, 1, 1)

    def on_mac_change_clicked(self, widget):
        func.getMac()

    def on_info_gathering_clicked(self, widget):
        func.infoinfo()

    def on_nmap_scan_clicked(self, widget):
        func.nmapscan()

    def on_searchsploit_clicked(self, widget):
        func.searchsploit()

    def on_niktoscan_clicked(self, widget):
        func.niktoscan()

    def on_exiftool_clicked(self, widget):
        func.exiftool()

    def on_wordpress_clicked(self, widget):
        func.wordpress()

    def on_wordlist_clicked(self, widget):
        func.wordlist()

    def on_rustscan_clicked(self, widget):
        func.rustscan()

    def on_tcpdump_clicked(self, widget):
        func.tcpdump()

    def on_docker_openvas_clicked(self, widget):
        func.docker_openvas()

    def on_docker_ollama_clicked(self, widget):
        func.docker_ollama()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

