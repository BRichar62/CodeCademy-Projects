class House:
  def __init__(self, input_city, input_rooms, input_price, input_occupied = True):
    self.city = input_city
    self.rooms = input_rooms
    self.price = input_price
    self.occupied = input_occupied

  def __repr__(self):
    # Printing a house will tell you it's city, number of rooms, price, and whether it's occupied.
    description = "The house in {city} has {rooms} rooms, and is ${price}.".format(city = self.city, rooms = self.rooms, price = self.price)
    return description

#print(a)
class Buyer:
  def __init__(self, input_desired_city, input_family_size, input_limit, input_hurry = False):
    self.desired_city = input_desired_city
    self.family_size = input_family_size
    self.limit = input_limit
    self.hurry = input_hurry
  def __repr__(self):
    # Printing a buyer will tell you their desired location, family size, spending limit, and whether they need to move quickly.
    description = "This family of {family_size} would like to live in {desired_city}, can spend up to ${limit} on their house.".format(desired_city = self.desired_city, family_size = self.family_size, limit = self.limit) 
    return description  

def match(buyer, house):
    if buyer.desired_city == house.city:
      print("House is in right area.")
    else:
      print("House is not a match.")
      return
    if buyer.family_size <= house.rooms:
      print("House is large enough.")
    else:
      print("House is too small.")
      return
    if buyer.limit >= house.price:
      print("House is affordable. Would you like to make an offer?")
    else:
      print("House is out of price range.Look at other listings.")
      return
    return        

# Begin interaction here.
buyer = []
name = input("Welcome to House Hunter. Please enter your name.\n")
print("Welcome " + name + ". Let's find you a house.\n")


# BobThis is the inventory of houses.

a = House("Kansas City", 4, 100000, True)
print(a)
b = House("Kansas City", 3, 80000, False)
print(b)
c = House("Independence", 2, 50000, True)
print(c)

#These are test buyers.
smith = Buyer("Independemce", 3, 90000)
print(smith)
jones = Buyer("Raytown", 2, 40000)
print(jones)
thompson = Buyer("Kansas City", 4, 150000)
print(thompson)

# These are test scenarios.
search = match(smith, a)
search = match(smith, b)