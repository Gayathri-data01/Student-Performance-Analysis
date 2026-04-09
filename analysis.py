# Student Performance Data Analysis

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('students.csv')

# Display first rows
print("Dataset Preview:\n", data.head())

# -------------------------------
# Basic Analysis
# -------------------------------

# Average scores
avg_scores = data[['math_score', 'reading_score', 'writing_score']].mean()
print("\nAverage Scores:\n", avg_scores)

# Top performers (total score)
data['total'] = data['math_score'] + data['reading_score'] + data['writing_score']
top_students = data.sort_values(by='total', ascending=False).head(5)
print("\nTop Performers:\n", top_students)

# Gender-wise average
gender_avg = data.groupby('gender')[['math_score', 'reading_score', 'writing_score']].mean()
print("\nGender-wise Average:\n", gender_avg)

# -------------------------------
# Visualization
# -------------------------------

# Average scores bar chart
avg_scores.plot(kind='bar', title='Average Scores')
plt.ylabel('Marks')
plt.show()

# Gender-wise comparison
gender_avg.plot(kind='bar', title='Gender-wise Performance')
plt.ylabel('Marks')
plt.show()

# Distribution of total scores
data['total'].plot(kind='hist', bins=10, title='Total Score Distribution')
plt.xlabel('Total Score')
plt.show()
