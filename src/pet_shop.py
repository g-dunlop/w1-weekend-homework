import pdb

# WRITE YOUR FUNCTIONS HERE


#  pet shop name
def get_pet_shop_name(dictionary):
    return dictionary["name"]

def get_total_cash(dictionary):
    current_cash = dictionary["admin"]["total_cash"]
    return current_cash

def add_or_remove_cash(dictionary, amount):
    new_cash = dictionary["admin"]["total_cash"] = get_total_cash(dictionary) + amount
    return new_cash

def get_pets_sold(dictionary):
    pets_sold = dictionary["admin"]["pets_sold"]
    return pets_sold

def pets_sold(dictionary):
    pets_we_sold = get_pets_sold(dictionary)
    return pets_we_sold

def increase_pets_sold(dictionary, amount):
     new_total = dictionary["admin"]["pets_sold"] = amount
     return new_total
    
def get_stock_count(dictionary):
    stock_count = len(dictionary["pets"])
    return stock_count

def get_pets_by_breed(dictionary, breed):
        pets = []
        for pet in dictionary["pets"]:
            if pet["breed"] == breed:
                pets.append(pet)
            
        if len(pets) == 0:
            return pets
        else:
            return pets
        
def find_pet_by_name(dictionary, name):
    for pet in dictionary["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(dictionary, name):
    index = 0
    for pet in dictionary["pets"]:
        if pet["name"] == name:
            del(dictionary["pets"][index])
        index += 1

def add_pet_to_stock(dictionary, new_pet):
    dictionary["pets"].append(new_pet)
    return dictionary["pets"]

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    existing_cash = customer["cash"]
    customer["cash"] = existing_cash - amount
    
    
def get_customer_pet_count(customer):
    pets = customer["pets"]
    return len(pets)

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
