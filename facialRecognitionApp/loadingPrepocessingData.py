import numpy as np

# # If you saved separate files:
# X = np.load("data/processed/X.npy")
# y = np.load("data/processed/y.npy")



# #DIMENSION OF THE X AND Y ARRAYS
# print(X.ndim)
# print(y.ndim)

import numpy as np

import matplotlib.pyplot as plt


# Load your data
X = np.load("data/processed/X.npy")  # shape: (N, 160, 160, 3)
y = np.load("data/processed/y.npy")  # shape: (N,)



# SHAPE OF THE X AND Y 
print('SHAPE OF THE X AND Y ')
print(X.shape)
print(y.shape)

# 1. Choose an index to inspect
idx = 2  # change to any i in [0, len(X)-1]

# 2. Print its label and array stats
print(f"Sample index: {idx}")
print(f"Label: {y[idx]}")
print(f"Array shape: {X[idx].shape}")
print(f"Min / Max pixel value: {X[idx].min():.3f} / {X[idx].max():.3f}")

# 3. (Optional) Print raw pixel data for the first row
print("First row pixels:", X[idx][0,2])
print("First row pixels:", X[idx][0,2][1])
print("First row pixels:", X[idx][0,2][0:2])
# 4. Display the image
plt.imshow(X[idx])
plt.title(f"Label: {y[idx]}")
plt.axis('off')
plt.show()