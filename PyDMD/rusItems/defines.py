# -*- coding: utf-8 -*-
def выведи(знач):
    """
    Русский аналог print(...)
    """
    return print(знач)

def диапазон(знач):
    """
    Русский аналог range(...)
    """
    return range(знач)

def список(знач):
    """
    Русский аналог list(...)
    """
    
    return list(знач)

def списокДиапазона(знач):
    """
    Русский аналог list(range(...))
    """
    
    return список(диапазон(знач)) 

def ошибка(сооб):
    """
    Вывод сообщения об ошибке
    """
    from sys import stderr
    stderr.write("Ошибка: %s\n" % (сооб,))
    
def проблема(сооб):
    """
    Вывод сообщения о приблеме
    """
    from sys import stderr
    stderr.write("Проблема: %s\n" % (сооб,))
    
def файлыВПапке(пап, фильтр_файлов=None):
    from fnmatch import filter
    import os
    файлы = [walkdir[0]+"\\"+file for walkdir in os.walk(пап) for file in walkdir[2]]
    if фильтр_файлов != None:
        файлы = filter(файлы, фильтр_файлов)
    return файлы



def тест():
    выведи(диапазон(10))
    выведи(список(диапазон(12)))
    выведи(списокДиапазона(5))
    ошибка("полный алес")
    проблема("результат неуд")
    флы = файлыВПапке("d:\Python36\Scripts")
    for f in флы:
        выведи(f)
    
тест()
