import streamlit as st
import json

# Tahap 3: Fungsi Backend untuk menyedot data JSON
def load_database():
    with open('database.json', 'r') as file:
        return json.load(file)

buku_ingatan = load_database()

# Setup Layar
st.set_page_config(page_title="Buku AI", layout="wide")

# ==========================================
# TAHAP 4: MERENDER ANTARMUKA VISUAL (UI BARU)
# ==========================================

# --- BAGIAN KIRI (REMOTE CONTROL / NAVIGASI) ---
st.sidebar.header("Daftar Isi 📚")

# 1. Memilih Laci Utama (Bab)
daftar_bab = list(buku_ingatan.keys())
pilihan_bab = st.sidebar.selectbox("Pilih Bab:", daftar_bab)

# Menarik data khusus untuk Bab yang dipilih
data_sub_bab = buku_ingatan[pilihan_bab]
st.sidebar.write("---") # Garis pembatas di sidebar

# 2. Memilih Map Spesifik (Sub-bab) menggunakan Radio Button
daftar_topik = list(data_sub_bab.keys())
pilihan_topik = st.sidebar.radio("Pilih Materi:", daftar_topik)


# --- BAGIAN TENGAH (RUANG BACA KHUSUS) ---
# Layar ini sekarang 100% bersih dari tombol pilihan!

st.title("Buku Pintar Arsitek AI 🤖")
st.subheader(f"📖: {pilihan_bab}")
st.write("---")

# 3. Menampilkan HANYA satu materi yang sedang dipilih di remote control
st.success(f"**{pilihan_topik}**")
st.write(data_sub_bab[pilihan_topik])