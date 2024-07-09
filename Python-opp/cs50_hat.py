import random

class Hat:
    houses = ['seeta', 'mukono', 'kireka']
    
    @classmethod
    def sorting(cls, name):
        print(f'{name} is in {random.choice(cls.houses)}')

 
 Hat.sorting('samuel')