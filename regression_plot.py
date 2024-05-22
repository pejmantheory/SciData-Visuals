import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset from the local files
df = pd.read_csv('CaliforniaHousing/cal_housing.data', header=None, sep=',')
column_names = ["longitude", "latitude", "housing_median_age", "total_rooms", "total_bedrooms", 
                "population", "households", "median_income", "median_house_value"]
df.columns = column_names

# Add derived feature 'AveRooms' (average number of rooms)
df['AveRooms'] = df['total_rooms'] / df['households']

# Create a regression plot
plt.figure(figsize=(10, 6))
sns.regplot(x='AveRooms', y='median_house_value', data=df, line_kws={"color":"r","alpha":0.7,"lw":2})

plt.title('Regression Plot: Average Number of Rooms vs. Median House Value')
plt.xlabel('Average Number of Rooms')
plt.ylabel('Median House Value')
plt.show()
