import csv

class Item:
    pay_rate = 0.8 # class variable
    all = [] # list of instances of this class

    def __init__(self, name: str, price: float, quantity=0):
        # validation of price and quantity
        assert price >= 0, f"Price {price} is neither greater than nor equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is neither greater than nor equal to zero"

        # Instance variables
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

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
        return f"Item('{self.name}', {self.price}, {self.quantity})"

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(item1.total_price())
# print(item2.total_price())

# Accessing class variables
# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)

# All the class level attributes
# print(Item.__dict__)

# All the instance level attributes
# print(item1.__dict__)

# item1.apply_discount()
# print(item1.price)

# Changing class level attribute for a particular object
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

# list of all instances
# print(Item.all)
# for instance in Item.all:
# print(instance.name)

# Creating instances from a csv file
# Item.instantiate_from_csv()
# print(Item.all)

# Checking is `is_integer` method
print(Item.is_int(7.6))
print(Item.is_int(7))
print(Item.is_int(7.0))