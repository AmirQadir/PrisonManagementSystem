"""
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""

import cv2

class video:

    def show_webcam(self,mirror=False):
        
        try:
            cam = cv2.VideoCapture(0)
            while True:
                ret_val, img = cam.read()
                if mirror: 
                    img = cv2.flip(img, 1)
                cv2.imshow('my webcam', img)
                if cv2.waitKey(1) == 27: 
                    break  # esc to quit
            cv2.destroyAllWindows()
        except:
            print("No camera found")

    def main(self):
        self.show_webcam(mirror=True)




if __name__ == '__main__':
    
    vid = video()
    vid.main()