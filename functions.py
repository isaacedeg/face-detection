import cv2


def detect_faces(vidCapture, scaleFactor, minNeighbors, color):
    # Load the pre-trained Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Initialize the webcam
    cap = vidCapture
    
    # Read the frames from the webcam
    ret, frame = cap.read()
    
    # Convert the frames to grayscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Detect the faces using the face cascade classifier
    faces = face_cascade.detectMultiScale(frame, scaleFactor=scaleFactor, minNeighbors=minNeighbors)
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
    # Display the frames
    return frame

def hex_to_rgb(hex_color):
    # Remove '#' if present
    hex_color = hex_color.lstrip('#')
    
    # Convert hexadecimal to RGB
    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    return rgb_color

