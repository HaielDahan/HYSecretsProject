import streamlit as st
from PIL import Image
from io import BytesIO
from streamlit_option_menu import option_menu
import HYS_en as en
import os
import HYS_dec as dec
from PIL.PngImagePlugin import PngInfo

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sepython
import LSB_emb
import SilentEye_emb
import altair as alt

import base64

import file_reader as fr
def Home():
    # st.write("<h1 style='position:absolute; top:90%; left:30%; transform:translate(-50%, -50%);'>Welcome""</h1>",
    #          unsafe_allow_html=True)
    # st.write("<h1 style='position:absolute; top:60%; left:30%; transform:translate(-50%, -25%);'>HYSecrets</h1>",
    #          unsafe_allow_html=True)
    with open("Backround/home_page.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    # image_path = "Backround/home page.jpg"
    # st.markdown(
    #     """
    #     <style>
    #     .image {
    #         position: absolute;
    #         top: 0%;
    #         left: 0%;
    #         transform: translate(-50%, -50%);
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True,
    # )
    # st.image(image_path, width=200)
    # image = Image.open("Backround/home page.jpg")
def Encryption():
    title_html = '''
        <h1 style="font-size: 32px;">🔒 Please select an image to encrypt</h1>
    '''

    st.markdown(title_html, unsafe_allow_html=True)
    st.session_state.text = ""
    st.session_state.text = st.text_input('Enter your message', max_chars=None ,value=st.session_state.text, key="1")
    uploaded_file = st.file_uploader("Upload a photo", type=["png"], key="uploader1")
    image_path=""
    st.session_state['image_en']=0
    if uploaded_file is not None:
        st.session_state['image_en'] = 1
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
            # Get the path of the file you uploaded
            image_path = os.path.abspath(uploaded_file.name)

            st.session_state['path'] = image_path
        # Process image
        # processed_img =Image.open(uploaded_file)
        processed_img = None
        if st.button('Send'):

            # remove testFolder
            folder_path = "testFolder"
            fr.remove_files_in_folder(folder_path)

            # starting encryption
            im = Image.open(image_path)
            try:
                # add original image to testFolder
                new_string = image_path.rsplit("\\", 1)[0]
                #print(new_string)
                image_name = image_path.split('\\')[-1]
                #print(image_path)
                new_path = new_string + "\\testFolder\\" + image_name
                #print(new_path)
                im.save(new_path)

            except:

                # add original image to testFolder
                new_string = image_path.rsplit("/", 1)[0]
                #print(new_string)
                image_name = image_path.split('/')[-1]
                #print(image_path)
                new_path = new_string + "/testFolder/" + image_name
                #print(new_path)
                im.save(new_path)




            # Do something with the message

            processed_img = en.HYS_encoding(image_path, st.session_state.text)
            st.session_state['pic'] = processed_img
            LSB_emb.main(image_path, st.session_state.text)
            SilentEye_emb.main(image_path,st.session_state.text, 3)



            # Clear the text input
            # Display processed image
            st.image(processed_img, caption='Processed Image', use_column_width=True)

            st.session_state.text = ""
            processed_img = st.session_state['pic']

            if processed_img is not None:
                buffered = BytesIO()
                metadata = PngInfo()
                metadata.add_text("Number", str(processed_img.text.get('Number')))
                processed_img.save(buffered, format="PNG", pnginfo=metadata)
                val = buffered.getvalue()
                st.download_button(
                    label="Download processed Image",
                    data=val,
                    file_name='processed_image.png',
                    mime='image/PNG'
                )

            else:
                st.warning("No processed image found. Please click on 'Send' to process the image first.")

        os.remove(st.session_state['path'])
    if st.session_state['image_en']==0:
        col1, col2, col3 = st.columns([1, 6, 1])

        with col1:
            st.write("")

        with col2:
            st.image("Backround/encryption.jpg",width=370)

        with col3:
            st.write("")

def Decryption():
    st.session_state['image_de'] = 0
    title_html = '''
        <h1 style="font-size: 32px;">🔓 Please select an image to decryption</h1>
    '''
    st.markdown(title_html, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload a photo", type=["png"],  key="uploader2")
    if uploaded_file is not None:
        st.session_state['image_de'] = 1
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

            # Get the path of the file you uploaded
            image_path = os.path.abspath(uploaded_file.name)

        # Process image
        my_dec = dec.dec_HYS(image_path)
        processed_img = my_dec[0]


        # Display processed image
        st.image(processed_img, caption='Processed Image', use_column_width=True)

        if st.button('Show hidden information'):
            if (my_dec[1] == "error"):
                st.error("In this image we could not identify hidden information or it was not hidden by our system")
            else:
                st.write(my_dec[1])

        os.remove(image_path)
    if st.session_state['image_de'] == 0:
        col1, col2, col3 = st.columns([1, 6, 1])

        with col1:
            st.write("")

        with col2:
            st.image("Backround/decryption.jpg", width=495)

        with col3:
            st.write("")
        # ------------------------------------------------------------------------------

def About():
    st.write("""
    # 🕵️‍♂️ HYSecrets 🕵️‍♀️

     HYSecrets is an app that allows you to hide and interpret secret messages within an image. 🔒 This app uses a technique called steganography, which involves embedding hidden messages within an image in a way that is not visible to the naked eye. 🤫

     # 👉 How to use HYSecrets
     To use HYSecrets, first select the Encryption or Decoding option from the sidebar. If you select Encryption, you can upload an image and enter a message to hide within the image. HYSecrets will then embed the message within the image and save the resulting image to your computer. If you select Decoding, you can upload an image that has a hidden message, and HYSecrets will reveal the message for you. 🔍

     # 🔍 About steganography
     Steganography is the practice of concealing a message within another message or a file. This technique is often used to hide the fact that a message is being sent, as well as to hide the contents of the message itself. Steganography can be used to hide messages within images, audio files, video files, and more. 🌐

     # ℹ️ About HYSecrets
     HYSecrets is a project developed by [Haiel dahan and Yakir ovadia]. If you have any questions or feedback, please feel free to contact me at [Your Email Address]. 📧

     """)



def SEdata():
    title_html = '''
            <h1 style="font-size: 32px;">📊 StagExpose Data Analysis</h1>
        '''

    st.markdown(title_html, unsafe_allow_html=True)
    if st.button('Run StegExpose'):
        sepython.py_stegExpose()
        df = pd.read_csv("check.csv")

        # create animated bar chart
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('File name', title='File name',axis=alt.Axis(labelAngle=0)),
            y=alt.Y('Fusion (mean)', title='Fusion (mean)'),
            color=alt.Color('File name', legend=None),
            tooltip=['File name', 'Fusion (mean)']
        ).properties(
            width=600,
            height=400,
            title='Comparison of values over time'
        ).transform_window(
            rank='rank(Fusion (mean)',
            sort=[alt.SortField('Fusion (mean)', order='descending')],
            groupby=['timestamp']
        ).transform_filter(
            alt.datum.rank <= 5
        ).transform_window(
            rank='rank(rank)',
            sort=[alt.SortField('rank', order='ascending')],
            groupby=['File name']
        ).transform_filter(
            alt.datum.rank <= 5
        ).transform_window(
            timestamp='row_number()'
        )

        # display chart in Streamlit
        st.altair_chart(chart, use_container_width=True)



    else:
        np.random.normal(0, 1, size=100)
        fig, ax = plt.subplots()
        st.pyplot(fig)


def Sidebar():
    st.sidebar.title("HYSecrets option:")
    with st.sidebar:
        st.image("Backround/banner-image-2.png", width=200)
        choose = option_menu(menu_title="Option :",
                                     options=['Home', 'Encryption', 'Decryption', 'StegExpose data','About'],
                                     icons=['house-door','lock','unlock','bar-chart-line' ,'info-square'], default_index=0)
    # choose = st.sidebar.radio("Choose your option :", ['Home', 'Encryption', 'Decoding', 'About'])
    if choose == 'Home':
        Home()
    elif choose == 'Encryption':
        Encryption()
    elif choose == 'Decryption':
        Decryption()
    elif choose == 'About':
        About()
    else:
        SEdata()


Sidebar()


#######################################################
# def add_bg_from_local(image_file):
#     st.write("<h1 style='position:absolute; top:90%; left:30%; transform:translate(-50%, -50%);'>Welcome""</h1>",
#              unsafe_allow_html=True)
#     st.write("<h1 style='position:absolute; top:60%; left:30%; transform:translate(-50%, -25%);'>HYSecrets</h1>",
#              unsafe_allow_html=True)
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
#             background-size: contain;
#             background-repeat: no-repeat;
#             background-position: center;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )