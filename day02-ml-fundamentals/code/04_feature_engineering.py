"""
Day 2 - Step 4: Feature Engineering
Creates 'family_size' and 'is_alone' features from sibsp/parch.
"""

# We define 'family_size' (adding siblings, spouses, parents, children, and the passenger)
df['family_size'] = df['sibsp'] + df['parch'] + 1

# 'is_alone' indicates if family size is exactly 1
df['is_alone'] = (df['family_size'] == 1).astype(int)

print("Feature creation sample:")
df[['sibsp', 'parch', 'family_size', 'is_alone']].head()