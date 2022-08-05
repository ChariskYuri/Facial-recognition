import PIL.ImageShow
import os
from PIL import Image
from numpy import asarray
import numpy as np
from mtcnn.mtcnn import MTCNN
import cv2
def save_faces(final_dirname, org_dirname, size=(320, 320)):
    for root, dirs, files in os.walk(org_dirname, topdown=False):
        if os.path.basename(root) == 'Nguyễn_Trí_Anh_K16':
        # count_dirs = 0
        # for name in dirs[2:4]:
        #     count_dirs += 1
        #     print(count_dirs)
        #     os.mkdir(final_dirname + '/' + name)
        #     count_files = 0
        # for file in files:
        #     file_paths = []
        #     file_paths.append(os.path.join(root, file))
            for file in files: #Get all files.
                path = os.path.join(root, file)
                label = os.path.basename(root)
                image = cv2.imread(path)
                print(os.path.isfile(path))
                #Face detection and cropping.
                #image = Image.open(path)
                #image = image.convert('RGB')
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = image.resize((600, 600))
                pixels = asarray(image)
                pixels = pixels.astype("float32") / 255.0
                detector = MTCNN()
                results = detector.detect_faces(pixels)
                if not len(results) == 0:
                    print(root)
                    x1, y1, width, height = results[0]['box']
                    x1, y1 = abs(x1), abs(y1)
                    x2, y2 = x1 + width, y1 + height
                    face = pixels[y1:y2, x1:x2]
                    image = Image.fromarray(face)
                    image = image.resize(size)
                    #Check if dir exists then save new cropped image.
                    if not os.path.exists(final_dirname + '/' + label):
                        os.mkdir(final_dirname + '/' + label)
                    image.save(final_dirname + '/' + label + '/' + file)
        # for file_path in file_paths:
        #     image = Image.open(file_path)
        #     image = image.convert('RGB')
        #     pixels = asarray(image)
        #     detector = MTCNN()
        #     results = detector.detect_faces(pixels)
        #     x1, y1, width, height = results[0]['box']
        #     x1, y1 = abs(x1), abs(y1)
        #     x2, y2 = x1 + width, y1 + height
        #     face = pixels[y1:y2, x1:x2]
        #     image = Image.fromarray(face)
        #     image = image.resize(size)
        #     image.save(final_dirname + '/' + name + '/' + str(count_files) + '.jpg')

save_faces('D:/Projects/Face Recog Group/320faces', 'D:/Projects/Face Recog Group/Final_v3')
