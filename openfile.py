# -*- coding: utf-8 -*-
###########################################################
#------ GNU GPL2 -----------------------------------------#

import pygtk
pygtk.require('2.0')
import gtk, sys

def whatnamefile():
    namefile = openfile.get_filename()    
    return namefile

    #диалог открытия файла
def on_clk_open(poschitalka):
    openfile = gtk.FileSelection("Открыть файл")
    openfile.run()
    itog = openfile.ok_button.connect("clicked", whatnamefile)
    openfile.destroy()
    poschitalka.wins.set_buffer(itog)

