#!/usr/bin/env python

import math


class RegularPolygon:

    nbr_sides: int
    center_x: float
    center_y: float
    rotation: float
    circumradius: float
    inradius: float
    side_length: float

    def __init__(self, nbr_sides, center_x=0.0, center_y=0.0, rotation=0.0):
        self.nbr_sides = nbr_sides
        self.center_x = center_x
        self.center_y = center_y
        self.rotation = rotation

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
        

    @staticmethod
    def side_length_from_inradius(nbr_sides, inradius):
        return 2.0 * inradius * math.tan(math.pi / nbr_sides)

    @staticmethod
    def side_length_from_circumradius(nbr_sides, circumradius):
        return 2.0 * circumradius * math.sin(math.pi / nbr_sides)

    @staticmethod
    def inradius_from_side_length(nbr_sides, side_length):
        return 0.5 * side_length / math.tan(math.pi / nbr_sides)

    @staticmethod
    def inradius_from_circumradius(nbr_sides, circumradius):
        return circumradius * math.cos(math.pi / nbr_sides)

    @staticmethod
    def circumradius_from_side_length(nbr_sides, side_length):
        return 0.5 * side_length / math.sin(math.pi / nbr_sides)

    @staticmethod
    def circumradius_from_inradius(nbr_sides, inradius):
        return inradius / math.cos(math.pi / nbr_sides)

    @staticmethod
    def from_side_length(clss, side_length, center_x=0.0, center_y=0.0, rotation=0.0):
        poly = clss(center_x=center_x, center_y=center_y, rotation=rotation)
        poly.side_length = side_length
        poly.inradius = RegularPolygon.inradius_from_side_length(poly.nbr_sides, side_length)
        poly.circumradius = RegularPolygon.circumradius_from_side_length(poly.nbr_sides, side_length)
        return poly

    @staticmethod
    def from_inradius(clss, inradius, center_x=0.0, center_y=0.0, rotation=0.0):
        poly = clss(center_x=center_x, center_y=center_y, rotation=rotation)
        poly.inradius = inradius
        poly.side_length = RegularPolygon.side_length_from_inradius(poly.nbr_sides, inradius)
        poly.circumradius = RegularPolygon.circumradius_from_inradius(poly.nbr_sides, inradius)
        return poly

    @staticmethod
    def from_circumradius(clss, circumradius, center_x=0.0, center_y=0.0, rotation=0.0):
        poly = clss(center_x=center_x, center_y=center_y, rotation=rotation)
        poly.circumradius = circumradius
        poly.side_length = RegularPolygon.side_length_from_circumradius(poly.nbr_sides, circumradius)
        poly.inradius = RegularPolygon.inradius_from_circumradius(poly.nbr_sides, circumradius)
        return poly


class Triangle(RegularPolygon):

    def __init__(self, center_x=0.0, center_y=0.0, rotation=0.0):
        super(Triangle, self).__init__(nbr_sides=3, center_x=center_x, center_y=center_y, rotation=rotation)


class Square(RegularPolygon):

    def __init__(self, center_x=0.0, center_y=0.0, rotation=0.0):
        super(Square, self).__init__(nbr_sides=4, center_x=center_x, center_y=center_y, rotation=rotation)


class Pentagon(RegularPolygon):
    
    def __init__(self, center_x=0.0, center_y=0.0, rotation=0.0):
        super(Pentagon, self).__init__(nbr_sides=5, center_x=center_x, center_y=center_y, rotation=rotation)


class Hexagon(RegularPolygon):

    def __init__(self, center_x=0.0, center_y=0.0, rotation=0.0):
        super(Hexagon, self).__init__(nbr_sides=6, center_x=center_x, center_y=center_y, rotation=rotation)


class Heptagon(RegularPolygon):

    def __init__(self, center_x=0.0, center_y=0.0, rotation=0.0):
        super(Heptagon, self).__init__(nbr_sides=7, center_x=center_x, center_y=center_y, rotation=rotation)


class Octagon(RegularPolygon):

    def __init__(self, center_x=0.0, center_y=0.0, rotation=0.0):
        super(Octagon, self).__init__(nbr_sides=8, center_x=center_x, center_y=center_y, rotation=rotation)


class Nonagon(RegularPolygon):

    def __init__(self, center_x=0.0, center_y=0.0, rotation=0.0):
        super(Nonagon, self).__init__(nbr_sides=9, center_x=center_x, center_y=center_y, rotation=rotation)


class Decagon(RegularPolygon):

    def __init__(self, center_x=0.0, center_y=0.0, rotation=0.0):
        super(Decagon, self).__init__(nbr_sides=10, center_x=center_x, center_y=center_y, rotation=rotation)
        

if __name__ == '__main__':
    tri = RegularPolygon.from_side_length(Triangle, 1)
    print(tri)
    print(tri.vertices())

    hex = RegularPolygon.from_side_length(Hexagon, 1)
    print(hex.vertices())
