# -*- coding: utf-8 -*-
###########################################################
#------ GNU GPL2 -----------------------------------------#
###########################################################
# вынес в отдельный класс окно about, вызываемое в меню программы


#открытие диалога about
def on_clk_about(self, widget):
    about = gtk.AboutDialog()
    about.set_program_name("Посчиталка")
    about.set_version("0.1")
    about.set_copyright("(c) М.Томилов")
    about.set_comments("Эта небольшая программа предназначена для подсчета и вывода статистики по тексту")
    about.set_website("http://le087.ru")
    # about.set_logo(gtk.gdk.pixbuf_new_from_file("battery.png"))
    about.run()
    about.destroy()

