# -*- coding: utf-8 -*-
"""Tarefa 3.1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bVx8BY4TQ4VXpZ3nY2i3U7AlOO8T8qiO
"""

import random

# Declare e inicialize uma lista com 250 inteiros aleatórios
lista_inteiros = [random.randint(1, 1000) for _ in range(250)]

# Aplica o método reverse na lista
lista_inteiros.reverse()

# Imprime o resultado
print(lista_inteiros)