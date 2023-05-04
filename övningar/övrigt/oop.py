from dataclasses import dataclass
@dataclass
class Rectangle:
    Width: int = 0
    height: int = 0

def calculateArea(rect)
    area = rect.Width * rect.Height
    return area

r = Rectangle()
r.Width = 20
r.height = 10
print(calculateArea(r))


@dataclass
class Person:
    name: str = ""
    StreetAdress: str = ""
    Postalcode: int = 0
    City: str = ""
@dataclass
class HouseBluePrint:
    color: str = ""
    NrOfWindows: int = 0
    address: str = ""

mittHus = HouseBluePrint("brown",12,"testgatan 12")
#mittHus.color = "Brown"
#mittHus.NrOfWindows = 12
#mittHus.adress = "testgatan 12"

syrransHus = HouseBluePrint()
syrransHus.color = "Brown"
syrransHus.NrOfWindows = 15
syrransHus.address = "test"
