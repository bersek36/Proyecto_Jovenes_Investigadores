from flask import Flask,render_template,request,Response
from imutils.video import WebcamVideoStream
from camera import VideoCamera
import base64,cv2

app=Flask(__name__)

def gen(camera):
    while True:
        data= camera.get_frame()

        frame=data[0]
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n'+frame+ b'\r\n\r\n')

@app.route('/')
def video_feed():
    return Response(gen(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)




        

