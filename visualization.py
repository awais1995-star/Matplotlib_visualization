import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,10)
y=np.arange(1,10)

plt.scatter(x,y,c="g")
plt.title("I am Graph")
plt.xlabel("Label 1")
plt.ylabel("Label 2")
plt.show()

#Seaborn

import seaborn as sns
data=sns.load_dataset('tips')
print(data.head())

corelation =data.corr()
print(corelation)
sns.heatmap(corelation)
plt.show()
