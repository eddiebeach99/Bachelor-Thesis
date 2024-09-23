import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.patheffects as pe
import matplotlib.colors as colors
from adjustText import adjust_text

# Script made for plotting the ordinal embeddings
cmap = colors.LinearSegmentedColormap.from_list("", ["black", "white"])

sns.set_context("poster")
df = pd.read_csv('embeddings/embedding_sub1_sess10.csv')
reflectance = [0.027, 0.11, 0.25, 0.44, 0.69, 1]
df['reflectance_transformed'] = df['reflectance']**(1/2.2)
grey_values = [0.009, 0.037, 0.083, 0.148, 0.232, 0.335, 0.027, 0.107, 0.240, 0.426, 0.665, 0.961, 0.081, 0.316, 0.710]
grey_values2 = ['0.009', '0.037', '0.083', '0.148', '0.232', '0.335', '0.027', '0.107', '0.240', '0.426', '0.665', '0.961', '0.081', '0.316', '0.710']
fig, ax = plt.subplots()

markers = ['o', 's', '^', 'X', 'P', '*', 'X']
g = scatter_plot = sns.scatterplot(data=df, x='x', y='y', hue='illumination', palette=cmap, style='reflectance', markers=markers[:len(reflectance)], ax=ax, edgecolor="black",legend=False,s=180)


annotations = []
for index, row in df.iterrows():
    #ax.annotate('{}{}'.format(int(row['reflectance']), int(row['illumination'])), (row['x'], row['y']), alpha=0.5

    annotations.append(ax.annotate(grey_values[index], (row['x'], row['y']), alpha=0.33, fontsize=17))

adjust_text(annotations, ax=ax)




ax.set_xlabel('Dimension 1')
ax.set_ylabel('Dimension 2')
g.set(ylim = (-0.5,0.5), xlim = (-0.35, 0.45))
illumination_legend_elements = [
    plt.Line2D([0], [0], marker='o', linestyle='', markersize=10, markerfacecolor= "black", markeredgecolor='black', label='29.0'),
    plt.Line2D([0], [0], marker='o', linestyle='', markersize=10, markerfacecolor= "grey", markeredgecolor='black', label='100'),
    plt.Line2D([0], [0], marker='o', linestyle='', markersize=10, markerfacecolor= "white", markeredgecolor='black', label='310')
]

ax.legend(handles=illumination_legend_elements, loc='center left', bbox_to_anchor=(1, 0.9), title='Illumination \n [in %]', title_fontsize=18)

marker_dict = dict(zip(reflectance, markers[:len(reflectance)]))
legend_elements = [
    plt.Line2D([0], [0], marker=marker_dict[value], linestyle='', markersize=10,
               markerfacecolor='black', markeredgecolor='black', label='{}'.format(value*100))
    for value in reflectance
]


ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.7), title='Reflectance \n [in %]', title_fontsize=18)
ax_r = ax.twinx()
ax_r.get_yaxis().set_visible(False)
ax_r.legend(handles=illumination_legend_elements, loc='center left', bbox_to_anchor=(1,0.2), title='Illumination \n [in %]', title_fontsize=18)


plt.show()
