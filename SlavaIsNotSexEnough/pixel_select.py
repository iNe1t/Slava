from PIL import Image
import cv2
import os

img_for_map = input("Введи имя картинки для создания тепловой карты: ")
img2 = input("Введи имя тепловой картинки: ")

if img_for_map != "":
    # Считываем картинку
    img = cv2.imread(img_for_map)
    # Пропускаем через тепловой фильтр
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    heatmap_img = cv2.applyColorMap(gray_img, cv2.COLORMAP_JET)
    # Заменяем исходник на обработанную картинку
    os.system("del "+ str(img_for_map))
    cv2.imwrite(img_for_map, heatmap_img)

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
for pixel in list_of_test_pixels: # [::100]
    if pixel[0] > pixel[2]:
        percent_of_warm_pixels = percent_of_warm_pixels + 1

print("Теплых пикселей: "+ str(percent_of_warm_pixels))
all_pic_pixels = len(list_of_test_pixels)
print("Всего пикселей: "+ str(all_pic_pixels))
divide = percent_of_warm_pixels / all_pic_pixels
print("Поделили: " + str(divide))
percent = divide *100
print(percent)
           