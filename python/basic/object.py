import datetime

class Student():
    def __init__(self, id, firstname, lastname, age):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    def age1(self):
        self.age -= 1

        return self.age




def main():
   std = Student(1,"Nany", "Fonseca", 22)
   print(std.id)
   print(std.firstname)
   print(std.lastname)
   print(std.age)
   print(std.age1())
   print(std.age)
  


main()
