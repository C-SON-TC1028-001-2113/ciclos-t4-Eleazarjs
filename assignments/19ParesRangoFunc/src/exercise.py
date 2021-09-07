
def main():
    num1 = int(input("Valor 1: "))
    num2 = int(input("Valor 2: "))

    if num1>0 and num2>0:
        if num1!=num2:
            if num1>num2:
                for num in range(num2,num1+1):
                    if num%2==0:
                        print(num)
            elif num2>num1:
                for num in range(num1,num2+1):
                    if num%2==0:
                        print(num)
        else:
            print("No hay pares")   

            
                         
if __name__=='__main__':
    main()