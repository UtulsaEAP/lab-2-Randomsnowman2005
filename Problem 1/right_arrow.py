def right_arrow():
    base_char = input()
    head_char = input()

    row1 = '      ' + head_char
    Base = base_char + base_char +base_char+base_char+base_char
    row2 = Base+ head_char + head_char
    row3 = Base + head_char+head_char+head_char
    row4 = Base + head_char

    print(row1)
    print(row2)
    print(row3)
    print(row2)
    print(row4)

if __name__ == "__main__":
    right_arrow()