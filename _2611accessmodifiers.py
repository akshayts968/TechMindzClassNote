
class Student:
    def __init__(self,name,m1,m2,m3,m4,m5):
        # Instance Variables
        self.name = name # Others are public can be accesed from any where
        self._m1 = m1 # Protected variable can use inside class,subclass,same package but not in other package means other module
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.__m5 = m5 # Privzte only used inside the class but not in  subclass,same package other package
        # self.sum = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
    def sum_of_marks(self):
        sum = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        print(f"{self.name} has a Total of {sum} out of 250")