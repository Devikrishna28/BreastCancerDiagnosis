# app.py - Streamlit breast cancer diagnosis app
import streamlit as st
import pandas as pd
import pickle

st.title('Breast Cancer Diagnosis')

# Load model (placeholder)
model_path = 'model.pkl'
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.warning('Model not found or could not be loaded.')
    model = None

# Load dataset preview
if st.checkbox('Show dataset preview'):
    try:
        df = pd.read_csv('dataset.csv')
        st.dataframe(df.head())
    except Exception as e:
        st.error('Dataset not found.')

# Simple input form (placeholder)
st.subheader('Input features')
# TODO: add actual feature inputs
st.write('Feature inputs go here')

if st.button('Predict'):
    if model:
        st.success('Prediction: ...')
    else:
        st.error('Model not loaded.')
