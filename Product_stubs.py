class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
   
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        if quantity < 10:
            total_price = quantity * self.price
        elif 10 <= quantity < 100:
            total_price = quantity * self.price * 0.9  # 10% discount
        else:
            total_price = quantity * self.price * 0.8  # 20% discount
        
        return total_price


  def make_purchase(self, quantity):
      pass

# create product object
# make purchases against different product quantities (make sure to run each test case)
# do not forget to handle exceptions
# print the remaining stock after each purchase