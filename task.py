days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
curr=input("Enter today: ")

for m in range(len(days)):
    if curr==days[m]:
            print(f"\nSchedule For {days[m]}: ")
            print("Enter number of tasks: ")
            task=[]
            n=int(input())
            for i in range(n):
                print(f"Enter task {i+1}:")
                t=input()
                task.append(t)
            print(f"Tasks for {days[m]}: ")
            for index,i in enumerate(task):
                print(f"Task {index+1} : {i}")
