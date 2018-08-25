#!/usr/bin/env python

import math

TRIANGLE = 3
SQUARE = 4
PENTAGON = 5
HEXAGON = 6
HEPTAGON = 7
OCTAGON = 8
NONAGON = 9
DECAGON = 10
HENDECAGON = 11
DODECAGON = 12
TRIDECAGON = 13
TETRADECAGON = 14


class RegularPolygon:

    nbr_sides: int
    center_x: float
    center_y: float
    rotation: float
    circumradius: float
    inradius: float
    side_length: float

    def center(self):
        return self.center_x, self.center_y

    def vertices(self):
        rad = 2.0 * math.pi / self.nbr_sides
        v = []
        for i in range(self.nbr_sides):
            x = self.center_x + self.circumradius * math.cos(self.rotation + (rad * i))
            y = self.center_y + self.circumradius * math.sin(self.rotation + (rad * i))
            v.append((x, y))
        return v

    def interior_angle(self):
        return (self.nbr_sides - 2.0) / self.nbr_sides * math.pi

    def exterior_angle(self):
        return 2.0 * math.pi - self.interior_angle()

    def sagitta(self):
        return self.circumradius - self.inradius

    def side_midpoints(self):
        v = self.vertices()
        m = []
        midpoint = (lambda x1, x2: 0.5 * (x1 + x2))
        for i in range(self.nbr_sides):
            p1 = v[i]
            p2 = v[i+1] if i+1 < self.nbr_sides else v[0]
            x = midpoint(p1[0], p2[0])
            y = midpoint(p1[1], p2[1])
            m.append((x, y))
        return m


def side_length_from_inradius(nbr_sides, inradius):
    return 2.0 * inradius * math.tan(math.pi / nbr_sides)


def side_length_from_circumradius(nbr_sides, circumradius):
    return 2.0 * circumradius * math.sin(math.pi / nbr_sides)


def inradius_from_side_length(nbr_sides, side_length):
    return 0.5 * side_length / math.tan(math.pi / nbr_sides)


def inradius_from_circumradius(nbr_sides, circumradius):
    return circumradius * math.cos(math.pi / nbr_sides)


def circumradius_from_side_length(nbr_sides, side_length):
    return 0.5 * side_length / math.sin(math.pi / nbr_sides)


def circumradius_from_inradius(nbr_sides, inradius):
    return inradius / math.cos(math.pi / nbr_sides)


def from_side_length(nbr_sides, side_length, center_x=0.0, center_y=0.0, rotation=0.0):
    poly = RegularPolygon()
    poly.nbr_sides = nbr_sides
    poly.center_x = center_x
    poly.center_y = center_y
    poly.rotation = rotation
    poly.side_length = side_length
    poly.inradius = inradius_from_side_length(poly.nbr_sides, side_length)
    poly.circumradius = circumradius_from_side_length(poly.nbr_sides, side_length)
    return poly


def from_inradius(nbr_sides, inradius, center_x=0.0, center_y=0.0, rotation=0.0):
    poly = RegularPolygon()
    poly.nbr_sides = nbr_sides
    poly.center_x = center_x
    poly.center_y = center_y
    poly.rotation = rotation
    poly.inradius = inradius
    poly.side_length = side_length_from_inradius(poly.nbr_sides, inradius)
    poly.circumradius = circumradius_from_inradius(poly.nbr_sides, inradius)
    return poly


def from_circumradius(nbr_sides, circumradius, center_x=0.0, center_y=0.0, rotation=0.0):
    poly = RegularPolygon()
    poly.nbr_sides = nbr_sides
    poly.center_x = center_x
    poly.center_y = center_y
    poly.rotation = rotation
    poly.circumradius = circumradius
    poly.side_length = side_length_from_circumradius(poly.nbr_sides, circumradius)
    poly.inradius = inradius_from_circumradius(poly.nbr_sides, circumradius)
    return poly
