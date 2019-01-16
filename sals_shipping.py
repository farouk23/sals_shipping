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

#print(normal_ground_shipping_cost(8.4))
