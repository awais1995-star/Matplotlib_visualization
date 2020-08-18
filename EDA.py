import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import missingno as mn
import numpy as np

#Reading Data
data=pd.read_csv('titanic_train.csv')


#Visualization of missing Values
# sns.heatmap(data.isnull(),cbar=False)
# mn.matrix(data)
# mn.heatmap(data)


#Visualization of Data For Analysis

sns.set_style('whitegrid')
sns.countplot(x='Survived',data=data)
sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Sex',data=data)
plt.show()

