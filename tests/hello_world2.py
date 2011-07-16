# -*- coding: utf-8 -*-

#Hello World!

#подключаем библиотеку pygtk и gtk
import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld2:
    def callback(self, widget, data):
        print "Hello again - %s was pressed" % data

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Hello Buttons!")
        self.window.connect("delete_event", self.delete_event)
        self.window.set_border_width(10)
        self.box1 = gtk.HBox(False, 0)
        self.window.add(self.box1)
        self.button1 = gtk.Button("Button 1")
        self.button1.connect("clicked",self.callback, "button 1")
        self.box1.pack_start(self.button1, False, False, 3)
        self.button1.show()
        self.button2 = gtk.Button("Button 2")
        self.button2.connect("clicked", self.callback, "button 2")
        self.box1.pack_start(self.button2, False, False, 3)
        
        self.button2.show()
        self.box1.show()
        self.window.show()

def main():
    gtk.main()
    

if __name__ == "__main__":
    hello = HelloWorld2()
    main()

