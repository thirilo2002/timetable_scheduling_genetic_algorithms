import random
Week_day=5
No_of_class=9
class Data :
    def __init__(self,student,professor,course,room):
        self.student=student
        self.professor=professor
        self.course=course
        self.room=room
        self.timeslots=[[ [] for _ in range(No_of_class)] for _ in range(Week_day)]

    def assign_random(self):
        max_room=len(self.room)
        #max_room=1
        for course in self.course:
            k=course.periods
            for _ in range(int(k)):
                x,y=random.randint(0,Week_day-1),random.randint(0,No_of_class-1)
                while (course.course in self.timeslots[x][y] or  len(self.timeslots[x][y])==max_room):
                    x,y=random.randint(0,Week_day-1),random.randint(0,No_of_class-1)
                self.timeslots[x][y].append(course.course)
        # for i in range(5):
        #     print(self.timeslots[i])
        #     print()