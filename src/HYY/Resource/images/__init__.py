from PIL import Image, ImageDraw, ImageFont

img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
Draw = ImageDraw.Draw(img)
Draw.line((10, 10, 21, 21), fill="black", width=1)
Draw.line((10, 11, 20, 21), fill="black", width=1)
Draw.line((11, 10, 21, 20), fill="black", width=1)

Draw.line((10, 21, 21, 10), fill="black", width=1)
Draw.line((10, 20, 20, 10), fill="black", width=1)
Draw.line((11, 21, 21, 11), fill="black", width=1)
img.save("close.png")

img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
Draw = ImageDraw.Draw(img)
Draw.line((10, 15, 21, 15), fill="black", width=2)
img.save("minimize.png")