'''

Imagine you're writing a game with different creatures that will fight
each other. Goblins, for instance:

>>> goby = Goblin('Goby')
>>> goby.name
'Goby'

Like all creatures, Goblins have attributes for their hitpoints, attack
damage, and defensive armor.

>>> goby.hitpoints
10
>>> goby.damage
3
>>> goby.armor
1

You also have Orcs, who are a bit tougher:

>>> morgash = Orc('Morgash')
>>> morgash.name
'Morgash'
>>> morgash.hitpoints
15
>>> morgash.damage
5
>>> morgash.armor
2

And HillOrcs, who are even tougher (but with a weakness you'll learn
about later):

>>> narbul = HillOrc('Narbul')
>>> narbul.name
'Narbul'
>>> narbul.hitpoints
20
>>> narbul.damage
5
>>> narbul.armor
3

There's also skeletons, who don't have any armor at all:

>>> bonez = Skeleton('Bonez')
>>> bonez.name
'Bonez'
>>> bonez.hitpoints
8
>>> bonez.damage
4
>>> bonez.armor
0

And finally, Ewoks. Who are tiny, but pack a punch (by
creating clever, devastating traps):

>>> teebo = Ewok('Teebo')
>>> teebo.name
'Teebo'
>>> teebo.hitpoints
4
>>> teebo.damage
10
>>> teebo.armor
1

Each of these inherit from a class called Creature. In writing your
code, be sure to put as many methods and member variables as possible
in this base class, overriding in the subclass when necessary.

>>> isinstance(goby, Creature)
True
>>> isinstance(morgash, Creature)
True
>>> isinstance(narbul, Creature)
True
>>> isinstance(bonez, Creature)
True
>>> isinstance(teebo, Creature)
True

You can check whether a creature is alive:

>>> bonez.is_alive()
True
>>> bonez.hitpoints = 0
>>> bonez.is_alive()
False
>>> bonez.hitpoints = 8
>>> bonez.is_alive()
True

The hitpoints, damage and armor values come into play when the
creatures fight.  The total damage done is equal to the attacker's
"damage" value, minus the target's "armor" value. The attack() method
returns the net damage done:

>>> goby.hitpoints
10
>>> bonez.hitpoints
8
>>> bonez.attack(goby)
3
>>> goby.hitpoints
7

Skeletons have no armor, so they take the full impact!
>>> goby.attack(bonez)
3
>>> bonez.hitpoints
5

When there's more than one creature to fight, an attacker has to
choose. Goblins and Ewoks simply choose the first one in the list:

>>> creatures = [narbul, goby, teebo, bonez, morgash]
>>> target = goby.select_target(creatures)
>>> target.name
'Narbul'
>>> target = teebo.select_target(creatures)
>>> target.name
'Narbul'

Skeletons are more devious and opportunistic. They will choose the
creature in the list with the fewest hit points:

>>> target = bonez.select_target(creatures)
>>> target.name
'Teebo'

Orcs (including Hill Orcs) are more complex. First, they won't attack
other orcs at all... unless there's no one to attack *except* an
orc. And among those it's willing to attack, it will pick the one with
the worst armor:

>>> target = narbul.select_target(creatures)
>>> target.name
'Bonez'
>>> target = morgash.select_target(creatures)
>>> target.name
'Bonez'

If there's no one to attack BUT orcs, then an orc will happily attack
the one with the worst (lowest) armor:

>>> only_orcs = [narbul, morgash]
>>> another_orc = Orc('Nashba')
>>> target = another_orc.select_target(only_orcs)
>>> target.name
'Morgash'

Hill Orcs have a weakness. Though strong and tough, they are TERRIFIED of
skeletons. If they attack one, fear reduces their muscles to jelly, and they do
no damage at all:

>>> bonez.hitpoints
5
>>> narbul.attack(bonez)
0
>>> narbul.attack(bonez)
0
>>> narbul.attack(bonez)
0
>>> bonez.hitpoints
5

'''

# Write your code here:


class Creature:
    hitpoints = 0
    armor = 0
    damage = 0

    def __init__(self, name):
        self.name = name

    def is_alive(self):
        return True if self.hitpoints > 0 else False

    def attack(self, creature):
        attack_points = self.damage-creature.armor
        attack_points = min(creature.hitpoints, attack_points)
        creature.hitpoints -= attack_points
        return attack_points

    def select_target(self, creatures):
        return creatures[0]


class Goblin(Creature):
    hitpoints = 10
    damage = 3
    armor = 1


class Orc(Creature):
    hitpoints = 15
    damage = 5
    armor = 2

    def select_target(self, creatures):
        candidates = [creature for creature in creatures
                      if not isinstance(creature, Orc)]

        if len(candidates) == 0:
            candidates = creatures

        return min(candidates, key=lambda creature: creature.armor)


class HillOrc(Orc):
    hitpoints = 20
    damage = 5
    armor = 3

    def attack(self, creature):
        if isinstance(creature, Skeleton):
            return 0
        return super().attack(creature)


class Skeleton(Creature):
    hitpoints = 8
    damage = 4

    def select_target(self, creatures):
        return min(creatures, key=lambda creature: creature.hitpoints)


class Ewok(Creature):
    hitpoints = 4
    damage = 10
    armor = 1
# Do not edit any code below this line!


if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
