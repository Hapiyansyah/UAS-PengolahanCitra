| Nama  |  Nim | Kelas |
| ------------- | ------------- |------------- |
| Mohammad Hapiyansyah  | 312210243 | TI 22 A2 |
| Mohammad Ryamizar Ryopa Sakti  | 312210185 | TI 22 A2 |

## Penjelasan Proyek Segmentasi Gambar Menggunakan K-Means dan Streamlit

### Deskripsi Proyek
Aplikasi ini memungkinkan pengguna untuk mengunggah gambar, memilih jumlah cluster untuk segmentasi, dan kemudian melihat hasil segmentasi serta persentase warna yang ada pada gambar. Warna-warna tersebut akan dikenali dan ditampilkan dalam bentuk kotak warna beserta nama warna dan persentase kemunculannya.

### Struktur Kode

1. **Import Library yang Dibutuhkan**
   - `streamlit`: Untuk membuat antarmuka web.
   - `cv2` dan `numpy`: Untuk manipulasi dan pengolahan gambar.
   - `KMeans` dari `sklearn.cluster`: Untuk melakukan segmentasi gambar menggunakan algoritma K-Means.
   - `PIL.Image`: Untuk memuat gambar.
   - `scipy.spatial.distance`: Untuk menghitung jarak Euclidean antara warna.

2. **Daftar Warna dan Nama Warna**
   - Daftar warna ini digunakan untuk mengenali dan menampilkan warna-warna dominan yang ada pada gambar setelah disegmentasi.

3. **Fungsi `recognize_color`**
   - Fungsi ini menerima nilai RGB dan mencari nama warna yang paling dekat dengan nilai RGB tersebut menggunakan jarak Euclidean.

4. **Fungsi `load_image`**
   - Fungsi ini digunakan untuk memuat dan mengubah ukuran gambar yang diunggah oleh pengguna.

5. **Fungsi `segment_image`**
   - Fungsi ini melakukan segmentasi gambar menggunakan algoritma K-Means. Gambar diubah menjadi array piksel, lalu dilakukan segmentasi, dan hasilnya dikembalikan dalam bentuk gambar yang telah disegmentasi, label tiap piksel, dan pusat cluster.

6. **Fungsi `calculate_color_percentages`**
   - Fungsi ini menghitung persentase kemunculan setiap warna dalam gambar berdasarkan label hasil segmentasi.

7. **Fungsi `display_color_percentages`**
   - Fungsi ini menampilkan warna-warna dominan beserta persentase kemunculannya dalam bentuk kotak warna dan teks di antarmuka Streamlit.

8. **Antarmuka Streamlit**
   - Bagian ini berisi kode untuk membuat antarmuka web. Pengguna dapat mengunggah gambar, memilih jumlah cluster, dan melihat hasil segmentasi serta persentase warna yang ada pada gambar.

### Langkah-Langkah Menjalankan Aplikasi

1. **Clone atau Download Repository ini, lalu buka terminal dan jalankan perintah berikut:**
   ```bash
   git clone https://github.com/Hapiyansyah/UAS-PengolahanCitra.git
   ```
   ```
   cd UAS-PengolahanCitra
   ```
3. **Instal dependensi yang dibutuhkan dengan menjalankan perintah berikut di terminal:**
    ```bash
    pip install streamlit scikit-learn opencv-python pillow scipy
    ```

4. **Jalankan aplikasi Streamlit dengan perintah berikut:**
    ```bash
    streamlit run app.py
    ```
5. **Aplikasi Streamlit akan terbuka di browser Anda. Anda dapat mengunggah gambar, memilih jumlah cluster, dan melihat hasil segmentasi serta warna-warna yang ada beserta persentase.**

### Tampilan Aplikasi

**Tampilan Halaman**
![halaman](pict/halaman.png)

**Tampilan Gambar Asli**
!

**Tampilan Gambar Tersegmentasi**
!

**Tampilan Persentase Warna**
!
