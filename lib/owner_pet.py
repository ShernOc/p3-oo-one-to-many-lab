class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    all = []
    
    def __init__(self, name, pet_type, owner = None):
        if pet_type not in self.PET_TYPES: 
            raise Exception("Pet is not there ")
    
        self.pet_type = pet_type
        self.name = name 
        self.owner = owner
        Pet.all.append(self)  #storing the Pet class 
        
    
class Owner:

    def __init__(self,name):
        self.name = name 
        self.owner_pet = []
    
    def pets(self):
        #returns full list of the owners pet
        return [pet for pet in Pet.all]
    
    
    def add_pet(self,pet):
        if isinstance(pet, Pet):
            pet.owner  = self
            self.owner_pet.append(pet)
        else:
            raise Exception ("Error")
        
    #returns sorted list of pets by their name  
    def get_sorted_pets(self):
       return sorted(self.pets(), key=lambda pet: pet.name)
   
            
    

    
    
    
        