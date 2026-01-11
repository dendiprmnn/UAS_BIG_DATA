🚀 UAS_BIG_DATA - Analisis Pelayanan Publik Berbasis Big Data
📋 Deskripsi Proyek
Proyek ini merupakan sistem analisis sentimen publik terhadap pelayanan kesehatan dengan mengintegrasikan data dari media sosial (Twitter) dan data pemerintah. Dibangun menggunakan pendekatan Big Data dengan visualisasi dashboard interaktif.

🛠️ Teknologi yang Digunakan
Python 3.8+

Streamlit - Dashboard interaktif

Pandas - Manipulasi data

Scikit-learn - Machine Learning (Naïve Bayes)

NetworkX - Analisis jejaring sosial

Matplotlib - Visualisasi data

⚡ Langkah-langkah Menjalankan Proyek
1. Install Library yang Diperlukan

pip install streamlit pandas scikit-learn networkx matplotlib

2. Jalankan Script Analisis Data (URUTAN PENTING!)
# 1. Pembersihan data tweet
python src/cleaning.py

# 2. Analisis sentimen dengan machine learning
python src/sentiment_model.py

# 3. Analisis jejaring sosial
python src/network_analysis.py

3. Jalankan Dashboard Streamlit

streamlit run src/app.py

4. Akses Dashboard
Buka browser dan kunjungi: http://localhost:8501

🔧 Penjelasan Script
cleaning.py
Membersihkan data tweet dari karakter tidak penting

Mengubah teks menjadi lowercase

Menghasilkan file twitter_clean.csv

sentiment_model.py
Menggunakan algoritma Naïve Bayes untuk klasifikasi sentimen

Labeling otomatis berdasarkan kata kunci negatif

Menghasilkan file twitter_sentiment.csv

network_analysis.py
Membangun jaringan antara pengguna dan kata kunci penting

Kata kunci: bpjs, rumah sakit, pelayanan, antrian

Menghasilkan file sna_edges.csv untuk visualisasi network

app.py
Dashboard utama dengan Streamlit

Layout responsive dengan sidebar filter

Multiple visualizations dalam satu tampilan
