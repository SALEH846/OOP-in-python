from item import Item
from phone import Phone

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
# print(Item.is_int(7.6))
# print(Item.is_int(7))
# print(Item.is_int(7.0))

# Inheritance
# phone1 = Phone("jscPhonev10", 500, 5, 1)
# print(phone1.total_price())
# phone2 = Phone("jscPhonev20", 700, 5, 1)
# print(Item.all)
# print(Phone.all)

# Property decorator
# So, a particualr attribute can only be set only once
# item6 = Item("MyItem", 500)
# print(item6.name)
# item6.name = "OtherItem" # will throw an error as we can't set it twice (in case '@name.setter' decorator is not defined)

# Changing 'name; attribute
# item6.name = "OtherItem"
# print(item6.name)