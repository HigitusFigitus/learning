import unittest
from star_wars_magic_methods.saber_crystal import SaberCrystal


class SaberCrystalTestCase(unittest.TestCase):
    def test_creation(self):
        red_crystal = SaberCrystal()
        self.assertEquals(red_crystal.red, 255)
        self.assertEquals(red_crystal.green, 0)
        self.assertEquals(red_crystal.blue, 0)
        self.assertEquals(red_crystal.color, (255,0,0))
        
    def test_equality(self):
        one_crystal = SaberCrystal(color=(0,255,0))
        two_crystal = SaberCrystal(color=(0,255,0))
        self.assertEquals(one_crystal, two_crystal)

    def test_addition(self):
        red_crystal = SaberCrystal()
        green = (0,255,0)
        green_crystal = SaberCrystal(color=green)
        blue = (0,0,255)
        blue_crystal = SaberCrystal(color=blue)
        white_crystal = SaberCrystal(color=(255,255,255))
        self.assertEquals(red_crystal + blue_crystal + green_crystal, white_crystal)
        self.assertEquals(red_crystal + blue + green, white_crystal)

    def test_in_place_addition(self):
        red_crystal = SaberCrystal()
        green = (0,255,0)
        green_crystal = SaberCrystal(color=green)
        blue = (0,0,255)
        blue_crystal = SaberCrystal(color=blue)
        white_crystal = SaberCrystal(color=(255,255,255))
        red_crystal += green_crystal + blue_crystal
        self.assertEquals(red_crystal, white_crystal)
        red_crystal = SaberCrystal()
        red_crystal += green
        red_crystal += blue
        self.assertEquals(red_crystal, white_crystal)
        
    def test_addition_does_not_go_over(self):
        white_crystal = SaberCrystal(color=(255,255,255))
        red_crystal = SaberCrystal()
        red_crystal += white_crystal
        self.assertEquals(red_crystal, white_crystal)
        whiter_crystal = red_crystal + white_crystal
        self.assertEquals(whiter_crystal, white_crystal)

    def test_subtraction(self):
        red_crystal = SaberCrystal()
        green = (0,255,0)
        green_crystal = SaberCrystal(color=green)
        blue = (0,0,255)
        blue_crystal = SaberCrystal(color=blue)
        white_crystal = SaberCrystal(color=(255,255,255))
        self.assertEquals(white_crystal - blue_crystal - green_crystal, red_crystal)
        self.assertEquals(white_crystal - blue - green, red_crystal)

    def test_in_place_subtraction(self):
        red_crystal = SaberCrystal()
        green = (0,255,0)
        green_crystal = SaberCrystal(color=green)
        blue = (0,0,255)
        blue_crystal = SaberCrystal(color=blue)
        white_crystal = SaberCrystal(color=(255,255,255))
        white_crystal -= blue_crystal + green_crystal
        self.assertEquals(white_crystal, red_crystal)
        white_crystal = SaberCrystal(color=(255,255,255))
        white_crystal -= blue
        white_crystal -= green
        self.assertEquals(white_crystal, red_crystal)

    def test_one_color_in_another(self):
        red_crystal = SaberCrystal()
        green = (0,255,0)
        green_crystal = SaberCrystal(color=green)
        blue = (0,0,255)
        blue_crystal = SaberCrystal(color=blue)
        white_crystal = SaberCrystal(color=(255,255,255))
        self.assertTrue(red_crystal in white_crystal)
        self.assertFalse(red_crystal in green_crystal)
        self.assertTrue(green in white_crystal)
        self.assertFalse(blue in red_crystal)
