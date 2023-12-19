jobs = []  # global integer, 100 by 2 elements
numberofjobs = 0 # global integer


def initialise():
    global jobs
    global numberofjobs
    for i in range(0, 100):
        jobs.append([-1, -1])
    numberofjobs = 0


def addjob(jobnumber, priority):
    global jobs
    global numberofjobs
    if numberofjobs == 100:
        print("Not added.")
    else:
        jobs[numberofjobs] = [jobnumber, priority]
        print("Added.")
        numberofjobs += 1


def insertionsort():
    global jobs
    global numberofjobs
    for I in range(1, numberofjobs):  # Start from the second element
        current1 = jobs[I][0]
        current2 = jobs[I][1]
        J = I - 1
        while J >= 0 and jobs[J][1] > current2:
            jobs[J + 1][0] = jobs[J][0]
            jobs[J + 1][1] = jobs[J][1]
            J -= 1
        jobs[J + 1][0] = current1
        jobs[J + 1][1] = current2


def printarray():
    global jobs
    global numberofjobs
    for X in range(0, numberofjobs):
        print(str(jobs[X][0]), " priority ", str(jobs[X][1]))


initialise()
addjob(12, 10)
addjob(526, 9)
addjob(33, 8)
addjob(12, 9)
addjob(78, 1)

insertionsort()
printarray()
