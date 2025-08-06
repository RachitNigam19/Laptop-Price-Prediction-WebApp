# import streamlit as st
# import pickle
# import numpy as np 

# # importing the model
# pipe = pickle.load(open('pipe.pkl', 'rb'))
# df = pickle.load(open('df.pkl', 'rb'))

# #  Streamlit
# st.title("Laptop Price Predictor")


# # Brand
# company = st.selectbox('Brand', df['Company'].unique())

# # type of laptop 
# type = st.selectbox('Type', df['TypeName'].unique())

# # Ram 
# Ram = st.selectbox('RAM(in GB)', [2,4,6,8,12,16,24,32,64])

# # Weight
# weight = st.number_input('Weight of the Laptop')

# # Touch Screen
# touchscreen = st.selectbox('Touch Screen', ['Yes', 'No'])

# # IPS
# ips = st.selectbox('IPS', ['NO', 'Yes'])

# # Screen Size 
# screensize = st.number_input('Screen Size')

# # Resolutions
# resolutions = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800',
#      '2880x1800', '2560x1600', '2560x1440', '2304x1440'])

# # cpu brand 
# cpu = st.selectbox('CPU', df['cpu_brand'].unique())

# #hdd
# hdd = st.selectbox('HDD(in GB)', [0,128,256,512,1024,2048])

# #ssd
# ssd = st.selectbox('SSD(in GB)', [0,128,256,512,1024,2048])

# # GPU 
# gpu = st.selectbox('GPU',df['gpu brand'].unique())

# # oS
# os = st.selectbox('OS', df['os_cat'].unique())

# if st.button('Predict price'):
#               # query 
#               ppi = None
#               if touchscreen == 'Yes':
#                       touchscreen = 1
#               else:
#                       touchscreen = 0

#               if ips == 'Yes':
#                       ips = 1
#               else:
#                       ips = 0
              
#               X_res = int(resolutions.split('x')[0])
#               y_res = int(resolutions.split('x')[1])

#               ppi = ((X_res**2) + (y_res**2))**0.5/screensize

#               query = np.array([company,type,Ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
#               query = query.reshape(1,12)
#               st.title("The Predicted Price of the Laptop for this confriguation is"str(round(int(np.exp(pipe.predict(query)[0])))))
import streamlit as st
import pickle
import numpy as np

# Load model and data
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Set page config
st.set_page_config(page_title="Laptop Price Predictor", layout="centered")

# Custom CSS for dark mode
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .stSelectbox > div > div {
            color: black !important;
        }
    </style>
    """, unsafe_allow_html=True)

st.title("💻 Laptop Price Predictor")

# Layout in two columns
col1, col2 = st.columns(2)

with col1:
    company = st.selectbox('💼 Brand', df['Company'].unique())
    type = st.selectbox('📟 Type', df['TypeName'].unique())
    Ram = st.selectbox('💾 RAM (GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
    weight = st.number_input('⚖️ Weight (kg)')
    touchscreen = st.selectbox('🖱️ Touchscreen', ['Yes', 'No'])
    ips = st.selectbox('📺 IPS Display', ['Yes', 'No'])

with col2:
    screensize = st.number_input('📐 Screen Size (inches)')
    resolutions = st.selectbox('🔢 Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800',
                                                 '2880x1800', '2560x1600', '2560x1440', '2304x1440'])
    cpu = st.selectbox('🧠 CPU', df['cpu_brand'].unique())
    hdd = st.selectbox('💽 HDD (GB)', [0, 128, 256, 512, 1024, 2048])
    ssd = st.selectbox('🚀 SSD (GB)', [0, 128, 256, 512, 1024, 2048])
    gpu = st.selectbox('🎮 GPU', df['gpu brand'].unique())
    os = st.selectbox('🖥️ OS', df['os_cat'].unique())

# Prediction
if st.button('🎯 Predict Price'):
    # Encode touchscreen and ips
    touchscreen_val = 1 if touchscreen == 'Yes' else 0
    ips_val = 1 if ips == 'Yes' else 0

    # Calculate PPI
    X_res = int(resolutions.split('x')[0])
    Y_res = int(resolutions.split('x')[1])
    ppi = ((X_res ** 2 + Y_res ** 2) ** 0.5) / screensize

    # Prepare input
    query = np.array([company, type, Ram, weight, touchscreen_val, ips_val, ppi, cpu, hdd, ssd, gpu, os])
    query = query.reshape(1, 12)

    predicted_price = int(np.exp(pipe.predict(query)[0]))

    st.success(f"💰 **Estimated Price: ₹{predicted_price}**")
