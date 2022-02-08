import streamlink
import cv2
import imutils
from win32api import GetSystemMetrics

url = 'https://youtu.be/1EiC9bvVGnk'
streams = streamlink.streams(url)
print(streams)
framecount = 0
cap = cv2.VideoCapture(streams["best"].url)
fps = int(cap.get(cv2.CAP_PROP_FPS))
print("Waiting....")
while True:
    ret, frame = cap.read()
    framecount += 1
    rsframe = imutils.resize(frame, GetSystemMetrics(0), GetSystemMetrics(1)) #width=1600, height=900
    if framecount == (fps * 1800):
        print("Frame 1")
        cv2.imwrite(r"C:\Users\trcyp\Downloads\PiClock-Python3-SerBrynden\PiClock-Python3-SerBrynden\Clock\images\slideshow\capture.jpg", rsframe)
    if framecount == (fps * 900):
        print("Frame 2")
        framecount = 0
        cv2.imwrite(r"C:\Users\trcyp\Downloads\PiClock-Python3-SerBrynden\PiClock-Python3-SerBrynden\Clock\images\slideshow\capture2.jpg", rsframe)
        #cv2.imshow(frame) #('Jackson, WY', frame)
        #mybg = cv2.imshow('Jackson, WY', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
