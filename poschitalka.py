# -*- coding: utf-8 -*-
###########################################################
#------ GNU GPL2 -----------------------------------------#
###########################################################
#------ Autor by Mak Tomilov(c)2011-----------------------#
###########################################################


#####################################
# подключаем библиотеку pygtk и gtk
#####################################     
try:
     import sys, pygtk
     pygtk.require('2.0')
     
except:
     print 'Не удалось импортировать модуль PyGTK'
     sys.exit(1)

import gtk, sys 
import os
import string

####################################
# подключаем самописанные модули
######################################
import aboutpunkt # диалог about

#################################
#определяем глобальные переменные
###################################

#текстовый буфер
txtbuf = gtk.TextBuffer()
#создаем текстовый буфер для помещения туда текста
txtbuf.set_text('')

# переменные для статистики текста
titlestat = gtk.Label("Статистика текста для файла: ")
sum_char_spase_label = gtk.Label("Количество символов\nс пробелами: ")
sum_char_label = gtk.Label("Количество символов\nбез пробелов: ")
average_word = gtk.Label("Средняя длина\nслова: ")
average_word_in_sentence = gtk.Label("Среднее количество\nслов в предложении: ")
average_sentence_in_parag = gtk.Label("Среднее количество\nпредложений в абзаце: ")
paragraph = gtk.Label("Количество\nабзацев: ")
words = gtk.Label("Количество слов\nв тексте: ")

#######################################################
# основной класс, на основе которого рисуется интерфейс#
#######################################################
class poschitalka(gtk.Window):

    def __init__(self):
        #непонятно, что мы тут делаем
        super(poschitalka, self).__init__()

