# Analyzing Data with Pandas and Visualizing Results with Matplotlib
# Power Learn Project Africa - Assignment
# Author: [Your Name]
# Date: [Today's Date]

# Importing the needed libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# I’m setting seaborn style for nicer looking charts
sns.set(style="whitegrid")

# Step 1: Load the dataset
# I'll use the Iris dataset as an example. It's small and well-known.
try:
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: The dataset file was not found.")
    exit()
except pd.errors.EmptyDataError:
    print("Error: The dataset is empty.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()

# Step 2: Explore the dataset
print("\nFirst 5 rows of the dataset:")
print(df.head())

print("\nData types of each column:")
print(df.dtypes)

print("\nChecking for missing values:")
print(df.isnull().sum())

# Step 3: Handle missing values
# (This dataset actually has no missing values, but I’ll still add code to handle them.)
if df.isnull().sum().any():
    df.fillna(df.mean(numeric_only=True), inplace=True)
    print("Missing values filled with column means.")
else:
    print("No missing values found.")

# Step 4: Basic statistics
print("\nBasic statistics of the dataset:")
print(df.describe())

# Step 5: Grouping data
# I'll group by species and find the average petal_length for each
grouped = df.groupby("species")["petal_length"].mean()
print("\nAverage petal length per species:")
print(grouped)

# Finding: The 'virginica' species has the longest average petal length.
# This is interesting because it might help in species identification.

# Step 6: Data Visualizations

# Line Chart - Trend of sepal_length over index (just for demonstration)
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["sepal_length"], label="Sepal Length", color="blue")
plt.title("Sepal Length Trend Over Index")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# Bar Chart - Average petal_length per species
plt.figure(figsize=(8, 5))
grouped.plot(kind="bar", color=["green", "orange", "purple"])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# Histogram - Distribution of sepal_width
plt.figure(figsize=(8, 5))
plt.hist(df["sepal_width"], bins=15, color="skyblue", edgecolor="black")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot - Relationship between sepal_length and petal_length
plt.figure(figsize=(8, 5))
plt.scatter(df["sepal_length"], df["petal_length"], alpha=0.7, color="red")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()

print("\nAnalysis complete! All charts have been displayed successfully.")
