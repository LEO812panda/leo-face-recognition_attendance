import cv2

RTSPURL = 'rtsp://admin:@122.176.110.134:554/ch0_0.264'
cv2.namedWindow("preview")
vc = cv2.VideoCapture(RTSPURL)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

vc.release()
cv2.destroyWindow("preview")