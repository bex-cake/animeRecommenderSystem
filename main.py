# эти библиотеки нам уже знакомы
import pandas as pd
import numpy as np

# модуль sparse библиотеки scipy понадобится
# для работы с разреженными матрицами (об этом ниже)
from scipy.sparse import csr_matrix

# из sklearn мы импортируем алгоритм k-ближайших соседей
from sklearn.neighbors import NearestNeighbors

animes = pd.read_csv('animes.csv')
reviews = pd.read_csv('reviews.csv')
reviews.drop(['uid', 'text', 'scores', 'link'], axis = 1, inplace = True)
reviews.head(3)
animes.drop(['synopsis', 'genre', 'aired', 'episodes', 'members', 'popularity', 'ranked', 'score', 'img_url', 'link'], axis = 1, inplace = True)
animes.head(3)
user_item_matrix = pd.pivot_table(reviews, index = 'anime_uid', columns = 'profile', values = 'score')
user_item_matrix.head()