# если вдруг надумаю показать иконку        
#        try:
#            self.set_icon_from_file("web.png")
#        except Exception, e:
#            print e.message
#            sys.exit(1)

        self.set_title("Посчиталка")#обзываем заголовок
        self.set_size_request(650,550)#размеры окна
        self.set_position(gtk.WIN_POS_CENTER)#ставим окно по центру
        self.connect("destroy", gtk.main_quit)#обработчик кнопки на закрытие окна

        #############################################
        # рисуем меню
        menub = gtk.MenuBar()

        # меню файл
        filemenu = gtk.Menu()
        filem = gtk.MenuItem("Файл")
        filem.set_submenu(filemenu)
        
        # пункт меню открыть
        openf = gtk.MenuItem("Открыть файл")
        openf.connect("activate", FileSelectionNum().on_clk_open)
        filemenu.append(openf)

        # пункт меню сохранить статистику
        savestat = gtk.MenuItem("Сохранить статистику")
        filemenu.append(savestat)

        # пункт меню выход
        close = gtk.MenuItem("Выход")
        close.connect("activate", gtk.main_quit)#по нажатии закрываем программу
        filemenu.append(close)#добавляем в меню пункт выход

        # меню справка 
        helpmenu = gtk.Menu()
        helper = gtk.MenuItem("Справка")
        helper.set_submenu(helpmenu)

        # пункт меню справка
        helperitem = gtk.MenuItem("Справка")
        helpmenu.append(helperitem)

        #########################################
        # пункт меню о программе
        # создаем объект класса aboutm
        about = gtk.MenuItem("О программе")
        helpmenu.append(about)
        about.connect("activate", aboutpunkt.on_clk_about)#диалог О программе

        # добавляем созданные меню в меню бар
        menub.append(filem)
        menub.append(helper)

        ##################################################
        # кнопки
        btn_close = gtk.Button("Выход")#рисуем кнопку выход, тем не менее, для нее еще нужен будет обработчик
        btn_close.connect("clicked", gtk.main_quit)#обрабатываем клик на кнопку, как закрытие окна
        btn_close.set_tooltip_text("Нажмите, чтобы выйти из программы")
        btn_close.set_size_request(65, 30)

        # сохранить статистику
        btn_save_stat = gtk.Button("Сохранить статистику")
        btn_save_stat.set_tooltip_text("Нажмите, что бы сохранить статистику по тексту в файл")
        btn_save_stat.set_size_request(190, 30)
        btn_save_stat.connect("clicked", SaveStat().save_stat_txt)
        
        # тестовая кнопка
        btn_test = gtk.Button("Открыть файл")
        btn_test.connect("clicked", FileSelectionNum().on_clk_open)
        btn_test.set_size_request(130, 30)
        
        # подсчет статистики
        btn_stat = gtk.Button("Подсчитать")
        btn_stat.connect("clicked", SymbolCalculate().push_all)
        btn_stat.set_size_request(100, 30)

        # создаем область для прокручивания
        scroolwin = gtk.ScrolledWindow()
        scroolwin.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        
        # окно для редактирования текста
        wins = gtk.TextView()
        wins.set_editable(True)#разрешаем редактировать текс в текстовом поле
        wins.modify_fg(gtk.STATE_NORMAL, gtk.gdk.Color(5140, 5140, 5140))
        wins.set_cursor_visible(True)#разрешаем отображать курсор
        wins.set_wrap_mode(gtk.WRAP_WORD)#устанавливаем в текстовом буфере перенос по словам
        wins.set_buffer(txtbuf)

        # прописываем окно просмотра текста в прокручиваемой области
        scroolwin.add(wins)


        #################################        
        # вывод статистики
        ##################################        
        
        # статус бар
        statusbar = gtk.Statusbar()
        statusbar.push(1, "Ready")
        
        # выравнивание
        halign = gtk.Alignment(0, 0, 0, 0)
        halign.add(titlestat)
        halign_paragr = gtk.Alignment(0, 0, 0, 0)
        halign_paragr.add(paragraph)
        halign_sum_char_out = gtk.Alignment(0, 0, 0, 0)
        halign_sum_char_out.add(sum_char_spase_label)
        halign_sum_char_with = gtk.Alignment(0, 0, 0, 0)
        halign_sum_char_with.add(sum_char_label)
        halign_average_word = gtk.Alignment(0, 0, 0, 0)
        halign_average_word.add(average_word)
        halign_average_word_in_sentence = gtk.Alignment(0, 0, 0, 0)
        halign_average_word_in_sentence.add(average_word_in_sentence)
        halign_sentence_in_parag = gtk.Alignment(0, 0, 0, 0)
        halign_sentence_in_parag.add(average_sentence_in_parag)
        halign_words = gtk.Alignment(0, 0, 0, 0)
        halign_words.add(words)
        menualign = gtk.Alignment(0, 0, 0, 0)
        menualign.add(menub)
        menualign

        #таблица для разметки содержимого
        table = gtk.Table(10, 8, True)
        table.set_row_spacings(4)#устанавливаем расстояния между строчками таблицы
        table.set_col_spacings(4)#устанавливаем расстояния между столбцами таблицы
        table.attach(menualign, 0, 8, 0, 1, gtk.FILL, gtk.FILL, 1, 1)
        table.attach(btn_close, 7, 8, 9, 10, gtk.EXPAND, gtk.EXPAND, 1, 1)#добавляем кнопку close
        table.attach(scroolwin, 0, 5, 1, 9, gtk.FILL, gtk.FILL, 1, 1)#добавляем прокручиваемое поле
        table.attach(halign, 5, 8, 1, 2, gtk.FILL, gtk.FILL, 0, 0)# надпись статистика текста
        table.attach(halign_sum_char_with, 5, 8, 2, 3, gtk.FILL, gtk.FILL, 0, 0)#надпись количество символов с пробелами
        table.attach(halign_sum_char_out, 5, 8, 3, 4, gtk.FILL, gtk.FILL, 0, 0)#надпись количество символов без пробелов
        table.attach(halign_average_word, 5, 8, 4, 5, gtk.FILL, gtk.FILL, 0, 0)#среднее количество букв в слове
        table.attach(halign_average_word_in_sentence, 5, 8, 5, 6, gtk.FILL, gtk.FILL, 0, 0)#среднее количество слов в предложении
        table.attach(halign_sentence_in_parag, 5, 8, 6, 7, gtk.FILL, gtk.FILL, 0, 0)#среднее количество предложений в абзаце
        table.attach(halign_paragr, 5, 8, 7, 8, gtk.FILL, gtk.FILL, 0, 0)#количество абзацев
        table.attach(halign_words, 5, 8, 8, 9, gtk.FILL, gtk.FILL, 0, 0)#количество слов
        table.attach(btn_save_stat, 4, 7, 9, 10, gtk.EXPAND, gtk.EXPAND, 1, 1)#добавляем кнопку сохранить статистику
        table.attach(btn_test, 3, 4, 9, 10, gtk.EXPAND, gtk.EXPAND, 1, 1)#добавляем кнопку test
        table.attach(btn_stat, 1, 3, 9, 10, gtk.EXPAND, gtk.EXPAND, 1, 1)#добавляем кнопку

        ################################################
        # вывод созданных объектов на экран
        self.add(table)#добавляем table в окно
        self.show_all()#даем команду все показать

