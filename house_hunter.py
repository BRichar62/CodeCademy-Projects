class House:
  def __init__(self, input_city, input_rooms, input_price):
    self.city = input_city
    self.rooms = input_rooms
    self.price = input_price
  

  def __repr__(self):
    # Printing a house will tell you it's city, number of rooms, and price.
    description = "The house in {city} has {rooms} rooms, and is ${price}.".format(city = self.city, rooms = self.rooms, price = self.price)
    return description

#print(a)
class Buyer:
  def __init__(self, input_desired_city, input_family_size, input_limit):
    self.desired_city = input_desired_city
    self.family_size = input_family_size
    self.limit = input_limit
    
  def __repr__(self):
    # Printing a buyer will tell you their desired location, family size, and spending limit.
    description = "This family of {family_size} would like to live in {desired_city}, can spend up to ${limit} on their house.".format(desired_city = self.desired_city, family_size = self.family_size, limit = self.limit) 
    return description  

def match(buyer, house):
    if buyer.desired_city == house.city and buyer.family_size <= house.rooms and buyer.limit >= house.price:
      print("We have a match!")
      
    else:
      #print("House is not a match.")
      return "No other matches."
    #if buyer.family_size <= house.rooms:
      #print("House is large enough.")
    #else:
      #print("House is too small.")
      #return
    #if buyer.limit >= house.price:
      #print("House is affordable. Would you like to make an offer?")
    #else:
      #print("House is out of price range. Look at other listings.")
      #return
    return house       

# Begin interaction here.
#buyer = []
buyer = input("Welcome to House Hunter. Please enter your name.\n")
print("Welcome " + buyer + ". Let's find you a house.\n")
desired_city = input("Would you like to live in Kansas City, Independence, or Raytown?\n")
#buyer.append(desired_city)
family_size = input("How many are in your household?\n")
#buyer.append(int(family_size))
limit = input("What is the limit that you can afford?\n")
#buyer.append(int(limit))
#print(buyer)
family = Buyer(desired_city, int(family_size), int(limit))



# This is the inventory of houses.

a = House("Kansas City", 4, 100000)

print(match(family, a))
b = House("Kansas City", 3, 80000)
print(match(family, b))
c = House("Independence", 2, 50000)
print(match(family, c))

#These are test buyers.
#smith = Buyer("Independemce", 3, 90000)
#print(smith)
#jones = Buyer("Raytown", 2, 40000)
#print(jones)
#thompson = Buyer("Kansas City", 4, 150000)
#print(thompson)

# These are test scenarios.
#search = match(smith, a)
#search = match(smith, b)