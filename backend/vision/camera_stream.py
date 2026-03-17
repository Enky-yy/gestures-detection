import cv2 as cv

class CameraStream:

    def __init__(self, camera_id =0):
        self.cap = cv.VideoCapture(camera_id)

    def read(self):
        ret , frame = self.cap.read()
        if not ret:
            return None
        return frame
    
    def release(self):
        self.cap.release()