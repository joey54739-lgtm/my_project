import numpy as np
import pandas as pd

print("--- NumPy and Pandas Solutions ---")

# --- Task 1 ---
print("\n--- Task 1: Test if no elements are zero ---")
# Question: Write a Numpy program to test whether none of the elements of a given array is zero.

# Create an array that has no zeros
array_a = np.array([1, 2, 3, 4, 5])
# Create an array that contains a zero
array_b = np.array([1, 2, 0, 4, 5])

# The np.all() function checks if ALL elements in the array are True.
# In Python, non-zero numbers are treated as True, and 0 is treated as False.
# So, np.all(array) will return True only if all numbers are non-zero.
result_a = np.all(array_a)
result_b = np.all(array_b)

print(f"Array A: {array_a}")
print(f"Are none of the elements in Array A zero? {result_a}") # Expected: True
print(f"Array B: {array_b}")
print(f"Are none of the elements in Array B zero? {result_b}") # Expected: False


# --- Task 2 ---
print("\n--- Task 2: Element-wise comparison of two arrays ---")
# Question: There are two arrays. The first array, array1 contains the values 45, 67, 23
# and array2 contains the values 56, 23, and 89.
# Write a Numpy program to create an element-wise comparison
# (greater, greater_equal, less and less_equal) of those two arrays.

array1 = np.array([45, 67, 23])
array2 = np.array([56, 23, 89])

print(f"Array 1: {array1}")
print(f"Array 2: {array2}")

# np.greater() checks if elements in array1 are greater than elements in array2
print(f"Element-wise comparison (greater): {np.greater(array1, array2)}")
# [45 > 56, 67 > 23, 23 > 89] -> [False, True, False]

# np.greater_equal() checks for greater than or equal to
print(f"Element-wise comparison (greater_equal): {np.greater_equal(array1, array2)}")
# [45 >= 56, 67 >= 23, 23 >= 89] -> [False, True, False]

# np.less() checks for less than
print(f"Element-wise comparison (less): {np.less(array1, array2)}")
# [45 < 56, 67 < 23, 23 < 89] -> [True, False, True]

# np.less_equal() checks for less than or equal to
print(f"Element-wise comparison (less_equal): {np.less_equal(array1, array2)}")
# [45 <= 56, 67 <= 23, 23 <= 89] -> [True, False, True]


# --- Task 3 ---
print("\n--- Task 3: Create an array of 8 zeros, 5 ones, 10 fives ---")
# Question: Write a Numpy program to create an array of 8 zeros, 5 ones, 10 fives.

# np.zeros(8) creates an array of 8 zeros.
array_zeros = np.zeros(8)
# np.ones(5) creates an array of 5 ones.
array_ones = np.ones(5)
# np.full(10, 5) creates an array of length 10, filled with the number 5.
# An alternative is np.ones(10) * 5
array_fives = np.full(10, 5)

# np.concatenate() joins a sequence of arrays together.
final_array_task3 = np.concatenate((array_zeros, array_ones, array_fives))

print(f"Array of 8 zeros: {array_zeros}")
print(f"Array of 5 ones: {array_ones}")
print(f"Array of 10 fives: {array_fives}")
print(f"Combined array: {final_array_task3}")


# --- Task 4 ---
print("\n--- Task 4: Add a vector to each row of a matrix ---")
# Question: Write a Numpy program to add a vector v with values 2, 0, 2
# to each row of a matrix m with values:
# [23 45 11]
# [12 23 54]
# [29 19 34]
# [1 23 10]

m = np.array([
    [23, 45, 11],
    [12, 23, 54],
    [29, 19, 34],
    [1, 23, 10]
])
v = np.array([2, 0, 2])

print("Original Matrix (m):")
print(m)
print(f"\nVector (v): {v}")

# This uses a powerful NumPy feature called "broadcasting".
# NumPy sees that the matrix 'm' has 3 columns and the vector 'v' has 3 elements.
# It automatically "broadcasts" or "stretches" the vector 'v'
# so it is added to EACH row of the matrix 'm'.
# [23 45 11] + [2 0 2] = [25 45 13]
# [12 23 54] + [2 0 2] = [14 23 56]
# ...and so on.
result_matrix = m + v

print("\nResult after adding vector v to each row of m:")
print(result_matrix)


# --- Task 5 ---
print("\n--- Task 5: Create 5x5 array with 1 on border and 25 inside ---")
# Question: Write a NumPy program to create a 5x5 2d array with 1 on the border and 25 inside.

# First, create a 5x5 array filled entirely with 1s.
array_5x5 = np.ones((5, 5))

print("Step 1: Create a 5x5 array of 1s:")
print(array_5x5)

# Now, we select the "inside" part of the array.
# In Python indexing, 1:-1 means "start at index 1 and go up to, but not including, the last index".
# array_5x5[1:-1, 1:-1] selects:
# Rows: index 1, 2, 3 (not 0 or 4)
# Columns: index 1, 2, 3 (not 0 or 4)
# This gives us the 3x3 inner block.
array_5x5[1:-1, 1:-1] = 25

print("\nStep 2: Set the inner 3x3 block to 25:")
print(array_5x5)


# --- Task 6 ---
print("\n--- Task 6: Find common values between two arrays ---")
# Question: Write a NumPy program to find common values between two arrays.
# Array1 [23, 45, 11, 5]
# Array2 [23, 5, 1]

array_c1 = np.array([23, 45, 11, 5])
array_c2 = np.array([23, 5, 1])

print(f"Array 1: {array_c1}")
print(f"Array 2: {array_c2}")

# np.intersect1d() (intersect 1-dimensional) finds the elements
# that are present in both arrays.
common_values = np.intersect1d(array_c1, array_c2)

