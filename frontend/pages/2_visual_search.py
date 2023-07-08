import os
import json
from PIL import Image
import streamlit as st

from azure import *


def fetch_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

# Streamlit app
st.title("Visual Search with Azure Computer Vision using Field Image")

image_file = st.file_uploader("Choose a Image",type=['png','jpg'])

if image_file is not None:
    with open(os.path.join("upload_files",image_file.name),"wb") as f: 
      f.write(image_file.getbuffer())  

    test_image = Image.open(image_file)
    st.image(test_image)

    img_path = "./upload_files/"+image_file.name
    nobackground_image = ""

    with open("img_embeddings.json") as f:
            list_emb = json.load(f)
    
    if st.button("Remove Backgound"):
        nobackground_image = remove_background(img_path)
        st.image(nobackground_image)
    
    if st.button("Get Similar Images"):
        image_files = fetch_files("./fashion_dataset")
        results = get_results_using_image_custom("./without_background.jpg", image_files, list_emb, topn=6, disp=True)
        
        # Display results
        for i in range(0, len(results), 3):
            row_images = results[i:i + 3]
            row = st.columns(3)
            for j, data in enumerate(row_images):
                with row[j]:
                    st.image(data[0], use_column_width=True)
                    st.write("Similarity Index: ", data[1])


    
