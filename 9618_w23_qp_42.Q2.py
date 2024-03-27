circularqueue = []  # Saledata, 5 items
head = 0
tail = 0
numberofitems = 0


def enqueue(newrec):
    global numberofitems
    global head
    global tail
    if numberofitems == 5:
        return -1
    else:
        circularqueue[tail] = newrec
        if tail == 4:
            tail = 0
        else:
            tail += 1
        numberofitems += 1
        return 1


def dequeue():
    global numberofitems
    global head
    global tail
    pop = saledata("", -1)
    if numberofitems != 0:
        pop = circularqueue[head]
        numberofitems -= 1
        if head == 4:
            head = 0
        else:
            head += 1
    return pop


def enterecord():
    id = str(input("Enter item id: "))
    quant = int(input("Enter number of items: "))
    record = saledata(id, quant)
    if enqueue(record) == -1:
        print("Full")
    else:
        print("Stored")


class saledata:
    def __init__(self, id, quantity):
        self.saleid = id
        self.quantity = quantity


for i in range(0, 5):
    circularqueue.append((saledata("", -1)))

enterecord()
enterecord()
enterecord()
enterecord()
enterecord()
enterecord()
outch = dequeue()
if outch.saleid == "":
    print("No items on this ID")
else:
    print(f"id: {outch.saleid}, quantity: {outch.quantity}")
enterecord()
for i in range(0, 5):
    print(f"{circularqueue[i].saleid}, {circularqueue[i].quantity}")
