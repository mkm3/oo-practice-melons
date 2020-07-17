############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""


    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.first_harvest = first_harvest
        self.code = code
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name



    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        print(f'Code updated to {new_code}')


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(1998, 'musk', 'green', True, True, "Musk Melon")
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType(2003, "cas", "orange", False, False, "Casaba")
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')
    all_melon_types.append(cas)


    cren = MelonType(1996, "cren","green", False, False, "Crenhsaw")
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)


    yellow = MelonType(2013,"yellow", "ice cream", True, True, "Yellow Watermelon")
    yellow.add_pairing('ice cream')
    all_melon_types.append(yellow)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for pairing in melon.pairings:
            print(f'- {pairing}')
        print()

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melons_by_code = {}

    for melon in melon_types:
        if melon.code not in melons_by_code:
            melons_by_code[melon.code] = melon

    return melons_by_code


print(make_melon_types())

# print(print_pairing_info(cren))
# print(make_melon_type_lookup(cren))
# print(musk.name, "pairs with" /n, "-", pairing.name)
# print(cas.name, "pairs with" /n, "-", p2.name,  "and", pairing.name)
# print(cren.name, "pairs with" /n, "-", p3.name)
# print(yellow.name, "pairs with" /n, "-", p4.name)

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def __init__(self, melon_type, shape_rating, color_rating, field, farmer):
        """Initialize a melon."""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating 
        self.field = field
        self.farmer = farmer

    def is_sellable():
        if shape_rating

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons_by_code = make_melon_type_lookup(melon_types)
    melons =[]

    melon_1 = Melon(melons_by_code['yellow'], 8, 7, 2, 'Sheila') 
    melon_2 = Melon(melons_by_code['yellow'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_code['yellow'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_code['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_code['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_code['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_code['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_code['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_code['yellow'], 7, 10, 3, 'Sheila')

    melon.extend([melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9])

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



