# def even_odd(number):
#     if number & 1==0:
#         print("even")
#     else:
#         print("odd")


def even_odd(number):
    binary_number = bin(number)[2:]  # convert to binary and remove the '0b' prefix
    if binary_number[-1] == '0':  # check if the last (least significant) bit is 0
        print("even")
    else:
        print("odd")
        
even_odd(4)
even_odd(9)