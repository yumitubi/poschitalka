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



        #создаем VBOX
        vbox = gtk.VBox(False, 3)

        
        ############################################
        #--------------рисуем меню------------------#
        menub = gtk.MenuBar()
        #меню файл
        filemenu = gtk.Menu()
        filem = gtk.MenuItem("Файл")
        filem.set_submenu(filemenu)
        #пункт меню открыть
        openf = gtk.MenuItem("Открыть файл")
        filemenu.append(openf)
        #пункт меню открыть
        savestat = gtk.MenuItem("Сохранить статистику")
        filemenu.append(savestat)
        #пункт меню выход
        close = gtk.MenuItem("Выход")
        close.connect("activate", gtk.main_quit)#по нажатии закрываем программу
        filemenu.append(close)#добавляем в меню пункт выход

        #меню справка 
        helpmenu = gtk.Menu()
        helper = gtk.MenuItem("Справка")
        helper.set_submenu(helpmenu)
        #пункт меню справка
        helperitem = gtk.MenuItem("Справка")
        helpmenu.append(helperitem)
        #пункт меню о программе
        about = gtk.MenuItem("О программе")
        helpmenu.append(about)


        #добавляем созданные меню в меню бар
        menub.append(filem)
        menub.append(helper)


        #################################################
        #-------------------кнопки-----------------------#
        btn_close = gtk.Button("Выход")#рисуем кнопку выход, тем не менее, для нее еще нужен будет обработчик
        btn_close.connect("clicked", gtk.main_quit)#обрабатываем клик на кнопку, как закрытие окна
        btn_close.set_tooltip_text("Нажмите, чтобы выйти из программы")


        #добавляем менюбар в vbox
        vbox.pack_start(menub, False, False, 0)
        vbox.pack_end(btn_close, False, False, 5)


#        fixed = gtk.Fixed()#создаем контейнер
#        fixed.put(btn_close, 470, 415)#указываем координаты для кнопки
#        fixed.put(menub, 0, 0)
        
        self.add(vbox)#добавляем vbox в окно
        self.show_all()#даем команду все показать




#выполняем то, что определили функциями выше
PyApp()
gtk.main()

