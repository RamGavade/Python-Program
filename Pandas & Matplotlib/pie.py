import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('titanic.csv')
df['Age'].fillna(df['Age'].mean(), inplace=True)
plt.hist(df['Age'], bins=20, edgecolor='black')
plt.title('Pie Plot')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()