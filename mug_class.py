
class Mug():
    '''A virtual mug from which you can drink coffee'''
    def __init__(self, color: str, mug_volume = 8, contents = 'Nothing', contents_volume = 0.0):
        self.color = color
        self.mug_volume = mug_volume # in oz
        self.contents = contents
        self.contents_volume = contents_volume # in oz


    def drink(self, volume):
        '''Take a drink'''
        self.contents_volume -= volume
        if self.contents_volume <= 0:
            self.empty()


    def add_contents(self, volume, substance):
        '''add a substance to the mug'''
        if self.contents == 'Nothing' or self.contents == substance:
            self.contents = substance
            self.contents_volume += volume
        else:
            print("Don't mix drinks!!")

        if self.contents_volume > self.mug_volume:
            print(f"Your {substance} overflowed")
            self.contents_volume = self.mug_volume


    def empty(self):
        '''Empty the contents of the mug'''
        self.contents = 'Nothing'
        self.contents_volume = 0.0


    def __str__(self):
        '''Python uses this special method in cases where 
           it needs a string representation of your instance
        '''
        return f"A {self.color} mug with volume {self.mug_volume} containing {self.contents_volume} oz. of {self.contents}"

if __name__ == "__main__":
    mrnichols_mug = Mug("white")
    student_mug = Mug("blak", contents= 'Coffee', contents_volume=.5)

    mrnichols_mug.add_contents(10,'Water')
    print(mrnichols_mug)
    print(student_mug)
    print(mrnichols_mug.color)

    print("type", type(mrnichols_mug))
    print("id", id(mrnichols_mug))