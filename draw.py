#!/usr/bin/env python

from regpoly import RegularPolygon, TRIANGLE
import math
import cairo

CIRCUMRADIUS = 50
DIAMETER = CIRCUMRADIUS * 2
NBR_POLYGONS = 10
NBR_ROTATIONS = 8
WIDTH = DIAMETER * NBR_POLYGONS
HEIGHT = DIAMETER * NBR_ROTATIONS
print(WIDTH, HEIGHT)

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.set_source_rgb(1, 1, 1)
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.fill()

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(1.0)


def draw_poly(poly: RegularPolygon, ctx: cairo.Context):
    ctx.save()
    v = poly.vertices()
    ctx.move_to(v[0][0], v[0][1])
    for i in range(1, len(v)):
        ctx.line_to(v[i][0], v[i][1])
    ctx.close_path()
    ctx.stroke()
    ctx.restore()


def draw_circle(center_x, center_y, radius, ctx: cairo.Context):
    ctx.save()
    ctx.arc(center_x, center_y, radius, 0.0, 2.0 * math.pi)
    ctx.stroke()
    ctx.restore()


for p in range(NBR_POLYGONS):
    for r in range(NBR_ROTATIONS):
        nbr_sides = p + 3
        center_x = CIRCUMRADIUS + (p * DIAMETER)
        center_y = CIRCUMRADIUS + (r * DIAMETER)
        rotation = r * (0.25 * math.pi)
        poly = RegularPolygon.from_circumradius(nbr_sides, CIRCUMRADIUS, center_x=center_x, center_y=center_y, rotation=rotation)
        draw_poly(poly, ctx)
        # draw_circle(poly.center_x, poly.center_y, poly.circumradius, ctx)
        # draw_circle(poly.center_x, poly.center_y, poly.inradius, ctx)


surface.write_to_png("test.png")



