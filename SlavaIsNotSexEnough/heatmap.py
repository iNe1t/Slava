import numpy as np
import cv2

img = cv2.imread('Sample.jpg')

# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# heatmap_img = cv2.applyColorMap(gray_img, cv2.COLORMAP_JET)

brown = [72 ,86 ,255]  # RGB
diff = 20
boundaries = [([brown[2]-diff, brown[1]-diff, brown[0]-diff],
               [brown[2]+diff, brown[1]+diff, brown[0]+diff])]
# in order BGR as opencv represents images as numpy arrays in reverse order

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype=np.uint8)
    upper = np.array(upper, dtype=np.uint8)
    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask=mask)

    ratio_brown = cv2.countNonZero(mask)/(img.size/3)
    print('blue pixel percentage:', np.round(ratio_brown*100, 2))

    cv2.imshow("images", np.hstack([img, output]))
    cv2.waitKey(0)