import streamlit as st
import numpy as np
from PIL import Image, ImageDraw

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

    # Generar un heatmap simulado usando PIL
    st.write("Generando mapa de calor (simulado)...")
    heatmap = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(heatmap)

    # Dibujar círculos simulados en el heatmap
    for _ in range(5):
        x, y = np.random.randint(0, image.size[0]), np.random.randint(0, image.size[1])
        draw.ellipse((x-30, y-30, x+30, y+30), fill=(255, 0, 0, 128))

    # Superponer el heatmap sobre la imagen original
    superimposed_img = Image.alpha_composite(image.convert("RGBA"), heatmap)
    st.image(superimposed_img, caption="Heatmap Simulado", use_column_width=True)
