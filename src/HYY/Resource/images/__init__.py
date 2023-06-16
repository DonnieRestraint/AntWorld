from PIL import Image, ImageDraw, ImageFont

img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
Draw = ImageDraw.Draw(img)
Draw.line((10, 10, 21, 21), fill="#766555", width=1)
Draw.line((10, 11, 20, 21), fill="#766555", width=1)
Draw.line((11, 10, 21, 20), fill="#766555", width=1)

Draw.line((10, 21, 21, 10), fill="#766555", width=1)
Draw.line((10, 20, 20, 10), fill="#766555", width=1)
Draw.line((11, 21, 21, 11), fill="#766555", width=1)
img.save("set_close.png")

img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
Draw = ImageDraw.Draw(img)
Draw.line((10, 15, 21, 15), fill="black", width=2)
img.save("minimize.png")


def filter_color(file_path, color_step=1):
    img_file = Image.open(file_path)
    print(img_file.size)
    new_file = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    width, height = img_file.size
    start_w, start_h = 16 - int(width / 2), 16 - int(height / 2)
    start_w = start_w if start_w > 0 else 0
    start_h = start_h if start_h > 0 else 0

    for x in range(width):
        for y in range(height):
            rgba = img_file.getpixel((x, y))
            if abs(rgba[1] - rgba[0]) >= color_step or abs(rgba[2] - rgba[1]) >= color_step:
                new_file.putpixel((x + start_w, y + start_h), (0, 0, 0, 250))
    new_file.save("cover_" + str(color_step) + "_" + file_path)


# filter_color("settings.png", 2)
