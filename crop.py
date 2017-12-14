from __future__ import division, print_function

import os
from PIL import Image, ImageOps, ImageDraw

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("path", type=str, default='shraman.jpg', metavar="[path]",
        help="Path to image.")
    parser.add_argument("-r", "--resize", type=float, default=1.0, metavar="[scale]", dest="scale",
        help="Resize by value in [0,1].")

    args = parser.parse_args()

    assert os.path.exists(args.path), "{} does not exist".format(args.path)
    base, ext = os.path.splitext(args.path)
    im = Image.open(args.path)

    sz = (int(im.size[0]*args.scale), int(im.size[1]*args.scale))
    im = im.resize(sz)
    im.save("{}-resized.png".format(base))

    mask = Image.new('L', sz, 0)
    c = (sz[0]//2, sz[1]//2)
    r = min(sz)//2
    draw = ImageDraw.Draw(mask)
    draw.ellipse((c[0]-r, c[1]-r, c[0]+r, c[1]+r), fill=255)

    im_circ = ImageOps.fit(im, sz, centering=(0.5, 0.5))
    im_circ.putalpha(mask)
    im_circ.save("{}-circle.png".format(base))
