import os
from imutils import paths

imagePaths = list(paths.list_images(f'Student/1008/1015'))



os.system(f'python encode.py --dataset Student/1008/1015 --encodings Student/1008/1015/encodings.pickle')