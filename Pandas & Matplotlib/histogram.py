import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df =pd.read_csv('titanic.csv')
data=df[['Age','Survived']]
plt.hist(data, bins=5)  
plt.title('Histogram Example')
plt.xlabel('Age')
plt.ylabel('Survived')
plt.show()