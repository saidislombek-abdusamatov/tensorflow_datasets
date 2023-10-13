import tensorflow as tf
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import cv2

deep_weeds = tf.keras.models.load_model('models/deep_weeds.h5')
eurosat = tf.keras.models.load_model('models/eurosat.h5')
svhn_cropped = tf.keras.models.load_model('models/svhn_cropped.h5')

classes = {
    'deep_weeds' : ['Chinee apple', 'Lantana', 'Parkinsonia', 'Parthenium', 'Prickly acacia', 'Rubber vine', 'Siam weed', 'Snake weed', 'Negative'],    
    'eurosat' : ['AnnualCrop', 'Forest', 'HerbaceousVegetation', 'Highway', 'Industrial', 'Pasture', 'PermanentCrop', 'Residential', 'River', 'SeaLake'],
    'svhn_cropped' : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
}

st.title("Tensorflow Datasets")

image = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"], accept_multiple_files=False)
if image:
    image = np.array(Image.open(image))
    st.image(image)

    option = st.selectbox(
        'Which model do you like to use model?',
        ('deep_weeds', 'eurosat', 'svhn_cropped'))

    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    size = (64,64)
    if option=='svhn_cropped':
        size = (32,32)
    img = cv2.resize(img, size, interpolation = cv2.INTER_AREA) / 255.
    img = np.expand_dims(img, axis=0)

    if st.button('Predict!'):
        result = eval(f'{option}.predict(img, verbose=0)')
        st.write('Result:',classes[option][result[0].argmax()])
        st.bar_chart(pd.DataFrame(result[0], index=classes[option]))