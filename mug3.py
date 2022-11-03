import random

class LiquidContainer():
    '''Object to hold liquid'''
    def __init__(self, type, volume, melting_point = 200, contents = "nothing", contents_volume = 0.0, contents_temp = 25, breakable = True):
        self.type = type # mug, bottle, cup, bucket, etc.
        self.volume = volume # ml
        self.contents = contents
        self.contents_volume = contents_volume # ml
        self.contents_temp = contents_temp #C
        self.breakable = breakable
        self.melting_point = melting_point
    
    def pour(self, volume_to_pour):
        '''pour liquid out of the container'''
        self.contents_volume -= volume_to_pour
        if self.contents_volume <= 0:
            self.empty()
        return self.contents_volume


    def shatter(self, surface = 'floor'):
        if not self.breakable:
            print(f"Your {self.type} is now on the floor")
        elif self.contents == 'nothing':
            print(f"Your {self.type} has shattered into {random.randint(100, 100000)} shards on the {surface}")
        else:
            print(f"Your {self.type} has shattered into {random.randint(100, 100000)} shards and you have {self.contents_volume} ml {self.contents} on the {surface}")

    def empty(self):
        self.contents = 'nothing'
        self.contents_volume = 0.0
        return f'{self.type} emptied'

    def add_liquid(self):
        pass

    def __str__(self):
        return f"A {self.volume} ml {self.type} that melts at {self.melting_point} with {self.contents_volume} ml of {self.contents}."


if __name__ == "__main__":
    mrnichols_mug = LiquidContainer('mug', 300, contents='coffee', contents_volume=200)
    jt_bottle = LiquidContainer('bottle', 1000, contents='water', contents_volume= 15)

    print("type", type(mrnichols_mug))
    print("id", id(mrnichols_mug))

    print(mrnichols_mug)
    mrnichols_mug.shatter('wall')