import taskA.index as taskA
import taskB.index as taskB

# loop to demonstrate tasks 
while(1):
  option = input("Choose option... \n1. demonstrate task 1 \n2. demonstrate task 2 \npress any key to exit....")
  if(option == "1"): 
    taskA.task()
  elif(option == "2"): 
    taskB.task()
  else: break