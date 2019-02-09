# Import OpenCV2 for image processing
import cv2
import os
import time


#start=time.time()
#period=100
def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
         os.makedirs(dir)
face_id=input('Enter your id ')
#print('kjjjjjjk')
# Start capturing video 
vid_cam = cv2.VideoCapture(0)

#print('kjppjjjjjk')

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize sample face image
count = 0

assure_path_exists("dataset/")
#print('kjppjmmjjjjk')

# Start looping
while(True):
    

    # Capture video frame
    _, image_frame = vid_cam.read()

    #print('kjppjjmmnnjjjk')
    # Convert frame to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    #print('kjppjjbbnnjjjk')
#print('kjppjjmmnnjjjk')

    # Loops for each faces
    for (x,y,w,h) in faces:

        # Crop the image frame into rectangle
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
        #print('kjppjjabnnjjjk')

        # Increment sample face image
        count += 1
        
        #print('kjppjjabnnjjjk')
        
        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
#        cv2.imwrite("dataset/"+str(id) +"." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)

    # To stop taking video, press 'q' for at least 100ms1
   # if cv2.waitKey(500) & 0xFF == ord('q'):
    #    break

  #  if time.time()>start+period:
  #      break;
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break;

    # If image taken reach 100, stop taking video
    elif count>=20:
        print("Successfully Captured!")
        break

# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()
