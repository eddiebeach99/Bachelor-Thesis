import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from adjustText import adjust_text

# Script that plots the vector differences between two conditions.

sns.set_context("poster")
df1 = pd.read_csv('embeddings/embedding_sub1_sess1.csv')
df2 = pd.read_csv('embeddings/embedding_sub1_sess2.csv')

mean_x = pd.concat([df1['x'], df2['x']], axis=1).mean(axis=1)
mean_y = pd.concat([df1['y'], df2['y']], axis=1).mean(axis=1)
mean_ref = df1['reflectance']
mean_illum = df1['illumination']
grey_values = [0.0094, 0.0373, 0.0832, 0.1476, 0.2320, 0.3347, 0.0272, 0.1066, 0.2395, 0.4258, 0.6654, 0.961, 0.0808, 0.3160, 0.7097]
df1['annotation'] = grey_values
df2['annotation'] = grey_values
#df1['annotation'] = df1['reflectance'].astype(str) + df1['illumination'].astype(str)
#df2['annotation'] = df2['reflectance'].astype(str) + df2['illumination'].astype(str)
plot = sns.scatterplot(data=df1, x='x', y='y', alpha=0.2, label='Surround Reflectance 0%', marker='^', s=180)
plot = sns.scatterplot(data=df2, x='x', y='y', alpha=0.2, label='Surround Reflectance 2%', s=180)
plot.set(xlabel='Dimension 1', ylabel='Dimension 2')
for i, row in df1.iterrows():
    plt.plot([row['x'], mean_x[i]], [row['y'], mean_y[i]], 'k-', alpha=0.1)
for i, row in df2.iterrows():
    plt.plot([row['x'], mean_x[i]], [row['y'], mean_y[i]], 'k-', alpha=0.1)


sns.scatterplot(x=mean_x, y=mean_y, color='red', marker='s', label='Average', s=180)

anno_texts = [str(mean_ref[i]) + str(mean_illum[i]) for i in range(len(mean_x))]
anno_pos = [(mean_x[i], mean_y[i]) for i in range(len(mean_x))]
annos = [plt.annotate(text, position, xytext=(-5, 5), textcoords='offset points', ha='right', va='bottom', alpha=0.4, fontsize=17) for text, position in zip(anno_texts, anno_pos)]

adjust_text(annos)

plt.show()
