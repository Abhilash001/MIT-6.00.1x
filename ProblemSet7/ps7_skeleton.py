import random as rand
import string

class AdoptionCenter:
	def __init__(self, name, species_types, location):
		self.name = name
		self.species_types = species_types
		self.location = location

	def get_number_of_species(self, animal):
		if animal in self.species_types:
			return self.species_types[animal]
		else:
			return 0

	def get_location(self):
		return (float(self.location[0]), float(self.location[1]))

	def get_species_count(self):
		return self.species_types.copy()

	def get_name(self):
		return self.name

	def adopt_pet(self, species):
		if species in self.species_types:
			self.species_types[species]-=1
			if self.species_types[species] is 0:
				del self.species_types[species]


class Adopter:
	def __init__(self, name, desired_species):
		self.name = name
		self.desired_species = desired_species

	def get_name(self):
		return self.name

	def get_desired_species(self):
		return self.desired_species

	def get_score(self, adoption_center):
		return 1.0*adoption_center.get_number_of_species(self.desired_species)


class FlexibleAdopter(Adopter):
	def __init__(self, name, desired_species, considered_species):
		Adopter.__init__(self, name, desired_species)
		self.considered_species = considered_species

	def get_score(self, adoption_center):
		return Adopter.get_score(self, adoption_center)+(0.3*sum([adoption_center.get_number_of_species(animal) for animal in self.considered_species]))


class FearfulAdopter(Adopter):
	def __init__(self, name, desired_species, feared_species):
		Adopter.__init__(self, name, desired_species)
		self.feared_species = feared_species

	def get_score(self, adoption_center):
		score = Adopter.get_score(self, adoption_center)-(0.3*adoption_center.get_number_of_species(self.feared_species))
		if score <= 0.0:
			return 0.0
		else:
			return score


class AllergicAdopter(Adopter):
	def __init__(self, name, desired_species, allergic_species):
		Adopter.__init__(self, name, desired_species)
		self.allergic_species = allergic_species

	def get_score(self, adoption_center):
		allergic_animals = [species for species in self.allergic_species if species in adoption_center.species_types]
		if allergic_animals != []:
			return 0.0
		return Adopter.get_score(self, adoption_center)


class MedicatedAllergicAdopter(AllergicAdopter):
	def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
		AllergicAdopter.__init__(self, name, desired_species, allergic_species)
		self.medicine_effectiveness = medicine_effectiveness

	def get_score(self, adoption_center):
		allergic_animals = [species for species in self.allergic_species if species in adoption_center.species_types]
		if allergic_animals != []:
			return min([self.medicine_effectiveness[animal] for animal in allergic_animals])*Adopter.get_score(self, adoption_center)
		return Adopter.get_score(self, adoption_center)


class SluggishAdopter(Adopter):
	def __init__(self, name, desired_species, location):
		Adopter.__init__(self, name, desired_species)
		self.location = location

	def get_linear_distance(self, to_location):
		from math import pow,sqrt
		return sqrt(pow(self.location[0]-to_location[0], 2) + pow(self.location[1]-to_location[1], 2))

	def get_score(self, adoption_center):
		from random import uniform
		if self.get_linear_distance(adoption_center.get_location()) < 1:
			return 1.0*adoption_center.get_number_of_species(self.desired_species)
		elif self.get_linear_distance(adoption_center.get_location()) < 3:
			return uniform(0.7, 0.9)*adoption_center.get_number_of_species(self.desired_species)
		elif self.get_linear_distance(adoption_center.get_location()) < 5:
			return uniform(0.5, 0.7)*adoption_center.get_number_of_species(self.desired_species)
		else:
			return uniform(0.1, 0.5)*adoption_center.get_number_of_species(self.desired_species)


def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
	new_list = [[adoption_center, adopter.get_score(adoption_center), adoption_center.get_name()] for adoption_center in list_of_adoption_centers]
	new_list.sort(key=name_wise)
	new_list.sort(key=score_wise, reverse=True)
	return [[adoption_center[0].get_name(), adoption_center[1]] for adoption_center in new_list]

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
	new_list = [[adopter, adopter.get_score(adoption_center), adopter.get_name()] for adopter in list_of_adopters]
	new_list.sort(key=name_wise)
	new_list.sort(key=score_wise, reverse=True)
	if n < len(new_list):
		return [[new_list[i][0].get_name(), new_list[i][1]] for i in range(n)]
	return [[adopter[0].get_name(), adopter[1]] for adopter in new_list]

def score_wise(item):
	return item[1]

def name_wise(item):
	return item[2]


adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat") 

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))

# how to test get_ordered_adoption_center_list
print get_ordered_adoption_center_list(adopter4, [ac,ac2,ac3,ac4,ac5,ac6])							
# you can print the name and score of each item in the list returned

adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog") 

ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2,10))

# how to test get_adopters_for_advertisement
print get_adopters_for_advertisement(ac, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10)
# you can print the name and score of each item in the list returned

