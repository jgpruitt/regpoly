#!/usr/bin/env python

import regpoly
import math
import cairo

CIRCUMRADIUS = 50
DIAMETER = CIRCUMRADIUS * 2
NBR_POLYGONS = 1
WIDTH = DIAMETER * NBR_POLYGONS
HEIGHT = DIAMETER
print(WIDTH, HEIGHT)

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.set_source_rgb(1, 1, 1)
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.fill()

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(1.0)

poly = regpoly.from_circumradius(regpoly.TRIANGLE, CIRCUMRADIUS, center_x=CIRCUMRADIUS, center_y=CIRCUMRADIUS)
vertices = poly.vertices()
print(vertices)
p1 = vertices[0]
p2 = vertices[1]
p3 = vertices[2]
ctx.move_to(p1[0], p1[1])
ctx.line_to(p2[0], p2[1])
ctx.line_to(p3[0], p3[1])
ctx.close_path()
ctx.stroke()

ctx.arc(CIRCUMRADIUS, CIRCUMRADIUS, CIRCUMRADIUS, 0.0, 2.0 * math.pi)
ctx.stroke()

surface.write_to_png("test.png")



