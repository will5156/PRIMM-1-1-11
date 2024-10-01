"""
PRIMM: 1+1 = 11
Description of program here
William - 10/1/2024
"""

def main():
    #prompts user for numbers
    num1: float = float(input("Enter a number: "))
    num2: float = float(input("Enter another number: "))
    #add numbers together
    total: float = num1+num2
    #output
    print(f"{num1} + {num2} = {total}")
    print(f"{num1} - {num2} = {num1-num2}")
    print(f"{num1} * {num2} = {num1*num2}")
    print(f"{num1} / {num2} = {num1/num2}")
    print(f"{num1} // {num2} = {num1//num2}")
    print(f"{num1} ** {num2} = {num1**num2}")
    print(f"{num1} % {num2} = {num1%num2}")

if __name__ == "__main__":
  main()
