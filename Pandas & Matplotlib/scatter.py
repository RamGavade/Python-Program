import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df =pd.read_csv('titanic.csv')
x = df['Age']
y = df['Fare']
plt.scatter(x, y)
plt.title('Scatter')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()