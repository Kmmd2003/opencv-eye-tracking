import cv2 as cv
import numpy as np
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.FaceMeshModule import FaceMeshDetector

LEFT_EYE = [33, 246, 161, 160, 159, 158, 157, 173,
            133, 155, 154, 153, 145, 144, 163, 7]

RIGHT_EYE = [362, 382, 381, 380, 374, 373, 390, 249,
             263, 466, 388, 387, 386, 385, 384, 398]


detector = FaceDetector()
meshdetector = FaceMeshDetector(maxFaces=1)

def process_eye(points, img):
    (ex, ey, ew, eh) = cv.boundingRect(points)
    eye_roi = img[ey:ey+eh, ex:ex+ew]
    eye_roi_gray = cv.cvtColor(eye_roi, cv.COLOR_BGR2GRAY)
    _, iris = cv.threshold(eye_roi_gray, 25, 255, cv.THRESH_BINARY_INV)
    contours, _ = cv.findContours(iris, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv.contourArea(x), reverse=True)
    
    if contours:
        (ix, iy, iw, ih) = cv.boundingRect(contours[0])
        ix_center, iy_center = ix+int(iw/2)+ex, iy+int(ih/2)+ey
        cv.circle(img, (ix_center, iy_center), 10, (0, 0, 255), -1)
        offset = 12
        ix_center_e = ix + int(iw/2)
        
        if ix_center_e > int(ew/2)+offset:
            text = ("right")
        elif ix_center_e < int(ew/2)-offset:
            text = ("left")
        else:
            text = ("center")
            
        cv.putText(frame2, text, (100, 100), cv.FONT_HERSHEY_PLAIN, 3, (0, 60, 0), 2)

    return eye_roi

cap = cv.VideoCapture("Videos/eye_tracker3.mp4")

if(cap.isOpened() == False):
    print("Error opening video stream or file")
    
while(cap.isOpened()):
    ret, frame = cap.read()
    
    if not ret:
        break
    
    frame2 = frame.copy()
    
    if ret == True:
        face_img, bbox = detector.findFaces(frame)
        face_img, faces = meshdetector.findFaceMesh(frame)
        
        if bbox:
            center = bbox[0]['center']
            
            if  faces:
                 left_eye_point = np.array([[faces[0][p][0], faces[0][p][1]] for p in LEFT_EYE])
                 right_eye_point = np.array([[faces[0][p][0], faces[0][p][1]] for p in RIGHT_EYE])

                 eye_roi_left = process_eye(left_eye_point, frame2)
                 eye_roi_right = process_eye(right_eye_point, frame2)
        
                 cv.imwrite("Images/left_eye.jpg", eye_roi_left)
                 cv.imwrite("Images/right_eye.jpg", eye_roi_right)


        cv.imshow('frame2', frame2)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
cv.destroyAllWindows()

