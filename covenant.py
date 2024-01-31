class Covenant:

    def __init__(self, species):
        self.__species = species
#        self.__description = description
        self.__score = 0

    def get_species(self):
        return self.__species

#    def get_description(self):
#        return self.__description

    def increment_score(self):
        self.__score += 1

    def get_score(self):
        return self.__score


grunt = Covenant('Grunt')
elite = Covenant('Elite')
jackal = Covenant('Jackal')
hunter = Covenant('Hunter')
flood = Covenant('Flood')

species_list = [grunt, elite, jackal, hunter, flood]