print(f"Common values: {common_values}")


# --- Task 7 ---
print("\n--- Task 7: Array stacking and splitting ---")
# Question: Perform the following manipulation of the two arrays below:
# horizontal stacking, vertical stacking; divide the individual array horizontally and vertically.
# Array1              Array2
# [23, 45, 11]        [12, 23, 54]
# [1, 23, 10]         [3, 5, 1]
# [2, 3, 4]           [9, 1, 5]

array_s1 = np.array([
    [23, 45, 11],
    [1, 23, 10],
    [2, 3, 4]
])
array_s2 = np.array([
    [12, 23, 54],
    [3, 5, 1],
    [9, 1, 5]
])

print("Array 1:")
print(array_s1)
print("\nArray 2:")
print(array_s2)

# --- Stacking ---

# np.vstack() (vertical stack) stacks arrays on top of each other (row-wise).
# The number of columns must match.
v_stacked = np.vstack((array_s1, array_s2))
print("\nVertically Stacked (vstack):")
print(v_stacked)

# np.hstack() (horizontal stack) stacks arrays side-by-side (column-wise).
# The number of rows must match.
h_stacked = np.hstack((array_s1, array_s2))
print("\nHorizontally Stacked (hstack):")
print(h_stacked)

# --- Splitting (on Array 1) ---

# np.vsplit() (vertical split) splits an array into multiple sub-arrays vertically (row-wise).
# We split array_s1 into 3 equal parts.
v_split = np.vsplit(array_s1, 3)
print("\nVertically Split (vsplit on Array 1):")
print("Part 1:\n", v_split[0])
print("Part 2:\n", v_split[1])
print("Part 3:\n", v_split[2])

# np.hsplit() (horizontal split) splits an array into multiple sub-arrays horizontally (column-wise).
# We split array_s1 into 3 equal parts.
h_split = np.hsplit(array_s1, 3)
print("\nHorizontally Split (hsplit on Array 1):")
print("Part 1:\n", h_split[0])
print("Part 2:\n", h_split[1])
print("Part 3:\n", h_split[2])


# --- Setup for Pandas Tasks 8-13 ---
print("\n--- Pandas Tasks Setup ---")
# Sample DataFrame:
assessment_results = {
    'name': ['Anastasia', 'Paul', 'Kathe', 'Joseph', 'Linda', 'Michael', 'Matt', 'Laurentine', 'Chirstian', 'Jonas'],
    'score': [12.5, 10, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create the DataFrame
df = pd.DataFrame(assessment_results, index=labels)

print("Original DataFrame:")
print(df)


# --- Task 8 ---
print("\n--- Task 8: Get the first 3 rows of DataFrame ---")
# Question: Write a Pandas program to get the first 3 rows of a given DataFrame.

# .head(n) is the easiest way to get the first 'n' rows.
# .iloc[:3] also works (integer-location, rows 0, 1, 2)
first_3_rows = df.head(3)

print("First 3 rows:")
print(first_3_rows)


# --- Task 9 ---
print("\n--- Task 9: Select rows where attempts > 2 ---")
# Question: Write a Pandas program to select the rows where the
# number of attempts in the examination is greater than 2.

# This is called boolean indexing.
# 1. df['attempts'] > 2 creates a True/False series (e.g., [False, True, False, ...])
# 2. df[...] uses this series to filter the DataFrame, keeping only the 'True' rows.
attempts_gt_2 = df[df['attempts'] > 2]

print("Rows where attempts > 2:")
print(attempts_gt_2)


# --- Task 10 ---
print("\n--- Task 10: Count the number of rows and columns ---")
# Question: Write a Pandas program to count the number of rows and columns of a DataFrame.

# .shape returns a tuple (number_of_rows, number_of_columns)
shape = df.shape

print(f"Number of rows: {shape[0]}")
print(f"Number of columns: {shape[1]}")
# You can also use len(df) for just the row count.
# print(f"Row count using len(df): {len(df)}")


# --- Task 11 ---
print("\n--- Task 11: Select rows where score is between 14 and 20 ---")
# Question: Write a Pandas program to select the rows the score is between 14 and 20 (inclusive).

# We can do this by combining two conditions with '&' (which means AND).
# Notice the parentheses around each condition, which are required.
score_between_14_20 = df[(df['score'] >= 14) & (df['score'] <= 20)]

# A cleaner way is to use the .between() method
# score_between_14_20_alt = df[df['score'].between(14, 20)]
# print("\nRows where score is between 14 and 20 (alternative method):")
# print(score_between_14_20_alt)

print("Rows where score is between 14 and 20 (inclusive):")
print(score_between_14_20)


# --- Task 12 ---
print("\n--- Task 12: Change the score in row 'c' to 11.5 ---")
# Question: Write a Pandas program to change the score in row 'c' to 11.5

print(f"Score in row 'c' before change: {df.loc['c', 'score']}")

# We use .loc[] (location) to select by label.
# We select row 'c' and column 'score' and assign the new value.
df.loc['c', 'score'] = 11.5

print(f"Score in row 'c' after change: {df.loc['c', 'score']}")
print("\nDataFrame after change:")
# Note the score for 'Kathe' (row 'c') is now 11.5
print(df)


# --- Task 13 ---
print("\n--- Task 13: Calculate the mean score ---")
# Question: Write a Pandas program to calculate the mean score for each
# different student in DataFrame.
# (Note: Since each row is a different student, this just means the mean of the 'score' column)

# Select the 'score' column and call the .mean() method.
# This will automatically ignore the NaN (Not a Number) values by default.
mean_score = df['score'].mean()

print(f"The mean score for all students is: {mean_score:.2f}") # .2f formats to 2 decimal places


print("\n--- All tasks complete! ---")
