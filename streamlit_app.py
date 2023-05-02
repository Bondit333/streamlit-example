import streamlit as st
from instagrapi import Client
import os



def login(username, password):
    cl = Client()
    cl.login(username, password)
    return cl

def post_carousel(client, image_paths, caption):
    album = []
    for image_path in image_paths:
        media = client.media_configure_to_image(open(image_path, "rb"))
        album.append(media)
    client.media_album_configure(album, caption)


def process_form_data(name, username, password, college, images):


    imagepaths = []
    for image in images:
        if image.name.endswith(('.png', '.jpg', '.jpeg')):
            imagepaths.append(image)
    
    user = "Rykav333"


    client = login(user, os.environ("PASS"))

    post_carousel(client, imagepaths, "Example Caption")


    
    
def main():
    st.title("Instagram Post Submission")

    colleges = ["larmar2027"]

    name = st.text_input("Name")
    username = st.text_input("Username")
    passcode = st.text_input("Password for the instagram account to upload image (This is a tester box since the password you gave me is incorrect)")
    caption = st.text_area("Enter the caption for your post")
    college = st.selectbox("Select your college", options=colleges)
    images = st.file_uploader("Upload images", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    if st.button("Submit"):
        if name and username and college and images:
            process_form_data(name, username, passcode, college, images)
            st.success("Form submitted successfully!")
        else:
            st.error("Please fill in all the fields and upload at least one image.")

if __name__ == "__main__":
    main()
