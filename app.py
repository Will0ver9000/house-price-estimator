import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Title
st.title("🏡 House Price Predictor")
st.write("First ML Project on M1 Mac!")

# 1. Dummy Dataset for instant training
data = {
    "Square_Feet": [1000, 1500, 2000, 2500, 3000, 1200, 1800, 2200],
    "Bedrooms": [2, 3, 3, 4, 4, 2, 3, 4],
    "Price": [200000, 300000, 380000, 500000, 610000, 240000, 350000, 440000]
}
df = pd.DataFrame(data)

# 2. Train Model
X = df[["Square_Feet", "Bedrooms"]]
y = df["Price"]
model = RandomForestRegressor()
model.fit(X, y)

# 3. User Inputs via Web UI
sqft = st.slider("Square Feet:", 800, 4000, 1500)
beds = st.selectbox("Bedrooms:", [1, 2, 3, 4, 5], index=2)

# 4. Predict
if st.button("Estimate Price"):
    prediction = model.predict([[sqft, beds]])[0]
    st.success(f"Estimated Market Value: **${prediction:,.2f}**")