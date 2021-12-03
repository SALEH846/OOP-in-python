# When to use class methods and when to static methods?

class Item:
    @staticmethod
    def is_int(num):
        '''
        This should do something that has a relationship with the class,
        but not something that must be unique per instance!
        '''

    @classmethod
    def isntantiate_from_something(cls):
        '''
        This should also do something that has a relationship with the class, but usually,
        those are used to manipulate different structures of data to instantiate objects,
        like we have done with CSV.
        '''

# NOTE: A notable difference between static and class method is that static method does not pass reference of 
# the class itself as the first argument

# Static methods and class methods can also be called from instance level
item1 = Item()
item1.is_int(5)
item1.isntantiate_from_something()