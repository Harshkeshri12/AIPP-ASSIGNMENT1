# Importing libraries
import pandas as pd
import numpy as np

# Step 1: Create a sample dataset of applicants
np.random.seed(42)  # for reproducibility
num_applicants = 100

data = {
    'Applicant_ID': range(1, num_applicants + 1),
    'Gender': np.random.choice(['Male', 'Female'], num_applicants),
    'Experience_Years': np.random.randint(0, 11, num_applicants),
    'Education_Level': np.random.choice(['High School', 'Bachelors', 'Masters', 'PhD'], num_applicants),
    'Skill_Score': np.random.randint(40, 101, num_applicants),  # out of 100
    'Interview_Score': np.random.randint(30, 101, num_applicants)  # out of 100
}

df = pd.DataFrame(data)

# Step 2: Encode categorical features
education_mapping = {'High School': 1, 'Bachelors': 2, 'Masters': 3, 'PhD': 4}
df['Education_Score'] = df['Education_Level'].map(education_mapping)

# Step 3: Create a scoring system
# Weighted scoring system (you can modify weights)
df['Final_Score'] = (
    df['Experience_Years'] * 2 +
    df['Education_Score'] * 5 +
    df['Skill_Score'] * 0.4 +
    df['Interview_Score'] * 0.5
)

# Normalize final score to 0–100
df['Final_Score'] = 100 * (df['Final_Score'] - df['Final_Score'].min()) / (df['Final_Score'].max() - df['Final_Score'].min())

# Step 4: Analyze potential bias based on gender
gender_scores = df.groupby('Gender')['Final_Score'].mean().reset_index()

print("Average Score by Gender:\n")
print(gender_scores)
print("\n")



# Step 6: Bias check interpretation
diff = abs(gender_scores['Final_Score'].iloc[0] - gender_scores['Final_Score'].iloc[1])
if diff > 5:
    print("⚠️ Potential Bias Detected: Average scores differ significantly between genders.")
else:
    print("✅ No significant bias detected based on gender.")
