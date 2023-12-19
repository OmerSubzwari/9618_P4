class Picture:
    # Private Description : String
    # Private Width : Integer
    # Private Height : Integer
    # Private FrameColour : String

    def __init__(self, desc, w, h, fcol):
        self.__description = desc
        self.__width = w
        self.__height = h
        self.__framecolour = fcol

    def getdescription(self):
        return self.__description

    def getwidth(self):
        return self.__width

    def getheight(self):
        return self.__height

    def getcolour(self):
        return self.__framecolour

    def setdescription(self, newdesc):
        self.__description = newdesc


def readdata(pictureArray):
    file = "Pictures.txt"
    count = 0
    try:
        f = open(file, 'r')
        desc = f.readline().strip().lower()
        while desc != "":
            width = int(f.readline().strip())
            height = int(f.readline().strip())
            framecolour = f.readline().strip().lower()
            pictureArray[count] = Picture(desc, width, height, framecolour)

            count += 1
            desc = f.readline().strip().lower()  # Move this line inside the loop

        f.close()
    except IOError:
        print("File not found.")
    return count, pictureArray


pictureArray = []  # 100 element array
for i in range(100):
    pictureArray.append(Picture("", 0, 0, ""))

num, pictureArray = readdata(pictureArray)

fcol = input("Enter your frame's colour: ").lower()
maxwidth = int(input("Enter your frame's max height: "))
maxheight = int(input("Enter your frame's max width: "))
print("Matching picture frames: ")
for i in range(0, num):
    if (
            pictureArray[i].getcolour() == fcol and
            pictureArray[i].getwidth() <= maxwidth and
            pictureArray[i].getheight() <= maxheight
    ):
        print(
            pictureArray[i].getdescription(),
            pictureArray[i].getwidth(),
            pictureArray[i].getheight()
        )
