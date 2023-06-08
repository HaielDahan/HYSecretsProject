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

import file_reader as fr
def Home():
    st.write("<h1 style='position:absolute; top:20%; left:60%; transform:translate(-50%, -50%);'>Welcome""</h1>",
             unsafe_allow_html=True)
    st.write("<h1 style='position:absolute; top:60%; left:60%; transform:translate(-50%, -50%);'>HYSecrets</h1>",
             unsafe_allow_html=True)
    # st.title("Welcome")

    st.markdown(
        """
        <style>
        .image {
            position: absolute;
            top: 50%;
            left: 60%;
            transform: translate(-50%, -50%);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.image("Backround/home page.jpg", width=350)



def Encryption():
    st.write("Please select an image to encrypt")
    st.session_state.text = ""
    st.session_state.text = st.text_input('Enter your message', max_chars=None ,value=st.session_state.text, key="1")

    uploaded_file = st.file_uploader("Upload a photo", type=["png"], key="uploader1")
    image_path=""
    if uploaded_file is not None:
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
                print(new_string)
                image_name = image_path.split('\\')[-1]
                print(image_path)
                new_path = new_string + "\\testFolder\\" + image_name
                print(new_path)
                im.save(new_path)

            except:

                # add original image to testFolder
                new_string = image_path.rsplit("/", 1)[0]
                print(new_string)
                image_name = image_path.split('/')[-1]
                print(image_path)
                new_path = new_string + "/testFolder/" + image_name
                print(new_path)
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

        if st.button('Download Processed Image'):
            processed_img = st.session_state['pic']

            if processed_img is not None:
                buffered = BytesIO()
                metadata = PngInfo()
                metadata.add_text("Number", str(processed_img.text.get('Number')))
                processed_img.save(buffered, format="PNG", pnginfo=metadata)
                val = buffered.getvalue()
                st.download_button(
                    label="Download",
                    data=val,
                    file_name='processed_image.png',
                    mime='image/PNG'
                )

            else:
                st.warning("No processed image found. Please click on 'Send' to process the image first.")

        os.remove(st.session_state['path'])


def Decryption():
    st.write("Please select an image to decode")
    uploaded_file = st.file_uploader("Upload a photo", type=["png"],  key="uploader2")
    if uploaded_file is not None:
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
    if st.button('Run StegExpose'):
        sepython.py_stegExpose()
        df = pd.read_csv("check.csv")

        # create animated bar chart
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('File name', title='File name'),
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
        arr = np.random.normal(1, 1, size=100)
        fig, ax = plt.subplots()
        # ax.hist(arr, bins=20)
        st.pyplot(fig)
    # arr = np.random.normal(1, 1, size=100)
    # fig, ax = plt.subplots()
    # ax.hist(arr, bins=20)
    #
    # st.pyplot(fig)


def Sidebar():
    st.sidebar.title("HYSecrets option:")
    with st.sidebar:
        st.image("banner-image-2.png", width=200)
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
# --------------------------------------------------------------------------#

# # Create download button
# if st.button('Download Processed Image'):
#     buffered = BytesIO()
#     processed_img.save(buffered, format="PNG")
#     val = buffered.getvalue()
#     st.download_button(
#         label="Download",
#         data=val,
#         file_name='processed_img.png',
#         mime='image/PNG'
#     )

# --------------------------------------------------------------------------#


#------------------לבדוק את האופציה הזאת-----------
# Read data from an Excel file
# data = pd.read_excel('example.xlsx')
#
# Select the columns you want to plot
# x = data['x']
# y = data['y']
#
# # Create a new figure and axis object using matplotlib's subplots() function
# fig, ax = plt.subplots()
#
# # Create a line plot of the selected data using matplotlib's plot() function
# ax.plot(x, y)
#
# # Set the x and y axis labels using matplotlib's set_xlabel() and set_ylabel() functions
# ax.set_xlabel('X Axis Label')
# ax.set_ylabel('Y Axis Label')
#
# # Display the plot using Streamlit's st.pyplot() function
# st.pyplot(fig)
 #-----------------------------לבדוק גם את זאת זאת הטובה יותר ---------
# # Read data from an Excel file
# data = pd.read_excel('example.xlsx')
#
# # Select the columns you want to plot
# x = data['x']
# y = data['y']
#
# # Create a new figure and axis object using matplotlib's subplots() function
# fig, ax = plt.subplots()
#
# # Create a line plot of the selected data using matplotlib's plot() function
# ax.plot(x, y)
#
# # Set the x and y axis labels using matplotlib's set_xlabel() and set_ylabel() functions
# ax.set_xlabel('X Axis Label')
# ax.set_ylabel('Y Axis Label')
#
# # Set the x and y axis tick values using matplotlib's set_xticks() and set_yticks() functions
# ax.set_xticks([i/10 for i in range(11)])
# ax.set_yticks([i/10 for i in range(11)])
#
# # Display the plot using Streamlit's st.pyplot() function
# st.pyplot(fig)

# arr = np.random.normal(1, 1, size=100)
# fig, ax = plt.subplots()
# ax.hist(arr, bins=20)
# st.pyplot(fig)