# -*- coding: utf-8 -*-
###########################################################
#------ GNU GPL2 -----------------------------------------#
###########################################################



#подключаем библиотеку pygtk и gtk
import pygtk
pygtk.require('2.0')
import gtk, sys
import os
import string






#######################################################
#основной класс, на основе которого рисуется интерфейс#
#######################################################
class poschitalka(gtk.Window):

    def __init__(self):
        #непонятно, что мы тут делаем
        super(poschitalka, self).__init__()


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


        ##################################################
        #-------------------кнопки-----------------------#
        btn_close = gtk.Button("Выход")#рисуем кнопку выход, тем не менее, для нее еще нужен будет обработчик
        btn_close.connect("clicked", gtk.main_quit)#обрабатываем клик на кнопку, как закрытие окна
        btn_close.set_tooltip_text("Нажмите, чтобы выйти из программы")
        btn_close.set_size_request(65, 30)
        #сохранить статистику
        btn_save_stat = gtk.Button("Сохранить статистику")
        btn_save_stat.set_tooltip_text("Нажмите, что бы сохранить статистику по тексту в файл")
        btn_save_stat.set_size_request(190, 30)

        #создаем область для прокручивания
        scroolwin = gtk.ScrolledWindow()
        scroolwin.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
                
        #окно для редактирования текста
        wins = gtk.TextView()
        wins.set_editable(True)#разрешаем редактировать текс в текстовом поле
        wins.modify_fg(gtk.STATE_NORMAL, gtk.gdk.Color(5140, 5140, 5140))
        wins.set_cursor_visible(True)#разрешаем отображать курсор
        wins.set_wrap_mode(gtk.WRAP_WORD)#устанавливаем в текстовом буфере перенос по словам
        #table.attach(wins, 0, 2, 1, 3, gtk.FILL | gtk.EXPAND, gtk.FILL | gtk.EXPAND, 1, 1)
        #прописываем окно просмотра текста в прокручиваемой области
        scroolwin.add(wins)


        
        #вывод статистики
        titlestat = gtk.Label("Статистика текста:")
        
        #статус бар
        statusbar = gtk.Statusbar()
        statusbar.push(1, "Ready")
        


        #таблица для разметки содержимого
        table = gtk.Table(10, 8, True)
        table.set_row_spacings(4)#устанавливаем расстояния между строчками таблицы
        table.set_col_spacings(4)#устанавливаем расстояния между столбцами таблицы
        table.attach(menualign, 0, 8, 0, 1, gtk.FILL, gtk.FILL, 1, 1)
        table.attach(btn_close, 7, 8, 9, 10, gtk.EXPAND, gtk.EXPAND, 1, 1)#добавляем кнопку close
        table.attach(scroolwin, 0, 5, 1, 9, gtk.FILL, gtk.FILL, 1, 1)#добавляем текстовое поле
        table.attach(halign, 5, 8, 1, 2, gtk.FILL, gtk.FILL, 0, 0)#добавляем выравнивание в таблице
        table.attach(btn_save_stat, 4, 7, 9, 10, gtk.EXPAND, gtk.EXPAND, 1, 1)#добавляем кнопку сохранить статистику


        #добавляем менюбар в vbox
#        vbox.pack_start(menub, False, False, 0)
#        vbox.pack_start(wins, True, True, 0)
#        vbox.pack_start(table, False, False, 5)
#        vbox.pack_end(statusbar, False, False, 0)


#        fixed = gtk.Fixed()#создаем контейнер
#        fixed.put(btn_close, 470, 415)#указываем координаты для кнопки
#        fixed.put(menub, 0, 0)
        
        self.add(table)#добавляем table в окно
        self.show_all()#даем команду все показать


    
class appmenu():
    
    def drawmenu():
        #############################################
        #--------------рисуем меню------------------#
        menub = gtk.MenuBar()
        #меню файл
        filemenu = gtk.Menu()
        filem = gtk.MenuItem("Файл")
        filem.set_submenu(filemenu)
        
        #создаем объект диалога открытия файла
        dialogof = opfile()
        

        #пункт меню открыть
        openf = gtk.MenuItem("Открыть файл")
        openf.connect("activate", dialogof.on_clk_open)
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
        about.connect("activate", self.on_clk_about)#диалог О программе


        #добавляем созданные меню в меню бар
        menub.append(filem)
        menub.append(helper)


        #выравнивание

        halign = gtk.Alignment(0, 0, 0, 0)
        halign.add(titlestat)
        menualign = gtk.Alignment(0, 0, 0, 0)
        menualign.add(appmenu())


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




#класс по работе с диалогом открытия файла
class opfile():
    #диалог открытия файла
    def on_clk_open(self, widget):
        openfile = gtk.FileSelection("Открыть файл")
        openfile.run()
        p = open(openfile.get_filename, 'r')
        per = p.readline()
        print p
        openfile.destroy()
    


#выполняем то, что определили функциями выше
poschitalka()
opfile()
gtk.main()

