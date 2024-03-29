import copy
import random
Week_day=5
No_of_class=10
class Population:
    Data=None
    def __init__(self,timeslots):
        self.population_size=10;
        self.fitness=None
        self.timeslots=timeslots
    def StudentsHavingClassSame(self,TimeTable=None):
        if TimeTable==None:
            TimeTable=self.Data.timeslots
        global res
        res=0
        Conflict_zones=[]
        for student in self.Data.student:
           
            for i in range(Week_day):
                for j in range(No_of_class):
                    
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
    def TeachersHavingClassSame(self,TimeTable=None):
        global res
        res=0
        if TimeTable==None:
            TimeTable=self.Data.timeslots
        Conflict_zones=[]
        for professor in self.Data.professor:
           
            for i in range(Week_day):
                for j in range(No_of_class):
                    
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
        cost1,List1=self.StudentsHavingClassSame()
        cost2,List2=self.TeachersHavingClassSame()
        return cost1+cost2
class Genetic_Algo:
    Data=None
    def __init__(self):
        self.populationsize=100
        self.population=[]
    def StudentsHavingClassSame(self,TimeTable=None):
        if TimeTable==None:
            TimeTable=self.Data.timeslots
        global res
        res=0
        Conflict_zones=[]
        for student in self.Data.student:
           
            for i in range(Week_day):
                for j in range(No_of_class):
                    
                    cnt=0
                    for courses in student.course:
                        cnt+=TimeTable[i][j].count(courses)
                    
                    if(cnt>=1):
                        cnt-=1
                        if cnt !=0:
                            Conflict_zones.append((i,j))
                    res+=cnt
        return res,Conflict_zones
    def TeachersHavingClassSame(self,TimeTable=None):
        global res
        res=0
        if TimeTable==None:
            TimeTable=self.Data.timeslots
        Conflict_zones=[]
        for professor in self.Data.professor:
           
            for i in range(Week_day):
                for j in range(No_of_class):
                    
                    cnt=0
                    for courses in professor.courses:
                        if courses in TimeTable[i][j]:
                            cnt+=TimeTable[i][j].count(courses)
                    
                    
                    if(cnt>=1):
                        cnt-=1
                        if cnt!=0:
                          Conflict_zones.append((i,j))
                    res+=cnt
        return res,Conflict_zones
    def GetFitness(self,TimeTable=None):
        cost1,List1=self.StudentsHavingClassSame(TimeTable)
        cost2,List2=self.TeachersHavingClassSame(TimeTable)
        return cost1+cost2
    def Populate(self):
        for _ in range(self.populationsize):
            self.Data.assign_random()
            self.population.append([0,copy.deepcopy(self.Data.timeslots)])
            self.Data.timeslots=[[ [] for _ in range(No_of_class)] for _ in range(Week_day)]
            self.population[-1][0]=self.GetFitness(self.population[-1][1])

    def printer(self,Timetable):
        for i in range(Week_day):
            for j in range(No_of_class):
                print(Timetable[i][j],end="  ")
            print("\n")
    def SortbyFitness(self):
        self.population.sort()
        
    def RemoveDuplicates(self,Timeslots):
        Dict=dict()
        
        for i in range(Week_day):
                for j in range(No_of_class):
                    for val in Timeslots[i][j]:
                        if val not in Dict.keys():
                          
                          Dict[val]=[]
                        else:
                            Dict[val].append((i,j))
        for value in Dict.keys():
            length=len(Dict[value])
            req=length//2
            res=0
            while(res<req):
                length=len(Dict[value])
                val=random.randint(0,length-1)
                Values=Dict[value][val]
                Dict[value].remove(Values)
                res+=1
        for i in range(Week_day):
                for j in range(No_of_class):
                    Timeslots[i][j]=[]
        #print(Timeslots)
        for keys in Dict.keys():
                for values in Dict[keys]:
                    u,v=values   
                    Timeslots[u][v].append(keys)
        #print(Timeslots)
        return Timeslots



    def NextGeneration(self):
         # 30 to next gen 
        Next=Genetic_Algo()
        for i in range(50):
            Next.population.append(self.population[i])
        
        # 70 Cross Over into Create Population
        for i in range(50):
            u=random.randint(0,49)
            v=random.randint(0,49)
            Time_slots=[[ [] for _ in range(No_of_class)] for _ in range(Week_day)]
            for i in range(Week_day):
                for j in range(No_of_class):
                    Time_slots[i][j].extend(self.population[u][1][i][j]+self.population[v][1][i][j])
            # print(Time_slots)
            # print("after Duplicates")
            Updated=self.RemoveDuplicates(Time_slots)
            # print(Updated)
            
            Next.population.append([self.GetFitness(Updated),Updated])
        return Next    

        
         
            
