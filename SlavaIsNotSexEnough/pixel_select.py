from PIL import Image
import cv2
import os

cap = cv2.VideoCapture(0)

while True:
    # Считываем картинку
    ret, frame = cap.read()

    # Пропускаем через тепловой фильтр
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    heatmap_img = cv2.applyColorMap(gray_img, cv2.COLORMAP_JET)
    
    cv2.imshow('frame', heatmap_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Получаем все пиксели теплого спектра
    warm_image = Image.open("warm_colors.jpg")
    warm_pixels = warm_image.getdata()
    list_of_warm_pixels = list(warm_pixels)

    # Получаем картинку для определения заполнения
    im_pil = Image.fromarray(heatmap_img)
    test_pixels = im_pil.getdata()
    list_of_test_pixels = list(test_pixels)

    # Считаем...
    percent_of_warm_pixels = 0
    for pixel in list_of_test_pixels: # [::100]
        if pixel[0] < pixel[2]:
            percent_of_warm_pixels = percent_of_warm_pixels + 1

    all_pic_pixels = len(list_of_test_pixels)
    divide = percent_of_warm_pixels / all_pic_pixels
    percent = divide * 100
    print(percent)