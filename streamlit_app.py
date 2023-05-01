import streamlit as st
from pymongo import MongoClient
from bson.binary import Binary
import os

def process_form_data(name, username, college, images):

    MONGO_URI = os.environ.get('MONGO_URI')
    client = MongoClient(MONGO_URI)
    db = client['Posts']
    collection = db['PendingPosts']

    image_binaries = []
    for image in images:
        if image.name.endswith(('.png', '.jpg', '.jpeg')):
            image_binary = Binary(image.read())
            image_binaries.append(image_binary)

    document = {
        "name": name,
        "username": username,
        "college": college,
        "images": image_binaries
    }

    collection.insert_one(document)

def main():
    st.title("College Post Submission")

    colleges = ["college1", "argmin"]

    name = st.text_input("Name")
    username = st.text_input("Username")
    college = st.selectbox("Select your college", options=colleges)
    images = st.file_uploader("Upload images", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    if st.button("Submit"):
        if name and username and college and images:
            process_form_data(name, username, college, images)
            st.success("Form submitted successfully!")
        else:
            st.error("Please fill in all the fields and upload at least one image.")

if __name__ == "__main__":
    main()
