class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def LEN(self):
        return len(self.items)

candy_dispenser = Stack()

# the candies available

tomato = 'tomato'
royalblue = 'royalblue' 
saddlebrown = 'saddlebrown'
chocolate = 'chocolate'
aqua = 'aqua'
purple = 'purple'
violet = 'violet'
pink = 'pink'
yellow = 'yellow'
blue = 'blue'
red = 'red'
orange = 'orange' 

# the initial order 12 candies were pushed

candy_dispenser.push(tomato)
candy_dispenser.push(royalblue)
candy_dispenser.push(saddlebrown)
candy_dispenser.push(chocolate)
candy_dispenser.push(aqua)
candy_dispenser.push(purple)
candy_dispenser.push(violet)
candy_dispenser.push(pink)
candy_dispenser.push(yellow)
candy_dispenser.push(blue)
candy_dispenser.push(red)
candy_dispenser.push(orange)

#new code goes down here:
