import random
import copy
from math import exp
Week_day=5
No_of_class=9
import matplotlib.pyplot as plt
class Simulated_annealing():
    
    def __init__ (self,Data,Timeavail=False):
        
        self.Data=Data
        self.dictionary=dict()
        for course in self.Data.course:
            self.dictionary[course.course]=course
        if Timeavail:
            self.Data.timeslots=Timeavail
        #self.Data.timeslots=[[[] for _ in  range(7)] for _ in range(5)]
        self.max_iterations=None
        
    def StudentsHavingClassSame(self,TimeTable=None):
        if TimeTable==None:
            TimeTable=self.Data.timeslots
        global res
        res=0
        Conflict_zones=[]
        for student in self.Data.student:
           
            for i in range(5):
                for j in range(7):
                    
                    cnt=0
                    for courses in student.course:
                        if courses in TimeTable[i][j]:
                            cnt+=1
                    
                    if(cnt>=1):
                        cnt-=1
                        if cnt !=0:
                            Conflict_zones.append((i,j))
                    res+=cnt
        return res,Conflict_zones
    def Having_Two_class_sameday(self,TimeTable=None):
        penalty=0
        List3=[]
        if not TimeTable:
            TimeTable=self.Data.timeslots
        for i in range(Week_day):
            Sets=set()
            for j in range(No_of_class):
                for course   in TimeTable[i][j]:
                    if course not in Sets:
                        Sets.add(course)
                    else:
                        List3.append((i,j))
                        penalty+=1
        return penalty,List3
    def TeachersHavingClassSame(self,TimeTable=None):
        global res
        res=0
        if TimeTable==None:
            TimeTable=self.Data.timeslots
        Conflict_zones=[]
        for professor in self.Data.professor:
           
            for i in range(5):
                for j in range(7):
                    
                    cnt=0
                    for courses in professor.courses:
                        if courses in TimeTable[i][j]:
                            cnt+=1
                    
                    
                    if(cnt>=1):
                        cnt-=1
                        if cnt!=0:
                          Conflict_zones.append((i,j))
                    res+=cnt
        return res,Conflict_zones
    def GetFitness(self):
        # cost1,List1=self.StudentsHavingClassSame()
        # cost2,List2=self.TeachersHavingClassSame()
        cost3,List3=self.Having_Two_class_sameday()
        return cost3,List3,0
    def Succesor(self,L1,L2=0):
        #val=random.choice([0,1])
        Reached=False
        while not Reached:
            Timeslots=copy.deepcopy(self.Data.timeslots)
        #    if len(L1)==0:
        #        val=1
        #    elif len(L2)==0:
        #        val=0
            
            
            u,v= random.choice(L1)

            x,y=random.randint(0,Week_day-1),random.randint(0,No_of_class-1)
            cnt=0
            Temp=Timeslots[x][y]
            Timeslots[x][y]=Timeslots[u][v]
            Timeslots[u][v]=Temp
            return Timeslots
                    
                    
      
       

            
                
    def There_exists_student(self,course,u,v,TimeTable):
        if not TimeTable[u][v]:
            return False
        
        Student_list=self.dictionary[course].students
        Student_first=set(Student_list)
        for courses in TimeTable[u][v]:
            Student_second=set(self.dictionary[courses].students)
            And=Student_first.intersection(Student_second)
            if And:
                return True
        return False
    def There_exists_Teacher(self,course,u,v,TimeTable):
        if not TimeTable[u][v]:
            return False
        
        Professor_list=self.dictionary[course].Professors
        Professor_first=set(Professor_list)
        for courses in TimeTable[u][v]:
            Professor_second=set(self.dictionary[courses].Professors)
            And=Professor_first.intersection(Professor_second)
            if And:
                return True
        return False


                        



        
    def annealing(self,max_iterations=5000):   
        self.max_iterations=max_iterations
        Temperature=1e+10
        beta=.97
        Curr=self
        iters=[]
        data=[]
        for iter in range(max_iterations):
            curr_cost,L1,L2 =   Curr.GetFitness()
            print(curr_cost)
            #data.append(curr_cost)
            iters.append(iter)
            data.append(curr_cost)
            if (curr_cost==0):
                print("goal has reached")
                # print(Curr.Data.timeslots)
                break
            
            Timeslots= self.Succesor(L1)
            Succesor=Simulated_annealing(Curr.Data,Timeslots)
            succ_cost,_,_=Succesor.GetFitness()
            Delta_E=succ_cost-curr_cost 
            if Delta_E < 0:
                Curr=Succesor
            else:
               p= random.random()
               q=exp(-Delta_E/Temperature)
               if(p>=q):
                   Curr=Succesor
            Temperature*=beta
        plt.plot(iters,data)
        plt.title("Gradient Descent")
        plt.xlabel("iterations")
        plt.ylabel("cost")
        plt.show()
        return Curr.Data.timeslots
       
            