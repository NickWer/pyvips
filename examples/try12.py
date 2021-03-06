#!/usr/bin/python3

import sys

import pyvips

im = pyvips.Image.new_from_file(sys.argv[1], access="sequential")

footer = pyvips.Image.black(im.width, 150)
left_text = pyvips.Image.text("left corner", dpi=300)
right_text = pyvips.Image.text("right corner", dpi=300)
footer = footer.insert(left_text, 50, 50)
footer = footer.insert(right_text, im.width - right_text.width - 50, 50)
footer = footer.ifthenelse(0, [255, 0, 0], blend=True)

im = im.insert(footer, 0, im.height, expand=True)

im.write_to_file(sys.argv[2])
