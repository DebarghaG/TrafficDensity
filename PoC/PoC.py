import numpy as np
import cv2 as cv


cap = cv.VideoCapture('video2.avi')
fgbg = cv.bgsegm.createBackgroundSubtractorMOG()

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv.imshow('frame',fgmask)
    n_white_pix = np.sum(fgmask == 255)
    print(n_white_pix)

    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()

#Done
