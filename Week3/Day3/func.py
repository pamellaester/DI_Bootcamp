class func:
    def __init__(self,number) -> None:
        self.number = number
 
    def __add__(self,another_number):
        return self.number + another_number.number


c1 = func(5)
c2 = func(10)

print(int(c1 + c2))