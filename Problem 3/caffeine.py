
import math
def caffeine():
    caffeine_mg = float(input())
    print (f'After 6 hours: {caffeine_mg / math.pow(2,1):.2f} mg')
    print (f'After 12 hours: {caffeine_mg / math.pow(2,2):.2f} mg')
    print (f'After 24 hours: {caffeine_mg / math.pow(2,4):.2f} mg')
    
if __name__ == "__main__":
    caffeine()