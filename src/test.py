customers = [
            {
                "name": "Alice",
                "pets": [],
                "cash": 1000
            },
            {
                "name": "Bob",
                "pets": [],
                "cash": 50
            },
            {
                "name": "Jack",
                "pets": [],
                "cash": 100
            }
        ]

# def get_customer_cash(customer):
#     return customer["cash"]

# print(get_customer_cash(customers[0]))
# def get_customer_cash(list):
#     customer_cash = []
#     for customer in list:
#         for i in customer:
#             if i == "cash":
#                 customer_cash.append(customer[i])
#     return customer_cash

# print(get_customer_cash(customers))
pet_shop = {
            "pets": [
                {
                    "name": "Sir Percy",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "King Bagdemagus",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "Sir Lancelot",
                    "pet_type": "dog",
                    "breed": "Pomsky",
                    "price": 1000,
                },
                {
                    "name": "Arthur",
                    "pet_type": "dog",
                    "breed": "Husky",
                    "price": 900,
                },
                {
                    "name": "Tristan",
                    "pet_type": "cat",
                    "breed": "Basset Hound",
                    "price": 800,
                },
                {
                    "name": "Merlin",
                    "pet_type": "cat",
                    "breed": "Egyptian Mau",
                    "price": 1500,
                }
            ],
            "admin": {
                "total_cash": 1000,
                "pets_sold": 0,
            },
            "name": "Camelot of Pets"
        }


# def find_pet_by_name(dictionary, name):
#     for pet in dictionary["pets"]:
#         if pet["name"] == name:
#             return pet

# print(find_pet_by_name(pet_shop, "Jeff"))

# def remove_pet_by_name(dictionary, name):
#     for pet in dictionary["pets"]:
#         index = 0
#         if pet["name"] == name:
#             del(dictionary["pets"][index])
#         index +=1
#     find_pet_by_name(dictionary, name)


# print(remove_pet_by_name(pet_shop, "Arthur"))

# def get_pets_by_breed(dictionary, breed):
#     pet_by_breed = []
#     for pet in dictionary["pets"]:
#         if pet["breed"] == breed:
#             pet_by_breed.append(pet)
        
#     if len(pet_by_breed) == 0:
#         return pet_by_breed
#     else:
#         return pet_by_breed
        
# print(get_pets_by_breed(pet_shop, "British Shorthair"))

# def get_pet_shop_name(dictionary):
#     return dictionary["name"]

# def get_total_cash(dictionary):
#     return dictionary["admin"]["total_cash"]



# def add_or_remove_cash(dictionary, amount):
#     current_cash = get_total_cash(dictionary)
#     cash = current_cash + amount
#     return cash

# def add_or_remove_cash_add(dictionary, amount):
#     cash = add_or_remove_cash(dictionary, amount)
#     return cash

# print(add_or_remove_cash_add(pet_shop, 10))

def add_pet_to_customer(customer, new_pet):
     updated = customer["pets"]
     print(updated)
     updated.append(new_pet)
     customer["pets"] = updated
     print(updated)

add_pet_to_customer(customers[0], pet_shop["pets"][2])
