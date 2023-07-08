import os
import streamlit as st

from azure import *
from cleanvision.imagelab import Imagelab

# st.title('Assignment 03')


def fetch_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list


def display_image_with_button(image_path):
    col = st.columns(2)
    col[0].image(image_path, use_column_width=True)
    button = col[1].button("Image Analysis", key=image_path)
    if button:

        image_description = describe_image_with_AzureCV4_custom(image_path)
        st.write("image: " + image_path)

        st.write("Main caption:")
        st.write(f"{image_description['mainCaption']} = {image_description['mainCaptionResult']:.3f}")

        st.write("   Detected tags:")
        for tag in image_description['detectedTags']:
            st.write(f"{tag['name']} = {tag['confidence']:.3f}")


def display_image_catalog():
    list_of_files = fetch_files("./fashion_dataset")
    images = list_of_files[0:15]

    st.title("Images catalog")

    for i in range(0, len(images), 3):
        row_images = images[i:i + 3]
        row = st.columns(3)
        for j, image in enumerate(row_images):
            with row[j]:
                display_image_with_button(image)


def display_dataset_report():
    imagelab = Imagelab(data_path="./fashion_dataset")
    imagelab.find_issues()
    st.write("Issues Summary: ", imagelab.issue_summary)


display_image_catalog()

if st.button("Get Summary"):
    display_dataset_report()