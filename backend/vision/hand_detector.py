import cv2 as cv
import mediapipe as mp

class HandDetector:

    def __init__(self):
        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence =0.7
        )

    def detect(self , frame):

        rgb = cv.cvtColor(frame , cv.COLOR_BG2BGR)

        results = self.hands.process(frame)
        
        return results.multi_hand_landmarks