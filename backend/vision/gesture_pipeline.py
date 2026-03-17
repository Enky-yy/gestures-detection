from .camera_stream import CameraStream
from .hand_detector import HandDetector
from .landmarks_extractor import extract_landmarks
from backend.ml.inference import predict_gesture

class GesturePipeline:

    def __init__(self):
        self.camera = CameraStream()

        self.detector = HandDetector()

    def process(self):

        frame = self.camera.read()

        hands = self.detector.detect(frame)

        if hands is None:
            return None
        
        for hand in hands:

            features = extract_landmarks(hand)

            gesture = predict_gesture(features)

            return gesture