from PIL import Image
from PIL import ImageFont, ImageDraw

def new_foto(name):
    image = Image.open(name)
    w, h = image.size  # мы присвоим w и h значения ширины и высоты, т.к. im.size содержит 2 значения в tuple(), им и присвоим
    return image.resize((w // 2, h // 2))



im_1 = Image.open('1726738317185732697.jpg')
im_2 = Image.open('1727340999138586771.jpg')
im_1.paste(im_2, (100,100))# в box передаем координаты вставки и вставляем одно изображ в другое

draw = ImageDraw.Draw(im_1)#создаем объект класса
font = ImageFont.truetype('Swiftchops.ttf', 75)#задаем шрифт и размер
draw.text((100,100),'You are welcome!', font=font, fill='red')#задаем текст, шрифт. цвет и место вставки
print(im_1.format, im_1.size, im_1.mode)

im_1.show()
