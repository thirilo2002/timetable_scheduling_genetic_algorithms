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
    def __str__(self):
        return f"{self.course},{self.Professors},{self.periods}"    
              