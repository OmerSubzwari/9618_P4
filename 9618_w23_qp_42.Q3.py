class employee:
    def __init__(self, hpay, enum, jtitle):
        self.__hourlypay = hpay
        self.__employeenumber = enum
        self.__jobtitle = jtitle
        self.__payyear2022 = [0.00] * 52

    def getemployeenumber(self):
        return self.__employeenumber

    def setpay(self, wnum, hnum):
        self.__payyear2022[wnum - 1] = hnum * self.__hourlypay

    def gettotalpay(self):
        totalpay = 0
        for j in range(0, 52):
            totalpay += self.__payyear2022[j]
        return totalpay


class manager(employee):
    def __init__(self, hpay, enum, jtitle, bvalue):
        super().__init__(hpay, enum, jtitle)
        self.__bonusvalue = bvalue

    def setpay(self, wnum, hnum):
        hnum *= (1 + self.__bonusvalue / 100)
        super().setpay(wnum, hnum)


employeeArray = [None] * 8  # Initialize with 8 elements

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
        ID = f.readline().strip()
        temp = f.readline().strip()
        try:
            bonus = float(temp)
            title = f.readline().strip()
            employeeArray[i] = manager(pay, ID, title, bonus)
        except ValueError:
            title = temp
            employeeArray[i] = employee(pay, ID, title)

    f.close()
except IOError:
    print("File not found.")


def enterhours():
    try:
        f = open("HoursWeek1.txt", "r")
        for i in range(0, 8):
            employeeID = f.readline().strip()
            hours_worked = float(f.readline())
            found = False
            for emp in employeeArray:
                if emp is not None and emp.getemployeenumber() == employeeID:
                    found = True
                    emp.setpay(1, hours_worked)
                    break

            if not found:
                print(f"Employee with ID {employeeID} not found.")

        f.close()
    except IOError:
        print("File not found.")



enterhours()
for i in range(0, 8):
    print(employee[y].getemployeenumber(), "", employee[y].gettotalpay())