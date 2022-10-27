
class Mug():
    '''Use this mug if you need to break something'''
    number = 42 # This is a class attribute
    def __init__(self, color, name = 'Default', breakable = True):
        self.name = name # Instance attributes are created in the constructor
        self.color = color
        self.breakable = breakable

        # All the code in this method executes when an instance is created
        print("New mug instance created!") 

    def smash(self, surface = 'floor'):
        '''Prints an appropriate line depending on the properties of the mug'''
        if self.breakable:
            print(f"There are now many {self.color} shards all over the {surface}")
        else:
            print(f"The mug called {self.name} is now on the {surface}")
        return id(self)

    def print_name(self):
        '''Print the mug nmae'''
        print(self.name)

    def change_name(self, new_name):
        '''Change the mug name'''
        self.name = new_name


if __name__ == "__main__":
    # Instantiation happens here
    robbies_mug = Mug('White')
    jareds_mug = Mug('Gray', 'Blender Bottle', breakable=False)

    # We can use our objects
    robbies_mug.print_name()
    robbies_mug.change_name('The Mug of VI')
    robbies_mug.print_name()
    smashed_id = robbies_mug.smash('wall')
    print(smashed_id)

    jareds_mug.print_name()
    jareds_mug.smash()

    # Our user-defined objects have a type and id
    print("type", type(jareds_mug))
    print("id", id(jareds_mug))





