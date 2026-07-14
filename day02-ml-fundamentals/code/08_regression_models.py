"""
Day 2 - Step 8: Regression Models (Target = Passenger Fare)
"""
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

X_reg = X.drop('fare', axis=1)
y_reg = X['fare']

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

# A. Linear Regression
lr_reg = LinearRegression()
lr_reg.fit(X_train_reg, y_train_reg)

# B. Polynomial Regression (Degree = 2)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train_reg)
X_test_poly = poly.transform(X_test_reg)
poly_reg = LinearRegression()
poly_reg.fit(X_train_poly, y_train_reg)

# C. Decision Tree Regressor
dt_reg = DecisionTreeRegressor(max_depth=5, random_state=42)
dt_reg.fit(X_train_reg, y_train_reg)

# D. Random Forest Regressor
rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)
rf_reg.fit(X_train_reg, y_train_reg)

print("All Regression Models Trained Successfully!")