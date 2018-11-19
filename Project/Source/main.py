import os
import time as T
import sys
import importlib
import datetime
sys.path.insert(0, r'\Users\reza yousofvand\Desktop\OS_Project\Project\Algorithm')

from processClass import process
# from  ..Algorithm import FCFS



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
finish_list = []

previous_process = None
previous_alg = None

switch_context = 1

finish_pre = -2

start_program = str(datetime.datetime.now())
start_program = start_program.replace(".","")
start_program = start_program.replace(":","-")
log_file = open(r"C:\Users\reza yousofvand\Desktop\OS_Project\Project\Log\\"+start_program+".txt","a")

def log(text):
    T.sleep(0.5)
    print(text)
    log_file.writelines(text+'\r\n')


process_number=int(input("Please enter number of process:\n"))
if process_number<1:
    while process_number<1:
        process_number = int(input("Error!\nPlease enter number of process:\n"))

os.system("cls")

print("Please enter your process (Arrival Time, Duration, Priority,):\n")

i = 1
while i <=process_number:

    entry = input("Enter Arrival Time of "+"process:"+str(i)+"\n")
    if entry == ""or not entry.isnumeric():
        while entry == ""or not entry.isnumeric():
            entry = input("Error!\nEnter Arrival Time of " +"process:"+str(i)+"\n")

    time = input("Enter Duration of "+"process:"+str(i)+"\n")
    if time == "" or not time.isnumeric() :
        while time == "" or not time.isnumeric():
            time = input("Error!\nEnter Duration of "+"process:"+str(i)+"\n")

    priority = input("Enter Priority of "+"process:"+str(i)+"\n")
    if priority == "" or not priority.isnumeric():
        while priority == "" or not priority.isnumeric():
            priority = input("Error!\nEnter Priority of " +"process:"+str(i)+"\n")

    process_list.append(process(i, int(entry), int(time), int(priority)))
    i += 1

os.system("cls")

algorithm_list = os.listdir(r"..\Algorithm")
algorithm_list.remove("Template.py")
algorithm_list.remove("__pycache__")
new_algorithm_list=[]
for i in algorithm_list:
    new_algorithm_list.append(i[:-3])
print(str(new_algorithm_list))
q1_algorithm = input("Please choose 1st Queue algorithm \n")
while not (q1_algorithm + ".py" in algorithm_list):
    q1_algorithm = input("Error!\nPlease choose 1st Queue algorithm \n")
if q1_algorithm == "RR":
    q2_algorithm = input("Please choose 2nd Queue algorithm \n")
    while not (q2_algorithm + ".py" in algorithm_list):
        q2_algorithm = input("Error!\nPlease choose 2nd Queue algorithm \n")

    if q2_algorithm =="RR":
        q3_algorithm = input("Please choose 3ed Queue algorithm \n")
        while not (q3_algorithm + ".py" in algorithm_list):
            q3_algorithm = input("Error!\nPlease choose 3ed Queue algorithm \n")

os.system("cls")
for i in process_list:
    log("Process"+str(str(i.name))+" arrival Time: "+str(i.entry)+"  duration: "+str(i.time)+" priority: "+str(i.priority))
    log("-------------------------------------------------------------------------------------------------------------------------")

if q1_algorithm:
    log("1st Queue algorithm" + str(q1_algorithm))

if q2_algorithm:
    log("2nd Queue algorithm" + str(q2_algorithm))

if q3_algorithm:
    log("3ed Queue algorithm" + str(q3_algorithm))


def process(previous_process):
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

