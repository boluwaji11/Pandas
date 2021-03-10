import pandas as pd

grades = pd.Series([87, 100, 94])

print(grades)

same_grade = pd.Series(98.6, range(3))

print(same_grade)

print(grades[0])
grades.count()
grades.mean()
grades.max()
grades.min()
grades.std()

print(grades.describe())

grades = pd.Series([87, 100, 94], index=["Wally", "Eva", "Sam"])

print(grades)

# If you initialize a Series with a dictionary, its keys
# becomes the Series' indices
grades = pd.Series({"Wally": 87, "Eva": 100, "Sam": 94})

# You can access individual elements via square brackets containing
# a custom index value

print(grades["Eva"])

print(grades.Wally)

print(grades.dtype)

print(grades.values)
