class Pizza:
  def __init__(self, size, crust_type, price):
    self._size = size
    self._toppings = []
    self._crust_type = crust_type
    self._price = price
  
  def get_toppings(self):
    return self._toppings
  
  def add_topping(self, topping):
    self._toppings.append(topping)
    
  def calculate_toppings(self):
    BASE_PRICE = 1.25
    return BASE_PRICE * len(self._toppings)
  
  def set_crust_type(self, crust_type):
    self._crust_type = crust_type
  
  def get_crust_type(self):
    return self._crust_type
  
  def get_total_price(self):
    return self._price + self.calculate_toppings()
  

  

  
  