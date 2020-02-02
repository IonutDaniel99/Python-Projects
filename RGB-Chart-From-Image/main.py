import numpy as np
import cv2
import matplotlib.pyplot as plt_percent
import matplotlib.pyplot as plt_pixels
plt_percent.rcdefaults()
plt_pixels.rcdefaults()


def main():

    name_of_photo = input("Name of photo and extenstion(Example: photo.png): ")

    red = 0
    green = 0
    blue = 0
    white = 0
    yellow = 0
    black = 0
    other = 0

    objects = ('Red', 'Green', 'Blue', 'Yellow', 'White', 'Black',  'Others')
    y_pos = np.arange(len(objects))
    img = cv2.imread(name_of_photo, cv2.IMREAD_COLOR)
    height, width, _ = img.shape
    for y in range(width):
        for x in range(height):
            r, g, b = img[x, y]
            if int(r) >= 240 and int(g) >= 240 and int(b) >= 240:
                white += 1
            elif int(r) < 60 and int(g) <= 60 and int(b) <= 60:
                black += 1
            elif int(r) >= int(g) and int(r) >= int(b):
                red += 1
            elif int(r) < 20 and int(b) >= 230 and int(g) >= 230:
                yellow += 1
            elif int(g) >= int(r) and int(g) >= int(b):
                green += 1
            elif int(b) >= int(r) or int(b) >= int(g):
                blue += 1
            else:
                other += 1

    red_percent = ((red/(height*width))*100)
    green_percent = ((green/(height*width))*100)
    blue_percent = ((blue/(height*width))*100)
    yellow_percent = ((yellow/(height*width))*100)
    white_percent = ((white/(height*width))*100)
    black_percent = ((black/(height*width))*100)
    other_percent = ((other/(height*width))*100)

    performance_pixels = [red, green, blue, yellow, white, black, other]
    performance_percent = [red_percent, green_percent,
                           blue_percent, yellow_percent,
                           white_percent, black_percent,
                           other_percent]

    plt_pixels.bar(y_pos, performance_pixels, align='center', alpha=1, color=[
                   'red', 'green', 'blue', 'yellow', '#ffffcc', 'black', 'gray'])

    plt_pixels.xticks(y_pos, objects)
    plt_pixels.ylabel('Number Of Pixels')
    plt_pixels.title('Colors')

    plt_pixels.show()

    plt_percent.bar(y_pos, performance_percent, align='center', alpha=1, color=[
        'red', 'green', 'blue', 'yellow', '#ffffcc', 'black', 'gray'])
    plt_percent.xticks(y_pos, objects)
    plt_percent.ylabel('Percent Of Colour')
    plt_percent.title('Colors')

    plt_percent.show()


if __name__ in "__main__":
    main()
