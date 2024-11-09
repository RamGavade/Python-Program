import matplotlib.pyplot as plt
import pandas as pd
df =pd.read_csv('titanic.csv')
# df['Age'].fillna(df['Age'].mean(), inplace=True)
# labels = df['Sex']
# sizes = df['Age']
sizes = [15, 30, 45, 10 ]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')
plt.show()