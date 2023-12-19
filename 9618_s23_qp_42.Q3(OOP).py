class employee:
    def __init__(self, hpay, enum, jtitle):
        self.__hourlypay = hpay  # Private hourlypay : Real
        self.__employeenumber = enum  # Private employeenumber : String
        self.__jobtitle = jtitle  # Private jobtitle : String
        self.__payyear2022 = []  # 52 elements Array
        for j in range(0, 52):
            self.__payyear2022.append(0.00)

    def getemployeenumber(self):
        return self.__employeenumber

    def setpay(self, wnum, hnum):
        self.__payyear2022[wnum - 1] = hnum * self.__hourlypay

    def gettotalpay(self):
        totalpay = 0
        for j in range(0, 52):
            totalpay = totalpay + self.__payyear2022[i]
        return totalpay


class manager(employee):
    def __init__(self, hpay, enum, jtitle, bvalue):
        super().__init__(hpay, enum, jtitle)
        self.__bonusvalue = bvalue  # Private bonusvalue : Single

    def setpay(self, wnum, hnum):
        hnum = hnum * (1 + self.__bonusvalue / 100)
        super().setpay(wnum, hnum)

def enterhours():
    try:
        f = open("HoursWeek1.txt","r")
        employeeID = ""

        for i in range(0, 8):
            employeeID =  f.readline()
            for j in range(0, 8):


employeeArray = []  # 8 Element Array
# Main program
pay = 0.00
ID = ""
bonus = 0.00
title = ""
temp = ""
try:
    f = open("Employees.txt", "r")
    for i in range(0, 8):
        pay = float(f.readline())
        ID = f.readline()
        temp = f.readline()
        try:
            bonus = float(temp)
            title = file.readline()
            employeeArray.append(manager(ID, pay, title, bonus))
        except:
            title = temp
            employeeArray.append(Employee(Id, pay, title))

    f.close()
except IOError:
    print("File not found.")

