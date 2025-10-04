# 💻 Laptop-Price-Prediction-WebApp

This repository contains a web application that predicts laptop prices based on user-provided specifications using a machine learning model. Built with Streamlit for an interactive UI and scikit-learn for predictive modeling, this project showcases skills in data science, feature engineering, and web development.
📖 Overview
The Laptop Price Prediction WebApp uses a RandomForestRegressor model to estimate laptop prices based on features like brand, CPU, GPU, RAM, storage, screen size, and more. The app incorporates feature engineering (e.g., calculating screen PPI) and a preprocessing pipeline for robust predictions. The interactive Streamlit interface allows users to input laptop specifications and receive instant price predictions.
🎯 Features

Predicts laptop prices based on:
Brand, Type, CPU, GPU
RAM, Storage, Weight
Screen Size, Resolution, IPS, Touchscreen
Operating System


Calculates screen PPI (pixels per inch) for enhanced prediction accuracy.
Responsive and user-friendly Streamlit UI with emojis and icons.
Preprocessing pipeline with OneHotEncoding and transformations for consistent data handling.
Trained on a comprehensive laptop dataset for reliable predictions.

🛠️ Tech Stack

Python: Core programming language.
Streamlit: For building the interactive web interface.
Scikit-learn: For the RandomForestRegressor model and preprocessing pipeline.
Pandas/NumPy: For data manipulation and feature engineering.
Pickle: For serializing the dataset (df.pkl) and pipeline (pipe.pkl).
Git: Version control with .gitignore for clean repository management.

🚀 Getting Started
Prerequisites

Python 3.8+
Git

Installation

Clone the repository:git clone https://github.com/RachitNigam19/Laptop-Price-Prediction-WebApp.git
cd Laptop-Price-Prediction-WebApp


Install dependencies:pip install -r requirements.txt


Ensure the serialized files (df.pkl, pipe.pkl) are in the root directory.

Usage

Run the Streamlit application:streamlit run app.py


Open the provided URL (e.g., http://localhost:8501) in your browser.
Input laptop specifications (e.g., brand, RAM, CPU) via the Streamlit UI to get a price prediction.

📂 Project Structure
Laptop-Price-Prediction-WebApp/
├── LV/                          # Additional project files or resources
├── app.py                       # Main Streamlit application
├── df.pkl                       # Serialized laptop dataset
├── pipe.pkl                     # Preprocessing pipeline (e.g., OneHotEncoding)
├── requirements.txt             # Project dependencies

🔍 How It Works

Dataset: The df.pkl file contains a preprocessed dataset of laptops with features like brand, CPU, RAM, etc.
Preprocessing: The pipe.pkl file stores a scikit-learn pipeline that handles OneHotEncoding and other transformations for consistent data input.
Model: A RandomForestRegressor model is trained to predict laptop prices, incorporating feature engineering like PPI calculation.
Web UI: The app.py script uses Streamlit to create an interactive interface for users to input specifications and view predictions.

🌟 Why This Project?

Demonstrates expertise in machine learning with scikit-learn and RandomForestRegressor.
Showcases skills in building interactive web applications with Streamlit.
Highlights proficiency in data preprocessing and feature engineering.
Reflects clean coding practices with a modular, well-organized codebase.
Provides a practical example of an ML-driven application for real-world use cases.

📫 Contact

GitHub: RachitNigam19
LinkedIn: Rachit Nigam
Email: rachitn46@gmail.com

Feel free to explore, contribute, or reach out for collaboration!
