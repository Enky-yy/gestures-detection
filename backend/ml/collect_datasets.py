import cv2
import mediapipe as mp
import csv
import os

DATASET_PATH = "../../datasets/gesture_dataset.csv"

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)

gesture_label = input("Enter gesture label: ")

data = []

print("Press 's' to save sample")
print("Press 'ESC' to exit")

while True:

    ret, frame = cap.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    landmarks = []

    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]

        for lm in hand.landmark:
            landmarks.append(lm.x)
            landmarks.append(lm.y)

        cv2.putText(frame, gesture_label,(10,50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,(0,255,0),2)

    cv2.imshow("Gesture Dataset Collector", frame)

    key = cv2.waitKey(1)

    if key == ord("s") and landmarks:

        row = [gesture_label] + landmarks
        data.append(row)

        print("Sample saved")

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

# Save dataset
os.makedirs("../../datasets", exist_ok=True)

with open(DATASET_PATH,"a",newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Dataset saved to:", DATASET_PATH)