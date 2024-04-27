class Class:
    def __init__(self,room):
        self.room=room
    def __str__(self):
        return f"{self.room}"
        
class Professor:
    def __init__(self,id,name,Course_list):
        self.courses=Course_list
        self.id=id
        self.name=name
    def __eq__(self,id):
        if self.id==id:
            return self
    def __str__(self):
        return f"{self.id},{self.name},{self.courses}"
    
class Student:
    def __init__(self,id,name,Courses):
        self.id=id
        self.name=name
        self.course=Courses        
    def __str__(self):
        return f"{self.id},{self.name},{self.course}"
class Courses:
    def __init__(self,Course,Proflist,periods):
        self.course=Course
        self.Professors=Proflist
        self.periods=periods
        self.students=[]
        
    def __str__(self):
        return f"{self.course},{self.Professors},{self.periods},{self.students}"    
              
# P1=Professor("1","thirilo","le")
# P2=Professor(2,"thirilo","le")
# print("teacher")
# Professors=[P1,P2]
# p_id=input("Enter the Professor Id\n")
# if p_id in Professors:
   
    