from PIL import Image
import cv2
import os

img1 = input("Введи имя картинки для создания тепловой карты: ")
img2 = input("Введи имя тепловой картинки: ")

if img1 != "":
    # Считываем картинку
    img = cv2.imread(img1)
    # Пропускаем через тепловой фильтр
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    heatmap_img = cv2.applyColorMap(gray_img, cv2.COLORMAP_JET)
    # Заменяем исходник на обработанную картинку
    os.system("del "+ str(img1))
    cv2.imwrite(img1, heatmap_img)

# Получаем все пиксели теплого спектра
warm_image = Image.open("warm_colors.jpg")
warm_pixels = warm_image.getdata()
list_of_warm_pixels = list(warm_pixels)
# Получаем картинку для определения заполнения
test_image = Image.open(img2)
test_pixels = test_image.getdata()
list_of_test_pixels = list(test_pixels)

# Считаем...
percent_of_warm_pixels = 0
for pixel in list_of_test_pixels[::100]:
    if pixel in list_of_warm_pixels:
        percent_of_warm_pixels = percent_of_warm_pixels + 1

aaa = len(list_of_test_pixels)/100
print(aaa)
percent = percent_of_warm_pixels / aaa *1000
print(percent)
           




