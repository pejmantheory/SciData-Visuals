import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
iris = sns.load_dataset("iris")

# Create the pair plot
sns.pairplot(iris, hue='species', palette='Dark2')

plt.suptitle('Pair Plot of Iris Dataset', y=1.02)
plt.show()
