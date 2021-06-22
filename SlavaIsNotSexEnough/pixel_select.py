from PIL import Image
an_image = Image.open("Sample.jpg")

sequence_of_pixels = an_image.getdata()
list_of_pixels = list(sequence_of_pixels)

print(list_of_pixels)


