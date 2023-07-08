import os
import streamlit as st

from azure_vision import dataset_quality_report, describe_image_with_AzureCV4


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

        image_description = describe_image_with_AzureCV4(image_path)
        st.write("image: " + image_path)

        st.write("Main caption:")
        st.write(f"{image_description['mainCaption']} = {image_description['mainCaptionResult']:.3f}")

        st.write("   Detected tags:")
        for tag in image_description['detectedTags']:
            st.write(f"{tag['name']} = {tag['confidence']:.3f}")


def display_image_catalog():
    list_of_files = fetch_files("./fashion")
    images = list_of_files[0:15]

    st.title("Images catalog")

    for i in range(0, len(images), 3):
        row_images = images[i:i + 3]
        row = st.columns(3)
        for j, image in enumerate(row_images):
            with row[j]:
                display_image_with_button(image)


def display_dataset_report():
    resp = dataset_quality_report("./dataset")

    st.write(resp.report)
    st.write(resp.summary)


display_image_catalog()
display_dataset_report()
