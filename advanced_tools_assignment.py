# Module 7 – Advanced Python Tools – Combined Assignment

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ASSIGNMENT 1 – NumPy


print("\n===== Assignment 1: NumPy =====")

# 1. Create a 1D NumPy array from 1 to 20
arr1 = np.arange(1, 21)
print("1D Array:", arr1)
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Median:", np.median(arr1))
print("Standard Deviation:", np.std(arr1))
print("Indices of elements > 10:", np.where(arr1 > 10)[0])

# 2. 2D NumPy Array (4x4) from 1 to 16
arr2 = np.arange(1, 17).reshape(4, 4)
print("\n2D Array:\n", arr2)
print("Transpose:\n", arr2.T)
print("Row-wise sum:", np.sum(arr2, axis=1))
print("Column-wise sum:", np.sum(arr2, axis=0))

# 3. Two 3x3 arrays with random integers (1–20)
a = np.random.randint(1, 21, (3, 3))
b = np.random.randint(1, 21, (3, 3))
print("\nArray A:\n", a)
print("Array B:\n", b)
print("Addition:\n", a + b)
print("Subtraction:\n", a - b)
print("Multiplication:\n", a * b)
print("Dot Product:\n", np.dot(a, b))

# 4. Reshape 1D array to 3x4 and slice
arr3 = np.arange(1, 13)
reshaped = arr3.reshape(3, 4)
print("\nReshaped (3x4):\n", reshaped)
print("Sliced (First 2 rows, Last 2 columns):\n", reshaped[:2, -2:])


# ASSIGNMENT 2 – Pandas

print("\n===== Assignment 2: Pandas =====")

# 1. Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'HR'],
    'Salary': [45000, 54000, 50000, 62000, 47000]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# a. Summary statistics
print("\nSummary (Age & Salary):\n", df[['Age', 'Salary']].describe())

# b. Average salary of HR department
hr_avg = df[df['Department'] == 'HR']['Salary'].mean()
print("Average HR Salary:", hr_avg)

# 2. Add 'Bonus' column (10% of salary)
df['Bonus'] = df['Salary'] * 0.10
print("\nWith Bonus Column:\n", df)

# 3. Filter employees aged between 25 and 30
filtered_df = df[(df['Age'] >= 25) & (df['Age'] <= 30)]
print("\nEmployees Aged 25-30:\n", filtered_df)

# 4. Group by Department and Average Salary
grouped_salary = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:\n", grouped_salary)

# 5. Sort by Salary and save to CSV
sorted_df = df.sort_values(by='Salary')
print("\nSorted by Salary:\n", sorted_df)
sorted_df.to_csv("sorted_employees.csv", index=False)


# ASSIGNMENT 3 – Matplotlib

print("\n===== Assignment 3: Matplotlib =====")

# 1. Line Plot
x = [1, 2, 3, 4, 5]
y = [10, 15, 25, 30, 50]
plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# 2. Bar Graph – Student Marks
students = ['John', 'Jane', 'Alice', 'Bob']
marks = [75, 85, 60, 90]
plt.figure(figsize=(6, 4))
plt.bar(students, marks, color=['blue', 'green', 'red', 'purple'])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3. Pie Chart – Revenue by Region
regions = ['North America', 'Europe', 'Asia', 'Others']
revenue = [45, 25, 20, 10]
explode = [0.1 if val == max(revenue) else 0 for val in revenue]
plt.figure(figsize=(6, 6))
plt.pie(revenue, labels=regions, autopct='%1.1f%%', explode=explode, shadow=True)
plt.title("Revenue Distribution")
plt.show()

# 4. Histogram – Random Values (1-100)
random_data = np.random.randint(1, 101, 1000)
plt.figure(figsize=(6, 4))
plt.hist(random_data, bins=20, color='skyblue', edgecolor='black')
plt.title("Histogram of Random Integers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
