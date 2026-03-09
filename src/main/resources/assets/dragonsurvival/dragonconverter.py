import os
from PIL import Image

srctexture = "./textures/dragon/custom/dragon/"
dsttexture = "./textures/dragon/custom/"
masktexture = "./mask.png"

mask = Image.open(os.path.realpath(masktexture), 'r')

for dp in os.walk(srctexture):
    for fp in dp[2]:
        try:
            with Image.open(dp[0] + '/' + fp, 'r').copy() as im:
                for x in range(im.width):
                    for y in range(im.height):
                        (r, g, b, a) = im.getpixel((x, y))
                        m = mask.getpixel((x, y))[0]
                        a *= m
                        im.putpixel((x, y), (r, g, b, a))
            im.save(dsttexture + fp)
        except KeyError as e:
            pass