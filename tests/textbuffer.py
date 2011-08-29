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


#определяем глобальные переменные
#текстовый буфер
txtbuf = gtk.TextBuffer()

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


        self.set_title("test с текстовым буфером")#обзываем заголовок
        self.set_size_request(650,550)#размеры окна
        self.set_position(gtk.WIN_POS_CENTER)#ставим окно по центру
        self.connect("destroy", gtk.main_quit)#обработчик кнопки на закрытие окна


        ##################################################
        #-------------------кнопки----------------------#
        btn_close = gtk.Button("Выход")#рисуем кнопку выход, тем не менее, для нее еще нужен будет обработчик
        btn_close.connect("clicked", gtk.main_quit)#обрабатываем клик на кнопку, как закрытие окна

        
        #тестовая кнопка
        btn_test = gtk.Button("Изменить значение буфера")
        btn_test.connect("clicked", self.replacetb)
        #создаем область для прокручивания
        scroolwin = gtk.ScrolledWindow()
        scroolwin.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        
        #создаем текстовый буфер для помещения туда текста
        txtbuf.set_text('test')
        
        
        #окно для редактирования текста
        wins = gtk.TextView()
        wins.set_editable(True)#разрешаем редактировать текс в текстовом поле
        wins.modify_fg(gtk.STATE_NORMAL, gtk.gdk.Color(5140, 5140, 5140))
        wins.set_cursor_visible(True)#разрешаем отображать курсор
        wins.set_wrap_mode(gtk.WRAP_WORD)#устанавливаем в текстовом буфере перенос по словам
        wins.set_buffer(txtbuf)
        #table.attach(wins, 0, 2, 1, 3, gtk.FILL | gtk.EXPAND, gtk.FILL | gtk.EXPAND, 1, 1)
        #прописываем окно просмотра текста в прокручиваемой области
        scroolwin.add(wins)

        #таблица для разметки содержимого
        table = gtk.Table(10, 8, True)
        table.set_row_spacings(4)#устанавливаем расстояния между строчками таблицы
        table.set_col_spacings(4)#устанавливаем расстояния между столбцами таблицы
        table.attach(btn_close, 7, 8, 9, 10, gtk.EXPAND, gtk.EXPAND, 1, 1)#добавляем кнопку close
        table.attach(scroolwin, 0, 5, 1, 9, gtk.FILL, gtk.FILL, 1, 1)#добавляем текстовое поле
        table.attach(btn_test, 3, 4, 9, 10, gtk.EXPAND, gtk.EXPAND, 1, 1)#добавляем кнопку test


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

    def replacetb():
        txtbuf.set_text('получилось')

#выполняем то, что определили функциями выше
poschitalka()
gtk.main()

