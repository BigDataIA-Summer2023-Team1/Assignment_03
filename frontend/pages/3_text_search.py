import json
import streamlit as st

from azure import *
from utils import fetch_files


# Streamlit app
st.title("Image Generation with Prompt")

# Input prompt
user_prompt = st.text_input("Enter a prompt")

with open("img_embeddings.json") as f:
    list_emb = json.load(f)

if st.button("Generate Images"):
    image_files = fetch_files("./fashion_dataset")
    results = get_results_using_prompt_custom(user_prompt, image_files, list_emb, topn=6, disp=True)

     # Display results
    for i in range(0, len(results), 3):
        row_images = results[i:i + 3]
        row = st.columns(3)
        for j, data in enumerate(row_images):
            with row[j]:
                st.image(data[0], use_column_width=True)
                st.write("Similarity Index: ", data[1])
