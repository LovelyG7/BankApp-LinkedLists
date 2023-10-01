""" 
Implementing a queue as a list with the python list method
"""

class Queue: 
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

class IceCreamShop: 
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        self.customer = customer
        self.flavor = flavor
        self.scoops = scoops

        if flavor is not self.flavors: 
            print("Sorry, we don't have that flavor")

        elif scoops is not [1-4]:
                print("Choose between 1-3 scoops.")
        else:
                print("Order Created!")

        order = {"customer": customer,"flavor":flavor, "scoops": scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
         for orders in self.orders.items:
            print("Customer: {orders['customer']} --Flavor: {orders['flavor']} --Scoops: {orders['scoops']} ")

    def next_order(self):
        print("Next order up!")
        icecream = self.orders.dequeue()
        print("Customer:",customer, "--Flavor:"flavor," --Scoops:"scoops)


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()