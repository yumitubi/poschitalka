# -*- coding: utf-8 -*-
###########################################################
#------ GNU GPL2 -----------------------------------------#

import pygtk
pygtk.require('2.0')
import gtk, sys

def whatnamefile():

    """узнаем имя файла"""
    namefile = openfile.get_filename()    
    txtbuf.set_text(namefile)

    
    #диалог открытия файла
def on_clk_open(poschitalka):

    """открытие файла"""
    openfile = gtk.FileSelection("Открыть файл")
    openfile.run()
    openfile.ok_button.connect("clicked", whatnamefile)
    openfile.destroy()
    

def replacetb(test, btn_test):

    """ Данная функция заливает в текстовый буфер текст из файла"""
    test = 'получилось'
    txtbuf.set_text(test)