while True:

    log("current time:"+str(current_time))
    for i in process_list:
        if i.entry <= current_time:
            queue1.append(i)
            log("Process"+str(i.name)+" entered to queue1 at "+str(current_time))
            process_list.remove(i)
    if len(queue1) != 0:
        if current_state !="Q1":
            if previous_process is None:

                text="Processor change its Queue from "
                if current_state == "Q2":
                    text=text +"queue2"
                elif current_state == "Q3":
                    text = text +"queue3"
                text = text +" to queue1 at " + str(current_time)
                log(text)
                current_state = "Q1"

            elif not previous_alg:
                if switch_context > 0:
                    for i in queue1:
                        i.wait += switch_context
                        i.save()
                    for i in queue2:
                        i.wait += switch_context
                        i.save()
                    for i in queue3:
                        i.wait += switch_context
                        i.save()

                    for i in process_list:
                        j = 1
                        while j <= switch_context:

                            if i.entry == current_time + j:
                                queue1.append(i)
                                log("current time:" + str(current_time +j))
                                log("Process" + str(str(i.name)) + " entered to queue1 at " + str(current_time + j ))
                                process_list.remove(i)
                            j += 1
                current_time = current_time +switch_context
                text = "Processor change its Queue from "
                if current_state == "Q2":
                    text = text + "queue2"
                elif current_state == "Q3":
                    text = text + "queue3"
                text = text + " to queue1 at " + str(current_time)
                log(text)
                current_state = "Q1"
                previous_process = None
                continue
        else:
            pass
    elif len(queue2) != 0:
        if current_state !="Q2":
            if previous_process is None:

                text="Processor change its Queue from "
                if current_state == "Q1":
                    text=text +"queue1"
                elif current_state == "Q3":
                    text = text +"queue3"
                text = text +" to queue2 at " + str(current_time)
                log(text)
                current_state = "Q2"

            elif not previous_alg:
                if switch_context > 0:
                    for i in queue1:
                        i.wait += switch_context
                        i.save()
                    for i in queue2:
                        i.wait += switch_context
                        i.save()
                    for i in queue3:
                        i.wait += switch_context
                        i.save()

                    for i in process_list:
                        j = 1
                        while j <= switch_context:

                            if i.entry == current_time + j:
                                flage = True
                                queue1.append(i)
                                log("current time:" + str(current_time +j))
                                log("Process" + str(str(i.name)) + " entered to queue1 at " + str(current_time + j))
                                process_list.remove(i)
                            j += 1
                current_time = current_time +switch_context
                text = "Processor change its Queue from "
                if current_state == "Q1":
                    text = text + "queue1"
                elif current_state == "Q3":
                    text = text + "queue3"
                text = text + " to queue2 at " + str(current_time)
                log(text)
                current_state = "Q2"
                previous_process = None
                continue
        else:
            pass
    elif len(queue3) !=0:
        if current_state !="Q3":
            if previous_process is None:

                text="Processor change its Queue from "
                if current_state == "Q1":
                    text=text +"queue1"
                elif current_state == "Q2":
                    text = text +"queue2"
                text = text +" to queue3 at " + str(current_time)
                log(text)
                current_state = "Q3"

            elif not previous_alg:
                if switch_context > 0:
                    for i in queue1:
                        i.wait += switch_context
                        i.save()
                    for i in queue2:
                        i.wait += switch_context
                        i.save()
                    for i in queue3:
                        i.wait += switch_context
                        i.save()

                    for i in process_list:
                        j = 1
                        while j <= switch_context:

                            if i.entry == current_time + j:
                                flage = True
                                queue1.append(i)
                                log("current time:" + str(current_time +j))
                                log("Process" + str(str(i.name)) + " entered to queue1 at " + str(current_time + j))
                                process_list.remove(i)
                            j += 1
                current_time = current_time +switch_context
                text = "Processor change its Queue from "
                if current_state == "Q1":
                    text = text + "queue1"
                elif current_state == "Q2":
                    text = text + "queue2"
                text = text + " to queue3 at " + str(current_time)
                log(text)
                current_state = "Q3"
                previous_process = None
                continue
        else:
            pass
    elif len(process_list) !=0:
        current_time +=1
        continue
    else:
        break

