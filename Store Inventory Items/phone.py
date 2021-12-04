from item import Item

class Phone(Item):
    all = [] # list of instances of this class

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function in order to get access to all the attributes and methods of parent class
        super().__init__(
            name, price, quantity
        )

        # validation of price and quantity
        assert broken_phones >= 0, f"Broken Phones {broken_phones} must be greater than or equal to zero"

        # Instance variables
        self.broken_phones = broken_phones

        Phone.all.append(self)