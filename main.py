import cv2 as cv
import mediapipe as mp

img = cv.imread('man.png')

mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    print(out.detections)

# cv.imshow("img",img)
# cv.waitKey(0)
#
#
# cv.destroyAllWindows()