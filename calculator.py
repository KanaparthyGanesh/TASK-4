def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if(y==0):
        return "ERROR !"
    return x/y
def moddivision(x,y):
    if(y==0):
        return " ERROR !"
    return x%y
def main():
    while True:
        choice=input("Enter choice (1/2/3/4/5/6): ")
        if choice=='6':
            print("Exiting the calculator,GOOdbye!")
            break
        if choice in ('1','2','3','4','5'):
            num1=int(input("Enter the first number : "))
            num2=int(input("Enter the second number : "))
            if choice=='1':
                print(f"The result is:{add(num1,num2)}")
            elif choice=='2':
                print(f"the result is:{subtract(num1,num2)}")
            elif choice=='3':
                print(f"the result is:{multiply(num1,num2)}")
            elif choice=='4':
                print(f"the result is:{divide(num1,num2)}")
            elif choice=='5':
                print(f"the result is:{moddivision(num1,num2)}")
        else:
            print("Invalid input .please entre a valid choice")
if __name__ =="__main__":
    main()
            
            
