from app import app
from flask import Flask, render_template, Response
#from camera import VideoCamera
import cv2
import threading
import time



cap=cv2.VideoCapture(1)


def gen():
    while True:
        success, image = cap.read()
        ret, jpeg = cv2.imencode('.jpg', image) 
        frame=jpeg.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)