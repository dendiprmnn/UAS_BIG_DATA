# 🚀 UAS_BIG_DATA  
## Analisis Pelayanan Publik Berbasis Big Data

---

## 📋 Deskripsi Proyek
Proyek ini merupakan sistem **analisis sentimen publik terhadap pelayanan kesehatan** dengan mengintegrasikan data dari **media sosial (Twitter)** dan **data pemerintah**.  
Sistem dibangun menggunakan pendekatan **Big Data** dan disajikan melalui **dashboard interaktif** untuk memudahkan visualisasi dan analisis data.

---

## 🛠️ Teknologi yang Digunakan
- **Python 3.8+**
- **Streamlit** — Dashboard interaktif
- **Pandas** — Manipulasi data
- **Scikit-learn** — Machine Learning (Naïve Bayes)
- **NetworkX** — Analisis jejaring sosial
- **Matplotlib** — Visualisasi data

---

## ⚡ Langkah-langkah Menjalankan Proyek

### 1️⃣ Install Library yang Diperlukan
Jalankan perintah berikut di terminal:

```bash
pip install streamlit pandas scikit-learn networkx matplotlib

### 2️⃣ Jalankan Script Analisis Data

'''bash
python src/cleaning.py

python src/sentiment_model.py

python src/network_analysis.py

### 3️⃣ Jalankan Dashboard Streamlit

'''bash
streamlit run src/app.py

### 4️⃣ Akses Dashboard
Buka browser dan kunjungi:

http://localhost:8501
