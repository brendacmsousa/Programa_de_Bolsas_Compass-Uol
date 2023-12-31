# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mfEe0D4AWUi85qY3cSBBvMf07ZaRbtu2
"""

# Passo 1: Instalar biblioteca names para geração de nomes aleatórios
!pip install names

# Passo 2: Importar as bibliotecas necessárias
import random
import time
import os
import names

# Passo 3: Definir os parâmetros para geração do dataset
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# Passo 4: Gerar os nomes aleatórios
aux = []
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))
dados = []
for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

# Passo 5: Gerar um arquivo de texto contendo todos os nomes
nome_arquivo = 'nomes_aleatorios.txt'
with open(nome_arquivo, 'w') as file:
    for nome in dados:
        file.write(nome + '\n')

# Passo 6: Abrir o arquivo e verificar seu conteúdo
with open(nome_arquivo, 'r') as file:
    conteudo = file.read()

print("Conteúdo do arquivo:")
print(conteudo)