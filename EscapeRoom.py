import inspect

print("You are trapped in a room.")
print("What do you do?")

class Room:
    def inspect(self):
        print("The walls are white. There is a window and a desk.")
        fixtures['desk'] = Desk()
        fixtures['walls'] = Walls()
        fixtures['window'] = Window()

    def help(self): print("room: inspect")

class Desk:
    def inspect(self):
        print("The desk has a drawer.")
        fixtures['drawer'] = Drawer()

    def help(self): print("desk: inspect")

class Drawer:
    def __init__(self):
        self.opened = False
        self.empty = False

    def inspect(self):
        if not self.opened:
            print("The drawer is closed.")
        elif self.empty:
            print("The drawer is empty.")
        else:
            print("You find a combination code: xyzzy")
            inventory.append("xyzzy")
            self.empty = True

    def open(self):
        if self.opened:
            print("It's already open!")
        else:
            print("The drawer slides open.")
            self.opened = True
            self.inspect()

    def close(self):
        if self.opened:
            print("The drawer slams shut.")
            self.opened = False
        else:
            print("It's already closed, silly.")

    def help(self): print("drawer: inspect, open, close")

class Walls:
    def inspect(self):
        print("There is a safe.")
        fixtures["safe"] = Safe()

    def help(self): print("walls: inspect")

class Safe:
    def __init__(self):
        self.opened = False
        self.items = ["hammer"]

    def inspect(self):
        print("You don't know how to open it.")

    def open(self):
        if self.opened:
            print("The safe is already open.")
        elif "xyzzy" in inventory:
            print("You find a hammer in the safe.")
            inventory.append("hammer")
            self.items.remove("hammer")
            self.open = True
        else:
            print("You need a code to open the safe.")
    
    def close(self):
        if self.opened:
            print("The safe closes and locks.")
        else:
            print("It's already closed.")

    def help(self): print("safe: inspect, open, close")

class Window:
    def inspect(self):
        print("It might break if you can hit it hard enough.")

    def hit(self):
        if "hammer" in inventory:
            print("You smash the window with the hammer and escape!")
            print("The End")
            quit()
        else:
            print("It's stronger than you thought.")

    def help(self): print("window: inspect, hit")

def NotFound(): print("You haven't found that.")

fixtures = { "room" : Room() }
inventory = []

while True:
    command = input("> ").strip()

    if command == "quit":
        print("Goodbye.")
        quit()

    elif " " in command:
        action,subject = command.split(" ")[:2]
        fixture = fixtures.get(subject);
        getattr(fixture, action, NotFound)()

    elif command == "status":
        print("You are carrying",inventory)
        print("You found %s" % list(fixtures.keys()))

    else:
        print("Unknown command:",command)

