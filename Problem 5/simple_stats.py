def simple_stats():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    prod = num1 * num2 * num3 * num4
    aver = (num1 + num2 + num3 +num4) / 4
    print(f'{prod:.0f} {aver:.0f}')
    print(f'{prod:.3f} {aver:.3f}')
if __name__ == "__main__":
    simple_stats()