import glob
import os
from load_batch_detail import LoadBatchDetail

batchId = 1015
ld = LoadBatchDetail()
root_dir = os.getcwd()
student_data_dir_path = os.path.join(root_dir,'Student')

TPBatchName, TPBatchId, TPCenterId, RTSPURL = ld.get_batch_details(batchId)

# print(TPBatchName)
# datasetPath = os.path.join(student_data_dir_path,str(TPCenterId), str(TPBatchId))
# images_path = glob.glob(os.path.join(datasetPath, "*.*"))
# #print("{} encoding images found.".format(len(images_path)))

# os.system(f'python encode.py --dataset Student\{TPBatchName} --encodings encodings.pickle')

os.system('python recognize_faces_video.py --encodings encodings.pickle --output output/webcam_face_recognition_output.avi --display 1')