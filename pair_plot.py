import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from a local file
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
iris = pd.read_csv("iris.data.txt", header=None, names=column_names)

# Create the pair plot
sns.pairplot(iris, hue='species', palette='Dark2')

plt.suptitle('Pair Plot of Iris Dataset', y=1.02)
plt.show()
