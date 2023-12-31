# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19haSI56uWBH6lMatQ7_8wnt1_f1EMg8t
"""

import pandas as pd

file_path = 'actors.csv'
df = pd.read_csv(file_path)

# 1. Identifique o ator/atriz com o maior número de filmes e o respectivo número de filmes.
max_movies_actor = df.loc[df['Number of Movies'].idxmax()]
print(f"1. Ator/atrizes com mais filmes: {max_movies_actor['Actor']} ({max_movies_actor['Number of Movies']} filmes)")

# 2. Apresente a média da coluna contendo o número de filmes.
average_movies = df['Number of Movies'].mean()
print(f"2. Média do número de filmes: {average_movies:.2f}")

# 3. Apresente o nome do ator/atriz com a maior média por filme.
max_average_actor = df.loc[df['Average per Movie'].idxmax()]
print(f"3. Ator/atrizes com maior média por filme: {max_average_actor['Actor']} ({max_average_actor['Average per Movie']:.2f} por filme)")

# 4. Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
most_frequent_movie = df['#1 Movie'].value_counts().idxmax()
frequency = df['#1 Movie'].value_counts().max()
print(f"4. Filme mais frequente: {most_frequent_movie} ({frequency} vezes)")