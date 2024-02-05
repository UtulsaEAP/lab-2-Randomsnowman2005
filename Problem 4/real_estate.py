
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    print(f'This house is ${current_price:.0f}. The change is ${current_price-last_month_price:.0f} since last month.')
    print(f'The estimated monthly mortgage is ${(current_price * 0.051) / 12:.2f}.')
if __name__ == "__main__":
    real_estate()