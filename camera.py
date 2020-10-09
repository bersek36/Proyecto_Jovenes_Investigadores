from imutils.video import WebcamVideoStream
import cv2

class VideoCamera(object):
    def __init__(self):
        self.stream= WebcamVideoStream(src=0).start()

    def __del__(self):
        self.stream.stop()

    def get_frame(self):
        image=self.stream.read()

        detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        face=detector.detectMultiScale(image,1.1,7)

        for (x,y,h,w) in face:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

        ret, jpeg = cv2.imencode('.jpg',image)
        data=[]
        data.append(jpeg.tobytes())
        return data
