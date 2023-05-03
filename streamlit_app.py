import streamlit as st
from pymongo import MongoClient
from bson.binary import Binary
import os

def process_form_data(name, username, college, images, caption, verification):
    MONGO_URI = "mongodb+srv://bonditcommunities:4vvwgomYBtMSkwkE@cluster0.rrr56f3.mongodb.net/?retryWrites=true&w=majority"

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
        "caption": caption,
        "verification": verification,
        "images": image_binaries
    }

    collection.insert_one(document)

def main():
    st.title("University Post Submission")
    colleges = ["larmar2027"]

    name = st.text_input("Name")
    username = st.text_input("Username")
    college = st.selectbox("Select your college", options=colleges)
    caption =  st.text_area("Post caption")
    verification = st.text_area("Paste in your college acceptance email for cornfirmation.")
    images = st.file_uploader("Upload images", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    if st.button("Post"):
        if name and username and college and images and caption and verification:
            process_form_data(name, username, college, images, caption, verification)
            st.success("Post submitted. Expect to see yout post in 24 hours!")
        else:
            st.error("Please fill in all the fields and upload at least one image.")
 

if __name__ == "__main__":
    main()
