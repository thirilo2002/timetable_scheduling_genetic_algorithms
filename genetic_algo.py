import copy
import random
Week_day=5
No_of_class=9

class Genetic_Algo:
    Data=None
    def __init__(self):
        self.populationsize=200
        self.population=[]
    def Diffuse(self,Timetable=None):
            Freeslots=[]
            for i in range(Week_day):
                    for j in range(No_of_class):
                        if not Timetable[i][j]:
                            Freeslots.append((i,j))
            return Freeslots
    def Freeslots_Day(self,TimeTable=None):
          Freeslots=[[]for i in range(Week_day)]
          print(Freeslots)
          for i in range(Week_day):
                for j in range(No_of_class):
                    if not TimeTable[i][j]:
                        Freeslots[i].append(j)
          return Freeslots

    def Having_Two_class_sameday(self,TimeTable=None):
        penalty=0
        List3=[[]for i in range(Week_day)]
        for i in range(Week_day):
            Sets=set()
            for j in range(No_of_class):
                for course   in TimeTable[i][j]:
                    if course not in Sets:
                        Sets.add(course)
                    else:
                        List3[i].append((j,course))
                        penalty+=1
        return penalty,List3



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
    def Mutate(self,TimeTable=None):
        x,y=random.randint(0,Week_day-1),random.randint(0,No_of_class-1)
        u,v=random.randint(0,Week_day-1),random.randint(0,No_of_class-1)
        if TimeTable[x][y]:
            choice=random.choice(TimeTable[x][y])
            TimeTable[u][v].append(choice)
            TimeTable[x][y].remove(choice)
        elif TimeTable[u][v]:
            choice=random.choice(TimeTable[u][v])
            TimeTable[x][y].append(choice)
            TimeTable[u][v].remove(choice)

        return TimeTable


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
        free_slots=self.Diffuse(TimeTable)
        
        cost1,List1=self.StudentsHavingClassSame(TimeTable)
        cost2,List2=self.TeachersHavingClassSame(TimeTable)
        #cost3,List3=self.Having_Two_class_sameday(TimeTable)
        if cost1 :
            u,v=List1[0]
            if free_slots:
                un,vn=free_slots.pop(0)
                value =TimeTable[u][v][0]
                TimeTable[u][v].remove(value)
                TimeTable[un][vn].append(value)
                
        elif cost2 :
            u,v=List2[0]
            if free_slots:
                un,vn=free_slots.pop(0)
                value =TimeTable[u][v][0]
                TimeTable[u][v].remove(value)
                TimeTable[un][vn].append(value)
                
                
        # elif cost3:
        #     u,v=List3[0]
        #     if free_slots and TimeTable[u][v]:
        #         un,vn=free_slots.pop(0)
        #         value =TimeTable[u][v][0]
        #         TimeTable[u][v].remove(value)
        #         TimeTable[un][vn].append(value)
            
        return 1/(1+cost1+cost2),[List1,List2]
    def Populate(self):
        for _ in range(self.populationsize):
            self.Data.assign_random()
            self.population.append([0,copy.deepcopy(self.Data.timeslots)])
            self.Data.timeslots=[[ [] for _ in range(No_of_class)] for _ in range(Week_day)]
            self.population[-1][0],_=self.GetFitness(self.population[-1][1])

    def printer(self,Timetable):
        for i in range(Week_day):
            for j in range(No_of_class):
                print(Timetable[i][j],end="  ")
            print("\n")
    def SortbyFitness(self):
        self.population.sort(reverse=True)
        
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
        # for i in range(20):
        #     Next.population.append(self.population[i])
        
        # # 70 Cross Over into Create Population
        # for i in range(80):
        #     u=random.randint(0,29)
        #     v=random.randint(0,29)
        #     Time_slots=[[ [] for _ in range(No_of_class)] for _ in range(Week_day)]
        #     for i in range(Week_day):
        #         for j in range(No_of_class):
        #             Time_slots[i][j].extend(self.population[u][1][i][j]+self.population[v][1][i][j])
        #     # print(Time_slots)
        #     # print("after Duplicates")
        #     Updated=self.RemoveDuplicates(Time_slots)
        #     # print(Updated)
        #     fitness,_=self.GetFitness(Updated)
        #     Next.population.append([fitness,Updated])
        
        for i in range(self.populationsize):
            p=random.uniform(0,1)
            if i<=30 :
                Next.population.append(self.population[i])
            else:
                if p<0.7:
                    u=random.randint(0,29)
                    v=random.randint(0,29)
                    Time_slots=[[ [] for _ in range(No_of_class)] for _ in range(Week_day)]
                    for i in range(Week_day):
                        for j in range(No_of_class):
                            Time_slots[i][j].extend(self.population[u][1][i][j]+self.population[v][1][i][j])
                    # print(Time_slots)
                    # print("after Duplicates")
                    Updated=self.RemoveDuplicates(Time_slots)
                    # print(Updated)
                    fitness,_=self.GetFitness(Updated)
                    Next.population.append([fitness,Updated])
                else:
                    Time_Table=self.Mutate(self.population[i][1])
                    fitness,_=self.GetFitness(Time_Table)
                    Next.population.append([fitness,Time_Table])
        #Next.SortbyFitness()
        return Next    

        
         
            
