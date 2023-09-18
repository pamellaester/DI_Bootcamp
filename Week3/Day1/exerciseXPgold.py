# # Exercise 1 : Geometry

# class circle:
#     def __init__(self,radius = 10):
#         self.radius = radius

#     def perimeter(self):
#        PI = 3.14
#        return 2 * PI * self.radius

#     def area(self):
#        PI = 3.14
#        return PI * self.radius * self.radius
    
#     def info(self):
#         print(f"he geometrical definition of a circle is. perimeter: {self.perimeter()} area {self.area()}")

    
# circle_geo = circle()
# circle_geo.info()

# Exercise 2 : Custom List Class

class MyList:
    def __init__(self, name_list ):
        self.list = name_list
        name_list = []

    def reversed_list(self,name_list):
        return name_list.reverse()
    
    def sorted_list(self):
        pass 


the_list = MyList("list",['Windows', 'macOS', 'Linux'])
the_list.reversed_list()