import os
import time
import sys
import importlib

sys.path.insert(0, r'\Users\reza yousofvand\Desktop\OS_Project\Project\Algorithm')

from processClass import process
from ..Algorithm import *



queue1 =[]
queue2 =[]
queue3 =[]

q1_algorithm = None
q2_algorithm = None
q3_algorithm = None

q1_quantom = 8
q2_quantom = 16

current_state = "Q1"
current_time = 0

process_list = []

previous_process = None

process_number=int(input("Please enter number of process:\n"))
if process_number<1:
    while process_number<1:
        process_number = int(input("Error!\nPlease enter number of process:\n"))

os.system("cls")

print("Please enter your process (Arrival Time, Duration, Priority,):\n")

i = process_number
while i:

    entry = input("Enter Arrival Time of "+"process:"+str(process_number-i+1)+"\n")
    if entry == ""or not entry.isnumeric():
        while entry == ""or not entry.isnumeric():
            entry = input("Error!\nEnter Arrival Time of " +"process:"+str(process_number-i+1)+"\n")

    time = input("Enter Duration of "+"process:"+str(process_number-i+1)+"\n")
    if time == "" or not time.isnumeric() :
        while time == "" or not time.isnumeric():
            time = input("Error!\nEnter Duration of "+"process:"+str(process_number-i+1)+"\n")

    priority = input("Enter Priority of "+"process:"+str(process_number-i+1)+"\n")
    if priority == "" or not priority.isnumeric():
        while priority == "" or not priority.isnumeric():
            priority = input("Error!\nEnter Priority of " +"process:"+str(process_number-i+1)+"\n")

    process_list.append(process(i, int(entry), int(time), int(priority)))
    i -= 1

os.system("cls")

algorithm_list = os.listdir(r"..\Algorithm")
algorithm_list.remove("Template.py")
print(str(algorithm_list))
q1_algorithm = input("Please choose 1st Queue algorithm \n")
while not (q1_algorithm in algorithm_list):
    q1_algorithm = input("Error!\nPlease choose 1st Queue algorithm \n")

q2_algorithm = input("Please choose 2nd Queue algorithm \n")
while not (q2_algorithm in algorithm_list):
    q2_algorithm = input("Error!\nPlease choose 2nd Queue algorithm \n")

q3_algorithm = input("Please choose 3ed Queue algorithm \n")
while not (q3_algorithm in algorithm_list):
    q3_algorithm = input("Error!\nPlease choose 3ed Queue algorithm \n")

while True:
    for i in process_list:
        if i.entry == current_time:
            queue1.append(i)
            process_list.remove(i)

    if current_state == "Q1" and len(queue1) == 0:
        current_state = "Q2"

    if current_state == "Q2" and len(queue2) == 0:
        current_state = "Q3"

    if current_state == "Q3" and len(queue1) == 0 and len(queue2) == 0 and len(queue3) == 0 and len(process_list) == 0:
        break
    elif current_state == "Q3" and len(queue1) == 0 and len(queue2) == 0 and len(queue3) == 0 and len(process_list) != 0:
        continue
    elif current_state == "Q3" and len(queue3) == 0 and (len(queue1) != 0 or len(queue2) != 0):
        if len(queue1) != 0:
            current_state = "Q1"

        elif len(queue2) != 0:
            current_state = "Q2"

    if current_state == "Q1":
        alg = importlib.import_module(q1_algorithm[:-3])

        alg.sort(queue1)
        if previous_process is None:
            previous_process = queue1[0]
            previous_process.start = current_time

        for i in queue1:
            i.wait += 1
            i.save()
        for i in queue2:
            i.wait += 1
            i.save()
        for i in queue3:
            i.wait += 1
            i.save()

        previous_process.wait -= 1
        previous_process.pass_time += 1
        previous_process.save()

        if previous_process.time == previous_process.pass_time:
            previous_process.passed = True
            previous_process.finish = current_time
            previous_process.save()
            queue1.remove(previous_process)
            previous_process = None
        if alg.pre_emptive == False:
            if previous_process.pass_time == q1_quantom:
                queue2.append(previous_process)
                queue1.remove(previous_process)
                previous_process=None


    elif current_state == "Q2":
        alg = importlib.import_module(q2_algorithm[:-3])

        alg.sort(queue2)
        if previous_process is None:
            previous_process = queue2[0]
            previous_process.start = current_time

        for i in queue1:
            i.wait += 1
            i.save()
        for i in queue2:
            i.wait += 1
            i.save()
        for i in queue3:
            i.wait += 1
            i.save()

        previous_process.wait -= 1
        previous_process.pass_time += 1
        previous_process.save()

        if previous_process.time == previous_process.pass_time:
            previous_process.passed = True
            previous_process.finish = current_time
            previous_process.save()
            queue1.remove(previous_process)
            previous_process = None
        if alg.pre_emptive == False:
            if previous_process.pass_time == q2_quantom:
                queue3.append(previous_process)
                queue2.remove(previous_process)
                previous_process = None



    elif current_state == "Q3":
        alg = importlib.import_module(q3_algorithm[:-3])

        alg.sort(queue3)
        if previous_process is None:
            previous_process = queue3[0]
            previous_process.start = current_time

        for i in queue1:
            i.wait += 1
            i.save()
        for i in queue2:
            i.wait += 1
            i.save()
        for i in queue3:
            i.wait += 1
            i.save()

        previous_process.wait -= 1
        previous_process.pass_time += 1
        previous_process.save()

        if previous_process.time == previous_process.pass_time:
            previous_process.passed = True
            previous_process.finish = current_time
            previous_process.save()
            queue1.remove(previous_process)
            previous_process = None


    current_time += 1











