import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a random dataset
data = np.random.rand(10, 12)
columns = [f'Var{i}' for i in range(1, 13)]
df = pd.DataFrame(data, columns=columns)

# Compute the correlation matrix
corr = df.corr()

# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap of Correlation Matrix')
plt.show()
