import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df =pd.read_csv('titanic.csv')
x = df['Sex']
y = df['Age']
print(x)
plt.bar(x, y)
plt.title('Bar Plot')
plt.xlabel('Sex')
plt.ylabel('Age')
plt.show()