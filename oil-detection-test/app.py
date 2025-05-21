import streamlit as st
from PIL import Image
import numpy as np
from ultralytics import YOLO

# Load model hasil training (ganti dengan nama file hasilmu)
model = YOLO("best.pt")

st.title("Deteksi Tumpahan Minyak di Laut")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Choose File")
    uploaded_file = st.file_uploader("Upload Gambar", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption="Gambar Asli", use_column_width=True)

with col2:
    st.markdown("### Hasil Deteksi")
    if uploaded_file is not None:
        img_array = np.array(image)
        results = model.predict(source=img_array, save=False, conf=0.25)
        result_img = results[0].plot()
        st.image(result_img, caption="Hasil Deteksi", use_column_width=True)

with col3:
    st.markdown("### Teks Penjelasan:")
    if uploaded_file is not None:
        detected_classes = [model.model.names[int(cls)] for cls in results[0].boxes.cls]
        if "tumpahan minyak" in detected_classes:
            st.write("Gambar terdeteksi ada tumpahan minyak.")
        else:
            st.write("Gambar tidak terdeteksi ada tumpahan minyak.")