###----------------------------------------------#### First Queue ####--------------------------------------###
###----------------------------------------------#### ########### ####--------------------------------------###
###----------------------------------------------#### ########### ####--------------------------------------###
###----------------------------------------------#### ########### ####--------------------------------------###



    if current_state == "Q1":
        alg = importlib.import_module(q1_algorithm)
        queue1 = alg.sort(queue1)
        text = ""
        for i in queue1:
            text = text + str(str(i.name)) + ","
        log("queue1 on " + str(current_time) + " is :" + text[:-1])
        previous_alg =alg.pre_emptive()
        if 1==(current_time - finish_pre):
            if switch_context > 0:
                for i in queue1:
                    i.wait += switch_context
                    i.save()
                for i in queue2:
                    i.wait += switch_context
                    i.save()
                for i in queue3:
                    i.wait += switch_context
                    i.save()

                for i in process_list:
                    j = 1
                    while j <= switch_context:

                        if i.entry == current_time + j:
                            flage = True
                            queue1.append(i)
                            log("current time:" + str(current_time + j))
                            log("Process" + str(str(i.name)) + " entered to queue1 at " + str(current_time + j))
                            process_list.remove(i)
                        j += 1
            current_time = current_time + switch_context
            for i in queue1:
                if i.name == previous_process:
                    i = previous_process
                    i.save()
            previous_process = queue1[0]
            continue

        if previous_alg == False:
            if previous_process is None:
                previous_process = queue1[0]
                log("Process" + str(previous_process.name) + " get Processor at " + str(current_time))
                if previous_process.start == 0:
                    previous_process.start = current_time
                    previous_process.save()

            else:
                if previous_process == queue1[0]:
                    pass
                else:
                    if switch_context > 0:
                        for i in queue1:
                            i.wait += switch_context
                            i.save()
                        for i in queue2:
                            i.wait += switch_context
                            i.save()
                        for i in queue3:
                            i.wait += switch_context
                            i.save()

                        for i in process_list:
                            j = 1
                            while j <= switch_context:

                                if i.entry == current_time + j:
                                    flage = True
                                    queue1.append(i)
                                    log("current time:" + str(current_time + j))
                                    log("Process" + str(str(i.name)) + " entered to queue1 at " + str(current_time + j))
                                    process_list.remove(i)
                                j += 1
                    current_time = current_time + switch_context
                    for i in queue1:
                        if i.name == previous_process:
                            i = previous_process
                            i.save()
                    previous_process = queue1[0]
                    continue


            process(previous_process)
            current_time += 1
            if previous_process.time == previous_process.pass_time:
                log("Process" + str(previous_process.name) + " finished at " + str(current_time))
                previous_process.passed = True
                previous_process.finish = current_time
                finish_pre =current_time
                previous_process.save()
                for i in queue1:
                    if i.name == previous_process:
                        i = previous_process
                        i.save()
                finish_list.append(previous_process)
                queue1.remove(previous_process)
                previous_process = None
            elif q1_algorithm == "RR":
                if previous_process.pass_time >= q1_quantom:
                    log("Process" + str(previous_process.name) + " move from queue1 to queue2 at " + str(current_time))
                    queue2.append(previous_process)
                    queue1.remove(previous_process)
                    previous_process = None

        else:
            if previous_process is None:
                previous_process = queue1[0]
                log("Process" + str(previous_process.name) + " get Processor at " + str(current_time))
                if previous_process.start == 0:
                    previous_process.start = current_time
                    previous_process.save()
            process(previous_process)
            current_time += 1

            if previous_process.time == previous_process.pass_time:
                log("Process" + str(previous_process.name) + " finished at " + str(current_time))
                previous_process.passed = True
                previous_process.finish = current_time
                finish_pre =current_time
                previous_process.save()
                for i in queue1 :
                    if i.name==previous_process.name:
                        i=previous_process
                        i.save()
                finish_list.append(previous_process)
                queue1.remove(previous_process)
                previous_process = None







