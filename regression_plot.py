import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
import pandas as pd

# Load the dataset
boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['MEDV'] = boston.target

# Create a regression plot
plt.figure(figsize=(10, 6))
sns.regplot(x='RM', y='MEDV', data=df, line_kws={"color":"r","alpha":0.7,"lw":2})

plt.title('Regression Plot: Number of Rooms vs. Median Value of Owner-Occupied Homes')
plt.xlabel('Number of Rooms')
plt.ylabel('Median Value of Owner-Occupied Homes')
plt.show()
