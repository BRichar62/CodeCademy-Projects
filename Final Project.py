class House:
  def __init__(self, input_zip, input_rooms, input_price, input_occupied = True):
    self.zip = input_zip
    self.rooms = input_rooms
    self.price = input_price
    self.occupied = input_occupied

  def __repr__(self):
    # Printing a house will tell you it's zip code, number of rooms, price, and whether it's occupied.
    description = "The house at {zip} has {rooms} rooms, and is ${price}.".format(zip = self.zip, rooms = self.rooms, price = self.price)
    return description

#print(a)
class Buyer:
  def __init__(self, input_desired_zip, input_family_size, input_limit, input_hurry = False):
    self.desired_zip = input_desired_zip
    self.family_size = input_family_size
    self.limit = input_limit
    self.hurry = input_hurry
  def __repr__(self):
    # Printing a buyer will tell you their desired location, family size, spending limit, and whether they need to move quickly.
    description = "This family of {family_size} would like to live in the {desired_zip} zip code, can spend up to ${limit} on their house.".format(desired_zip = self.desired_zip, family_size = self.family_size, limit = self.limit) 
    return description  

def match(buyer, house):
    if buyer.desired_zip == house.zip:
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
a = House(90210, 4, 100000, True)
print(a)
b = House(51827, 3, 80000, False)
print(b)
c = House(12345, 2, 50000, True)
print(c)
smith = Buyer(51827, 3, 90000)
print(smith)
jones = Buyer(12345, 2, 40000)
print(jones)
thompson = Buyer(90210, 4, 150000)
print(thompson)

search = match(smith, a)
search = match(smith, b)