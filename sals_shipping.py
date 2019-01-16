#Finding the Cheapest Shipping Method,should be a function that takes in
#the weight of an item and returns the cost of shipping the item at that wieght.

def normal_ground_shipping_cost(weight):
  if weight <= 2:
    return weight * 1.50 + 20
  elif weight > 2 and weight <= 6:
    return weight * 3.00 + 20
  elif weight > 6 and weight <= 10:
    return weight * 4.00 + 20
  else:
    return weight * 4.75 + 20

def drone_shipping_cost(weight):
  if weight <= 2:
    return weight * 4.50 + 0.00
  elif weight > 2 and weight <= 6:
    return weight * 9.00 + 0.00
  elif weight > 6 and weight <= 10:
    return weight * 12.00 + 0.00
  else:
    return weight * 14.25 + 0.00

def cheapest_shipping_method(weight):
  if normal_ground_shipping_cost(weight) < drone_shipping_cost(weight) and normal_ground_shipping_cost(weight) < premium_ground_shipping:
    return "The normal ground shipping method is the cheapest and it will cost you " + " " + str(normal_ground_shipping_cost(weight)) + " " + "to ship"
  elif  drone_shipping_cost(weight) < normal_ground_shipping_cost(weight) and drone_shipping_cost(weight) < premium_ground_shipping:
    return "The drone shipping method is the cheapest and it will cost you " + " " + str(drone_shipping_cost(weight)) + " " + "to ship"
  else:
    return "premium ground shipping method is the cheapest and it will cost you " + " " + str(premium_ground_shipping) + " " + "to ship"



#test the code below with the print function
#print(normal_ground_shipping_cost(8.4))
#print(drone_shipping_cost(1.5))
#print(cheapest_shipping_method(4.8))
#print(cheapest_shipping_method(41.5))
  
