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
    pets_we_sold = dictionary["admin"]["pets_sold"]
    return pets_we_sold

def pets_sold(dictionary):
    pets_we_sold = get_pets_sold(dictionary)
    return pets_we_sold

def increase_pets_sold(dictionary, number):
     new_total = dictionary["admin"]["pets_sold"] 
     new_total += number
     dictionary["admin"]["pets_sold"] = new_total
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
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
     updated = customer["pets"]
     updated.append(pet)
     customer["pets"] = updated

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(dictionary, pet_name, customer):
    pet = find_pet_by_name(dictionary, pet_name)
    if pet == None:
        return "Pet not found"
    else:
        afford = customer_can_afford_pet(customer, pet)
        if afford == False:
            return "insufficient funds"
        else:
            add_pet_to_customer(customer, pet)
            remove_pet_by_name(dictionary, pet_name)
            amount = pet["price"]
            remove_customer_cash(customer, amount)
            add_or_remove_cash(dictionary, amount)
            increase_pets_sold(dictionary, len(customer["pets"]))
