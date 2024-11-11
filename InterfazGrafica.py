import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Título de la aplicación
st.title("Identificación de Leptospiras usando CNN")

# Descripción
st.write("Sube una imagen para analizar y mostrar el resultado usando un modelo CNN entrenado.")

# Cargar el modelo
@st.cache_resource
def cargar_modelo():
    modelo = tf.keras.models.load_model("/content/drive/MyDrive/Leptospira_Proyecto/leptospira_model_checkpoint.weights.h5", compile=False)
    return modelo

model = cargar_modelo()

# Subir archivo
uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "png"])

if uploaded_file is not None:
    # Mostrar la imagen
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen subida", use_column_width=True)

    # Preprocesar la imagen
    img_array = np.array(image.resize((512, 512))) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Realizar la predicción
    st.write("Analizando la imagen...")
    prediccion = model.predict(img_array)[0][0]

    # Mostrar el resultado
    if prediccion > 0.5:
        st.success("Leptospiras detectadas en la imagen.")
    else:
        st.error("No se detectaron leptospiras en la imagen.")
