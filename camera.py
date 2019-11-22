import cv2
import numpy as np
import imutils
import os

def main():

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        ret, frame = cap.read()
        H = frame.shape[0]
        frame = frame[:,:H]
        big_frame = frame.copy()
        frame = imutils.resize(frame, height=512)
        cv2.imshow("pic", big_frame)
        if cv2.waitKey(50) & 0xFF == ord(" "):
            cv2.imwrite("./images/you.jpg", frame)
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
