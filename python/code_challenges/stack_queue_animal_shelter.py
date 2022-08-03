from data_structures.queue import Queue

class AnimalShelter:
    '''
    This class uses Queue to store two animal classes: Dog and Cat.
    '''
    def __init__(self):
        self.shelter = Queue()
        self.shelter_size = 0

    def enqueue(self, animal):
        '''
        Enqueue adds an animal class in to Queue.

        :params animal: Dog or Cat class that is added into the Queue
        :type animal: Dog/Cat object
        :return : None
        '''
        self.shelter.enqueue(animal)
        self.shelter_size += 1

    def dequeue(self, animal_str):
        '''
        Dequeue removes the first added animal class from the Queue.
        (Stretch goal)
        If an animal isn't prefered, return whichever animal has been waiting in the shelter the longest.

        :params animal_str: the animal that the user chooses
        :type animal_str: str
        :return :None/Dog object/Cat object
        '''

        # If the is no animal in the shelter, return None
        if self.shelter.is_empty():
            return None

        # Stretch Goal
        # No preferred. Return the animal waiting the longest.
        if animal_str == '':
            size = 1
            animal = self.shelter.dequeue()
            while size < self.shelter_size:
                self.shelter.enqueue(animal)
                animal = self.shelter.dequeue()
                size+=1
            return animal

        # If there is preference, return the first Dog/Cat that matches animal_str.
        size = 1
        animal = self.shelter.dequeue()

        while animal and size <= self.shelter_size:
            if animal_str == 'dog' and type(animal) == Dog:
                return animal
            if animal_str == 'cat' and type(animal) == Cat:
                return animal

            if self.shelter.is_empty():
                return None
            self.shelter.enqueue(animal)
            size +=1
            animal = self.shelter.dequeue()

        return None

class Dog:
    pass

class Cat:
    pass

