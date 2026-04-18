import cv2 as cv


class Webcam:
    def __init__(self):
        self.cap = cv.VideoCapture(0)

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        self.cap.release()

cap = cv.VideoCapture(0)