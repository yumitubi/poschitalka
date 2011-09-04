# -*- coding: utf-8 -*-
###########################################################
#------ GNU GPL2 -----------------------------------------#

import pygtk
pygtk.require('2.0')
import gtk, sys

#открытие диалога about
def on_clk_about(poschitalka):
    about = gtk.AboutDialog()
    about.set_program_name("Посчиталка")
    about.set_version("0.11 alfa")
    about.set_copyright("(c) М.Томилов")
    about.set_comments("Эта небольшая программа предназначена для подсчета и вывода статистики по тексту")
    about.set_website("http://le087.ru")
    # about.set_logo(gtk.gdk.pixbuf_new_from_file("battery.png"))
    about.run()
    about.destroy()

