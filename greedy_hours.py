#An office needs to distribute 2 tasks out of 6 to 3 employees
#The employees collectively must complete the tasks in the lowest amount of time possible
#It's assumed all employees will take the same amount of time to complete the tasks

task_hours = [6,7,3,9,2,4]
task_hours.sort()
#task list is now sorted from lowest to highest
Dan = []
Vicki = []
Reginald = []
#according to the greedy algorithm, 1 employee should have the lowest and highest, the next employee the next highest and lowest, and the last employee the middle values
Dan.append(task_hours[0])
Dan.append(task_hours[-1])
Vicki.append(task_hours[1])
Vicki.append(task_hours[-2])
Reginald.append(task_hours[2])
Reginald.append(task_hours[-3])   

print(f"Time required: {sum(Dan)}")