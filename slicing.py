import numpy as np

np.random.seed(42)  # For reproducibility
random_2d_array = np.random.randint(0, 100, size=(5, 5))
print("Original 2D Array:")
print(random_2d_array)

# Step 2: Extract a sub-matrix using slicing
sub_matrix = random_2d_array[1:4, 1:4]
print("\nSub-Matrix:")
print(sub_matrix)

# Step 3: Apply filtering to get values greater than a certain threshold
threshold = 50
filtered_values = sub_matrix[sub_matrix > threshold]
print("\nFiltered Values (greater than {}):".format(threshold))
print(filtered_values)

# Step 4: Sort the resulting values
sorted_values = np.sort(filtered_values)
print("\nSorted Values:")
print(sorted_values)

# Step 5: Perform negative indexing to access specific elements
negative_indexed_element = sorted_values[-1]
print("\nNegative Indexing - Last Element:")
print(negative_indexed_element)

# Step 6: Concatenate the original array and the sorted sub-matrix
concatenated_array = np.concatenate((random_2d_array, sorted_values.reshape(1, -1)), axis=0)
print("\nConcatenated Array:")
print(concatenated_array)

# for x in np.nditer(arrr):
#     if x > 3:
#         boolean_list.append(True)

#print(boolean_list)
