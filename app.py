import streamlit as st
import tempfile
import os
from functions import detect_faces, hex_to_rgb
import cv2

cap = cv2.VideoCapture(0)

st.title("Webcam Face Detector")

# Instructions for the user
st.markdown("### Instructions:")
st.write("1. Click the 'Start' button to activate your webcam.")
st.write("2. Click the 'Capture' button to take a photo and only shows after clicking 'Start'")
st.write("3. Adjust the parameters as needed.")
st.write("4. Detected faces will be highlighted.")
st.write("5. Click the 'Save Image' button to save the image with detected faces.")

# Parameters
min_neighbors = st.slider("Minimum Neighbors", min_value=1, max_value=10, value=5, step=1)
scale_factor = st.slider("Scale Factor", min_value=1.01, max_value=2.0, value=1.1, step=0.01)
color_picker = st.color_picker("Choose color for rectangles", "#ff0000")

frame_placeholder = st.empty()

start_button = st.button("Start")

if 'detectu' not in st.session_state:
    st.session_state.detectu = None

# Detect faces and display the image
if start_button:
    stop_button_pressed = st.button('Capture')
    while cap.isOpened():
        rgb_color = hex_to_rgb(color_picker)
        detected_image = detect_faces(cap, scale_factor, min_neighbors, rgb_color)
        st.session_state.detectu = detected_image
        frame_placeholder.image(detected_image, channels='RGB')
        if stop_button_pressed:
            break
        
    cap.release()   
     
show_image = st.button('Show Image')

try:
    if show_image:
        # Display the saved image
        st.image(st.session_state.detectu, channels="RGB", caption="Captured Image")
except AttributeError:
    st.error('Press the start button first')
        
save_image = st.button('Save Image')

try:
    if save_image: 
        
        # Save the captured image
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file = os.path.join(temp_dir, "captured_image.jpg")
            if st.session_state.detectu.any():
                cv2.imwrite(temp_file, st.session_state.detectu)
            else:
                raise KeyError('to click start first')
            st.success(f"Image saved successfully: {temp_file}")
except KeyError:
    st.error('No captured image to save')
    

        
    



            
