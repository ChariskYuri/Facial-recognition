import face_recognition
import pickle
import cv2
import pathlib
import os

print("[INFO] quantifying faces...")
data_dir = pathlib.Path('Final_v3')
imagePaths = list(data_dir.rglob('*/*'))

known_encodings = []
known_names = []

for (i, imagePath) in enumerate(imagePaths):
    print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))
    name = os.path.basename(os.path.dirname(imagePath)).replace(' ', '_')

    image = cv2.imread(str(imagePath))
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb, model='cnn')
    encodings = face_recognition.face_encodings(rgb, boxes)

    for encoding in encodings:
        known_encodings.append(encoding)
        known_names.append(name)

print('Done part 1.')