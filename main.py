from Details import Class ,Courses,Student,Professor
from schedule import Data
from genetic_algo import Genetic_Algo
from pdfwriter import *
Week_day=5
No_of_class=9
from annealing import Simulated_annealing
#from annealing import Simulated_annealing
def TimeTablepdf(TimeTable):
    NewTable=[[] for _ in range(Week_day+1)]
    NewTable[0]=["  ","8.00-9.00","9.00-10.00","10.00-11.00","11.00-12.00","1.00-2.00","2.00-3.00","3.00-4.00","4.00-5.00","5.00-6.00"]
    days=["Mon","Tue","Wed","Thurs","Fri"]
    for i,day in enumerate(days):
        NewTable[i+1].append(day)
    for i in range(1,Week_day+1):
                for j in range(No_of_class):
                    if TimeTable[i-1][j]:
                        NewTable[i].append(TimeTable[i-1][j][0])
                    else:
                        NewTable[i].append("  ")
   #create_pdf("hello.pdf",NewTable)
    return NewTable


def Parse(string):
    if string[0]=="!":
        return 0,9
    Split=string.split()
    
    List=[]
    if Split[0]=="<stud>":
        
        for i in range(1,len(Split)-2):
            List.append(Split[i])
        List.append(Split[len(Split)-2].split(','))
        return "student",Student(*List)
    elif Split[0]=="<prof>":
        for i in range(1,len(Split)-2):
            List.append(Split[i])
        List.append(Split[len(Split)-2].split(','))
        return "professor",Professor(*List)      
    elif Split[0]=="<course>":
        for i in range(1,len(Split)-1):
            if i==2:
               List.append(Split[i].split(","))
            else:
                List.append(Split[i])
            
        return "course",Courses(*List)    
    else:
       for i in range(1,len(Split)-1):
            List.append(Split[i])
       return "class",Class(*List)
def GetDetails():
    Students=[]
    Classes=[]
    Course=[]
    Professors=[]

    f=open("Details.txt","r")   
    while True:
        ans= f.readline()
        #print("ji",ans,"ji")
        if  not ans or ans=='\n':
            break
        type,Value=Parse(ans)
        #print(type)
        if type=='student':
            Students.append(Value)
            for course in Value.course:
                for course1 in Course:
                    if course1.course==course:
                        course1.students.append(Value.id)
             
        elif type=='class':
            Classes.append(Value)
        elif type=='course':
            Course.append(Value)
        elif type=='professor':
            Professors.append(Value)
            for course in Value.courses:
                for course1 in Course:
                    if course1.course==course:
                        course1.Professors.append(Value.id)
    return Students,Classes,Course,Professors




def main():
    Students,Classes,Course,Professors=GetDetails()
    d1=Data(Students,Professors,Course,Classes)
    Reached=False
    TimeTable=None
    for _ in range(1):
        d1.assign_random()
        # obj=Simulated_annealing(d1)
        # obj.annealing()

        Genetic_Algo.Data=d1
        Instances=Genetic_Algo()
        Instances.Populate()
        Instances.SortbyFitness()

        for _ in range(500):
            NewInstances=Instances.NextGeneration()
            
            NewInstances.SortbyFitness()
            print(NewInstances.population[0][0])
            if NewInstances.population[0][0]==1:


                print("Reached Solution")
                #free_slots=NewInstances.Diffuse(NewInstances.population[0][1])
                # free_list=NewInstances.Freeslots_Day(NewInstances.population[0][1])
                # cost3,list3=NewInstances.Having_Two_class_sameday(NewInstances.population[0][1])
                # for i  in range(Week_day):
                #     for j in range(Week_day):
                #         if i!=j:
                #             if free_list[i]:
                #                 k=free_list[i].pop(0)
                #                 if list3[j]:
                #                     slot,course=list3[j].pop(0)
                #                     NewInstances.population[0][1][j][slot].remove(course)
                #                     NewInstances.population[0][1][i][k].append(course)
                #                 else:
                #                     free_list[i].append(k)    

                    

                #NewInstances.printer(NewInstances.population[0][1])
                TimeTable=NewInstances.population[0][1]
                
                Reached=True
                break
            Instances=NewInstances
        #print("solution")
            if Reached:
                break
        print()
        sim_annealing=Simulated_annealing(Data=d1,Timeavail=TimeTable)
        TimeTable=sim_annealing.annealing()
        #TimeTablepdf(TimeTable)
        NewInstances.printer(TimeTable)
        check=int(input('Enter the 1 for Professor\nEnter 2 for student '))
        if check==2:
            s_id=input("Enter the Student Id : ")
            
            for student in Students:
                if student.id==s_id:
                    name=student.name
            name       
            courses_taken=[student.course for student in Students if student.id==s_id][0]
            print(courses_taken)
            TimeTableNew=[[ [] for _ in range(No_of_class)] for _ in range(Week_day)]

            for i in range(Week_day):
                for j in range(No_of_class):
                    for course in courses_taken:
                        if course in TimeTable[i][j]:
                            TimeTableNew[i][j].append(course)
            NewInstances.printer(TimeTableNew)
            TimeTableNew=TimeTablepdf(TimeTableNew)
            print(TimeTableNew)
            create_pdf(s_id+"_"+name+".pdf",TimeTableNew)

        else:
            
            p_id=input("Enter the Professor Id")
            for professor in Professors:
                if professor.id==p_id:
                    name=professor.name

            courses_taken=[professor.courses for professor in Professors if professor.id==p_id][0]
            print(courses_taken)
            TimeTableNew=[[ [] for _ in range(No_of_class)] for _ in range(Week_day)]

            for i in range(Week_day):
                for j in range(No_of_class):
                    for course in courses_taken:
                        if course in TimeTable[i][j]:
                            TimeTableNew[i][j].append(course)
            NewInstances.printer(TimeTableNew)
            TimeTableNew=TimeTablepdf(TimeTableNew)
            print(TimeTableNew)
            create_pdf(p_id+"_"+name+".pdf",TimeTableNew)
        if Reached:
            break

        

if __name__=="__main__":
    main()






    

    



     