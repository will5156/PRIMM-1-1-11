"""
PRIMM: 1+1 = 11
Description of program here
William - 10/1/2024
"""

def main():
    #prompts user for numbers
    num1: int = int(input("Enter a number: "))
    num2: int = int(input("Enter another number: "))
    #add numbers together
    total: int = num1+num2
    #output
    print(f"{num1} + {num2} = {total}")

if __name__ == "__main__":
  main()
