import cv2 as cv
import numpy as np
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.FaceMeshModule import FaceMeshDetector

LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249,
            263, 466, 388, 387, 386, 385, 384, 398]

RIGHT_EYE = [263, 466, 388, 387, 386, 385, 384, 398,
             362, 382, 381, 380, 374, 373, 390, 249]

detector = FaceDetector()
meshdetector = FaceMeshDetector(maxFaces=1)

face_img = cv.imread('Images/face_hd.jpg')
# img = cv.resize(face_img, (640, 480))  
face_img2 = face_img.copy()


face_img, bbox = detector.findFaces(face_img)
face_img, faces = meshdetector.findFaceMesh(face_img)

def process_eye(points, img):
    (ex, ey, ew, eh) = cv.boundingRect(points)
    eye_roi = img[ey:ey+eh, ex:ex+ew]
    eye_roi_gray = cv.cvtColor(eye_roi, cv.COLOR_BGR2GRAY)
    _, iris = cv.threshold(eye_roi_gray, 40, 255, cv.THRESH_BINARY_INV)
    contours, _ = cv.findContours(iris, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv.contourArea(x), reverse=True)
    
    if contours:
        (ix, iy, iw, ih) = cv.boundingRect(contours[0])
        ix_center, iy_center = ix+int(iw/2)+ex, iy+int(ih/2)+ey
        cv.circle(img, (ix_center, iy_center), 10, (0, 0, 255), -1)
        ix_center_e = ix + int(iw/2)
        
        if ix_center_e > int(ew/2):
            print("right")
        else:
            print("left")
    return eye_roi


if bbox:
    
    if faces:
        left_eye_point = np.array([[faces[0][p][0], faces[0][p][1]] for p in LEFT_EYE])
        right_eye_point = np.array([[faces[0][p][0], faces[0][p][1]] for p in RIGHT_EYE])

        eye_roi_left = process_eye(left_eye_point, face_img2)
        eye_roi_right = process_eye(right_eye_point, face_img2)
        
        cv.imwrite("Images/left_eye.jpg", eye_roi_left)
        cv.imwrite("Images/right_eye.jpg", eye_roi_right)
