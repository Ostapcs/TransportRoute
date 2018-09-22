"""Created by Ostap Kutyanskyy 22.09.18"""
arr = []


class TransportRoute:
    def __init__(self, beg, end, quan, length):
        self.beg = beg
        self.end = end
        self.quan = quan
        self.length = length

    def __str__(self):
        return "Beginnig : " + self.beg + " | " + "End : " + self.end + " | " + "Quantaty : " + str(
            self.quan) + " | " + "Lenght : " + str(self.length)
        # print(str)

    #
    # @property
    # def beg(self):
    #     return self.beg
    #
    # @property
    # def end(self):
    #     return self.end
    #
    # @property
    # def quan(self):
    #     return self.quan
    #
    # @property
    # def length(self):
    #     return self.length

    def getAvarageLengthBetweenStops(self):
        return int(self.length / self.quan)


def Input():
    beg = input("Enter beginning : ")
    end = input("Enter end : ")
    quan = int(input("Enter quantaty : "))
    length = int(input("Enter length : "))
    x = TransportRoute(beg, end, quan, length)
    arr.append(x)


def Sort():
    arr.sort(key=lambda rout: rout.length)

def avarageLengthBetweenStops(val):
    """    Prints routs if their avarage length between stops is less than parametr :"""
    print(avarageLengthBetweenStops.__doc__)
    for i in arr:
        if i.getAvarageLengthBetweenStops() < val:
            x = i.getAvarageLengthBetweenStops()
            x = str(x)
            print(i, end=" | Avarage length between stops = " + x + "\n")

def beginWithStop(stop):
    """
    Prints routs if their begin station is equal to parametr :"""
    beginStops = []
    for i in arr:
        if i.beg == stop:
            beginStops.append(i)

    print(beginWithStop.__doc__)
    for i in beginStops:
        print(i)

def maxQuantityStops():
    """
    Print rout with max quantity of stops"""
    print(maxQuantityStops.__doc__)
    maxStops = max(arr, key=lambda stops: stops.quan)
    for i in arr:
        if maxStops.quan == i.quan:
            print(i)

x = TransportRoute("Lviv", "Kyiv", 10, 551)  # 55,1
arr.append(x)
x = TransportRoute("Lviv", "Ternopil", 3, 130)  # 43,3
arr.append(x)
x = TransportRoute("Lviv", "Slavsko", 8, 120)  # 15
arr.append(x)
x = TransportRoute("Lviv", "Odesaa", 17, 1000)  # 58,8
arr.append(x)
x = TransportRoute("Kyiv", "Odesaa", 20, 600)  # 20
arr.append(x)
x = TransportRoute("Kyiv", "Kharkiv", 13, 450)  # 34,6
arr.append(x)
x = TransportRoute("Ternopil", "Lutsk", 8, 250)  # 31,25
arr.append(x)
x = TransportRoute("Ternopil", "Kharkiv", 20, 750)  # 20
arr.append(x)
x = TransportRoute("Kyiv", "Dnipro", 12, 350)  # 29
arr.append(x)

Sort()
for i in arr:
    print(i)
avarageLengthBetweenStops(30)
beginWithStop("Lviv")
maxQuantityStops()
# for i in arr:
#     print(i)
