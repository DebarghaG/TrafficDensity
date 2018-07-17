import numpy as np
import cv2 as cv


cap = cv.VideoCapture('video1.avi')
fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
white_pix = []

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv.imshow('frame',fgmask)
    n_white_pix = np.sum(fgmask == 255)
    white_pix.append(n_white_pix)

    print(n_white_pix)

    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

outfile.write("\n".join(white_pix))

cap.release()
cv.destroyAllWindows()

#Done
