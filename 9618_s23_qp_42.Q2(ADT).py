circularqueue = [] #SaleData, 5 items
global numberofitems #int
global head #int
global tail #int

class Saledata:
    def __init__(self, id, quantity):
        self.saleID = id
        self.salequantity = quantity


def enqueue(newrecord):
    global numberofitems  # int
    global head  # int
    global tail  # int
    if numberofitems == 5:
        return -1
    else:
        circularqueue[tail] = newrecord
        if tail == 4:
            tail = 0
        else:
            tail += 1
        numberofitems += 1
        return 1

def dequeue():
    global numberofitems  # int
    global head  # int
    global tail  # int
    removed = Saledata("", -1)
    if not numberofitems == 0:
        removed = circularqueue[head]
        numberofitems -= 1
        if head == 4:
            head = 0
        else:
            head += 1
    return removed

def enterrecord():
    global numberofitems  # int
    global head  # int
    global tail  # int
    id = input("Enter ID: ")
    quantity = int(input("Enter quantity: "))
    record = Saledata(id, quantity)
    if enqueue(record) == -1:
        print("Full")
    else:
        print("Stored")

#main
numberofitems = 0
head = 0
tail = 0
for x in range(0, 5):
    circularqueue.append((Saledata("",-1)))

enterrecord()
enterrecord()
enterrecord()
enterrecord()
enterrecord()
enterrecord()
recordremoved = dequeue()
if recordremoved.saleID == "":
    print("No items")
else:
    print(recordremoved.saleID, " ", recordremoved.salequantity)
enterrecord()

for i in range(0, 5):
    print(circularqueue[i].saleID, " ", circularqueue[i].salequantity)
