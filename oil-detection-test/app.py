import streamlit as st
from PIL import Image
from detect import detect_oil_spill

st.set_page_config(page_title="Deteksi Tumpahan Minyak di Laut", layout="wide")

st.markdown("<h1 style='text-align: center;'>Deteksi Tumpahan Minyak di Laut</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Choose File")
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="*Menampilkan gambar dari hasil input Choose File*", use_column_width=True)
    else:
        st.image("https://via.placeholder.com/300x200.png?text=Belum+ada+gambar", caption="*Menampilkan gambar dari hasil input Choose File*", use_column_width=True)

with col2:
    st.markdown("### Hasil Deteksi")
    if uploaded_file and st.button("Hasil Deteksi"):
        result_img, detected = detect_oil_spill(image)
        st.image(result_img, caption="*Menampilkan gambar dari input yang sudah terdeteksi oleh YOLOv8*", use_column_width=True)
        if detected:
            output_text = "gambar terdeteksi ada tumpahan minyak"
        else:
            output_text = "gambar tidak terdeteksi ada tumpahan minyak"
    else:
        st.image("https://via.placeholder.com/300x200.png?text=Belum+ada+deteksi", caption="*Menampilkan gambar dari input yang sudah terdeteksi oleh YOLOv8*", use_column_width=True)

with col3:
    st.markdown("### Teks Penjelasan:")
    if uploaded_file and st.button("Tampilkan Penjelasan", key="penjelasan"):
        st.write(output_text)
    else:
        st.write("Silakan unggah gambar dan klik tombol 'Hasil Deteksi' untuk melihat penjelasan.")
