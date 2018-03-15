# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 13:29:22 2018

@author: alain
"""

# Sous Windows
from ctypes import cdll
rep = "C:/Users/alain/Desktop/Projet_CAPTAIN_SBE_NUMERIQUE/L3 Python/Cours_en_ligne/Cours/Initiation à Python/"
lib = 'test.dll'
replib = rep +  lib
print(replib)
mydll = cdll.LoadLibrary(replib)

a= mydll.sum(4,7)

print(a)