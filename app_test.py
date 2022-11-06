
from flask import Flask, Response
import cv2
from face_rec import FaceRec

app = Flask(__name__)

CAM_URL = 'rtsp://admin:@122.176.110.134:554/ch0_0.264'

video = cv2.VideoCapture(CAM_URL)

@app.route('/')
def index():
    return "Default Message"
    

@app.route('/video_feed')
def video_feed():
    global video
    encoding_path = 'Student/1008/1015/encodings.pickle'
    fr = FaceRec(encoding_path, video)
    
    return Response(fr.gen_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True)