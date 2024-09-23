import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Script that plots a heat map between two sessions
sns.set_context('poster')

embedding1 = pd.read_csv('embeddings/embedding_sub1_sess1.csv')
embedding2 = pd.read_csv('embeddings/embedding_sub1_sess3.csv')
embedding1['reflectance'] = embedding1['reflectance'].astype(str)
embedding1['illumination'] = embedding1['illumination'].astype(str)
embedding2['reflectance'] = embedding2['reflectance'].astype(str)
embedding2['illumination'] = embedding2['illumination'].astype(str)

distances = np.zeros((len(embedding1), len(embedding2)))
for i in range(len(embedding1)):
    for j in range(len(embedding2)):


        distances[i][j] = np.sqrt((embedding1.iloc[i]['x'] - embedding2.iloc[j]['x']) ** 2 +
                                  (embedding1.iloc[i]['y'] - embedding2.iloc[j]['y']) ** 2)

plot = sns.heatmap(distances, cmap='Blues', xticklabels=embedding2['reflectance'] + '' + embedding2['illumination'],
            yticklabels=embedding1['reflectance'] + '' + embedding1['illumination'])

plot.set(xlabel = 'Lightness task', ylabel= 'Brightness task')
plt.title('')
plt.show()
