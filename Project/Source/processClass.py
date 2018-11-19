# -*- coding: UTF-8 -*-

import json


class process:

    def __init__(self, name, entry=0, time=0, priority=0, pass_time=0, passed=0, start=0, finish=0, wait=0, remaining=0) :
        self.name = name
        self.entry = entry
        self.time = time
        self.priority = priority
        self.pass_time = pass_time
        self.passed = passed
        self.start = start
        self.finish = finish
        self.wait = wait
        self.remaining = remaining
        file = open(r"..\Process\\"+str(self.name)+".txt", "w")
        dict = {"name":self.name, "time":self.time, "entry":self.entry, "priority":self.priority, "pass_time":self.pass_time,
                "passed":self.passed, "start":self.start, "finish":self.finish, "wait":self.wait}
        jsonfile = json.dumps(dict)
        file.write(jsonfile)
        file.close()

    def save(self):
        file = open(r"..\Process\\" + str(self.name) + ".txt", "w")
        dict = {"name": self.name, "time": self.time, "entry": self.entry, "priority": self.priority, "pass_time": self.pass_time,
                "passed": self.passed, "start": self.start, "finish": self.finish, "wait": self.wait}
        jsonfile = json.dumps(dict)
        file.write(jsonfile)
        file.close()

    def __str__(self):
        return self.name