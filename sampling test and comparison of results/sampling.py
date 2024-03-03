# -*- coding: utf-8 -*-

# Amostragem

## Carregamento da base de dados

import pandas as pd
import random
import numpy as np

dataset = pd.read_csv('census.csv')

dataset.shape

dataset.head()

dataset.tail()

## Amostragem aleatória simples

df_amostra_aleatoria_simples = dataset.sample(n = 100, random_state = 1)

df_amostra_aleatoria_simples.shape

df_amostra_aleatoria_simples.head()

def amostragem_aleatoria_simples(dataset, amostras):
  return dataset.sample(n = amostras, random_state=1)

df_amostra_aleatoria_simples = amostragem_aleatoria_simples(dataset, 100)
df_amostra_aleatoria_simples.shape

df_amostra_aleatoria_simples.head()

## Amostragem sistemática

dataset.shape

len(dataset) // 100

random.seed(1)
random.randint(0, 325)

68 + 325

393 + 325

np.arange(68, len(dataset), step = 325)

def amostragem_sistematica(dataset, amostras):
  intervalo = len(dataset) // amostras
  random.seed(1)
  inicio = random.randint(0, intervalo)
  indices = np.arange(inicio, len(dataset), step = intervalo)
  amostra_sistematica = dataset.iloc[indices]
  return amostra_sistematica

df_amostra_sistematica = amostragem_sistematica(dataset, 100)
df_amostra_sistematica.shape

df_amostra_sistematica.head()

## Amostragem por grupos

len(dataset) / 10

grupos = []
id_grupo = 0
contagem = 0
for _ in dataset.iterrows():
  grupos.append(id_grupo)
  contagem += 1
  if contagem > 3256:
    contagem = 0
    id_grupo += 1

print(grupos)

np.unique(grupos, return_counts=True)

np.shape(grupos), dataset.shape

dataset['grupo'] = grupos

dataset.head()

dataset.tail()

random.randint(0, 9)

df_agrupamento = dataset[dataset['grupo'] == 7]
df_agrupamento.shape

df_agrupamento['grupo'].value_counts()

def amostragem_agrupamento(dataset, numero_grupos):
  intervalo = len(dataset) / numero_grupos

  grupos = []
  id_grupo = 0
  contagem = 0
  for _ in dataset.iterrows():
    grupos.append(id_grupo)
    contagem += 1
    if contagem > intervalo:
      contagem = 0
      id_grupo += 1

  dataset['grupo'] = grupos
  random.seed(1)
  #grupo_selecionado = random.randint(0, numero_grupos)
  grupo_selecionado = random.randint(0, numero_grupos - 1) #Atualizado 16/10/2023
  return dataset[dataset['grupo'] == grupo_selecionado]

len(dataset) / 325

325 * 100

df_amostra_agrupamento = amostragem_agrupamento(dataset, 325)
df_amostra_agrupamento.shape, df_amostra_agrupamento['grupo'].value_counts()

df_amostra_agrupamento.head()

## Amostra estratificada

from sklearn.model_selection import StratifiedShuffleSplit

dataset['income'].value_counts()

7841 / len(dataset), 24720 / len(dataset)

0.2408095574460244 + 0.7591904425539756

100 / len(dataset)

split = StratifiedShuffleSplit(test_size=0.0030711587481956942)
for x, y in split.split(dataset, dataset['income']):
  df_x = dataset.iloc[x]
  df_y = dataset.iloc[y]

df_x.shape, df_y.shape

df_y.head()

df_y['income'].value_counts()

def amostragem_estratificada(dataset, percentual):
  split = StratifiedShuffleSplit(test_size=percentual, random_state=1)
  for _, y in split.split(dataset, dataset['income']):
    df_y = dataset.iloc[y]
  return df_y

df_amostra_estratificada = amostragem_estratificada(dataset, 0.0030711587481956942)
df_amostra_estratificada.shape

## Amostragem de reservatório

stream = []
for i in range(len(dataset)):
  stream.append(i)

print(stream)

def amostragem_reservatorio(dataset, amostras):
  stream = []
  for i in range(len(dataset)):
    stream.append(i)

  i = 0
  tamanho = len(dataset)

  reservatorio = [0] * amostras
  for i in range(amostras):
    reservatorio[i] = stream[i]

  while i < tamanho:
    j = random.randrange(i + 1)
    if j < amostras:
      reservatorio[j] = stream[i]
    i += 1

  return dataset.iloc[reservatorio]

df_amostragem_reservatorio = amostragem_reservatorio(dataset, 100)
df_amostragem_reservatorio.shape

df_amostragem_reservatorio.head()

## Comparativo dos resultados

dataset['age'].mean()

df_amostra_aleatoria_simples['age'].mean()

df_amostra_sistematica['age'].mean()

df_amostra_agrupamento['age'].mean()

df_amostra_estratificada['age'].mean()

df_amostragem_reservatorio['age'].mean()