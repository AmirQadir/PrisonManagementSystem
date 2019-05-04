"""
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""

import cv2
import time

class video:

    def show_webcam(self,mirror=False):
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        cap = cv2.VideoCapture("video2.mp4")
        isDone = False
        while True:
            r, frame = cap.read()
            if r:
                start_time = time.time()
                frame = cv2.resize(frame,(1280, 720)) # Downscale to improve frame rate
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) # HOG needs a grayscale image

                rects, weights = hog.detectMultiScale(gray_frame)
                if(len(rects)==2):
                    isDone = True
                    break
                print("Rects",len(rects)," Weights",weights)
                # Measure elapsed time for detections
                end_time = time.time()
                print("Elapsed time:", end_time-start_time)
                
                for i, (x, y, w, h) in enumerate(rects):
                    if weights[i] < 0.7:
                        continue
                    cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)

                cv2.imshow("preview", frame)
            k = cv2.waitKey(1)
           # if k & 0xFF == ord("q"): # Exit condition
            #    break
            if(isDone):
                break

    def main(self):
        self.show_webcam(mirror=True)




if __name__ == '__main__':
    
    vid = video()
    vid.main()