#####################################################
# класс, который подсчитывает статистику по тексту
####################################################        
class SymbolCalculate:

    def push_all(label, w):
        # количество символов с пробелами
        sum_ch = str(txtbuf.get_char_count())
        sum_char_spase_label.set_text("Количество символов\nс пробелами: "+sum_ch)
        # число абзацев
        sum_par = str(txtbuf.get_line_count())
        paragraph.set_text('Количество\nабзацев: '+sum_par)
        
        # количество символов без пробелов
        # считает все символы кроме пробела, табуляции и перевода каретки
        summ_chars_out_space = 0 # устанавливаем счетчик символов в 0
        end_buf = 1 # флаг для проверки, конец буфера или нет
        iter = txtbuf.get_start_iter() # создаем курсор
        while end_buf:
             proverka = iter.is_end() # возвращает значение true, если курсор находится в конце буфера
             if proverka == False:
                  char = iter.get_char() # получает символ под курсором
                  if char <> ' ' and char <> '\n' and char <> '\t': # проверяем, является ли он пробелом, табом либо ентером 
                       summ_chars_out_space = summ_chars_out_space + 1 # если нет, приплюсовываем к общему количеству символов
                       iter.forward_char() # перемещаем курсор на один символ вперед
                  else:
                       iter.forward_char() # иначе если это пробел, таб или ентер, просто передвигаем курсор на один символ вперед
                       
             else:
                  end_buf = 0 # иначе, если курсор в конце буфера, то ставим флаг в 0, что бы прервать цикл
        sum_char_label.set_text("Количество символов\nбез пробелов: "+str(summ_chars_out_space)) # записываем в нужное поле

        # количество слов в тексте
        # работает похожим образом, как и кол-во слов без пробелов
        iter = txtbuf.get_start_iter()
        summ_words = 0
        end_buf = 1
        while end_buf:
             proverka = iter.is_end()
             if proverka == False:
                  if iter.starts_word(): # проверяем, находится ли курсор в начале слова
                      summ_words = summ_words + 1 # если да, то плюсум счетчик
                      iter.forward_word_end()     # и переходим в конец слова
                  else:
                      iter.forward_char() # если нет, просто переходим на один символ вперед до следующего начала слова
             else:
                  end_buf = 0
        words.set_text("Количество слов\nв тексте: "+str(summ_words))          

        # среднее количество символов в слове
        # описание алгоритма:
        # алгоритм получился развесистый и немного сложный, но тем не менее, работает
        # следущим образом:
        # в начале, как и в алгоритмах выше, сначала устанавливаем курсор в начале буфера,
        # затем идет проверка на нахождение курсора вконце буфера, далее мы проверяем, находится
        # ли курсор в начале слова. Если да, то устанавливаем flag = 1 и двигаем курсор на символ вперед,
        # если нет то проверяем значение флага. Если флаг=1 и находится в конце слова, плюсуем счетчик,
        # устанавливаем флаг в 0 и двигаемся на символ вперед. Если флаг = 1, и курсор не находится
        # в конце слова, то просто плюсуем счетчик и сдвигаемся на символ вперед. Иначе, если
        # курсор не находится на начале слова и флаг не установлен в 1, то просто двигаемся на символ
        # вперед. Таким образом мы считаем только символы, заключенные между началом и концом слова
        iter = txtbuf.get_start_iter()
        summ_chars_av = 0
        end_buf = 1
        flag = 0
        while end_buf:
             proverka = iter.is_end()
             if proverka == False:
                  if iter.starts_word():
                      flag = 1 
                      summ_chars_av = summ_chars_av + 1
                      iter.forward_char()
                  else:
                      if flag:
                           if iter.ends_word():
                                flag = 0
                                summ_chars_av = summ_chars_av + 1
                                iter.forward_char()
                           else:
                                summ_chars_av = summ_chars_av + 1
                                iter.forward_char()
                      else:
                           iter.forward_char()
             else:
                  end_buf = 0
        if summ_words == 0:
             average_word.set_text("Средняя длина\nслова: 0")
        else:
             average_word.set_text("Средняя длина\nслова: "+str(summ_chars_av/summ_words))       
                  
        # среднее количество слов в предложении     
        # считаем количество предложение в тексте     
        iter = txtbuf.get_start_iter()
        summ_sentence = 0
        end_buf = 1
        while end_buf:
             proverka = iter.is_end()
             if proverka == False:
                  if iter.starts_sentence():
                      summ_sentence = summ_sentence + 1
                      iter.forward_sentence_end()
                  else:
                      iter.forward_char()
             else:
                  end_buf = 0
        if summ_sentence == 0:
             average_word_in_sentence.set_text("Среднее количество слов\nв предложении: 0")               
        else:     
             average_word_in_sentence.set_text("Среднее количество слов\nв предложении: "+str(summ_words/summ_sentence))          

        # считаем среднее количество предложений в абзаце
        if sum_par == 0:
             average_sentence_in_parag.set_text("Среднее количество\nпредложений в абзаце: 0")
        else:
             average_sentence_in_parag.set_text("Среднее количество\nпредложений в абзаце: "+str(summ_sentence/int(sum_par)))
        
