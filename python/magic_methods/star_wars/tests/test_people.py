import unittest
from star_wars_magic_methods.people import People


class PeopleTestCase(unittest.TestCase):
    def test_creation(self):
        luke = People('Luke Skywalker')
        self.assertEquals(luke.name, 'Luke Skywalker')
        self.assertTrue(luke.light_side)
        self.assertFalse(luke.dark_side)

    def test_string(self):
        leia = People('Leia Organa')
        self.assertEquals(str(leia), 'Leia Organa')

    def test_call(self):
        obiwan = People('Obi-Wan Kenobi')
        self.assertEquals(obiwan(), "Help me Obi-Wan Kenobi, you're my only hope.")

    def test_lightsaber(self):
        ahsoka = People('Ahsoka Tano')
        ventress = People('Asajj Ventress')
        self.assertEquals(ahsoka / ventress, 'Ahsoka Tano swings a lightsaber at Asajj Ventress.')
        with self.assertRaises(TypeError):
            ahsoka / 2.5

    def test_thermal_detonator(self):
        boushh = People('Boushh')
        jabba = People('Jabba the Hutt')
        self.assertEquals(boushh * jabba, "Boushh throws a thermal detonator at Jabba the Hutt!")
        with self.assertRaises(TypeError):
            boushh * 6

    def test_force_push(self):
        quigon = People('Qui-Gon Jinn')
        battledroid = People('Battle Droid')
        self.assertEquals(quigon >> battledroid, 'Qui-Gon Jinn uses the force to push Battle Droid away from them.')
        with self.assertRaises(TypeError):
            quigon >> 1

    def test_force_pull(self):
        yoda = People('Yoda')
        luke = People('Luke Skywalker')
        self.assertEquals(yoda << luke, "Yoda uses the force to pull Luke Skywalker towards them.")

    def test_turn_to_dark_side(self):
        anakin = People('Anakin Skywalker')
        self.assertTrue(anakin.light_side)
        self.assertFalse(anakin.dark_side)
        -anakin
        self.assertFalse(anakin.light_side)
        self.assertTrue(anakin.dark_side)

    def test_turn_to_light_side(self):
        vader = People('Darth Vader', dark_side=True)
        self.assertTrue(vader.dark_side)
        self.assertFalse(vader.light_side)
        +vader
        self.assertFalse(vader.dark_side)
        self.assertTrue(vader.light_side)

    def test_change_sides(self):
        revan = People('Revan')
        self.assertTrue(revan.light_side)
        ~revan
        self.assertFalse(revan.light_side)
        ~revan
        self.assertTrue(revan.light_side)
        
    def test_force_choke(self):
        vader = People('Darth Vader')
        motti = People('Admiral Motti')
        self.assertEquals(vader ^ motti, "Darth Vader force chokes Admiral Motti.")

    def test_shoots(self):
        han = People('Han Solo')
        greedo = People('Greedo')
        self.assertEquals(han == greedo, 'Han Solo shoots Greedo.')
        self.assertEquals(greedo == han, 'Han Solo shoots Greedo. BECAUSE HAN SHOOTS FIRST.')
