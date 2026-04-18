import cv2 as cv
import mediapipe as mp

img = cv.imread('man.png')

H, W, _ = img.shape

mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    if out.detections is not None:
        for detection in out.detections:
            bbox = detection.location_data.relative_bounding_box

            x1 = int(bbox.xmin * W)
            y1 = int(bbox.ymin * H)
            w  = int(bbox.width * W)
            h  = int(bbox.height * H)

            # draw rectangle
            cv.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)

    cv.imshow("img", img)
    cv.waitKey(0)
    cv.destroyAllWindows()