# timetable_scheduling_genetic_algorithms
## TimeTable  Scheduling Generation using Genetic ALgorithmn

# The Main.py contains Main code
Genetic_algo part
Basically We will randomly populate the population
Then Fitness function is used to sort Individual based on their Quality
Criteria for Fitness Function\n
      Hard Constraints:
      No student can have two class at a same time
      No  Teachers have to teach class at a same time
Fitness function= (1/(1+Number of conflicts(No student can have two class at a same time)+Number of conflicts(No  Teachers have to teach class at a same time)))
Higher Fitness function implies good Individual
current population= randomly assigned
loop
  sort the current population based on Fitness Function(Descending Order) 
  if Fitness[First Indidual in population(after sorted)]==1:
      stop Solution =First individual is reached
      break loop
  Top 30 send to next generation
  70 percentage of remaining population is crossover of two Best Individual(randomly from top 30 population)
  Crossover(It is Done By Merging two TimeTable so count of each courses is doubled so we will randomly remove half of each courses so that it satisfy the constraints)
  30  percentage of remaining population is formed by mutation
  Mutation (Randomly moving one course from one slot  to another)
  
  Next Generation is created 
  current =Next
  
loop

Solution is passed to simulated annealing to remove conflicts like having two class of same course on same day
simulated annealing will provide solution we will try to print it`


