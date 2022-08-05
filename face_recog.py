# import pathlib
#
# data_dir = pathlib.Path('Final_v3')
# images = list(data_dir.rglob('*/*'))
# print(images)
import face_recognition
from PIL import Image
image = face_recognition.load_image_file('Final_v3/Nguyễn Trí Anh - K16/275209675_693982151637982_3012759212400866276_n.jpg')
face_locations = face_recognition.face_locations(image)
print(len(face_locations))

for face_location in face_locations:
    top, right, bottom, left = face_location
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