#############################################################
# Класс который предоставляет диалоговое окно для выбора файла.
# Очень долго возился, что бы суметь передать из диалогового окна
# данные в переменную.
##################################################################
class FileSelectionNum:

    # получает путь до файла и передает его в глобальную переменную программы.
    def file_ok_sel(FileSelectionNum, w):
        txtbuf.set_text('')# очищаем текстовый буфер

        s_filename = FileSelectionNum.filew.get_filename()
        filename = open(s_filename)# получаем имя файла и открывем его для чтения
        stroki = filename.readlines()# читаем файл в список
        # к сожалению текстовый буфер умеет получать только строки, списки он обрабатывает никак, поэтому пришлось
        # заюзать цикл
        for i in stroki:
            txtbuf.insert_at_cursor(str(i))

        titlestat.set_text('Статистика текста для файла:\n'+s_filename.split('/')[-1])    
        filename.close()# оставляем сборщика мусора без работы
        FileSelectionNum.filew.destroy() # убиваем окно открытия файла по нажатию кнопки ок


        

    # убивает окно выбора файла
    def destroy_fs(FileSelectionNum, widget):
        FileSelectionNum.filew.destroy()

    # обработка нажатия кнопки открыть
    def on_clk_open(FileSelectionNum, r):
        # создаем объект окно выбора файла
        FileSelectionNum.filew = gtk.FileSelection("Выбор файла")

        # закрыть окно по нажатию крестика
        FileSelectionNum.filew.connect("destroy", FileSelectionNum.destroy_fs)
        # обработка кнопки ок
        FileSelectionNum.filew.ok_button.connect("clicked", FileSelectionNum.file_ok_sel)
   
        # обработка кнопки cancel
        FileSelectionNum.filew.cancel_button.connect("clicked", FileSelectionNum.destroy_fs)
        # устанавливаем файл по умолчанию
        FileSelectionNum.filew.set_filename("test_text.txt")
        # показываем созданный объект окно выбора файла
        FileSelectionNum.filew.show()

######################################################
# класс, который сохраняет статистику в файл
######################################################
class SaveStat:

    def save_stat_txt(SaveStat, w):


        save_stat_file = open('Statistics Text.txt', 'w')      

        s_titlestat = titlestat.get_text()
        # забавный момент. функция split делит строку по заданному разделителю (в данном случае /)
        # и создает список из строк. Но так как объект s_titlestat имеет несколько сток,
        # разделенных \n, то split обрабатывает верно только последнюю строку, оставляя предыдущую строку как есть,
        # вместо ожидаемого от нее удаления всего, что находится левее последнего '/'
        save_stat_file.write(s_titlestat.split('/')[-1] + '\n')
        
        s_sum_char_spase_label = sum_char_spase_label.get_text()
        save_stat_file.write(s_sum_char_spase_label.replace('\n', ' ')+'\n')

        s_sum_char_label = sum_char_label.get_text()
        save_stat_file.write(s_sum_char_label.replace('\n', ' ')+'\n')

        s_average_word = average_word.get_text()
        save_stat_file.write(s_average_word.replace('\n', ' ')+'\n')

        s_average_word_in_sentence = average_word_in_sentence.get_text()
        save_stat_file.write(s_average_word_in_sentence.replace('\n', ' ')+'\n')

        s_average_sentence_in_parag = average_sentence_in_parag.get_text()
        save_stat_file.write(s_average_sentence_in_parag.replace('\n', ' ')+'\n')

        s_paragraph = paragraph.get_text()
        save_stat_file.write(s_paragraph.replace('\n', ' ')+'\n')

        s_words = words.get_text()
        save_stat_file.write(s_words.replace('\n', ' ')+'\n') 

        save_stat_file.close()

############################################################
# выполняем то, что определили функциями выше
############################################################# 
poschitalka()
gtk.main()

#######################################
#-------- THE END PROGRAMM -----------#
#######################################
