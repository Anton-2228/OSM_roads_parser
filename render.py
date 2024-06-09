from PIL import Image, ImageDraw
from math import tan, radians, log, pi

Req = 6378160

def convert_to_pix(lon, lat):
    x = Req * radians(lon)
    y = Req * log(tan((pi / 4) + (radians(lat) / 2)))
    return x, y

def get_image_cord(cord, size, size_x_min, size_y_max):
    x = int((size_y_max - cord[1]))
    y = int((cord[0] - size_x_min))
    return (y, x)

def render(file, points, bounds):
    size_x_min, size_y_min = convert_to_pix(bounds["minlon"], bounds["minlat"])
    size_x_max, size_y_max = convert_to_pix(bounds["maxlon"], bounds["maxlat"])

    size = (int(abs(size_x_max - size_x_min)), int(abs(size_y_max - size_y_min)))

    image = Image.new("RGB", size)
    im = ImageDraw.Draw(image)
    for way in points:
        for x in range(len(way["nodes"])-1):
            node_x_f, node_y_f = convert_to_pix(way["nodes"][x]["lon"], way["nodes"][x]["lat"])
            node_x_s, node_y_s = convert_to_pix(way["nodes"][x+1]["lon"], way["nodes"][x+1]["lat"])
            f = get_image_cord((node_x_f, node_y_f), size, size_x_min, size_y_max)
            s = get_image_cord((node_x_s, node_y_s), size, size_x_min, size_y_max)
            im.line([f, s], fill="white", width=4)

    image.show()
    image.save(file)