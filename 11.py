def first():
    class restaurant:
        def __init__(self,restaurant_name,cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(self.restaurant_name, " ", self.cuisine_type)
        def open_restaurant(self):
            print(self.restaurant_name, " открыт")

    newrestaurant = restaurant("усы лисы", "итальянская")
    print(newrestaurant.restaurant_name)
    print(newrestaurant.cuisine_type)

    newrestaurant.describe_restaurant()
    newrestaurant.open_restaurant()
def second():
    class restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(self.restaurant_name, " ", self.cuisine_type)

        def open_restaurant(self):
            print(self.restaurant_name, " открыт")

    restaurant1 = restaurant("усы лисы1", "итальянская1")
    restaurant2 = restaurant("усы лисы2", "итальянская2")
    restaurant3 = restaurant("усы лисы3", "итальянская3")
    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()
def third():
    class restaurant:
        def __init__(self, restaurant_name, cuisine_type, rate):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rate = rate

        def describe_restaurant(self):
            print(self.restaurant_name, " ", self.cuisine_type)

        def open_restaurant(self):
            print(self.restaurant_name, " открыт")

        def rate(self, new_rate):
            self.rate = new_rate
            print("новое значение: ", self.rate)
    rating = int(input())
    rest1 = restaurant("усы лисы", "итальянская",4)
    rest1.rate(rating)
third()