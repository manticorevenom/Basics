# CS6704 Basic Workshop Coding.md
# Partners: Huayu Liang, Hunter Leary
#
# Method-level comments from Hunter Leary
# Works from Hunter Leary: roman_to_int: converts a string to integer value
# IDE / Text editor Hunter Leary used: VIM

# Method-level comments from Huayu Liang
# Works from Huayu Liang: romanToInt(): converts a integer to string value & romanToInt(): converts a string to intger value
# IDE / Text editor Huayu Liang used: Visual Studio Code

import os


def roman_to_int(roman:str) -> int:
    """Converts roman numeral to integer value"""
    convert = roman
    total = 0
    
    for vals in convert:
        if vals.__contains__("I"):
            total += 1
        elif vals.__contains__("V"):
            total += 5
        elif vals.__contains__("X"):
            total += 10
        elif vals.__contains__("L"):
            total += 50
        elif vals.__contains__("C"):
            total += 100
        elif vals.__contains__("D"):
            total += 500
        elif vals.__contains__("M"):
            total += 1000
        else:
            print("Error")
            
    return total

def romanToInt(s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number

def main():
    """Demonstrates functionality"""
    print("Numeral value is LVI")
    num_value = "LVI"
    integer = roman_to_int(num_value)
    print(f"Integer value is {integer}")

    print("Roman value is IV")
    rom_value = "IV"
    result = romanToInt(rom_value)
    print(f"Integer value is {result}")

    print("Roman value is LVI")
    rom_value_2 = "LVI"
    result_2 = romanToInt(rom_value_2)
    print(f"Integer value is {result_2}")
    

main()
