class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]

    @property
    def color(self):
        return (self.red, self.green, self.blue)

    @color.setter
    def color(self):
        self.color = color

    def __eq__(self, other):
        if self.color == other.color:
            return True
        return False

    def __add__(self, other):
        other = self.normalize(other)
        r = self.eight_bit_color(self.red + other.red)
        g = self.eight_bit_color(self.green + other.green)
        b = self.eight_bit_color(self.blue + other.blue)
        return SaberCrystal(color=(r,g,b))

    def __sub__(self, other):
        other = self.normalize(other)
        r = self.red - other.red
        g = self.green - other.green
        b = self.blue - other.blue
        return SaberCrystal(color=(r,g,b))

    def  __contains__(self, other):
        other = self.normalize(other)
        if self.red > 0 and other.red > 0 or \
            self.green > 0 and other.green > 0 or \
            self.blue > 0 and other.blue > 0:
            return True
        return False

    def normalize(self, other):
        if isinstance(other, tuple):
            return SaberCrystal(color=other)
        return other

    def eight_bit_color(self, value):
        if value > 255:
            value = 255
        return value
