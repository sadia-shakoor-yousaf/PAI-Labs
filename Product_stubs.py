class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
    
  def make_purchase(self, quantity):
      try:
        if quantity > self.amount:
            raise ValueError(f'Not enough product available. Quantity must be less than {self.amount}')
        elif quantity < 0:
            raise ValueError('Quantity must be greater than 0.')
        self.amount = self.amount - quantity
        price = self.get_price(quantity)
        print(f'Here\'s the total price charged: {price}')
      except ValueError as e:
         print(f'Error:{e}')
        
# create product object
# make purchases against different product quantities (make sure to run each test case)
# do not forget to handle exceptions
# print the remaining stock after each purchase