###----------------------------------------------#### Second Queue ####--------------------------------------###
###----------------------------------------------#### ############ ####--------------------------------------###
###----------------------------------------------#### ############ ####--------------------------------------###
###----------------------------------------------#### ############ ####--------------------------------------###


    elif current_state == "Q2":
        alg = importlib.import_module(q2_algorithm)
        queue2 = alg.sort(queue2)
        text = ""
        for i in queue2:
            text = text + str(str(i.name)) + ","
        log("queue2 on " + str(current_time) + " is :" + text[:-1])
        previous_alg =alg.pre_emptive()

        if 1==(current_time - finish_pre):
            if switch_context > 0:
                for i in queue1:
                    i.wait += switch_context
                    i.save()
                for i in queue2:
                    i.wait += switch_context
                    i.save()
                for i in queue3:
                    i.wait += switch_context
                    i.save()

                for i in process_list:
                    j = 1
                    while j <= switch_context:

                        if i.entry == current_time + j:
                            flage = True
                            queue1.append(i)
                            log("current time:" + str(current_time + j))
                            log("Process" + str(str(i.name)) + " entered to queue1 at " + str(current_time + j))
                            process_list.remove(i)
                        j += 1
            current_time = current_time + switch_context
            for i in queue2:
                if i.name == previous_process:
                    i = previous_process
                    i.save()
            previous_process = queue2[0]
            continue

        if previous_alg == False:
            if previous_process is None:
                previous_process = queue2[0]
                log("Process" + str(previous_process.name) + " get Processor at " + str(current_time))
                if previous_process.start == 0:
                    previous_process.start = current_time
                    previous_process.save()

            else:
                if previous_process == queue2[0]:
                    pass
                else:
                    if switch_context > 0:
                        for i in queue1:
                            i.wait += switch_context
                            i.save()
                        for i in queue2:
                            i.wait += switch_context
                            i.save()
                        for i in queue3:
                            i.wait += switch_context
                            i.save()

                        for i in process_list:
                            j = 1
                            while j <= switch_context:

                                if i.entry == current_time + j:
                                    flage = True
                                    queue1.append(i)
                                    log("current time:" + str(current_time + j))
                                    log("Process" + str(str(i.name)) + " entered to queue1 at " + str(current_time + j))
                                    process_list.remove(i)
                                j += 1
                    current_time = current_time + switch_context
                    for i in queue2:
                        if i.name == previous_process:
                            i = previous_process
                            i.save()
                    previous_process = queue2[0]
                    continue


            process(previous_process)
            current_time += 1

            if previous_process.time == previous_process.pass_time:
                log("Process" + str(previous_process.name) + " finished at " + str(current_time))
                previous_process.passed = True
                previous_process.finish = current_time
                finish_pre =current_time
                previous_process.save()
                for i in queue2:
                    if i.name == previous_process:
                        i = previous_process
                        i.save()
                finish_list.append(previous_process)
                queue2.remove(previous_process)
                previous_process = None
            elif q2_algorithm == "RR":
                if previous_process.pass_time >= q2_quantom:
                    log("Process" + str(previous_process.name) + " move from queue2 to queue3 at " + str(current_time))
                    queue3.append(previous_process)
                    queue2.remove(previous_process)
                    previous_process = None

        else:
            if previous_process is None:
                previous_process = queue2[0]
                log("Process" + str(previous_process.name) + " get Processor at " + str(current_time))
                if previous_process.start == 0:
                    previous_process.start = current_time
                    previous_process.save()
            process(previous_process)
            current_time += 1

            if previous_process.time == previous_process.pass_time:
                log("Process" + str(previous_process.name) + " finished at " + str(current_time))
                previous_process.passed = True
                previous_process.finish = current_time
                finish_pre =current_time
                previous_process.save()
                for i in queue2 :
                    if i.name==previous_process.name:
                        i=previous_process
                        i.save()
                finish_list.append(previous_process)
                queue2.remove(previous_process)
                previous_process = None



