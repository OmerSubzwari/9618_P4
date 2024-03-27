queue = [None for i in range(50)]  # Fixed size queue of 50 elements
tailpointer = 0  # Type integer
headpointer = 0  # Type integer
records = []  # Array to hold records of type RecordData
numberrecords = 0


def enqueue(item):
    global tailpointer, queue
    if tailpointer < len(queue):
        queue[tailpointer] = item
        tailpointer += 1
    else:
        print("Queue is full, cannot enqueue value.")


def dequeue():
    global headpointer, tailpointer, queue
    if headpointer != tailpointer:
        item = queue[headpointer]
        headpointer += 1
        return item
    else:
        print("The queue is empty.")
        return None


def readdata():
    try:
        with open("QueueData.txt", 'r') as data:
            for line in data:
                enqueue(line.strip())
    except FileNotFoundError:
        print("File not found")


class RecordData:
    def __init__(self, id, total):
        self.ID = id
        self.Total = total

    def setID(self, val):
        self.ID = val

    def getID(self):
        return self.ID

    def setTotal(self, val):
        self.Total = val

    def getTotal(self):
        return self.Total


def totaldata():
    global numberrecords, records
    dataaccessed = dequeue()
    if dataaccessed is None:
        return
    found = False
    for record in records:
        if record.getID() == dataaccessed:
            record.setTotal(record.getTotal() + 1)
            found = True
            break

    if not found:
        records.append(RecordData(dataaccessed, 1))
        numberrecords += 1


def outputrecords():
    for i in range(numberrecords):
        print(f"ID {records[i].getID()} Total {records[i].getTotal()}")


# Main
readdata()

while headpointer != tailpointer:
    totaldata()

outputrecords()
