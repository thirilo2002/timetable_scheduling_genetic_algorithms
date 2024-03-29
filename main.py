from Datas.Details import Class ,Courses,Student,Professor
from schedule import Data
from genetic_algo import Genetic_Algo
#from annealing import Simulated_annealing

Students=[]
Classes=[]
Course=[]
Professors=[]

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
            List.append(Split[i])
        return "course",Courses(*List)    
    else:
       for i in range(1,len(Split)-1):
            List.append(Split[i])
       return "class",Class(*List)
def GetDetails():
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
        elif type=='class':
            Classes.append(Value)
        elif type=='course':
            Course.append(Value)
        elif type=='professor':
            Professors.append(Value)




def main():
    GetDetails()
    d1=Data(Students,Professors,Course,Classes)
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
        if NewInstances.population[0][0]<=0:
            NewInstances.printer(NewInstances.population[0][1])
            print("Reached")
            break
        Instances=NewInstances

if __name__=="__main__":
    main()






    

    



     