import streamlit as st
import cv2
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
from scipy.spatial import distance

# Daftar warna dan nama warna
colors = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "White": (255, 255, 255),
    "Black": (0, 0, 0),
    "Yellow": (255, 255, 0),
    "Cyan": (0, 255, 255),
    "Magenta": (255, 0, 255),
    "Gray": (128, 128, 128),
    "Orange": (255, 165, 0),
    "Pink": (255, 192, 203),
    "Purple": (128, 0, 128),
    "Brown": (165, 42, 42),
    "Lime": (0, 255, 0),
    "Olive": (128, 128, 0),
    "Maroon": (128, 0, 0),
    "Navy": (0, 0, 128),
    "Teal": (0, 128, 128),
    "Silver": (192, 192, 192),
    "Gold": (255, 215, 0),
    "Lavender": (230, 230, 250),
    "Beige": (245, 245, 220),
    "Coral": (255, 127, 80),
    "Salmon": (250, 128, 114),
    "Khaki": (240, 230, 140),
    "Turquoise": (64, 224, 208),
    "Violet": (238, 130, 238),
    "Indigo": (75, 0, 130),
    "Chartreuse": (127, 255, 0),
    "Aquamarine": (127, 255, 212),
    "Periwinkle": (204, 204, 255),
    "Amber": (255, 191, 0),
    "Mint": (189, 252, 201),
    "Apricot": (251, 206, 177),
    "Crimson": (220, 20, 60),
    "Fuchsia": (255, 0, 255),
    "Orchid": (218, 112, 214),
    "Sienna": (160, 82, 45),
    "Azure": (240, 255, 255),
    "Cerulean": (0, 123, 167),
    "Rose": (255, 0, 127),
    "Mauve": (224, 176, 255),
}

# Fungsi untuk mengenali warna berdasarkan nilai RGB
def recognize_color(rgb_value):
    min_distance = float('inf')
    color_name = None
    for name, color in colors.items():
        dist = distance.euclidean(rgb_value, color)
        if dist < min_distance:
            min_distance = dist
            color_name = name
    return color_name

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

# Fungsi untuk menampilkan warna sebagai kotak dengan teks persentase
def display_color_percentages(percentages, centers):
    st.write("Persentase Warna Setiap Segmen:")
    for i, (percent, color) in enumerate(zip(percentages, centers)):
        color_name = recognize_color(color)
        color_hex = '#{:02x}{:02x}{:02x}'.format(int(color[0]), int(color[1]), int(color[2]))
        color_patch = f"background-color: {color_hex}; width: 50px; height: 50px; display: inline-block; margin-right: 10px; border: 1px solid #000;"
        st.markdown(f'<div style="{color_patch}"></div><span>Segmen {i+1} ({color_name}): {percent:.2f}%</span>', unsafe_allow_html=True)

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
        display_color_percentages(percentages, centers)
