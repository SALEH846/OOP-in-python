import csv

class Item:
    pay_rate = 0.8 # class variable
    all = [] # list of instances of this class

    def __init__(self, name: str, price: float, quantity=0):
        # validation of price and quantity
        assert price >= 0, f"Price {price} must be greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} must be greater than or equal to zero"

        # Instance variables
        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    # Property decorator = Read-only Attribute
    # 'name' attribute can only be set once
    def name(self):
        return self.__name

    @name.setter
    # We want to set 'name' attribute more than once even it is the read-only attribute
    def name(self, value):
        self.__name = value

    def total_price(self):
        return self.__price * self.quantity

    # converting this method from instance method to class method because we want it to call before an instance is 
    # created
    @classmethod # decorator
    def instantiate_from_csv(cls): # cls is the reference to the class itself
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    # Static method
    @staticmethod
    def is_int(num):
        # We will count out the floats that are point zero
        # For example: 5.0, 11.0
        if isinstance(num, float):
            # Check number is integer or not using `is_integer` function
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"