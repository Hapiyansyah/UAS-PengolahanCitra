import streamlit as st
import cv2
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd

# Fungsi untuk membaca dan mengubah ukuran gambar
def load_image(image_file):
    img = Image.open(image_file)
    return img

# Fungsi untuk segmentasi gambar menggunakan K-Means dan mengembalikan hasilnya
def segment_image(image, k):
    image = np.array(image)
    pixel_values = image.reshape((-1, 3))
    pixel_values = np.float32(pixel_values)

    # Implementasi K-Means
    kmeans = KMeans(n_clusters=k, random_state=0)
    labels = kmeans.fit_predict(pixel_values)
    centers = kmeans.cluster_centers_

    # Konversi kembali pusat cluster ke tipe data uint8
    centers = np.uint8(centers)
    segmented_image = centers[labels.flatten()]

    # Bentuk ulang gambar kembali ke ukuran asli
    segmented_image = segmented_image.reshape(image.shape)
    
    return segmented_image, labels, centers

# Fungsi untuk menghitung persentase setiap warna
def calculate_color_percentages(labels, centers):
    label_counts = np.bincount(labels)
    total_count = len(labels)
    
    percentages = (label_counts / total_count) * 100
    return percentages

# Fungsi untuk menampilkan warna sebagai kotak
def plot_colors(percentages, centers):
    fig, ax = plt.subplots(figsize=(8, 4))

    # Buat bar warna
    for i, (percent, color) in enumerate(zip(percentages, centers)):
        ax.barh(i, percent, color=np.array(color / 255).reshape(1, -1))
        
    ax.set_yticks(range(len(centers)))
    ax.set_yticklabels([f"Color {i+1}" for i in range(len(centers))])
    ax.set_xlabel('Percentage')
    ax.set_xlim(0, 100)
    
    st.pyplot(fig)

# Pembuatan antarmuka Streamlit
st.title("Segmentasi Gambar Menggunakan K-Means")
st.write("Unggah gambar dan pilih jumlah cluster untuk melakukan segmentasi.")

# Unggah gambar
image_file = st.file_uploader("Unggah gambar", type=["jpg", "jpeg", "png"])

if image_file is not None:
    image = load_image(image_file)
    st.image(image, caption='Gambar yang diunggah.', use_column_width=True)

    k = st.slider("Pilih jumlah cluster (k)", 1, 20, 4)

    if st.button("Segmentasi Gambar"):
        segmented_image, labels, centers = segment_image(image, k)
        st.image(segmented_image, caption='Gambar yang telah disegmentasi.', use_column_width=True)
        
        percentages = calculate_color_percentages(labels, centers)
        plot_colors(percentages, centers)

        # Buat tabel untuk menampilkan warna dan persentasenya
        colors_df = pd.DataFrame({
            'Color': [f"Color {i+1}" for i in range(len(centers))],
            'Percentage': percentages
        })
        
        st.write(colors_df)
