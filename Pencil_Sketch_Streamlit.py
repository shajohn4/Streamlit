import streamlit as st
import numpy as np
from PIL import Image
import cv2


def dodgeV2(x, y):
    return cv2.divide(x, 255-y, scale=256)


def pencilsketch(input_image):
    # img = cv2.imread(input_image)
    img_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_gaussian = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_gaussian)
    return(final_img)


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("This is a pencil sketcher program")
st.write("Convert your picture into pencil sketch")
img = st.sidebar.file_uploader("Upload Your Image", type=['jpeg', 'jpg'])

if img is None:
    print("Please upload an image to process")
else:
    image_var = Image.open(img)
    sketch_image = pencilsketch(np.array(image_var))
    st.write("Uploaded Image")
    st.image(img, use_column_width=True)
    st.write("Sketch Image")
    st.image(sketch_image, use_column_width=True)

st.write("Courtesy:-")
st.write("1LittleCoder and AskASwiss")
