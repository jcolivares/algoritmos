#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 09:35:12 2019

Torres de Hanoi

@author: juancarlosolivaresrojas
"""

def hanoi(n, origen, auxiliar, destino):
    if n==1:
        print(origen, "-->", destino)
    else:
        hanoi(n-1, origen, destino, auxiliar)
        print(origen, "-->", destino)
        hanoi(n-1, auxiliar, origen, destino)

hanoi(20, "Origen", "auxiliar", "destino")