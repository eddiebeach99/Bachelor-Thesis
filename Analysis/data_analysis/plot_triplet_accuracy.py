import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import re

# Script that plots the triplet accuracies
task_one = [{'subject': '1', 'condition': 'SRL1_PRL1', 'matching_percent': 91.17647058823529}, {'subject': '2', 'condition': 'SRL1_PRL1', 'matching_percent': 85.29411764705883}, {'subject': '3', 'condition': 'SRL1_PRL1', 'matching_percent': 91.5}, {'subject': '4', 'condition': 'SRL1_PRL1', 'matching_percent': 90.83333333333333}]

task_two = [{'subject': '1', 'condition': 'SRL1_PRL2', 'matching_percent': 88.33333333333333}, {'subject': '2', 'condition': 'SRL1_PRL2', 'matching_percent': 85.29411764705883}, {'subject': '3', 'condition': 'SRL1_PRL2', 'matching_percent': 92.16666666666666}, {'subject': '4', 'condition': 'SRL1_PRL2', 'matching_percent': 91.16666666666666}]
sns.set_context("poster")
#sns.set(rc={'figure.figsize':(11.7,8.27)})
data = task_one + task_two
df = pd.DataFrame(data)

means = df.groupby('condition')['matching_percent'].mean()
plot = sns.catplot(data=df, x="condition", y='matching_percent', hue="subject", kind="point", legend_out=True, height=8.27, aspect=11.7/8.27,
                   markers= ['o','^','s','X', 'D', '*', 'v', '+'])
plot.set(ylabel=' Same Responses [%]')
plot.set(ylim=(71, 100))
plot.legend.set_title('Observer')
plot.set(xlabel = '')

plot.ax.set_xticklabels(['Surround Reflectance 0%', 'Surround Reflectance 2%'])
for line in plot.ax.lines:
    line.set_alpha(0.5)

plt.show()



