def to_hex(num):
    decimaltoHexDigits = {0:"0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
    hexadecimal = ""
    if num == 0:
        hexadecimal += "0"
    while num > 0:
        remainder = num%16
        hexadecimal = decimaltoHexDigits[remainder] + hexadecimal
        num = num // 16
    return hexadecimal

def to_hexWith0(num):
    decimaltoHexDigits = {0:"00", 1: "01", 2: "02", 3: "03", 4: "04", 5: "05", 6: "06", 7: "07", 8: "08", 9: "09", 10: "0a", 11: "0b", 12: "0c", 13: "0d", 14: "0e", 15: "0f"}
    hexadecimal = ""
    if num == 0:
        hexadecimal += "0"
    elif num <= 15:
        hexadecimal += decimaltoHexDigits[num]
    else:
        hexadecimal = to_hex(num)
    return hexadecimal

def hex_color(red, green, blue):
    return "#" + to_hexWith0(red) + to_hexWith0(green) + to_hexWith0(blue)