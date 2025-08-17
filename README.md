  # 💻 Laptop Price Predictor

A web application that predicts the price of a laptop based on its specifications using machine learning and an interactive Streamlit UI.

---

## 🚀 Features
 
- Predict laptop prices based on:
  - Brand, Type, CPU, GPU
  - RAM, Storage, Weight
  - Screen Size, Resolution, IPS, Touchscreen
  - Operating System
- Calculates screen PPI for better accuracy
- Clean responsive UI with emojis and icons
- Built with `Streamlit`, `scikit-learn`, and `numpy`
 
---

## 🧠 Model Info

The app uses a `RandomForestRegressor` trained on a laptop dataset with feature engineering (e.g., PPI calculation). Preprocessing is handled via a pipeline that includes OneHotEncoding and transformations.

---

## 🗂️ Project Structure

