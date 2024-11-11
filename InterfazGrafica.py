import streamlit as st
import numpy as np
from PIL import Image, ImageDraw
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
    probabilidad_simulada = np.random.uniform(0.6, 0.99)  # Generar un porcentaje aleatorio
    resultado_simulado = "Leptospiras detectadas" if probabilidad_simulada > 0.7 else "No se detectaron leptospiras"

    # Mostrar el resultado simulado
    st.write(f"Probabilidad de detección: {probabilidad_simulada:.2%}")
    if resultado_simulado == "Leptospiras detectadas":
        st.success(f"{resultado_simulado}")
    else:
        st.error(f"{resultado_simulado}")

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

    # Mostrar gráficos de precisión y pérdida (simulados)
    st.write("Rendimiento del modelo (simulado):")

    epochs = list(range(1, 11))
    accuracy = [0.75, 0.80, 0.85, 0.87, 0.89, 0.91, 0.92, 0.93, 0.94, 0.95]
    loss = [0.5, 0.45, 0.4, 0.35, 0.3, 0.28, 0.25, 0.22, 0.2, 0.18]

    fig, ax = plt.subplots()
    ax.plot(epochs, accuracy, label="Precisión")
    ax.plot(epochs, loss, label="Pérdida")
    ax.set_xlabel("Épocas")
    ax.set_title("Precisión y Pérdida del Modelo")
    ax.legend()
    st.pyplot(fig)

    # Mostrar métricas simuladas
    st.write("Métricas del modelo (simuladas):")
    st.write("- Precisión: 95%")
    st.write("- Sensibilidad: 92%")
    st.write("- Especificidad: 93%")
