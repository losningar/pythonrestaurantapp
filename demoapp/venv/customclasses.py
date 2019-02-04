class Customer(object):
        def __init__(self):
            self.firstname = "empty"
            self.lastname  = "empty"
            self.email = "empty"
            self.address = "empty"
            self.postcode = "empty"
            self.city = "empty"
            self.username = "empty"
            self.password = "empty"

class Menu(object):
        def __init__(self):
            self.MenuItems = []
            
            
class Ingredient(object):
    def __init__(self):
        self.Name = "empty"
        self.Quantity = 0
                       
            

class MenuItem(object):
        def __init__(self):
            self.Type = "empty"
            self.Name = "empty"
            self.Size = "empty"
            self.Price = "empty"
            self.Ingredients = []          

class Employee(object):
        def __init__(self):
            self.firstname = "empty"
            self.lastname  = "empty"
            self.email = "empty"
            self.permissions = "empty"
            self.username = "empty"
            self.password = "empty"
            self.tokenID = "empty"


class ShoppingCart(object):
        def __init__(self):
            self.userid = "empty"
            self.MenuItems = []
            

            