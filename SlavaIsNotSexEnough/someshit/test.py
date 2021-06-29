import cv2

img = cv2.imread('SlavaIsNotSexEnough/pic.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
heatmap_img = cv2.applyColorMap(gray_img, cv2.COLORMAP_AUTUMN)
fin = cv2.addWeighted(heatmap_img, 0.7, img, 0.3, 0) 
cv2.imshow('oijd', fin)
cv2.waitKey(0)