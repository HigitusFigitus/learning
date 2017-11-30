class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self._dark_side = dark_side
    
    @property
    def dark_side(self):
        return self._dark_side
    
    @dark_side.setter
    def dark_side(self, ds_value):
        self._dark_side = ds_value
     
    @property
    def light_side(self):
        return not self.dark_side
    
    @light_side.setter
    def light_side(self, value):
        self._light_side = not value
    
    def __str__(self):
        return self.name

    def __call__(self):
        return 'Help me ' + self.name + ', you\'re my only hope.'
    
    def __truediv__(self, other):
        try:
            lightsaber = self.name + ' swings a lightsaber at ' + other.name + '.'
        except:
            raise TypeError
        return lightsaber
    
    def __mul__(self, other):
        try:
            thermal_detonator = self.name + ' throws a thermal detonator at ' + other.name + '!'
        except:
            raise TypeError
        return thermal_detonator
    
    def __rshift__(self, other):
        try:
            force_push = self.name + ' uses the force to push ' + other.name + ' away from them.'
        except:
            raise TypeError
        return force_push
    
    def __lshift__(self, other):
        try:
            force_pull = self.name + ' uses the force to pull ' + other.name + ' towards them.'
        except:
            raise TypeError
        return force_pull
    
    def __xor__(self, other):
        try:
            force_choke = self.name + ' force chokes ' + other.name + '.'
        except:
            raise TypeError
        return force_choke
    
    def __eq__(self, other):
        try:
            shoot = self.name + ' shoots ' + other.name + '.'
        except:
            raise TypeError
        if self.name == 'Greedo' and other.name == 'Han Solo':
            shoot = 'Han Solo shoots Greedo. BECAUSE HAN SHOOTS FIRST.'
        return shoot

    def __neg__(self):
        self.light_side = False
        self.dark_side = True

    def __pos__(self):
        self.light_side = True
        self.dark_side = False

    def __invert__(self):
        self.light_side = not self.light_side
        self.dark_side = not self.dark_side

    
    __div__ = __truediv__
