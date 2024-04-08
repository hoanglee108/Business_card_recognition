import streamlit as st
from PIL import Image
import tempfile
from Extraction import extract_data
import os


def load_image(image_file):
    img = Image.open(image_file)
    return img

def app():
    st.title("Extract Data From A Business Card:card_index:")
    st.image(load_image(r'sources/Scripts/picture.jpg'))
    st.sidebar.success("Home : Extract a business card.")
    st.header("Image Processing")
    image_file = st.file_uploader("Upload an image:arrow_heading_down:", type=["png", "jpg", "jpeg"])  # Fixed the file types here
    if image_file is not None:
        file_details = {"File name": image_file.name, "File type": image_file.type, "File size": image_file.size}
        st.write("Image details")
        st.write(file_details)
        st.write("Uploaded image")
        a = load_image(image_file)
        st.image(a, caption="Business card")
        option = st.radio("Extract information from image:", (" ", "Yes", "No"))
        if option == 'Yes':
            temp_directory = tempfile.TemporaryDirectory()  # Tạo thư mục tạm thời
            file_path = os.path.join(temp_directory.name, image_file.name)
            with open(file_path, "wb") as f:
                f.write(image_file.getbuffer())
                st.success("File Processing 🎈")
            extract_data(file_path)