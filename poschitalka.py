# -*- coding: utf-8 -*-
###########################################################
#------ GNU GPL2 ------------------------------------------
###########################################################



#подключаем библиотеку pygtk и gtk
#imporЗt pygtk
#pygtk.require('2.0')
import gtk, sys


#
class PyApp(gtk.Window):
    def __init__(self):
        #непонятно, что мы тут делаем
        super(PyApp, self).__init__()
        
        self.set_title("Poschitalka")#обзываем заголовок
        self.set_size_request(250,150)#размеры окна
        self.set_position(gtk.WIN_POS_CENTER)#ставим окно по центру
        
        self.connect("destroy", gtk.main_quit)#обработчик кнопки на закрытие окна

        self.show()#даем команду все показать

#выполняем то, что определили функциями выше
PyApp()
gtk.main()
