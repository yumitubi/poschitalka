# -*- coding: utf-8 -*-
###########################################################
#------ GNU GPL2 -----------------------------------------#
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


#если вдруг надумаю показать иконку        
#        try:
#            self.set_icon_from_file("web.png")
#        except Exception, e:
#            print e.message
#            sys.exit(1)


        self.set_title("Посчиталка")#обзываем заголовок
        self.set_size_request(550,450)#размеры окна
        self.set_position(gtk.WIN_POS_CENTER)#ставим окно по центру
        
        self.connect("destroy", gtk.main_quit)#обработчик кнопки на закрытие окна
        
        btn_close = gtk.Button("Выход")#рисуем кнопку выход, тем не менее, для нее еще нужен будет обработчик
        btn_close.connect("clicked", gtk.main_quit)#обрабатываем клик на кнопку, как закрытие окна
        
        btn_close.set_tooltip_text("Нажмите, чтобы выйти из программы")
        fixed = gtk.Fixed()#создаем контейнер
        fixed.put(btn_close, 470,415)#указываем координаты для кнопки

        
        self.add(fixed)#добавляем контейнер в окно
        self.show_all()#даем команду все показать




#выполняем то, что определили функциями выше
PyApp()
gtk.main()

