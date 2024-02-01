def telephone():
    phone_number = int(input())
    Start = phone_number // 10000000
    cut = phone_number % 10000000
    mid = cut // 10000
    end = cut % 10000
    print( '(',Start,')', mid,'-',end)
if __name__ == "__main__":
    telephone()