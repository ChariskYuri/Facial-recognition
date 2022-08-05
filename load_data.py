import pathlib
import os

data_dir = pathlib.Path('Final_v3')
images = list(data_dir.rglob('*/*'))
print(os.path.dirname(images[0]))
labels = []
for image in images:
    labels.append(os.path.basename(os.path.dirname(image)).replace(' ', '_'))

print(labels)
image_count = len(images)
print(image_count)

