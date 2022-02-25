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
