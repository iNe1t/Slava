# Windows-1252
# ascii
import chardet

some_str = b'\x8cAI\x12\x96IZWc\nT\xda\x9c\x88I\x12\x96Q'.decode('Windows-1252')
print(some_str)
# result = chardet.detect(b'\x8cAI\x12\x96IZWc\nT\xda\x9c\x88I\x12\x96Q')
# print("Кодировка строки выше " + result['encoding'])