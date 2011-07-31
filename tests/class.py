# -*- coding: utf-8 -*-

n = int(raw_input('Введите число: '))
t = int(raw_input('Введите число: '))

class a:
    def chislo(self):
        h = n*2
        return h
    
class c:
    def chislo(self):
        j = n*0.5
        return j
class z:
    def summ(self):
        b = a()
        m = c()
        q = b.chislo()+m.chislo()
        print q
                
    def raz(self,t):
        b = a()
        m = c()
        q = b.chislo()-m.chislo()*t
        print q

g = z()
g.summ()
g.raz(t)



