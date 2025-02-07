#!/usr/bin/env python3

# Définition d'un mixin pour les comportements de nage
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# Définition d'un mixin pour les comportements de vol
class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Définition de la classe Dragon qui hérite des comportements des mixins
class Dragon(SwimMixin, FlyMixin):

    def roar(self):
        print("The dragon roars!")
