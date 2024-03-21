from typing import Union

flag : bool = True

def greet(name : str) -> None:
    """Say hello to everyone"""
    print("Hi " + name)

greet("Manchester")
greet("Steven")

def myAbs(x : float) -> float:
    """Take the absolute of the floating-point input"""
    if x < 0:
        return (-x)
    else:
        return (x)
    

myAbs(12)

def greetAll(names : list[str]) -> None:
    for name in names: 
        greet(name)

greetAll(["Alice", "John", "Joe"])

#greetAll([12, 12])

some_data : tuple[int, bool, str] = (41, True, "Manchester")
#some_other_data : tuple[int, bool, str] = (41, 232132, "Manchester")

def myDiv(x : float, y : float) -> Union[float, None]:
    if y != 0: return x/y
    else: return None


myDict : dict[str, Union[float, str]] = {"temp": 273.0, "units": "Kelvin"}

#reveal_type(len)

