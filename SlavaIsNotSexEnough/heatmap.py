import numpy as np
import cv2
from colorthief import ColorThief


img = cv2.imread('SlavaIsNotSexEnough/pic.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
heatmap_img = cv2.applyColorMap(gray_img, cv2.COLORMAP_JET)

color_thief = ColorThief('SlavaIsNotSexEnough/warm_colors.jpg')
palette = color_thief.get_palette(color_count=150)
print(palette)

brown = [72 ,86 ,255]  # RGB
diff = 20
boundaries = [([brown[2]-diff, brown[1]-diff, brown[0]-diff],
               [brown[2]+diff, brown[1]+diff, brown[0]+diff])]
# in order BGR as opencv represents images as numpy arrays in reverse order

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype=np.uint8)
    upper = np.array(upper, dtype=np.uint8)
    mask = cv2.inRange(heatmap_img, lower, upper)
    output = cv2.bitwise_and(heatmap_img, heatmap_img, mask=mask)

    ratio_brown = cv2.countNonZero(mask)/(heatmap_img.size/3)
    print('blue pixel percentage:', np.round(ratio_brown*100, 2))

    cv2.imshow("images", np.hstack([heatmap_img, output]))
    cv2.waitKey(0)