###----------------------------------------------#### Thired Queue ####--------------------------------------###
###----------------------------------------------#### ############ ####--------------------------------------###
###----------------------------------------------#### ############ ####--------------------------------------###
###----------------------------------------------#### ############ ####--------------------------------------###




    elif current_state == "Q3":
        alg = importlib.import_module(q3_algorithm)
        queue3 = alg.sort(queue3)
        text = ""
        for i in queue3:
            text = text + str(str(i.name)) + ","
        log("queue3 on " + str(current_time) + " is :" + text[:-1])
        previous_alg =alg.pre_emptive()


        if 1==(current_time - finish_pre):
            if switch_context > 0:
                for i in queue1:
                    i.wait += switch_context
                    i.save()
                for i in queue2:
                    i.wait += switch_context
                    i.save()
                for i in queue3:
                    i.wait += switch_context
                    i.save()

                for i in process_list:
                    j = 1
                    while j <= switch_context:

                        if i.entry == current_time + j:
                            flage = True
                            queue1.append(i)
                            log("current time:" + str(current_time + j))
                            log("Process" + str(str(i.name)) + " entered to queue3 at " + str(current_time + j))
                            process_list.remove(i)
                        j += 1
            current_time = current_time + switch_context
            for i in queue3:
                if i.name == previous_process:
                    i = previous_process
                    i.save()
            previous_process = queue3[0]
            continue

        if previous_alg == False:
            if previous_process is None:
                previous_process = queue3[0]
                log("Process" + str(previous_process.name) + " get Processor at " + str(current_time))
                if previous_process.start == 0:
                    previous_process.start = current_time
                    previous_process.save()

            else:
                if previous_process == queue3[0]:
                    pass
                else:
                    if switch_context > 0:
                        for i in queue1:
                            i.wait += switch_context
                            i.save()
                        for i in queue2:
                            i.wait += switch_context
                            i.save()
                        for i in queue3:
                            i.wait += switch_context
                            i.save()

                        for i in process_list:
                            j = 1
                            while j <= switch_context:

                                if i.entry == current_time + j:
                                    flage = True
                                    queue1.append(i)
                                    log("current time:" + str(current_time + j))
                                    log("Process" + str(str(i.name)) + " entered to queue3 at " + str(current_time + j))
                                    process_list.remove(i)
                                j += 1
                    current_time = current_time + switch_context
                    for i in queue3:
                        if i.name == previous_process:
                            i = previous_process
                            i.save()
                    previous_process = queue3[0]
                    continue


            process(previous_process)
            current_time += 1

            if previous_process.time == previous_process.pass_time:
                log("Process" + str(previous_process.name) + " finished at " + str(current_time))
                previous_process.passed = True
                previous_process.finish = current_time
                finish_pre =current_time
                previous_process.save()
                for i in queue3:
                    if i.name == previous_process:
                        i = previous_process
                        i.save()
                finish_list.append(previous_process)
                queue3.remove(previous_process)
                previous_process = None


        else:
            if previous_process is None:
                previous_process = queue3[0]
                log("Process" + str(previous_process.name) + " get Processor at " + str(current_time))
                if previous_process.start == 0:
                    previous_process.start = current_time
                    previous_process.save()
            process(previous_process)
            current_time += 1

            if previous_process.time == previous_process.pass_time:
                log("Process" + str(previous_process.name) + " finished at " + str(current_time))
                previous_process.passed = True
                previous_process.finish = current_time
                finish_pre =current_time
                previous_process.save()
                for i in queue3 :
                    if i.name==previous_process.name:
                        i=previous_process
                        i.save()
                finish_list.append(previous_process)
                queue3.remove(previous_process)
                previous_process = None


finish_list = sorted(finish_list, key=lambda k: k.name)

for i in finish_list:
    log("-------------------------------------------------------------------------------------------------------------------------")
    log("Process"+str(str(i.name))+" arrival Time: "+str(i.entry)+"  duration: "+str(i.time)+" wait time: "+str(i.wait)+
        " complete: "+str(i.finish - i.entry )+" start: "+str(i.start)+" finish: "+str(i.finish))
log_file.close()


