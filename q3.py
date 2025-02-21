# import matplotlib.pyplot as plt


# group_A = [12, 15, 14, 13, 16, 18, 19, 15, 14, 20, 17, 14, 15, 40, 45, 50, 62]
# group_B = [12, 17, 15, 13, 19, 20, 21, 18, 17, 16, 15, 14, 16, 15]

# # Create subplots
# fig, axes = plt.subplots(1, 2, figsize=(12, 6))


# axes[0].boxplot(group_A)
# axes[0].set_title("Group A")
# axes[0].set_ylabel("Values")

# axes[1].boxplot(group_B)
# axes[1].set_title("Group B")
# axes[1].set_ylabel("Values")

# plt.show()


# import random 
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# with open("helix.txt", "r") as file:
#     genome_sequence = file.read().strip()  

# genome_list = list(genome_sequence)
# genome_length = len(genome_list)

# # Parametric equations for a helix
# t = np.linspace(0, 4 * np.pi, genome_length)  # About 2 turns
# x = np.cos(t)
# y = np.sin(t)
# z = np.linspace(0, 5, genome_length)  # Spread helix vertically
# coordinates = np.column_stack((x, y, z))


# color_map = {'A': 'red', 'T': 'blue', 'C': 'green', 'G': 'yellow'}
# colors = [color_map.get(nucleotide) for nucleotide in genome_list] #doesnt work without this liein 

# fig = plt.figure(figsize=(8, 6))
# ax = fig.add_subplot(projection='3d')
# ax.scatter(x, y, z, c=colors, marker='o')

# ax.set_xlabel("X Axis")
# ax.set_ylabel("Y Axis")
# ax.set_zlabel("Z Axis")
# ax.set_title("genomce visualization")

# plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image 
from numpy import asarray

# Load an image and convert it to a numpy array
img = Image.open("123.jpg")
img_array = asarray(img)

# Plot original image
plt.figure(figsize=(6,6))
plt.imshow(img_array)
plt.title("Original Image")
plt.axis("off")
plt.show()

# Rotate and flip the image
rotated_img = np.rot90(img_array)
flipped_img = np.fliplr(img_array)

# Plot rotated image
plt.figure(figsize=(6,6))
plt.imshow(rotated_img)
plt.title("Rotated Image")
plt.axis("off")
plt.show()

# Plot flipped image
plt.figure(figsize=(6,6))
plt.imshow(flipped_img)
plt.title("Flipped Image")
plt.axis("off")
plt.show()

# Convert image to grayscale
gray_img = np.dot(img_array[..., :3], [0.299, 0.587, 0.114])

# Plot grayscale image
plt.figure(figsize=(6,6))
plt.imshow(gray_img, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")
plt.show()





######## q4 


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import PCA
# df=pd.read_csv('Titanic-Dataset.csv')
# df.head(5)
# dtypes = df.dtypes
# print("\nData Types:\n", dtypes)

# # Check for missing values
# missing_values = df.isnull().sum()
# print("Missing Values:\n", missing_values)

# # Check for duplicate values
# duplicates = df.duplicated().sum()
# print("\nNumber of Duplicate Rows:", duplicates)

# # Get summary statistics
# summary = df.describe()
# print("\nSummary Statistics:\n", summary)

# Binning 'Age' column into categories
# bins = [18, 25, 35, 50, 100]
# labels = ['Young', 'Adult', 'Middle-Aged', 'Senior']
# df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
# print("\nBinned Age Groups:\n", df[['Age', 'Age Group']])









#from here it is histogram of age with and without binning 

# df['Age'].fillna(df['Age'].median(), inplace=True)

# # Define bins and labels
# bins = [18, 25, 35, 50, 100]
# labels = ['Young', 'Adult', 'Middle-Aged', 'Senior']

# # Create a new column for binned age groups
# df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

# # Plot histogram before binning
# plt.figure(figsize=(12, 5))

# plt.subplot(1, 2, 1)  # First subplot
# sns.histplot(df['Age'], bins=20, kde=True, color='blue')
# plt.xlabel('Age')
# plt.ylabel('Count')
# plt.title('Histogram of Age (Before Binning)')

# # Plot histogram after binning
# plt.subplot(1, 2, 2)  # Second subplot
# sns.countplot(x=df['Age Group'], palette='coolwarm')
# plt.xlabel('Age Group')
# plt.ylabel('Count')
# plt.title('Histogram of Age Groups (After Binning)')

# plt.tight_layout()  # Adjust layout for better visibility
# plt.show()

