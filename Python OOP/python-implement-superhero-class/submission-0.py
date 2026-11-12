class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name=name
        self.power=power
        self.health=health
        pass


# TODO: Create Superhero instances
sp1=SuperHero("Batman","Intelligence",100)
sp2=SuperHero("Superman","Strength",150)


# TODO: Print out the attributes of each superhero
print(f"{sp1.name}\n{sp1.power}\n{sp1.health}")
print(f"{sp2.name}\n{sp2.power}\n{sp2.health}")
