import numpy as np

def extract_landmarks(hand_lm):
    features=[]

    for lm in hand_lm:
        features.append(lm.x)
        features.append(lm.y)

    return np.array(features)