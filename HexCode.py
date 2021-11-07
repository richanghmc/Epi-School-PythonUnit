def to_hex(num):
    hexadecimal = ""
    x = [i for i in num]
    #decimaltoHexDigits = {0:"00", 1: "01", 2: "02", 3: "03", 4: "04", 5: "05", 6: "06", 7: "07", 8: "08", 9: "09", 10: "0a", 11: "0b", 12: "0c", 13: "0d", 14: "0e", 15: "0f"}
    # hexadecimal = ""
    # if num%16 == 0:
    #     hexadecimal = "0" + hexadecimal
    #     num//=16
    # while num != 0:
    #     if num%16 == 1:
    #         hexadecimal = "1" + hexadecimal
    #     if num%16 == 2:
    #         hexadecimal = "2" + hexadecimal
    #     if num%16 == 3:
    #         hexadecimal = "3" + hexadecimal
    #     if num%16 == 4:
    #         hexadecimal = "4" + hexadecimal
    #     if num%16 == 5:
    #         hexadecimal = "5" + hexadecimal
    #     if num%16 == 6:
    #         hexadecimal = "6" + hexadecimal
    #     if num%16 == 7:
    #         hexadecimal = "7" + hexadecimal
    #     if num%16 == 8:
    #         hexadecimal = "8" + hexadecimal
    #     if num%16 == 9:
    #         hexadecimal = "9" + hexadecimal
    #     if num%16 == 10:
    #         hexadecimal = "a" + hexadecimal
    #     if num%16 == 11:
    #         hexadecimal = "b" + hexadecimal
    #     if num%16 == 12:
    #         hexadecimal = "c" + hexadecimal
    #     if num%16 == 13:
    #         hexadecimal = "d" + hexadecimal
    #     if num%16 == 14:
    #         hexadecimal = "e" + hexadecimal
    #     if num%16 == 15:
    #         hexadecimal = "f" + hexadecimal
    #     num //= 16
    # return hexadecimal

def hex_color(red, green, blue):
    return "#" + to_hex(red) + to_hex(green) + to_hex(blue)