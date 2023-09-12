class Family:
    def __init__(self):
        self.member = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}
        ]     

    def born(self,**info):
        is_child = False
        self.members.append(info)
        print("New member in the family")

    def is_18(self,firstname):
        for member in self.member:
            if member['name'] == firstname and menver['age']> 18:
                return True
            else:
                return False

    def family_presentation(self):
        sentence = f"the{self.lastname}vfamily contains"
        for index, member in enumerate(self.members):
            sentence +=f" and {member['name']}"
        else
            sentence +=f" {member['name'],}"
        print(sentence)

my_family = Family('smith')
my_family.born(name = 'Lise', age = 18, gender = 'female', is_child = True)
my_family.family_presentation()



class TheIncredibles(Family):
    
    def use_power(self,name):
        if self.is_18(name):
            for member in self.member:
                if member["name"] :
                    print(member['name'])


existing_members:[
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]


   
