import streamlit as st
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Detección de Leptospiras (Interfaz Simulada)")

# Descripción
st.write("Esta es una interfaz preliminar que muestra cómo funcionaría el proceso de identificación de leptospiras usando una CNN.")

# Subir archivo
uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "png"])

if uploaded_file is not None:
    # Mostrar la imagen subida
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen subida", use_column_width=True)

    # Simulación de predicción
    st.write("Analizando la imagen...")
    resultado_simulado = np.random.choice(["Leptospiras detectadas", "No se detectaron leptospiras"])
    
    # Mostrar el resultado simulado
    if resultado_simulado == "Leptospiras detectadas":
        st.success("Leptospiras detectadas en la imagen.")
    else:
        st.error("No se detectaron leptospiras en la imagen.")

    # Simulación de Grad-CAM
    st.write("Generando mapa de calor (simulado)...")
    img_array = np.array(image.resize((512, 512)))
    heatmap = np.zeros_like(img_array[:, :, 0], dtype=np.uint8)

    # Crear un heatmap simulado con círculos
    for _ in range(5):
        x, y = np.random.randint(0, 512, size=2)
        cv2.circle(heatmap, (x, y), radius=30, color=255, thickness=-1)

    # Aplicar colormap al heatmap simulado
    heatmap_colored = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    superimposed_img = cv2.addWeighted(cv2.cvtColor(np.uint8(img_array), cv2.COLOR_RGB2BGR), 0.6, heatmap_colored, 0.4, 0)

    # Mostrar el heatmap superpuesto
    st.image(cv2.cvtColor(superimposed_img, cv2.COLOR_BGR2RGB), caption="Heatmap Simulado", use_column_width=True)

