import os;

from multiprocessing import Process, current_process

# num1 = float(input("Enter First Integer:"))
# num2 = float(input("Enter Second Integer:"))

try:
    num1 = float(input("Enter First Integer:"))
    num2 = float(input("Enter Second Integer:"))
  

except:
    ValueError
    print("Not a valid choice! Try again")
    num1 = float(input("Enter First Integer:"))
    num2 = float(input("Enter Second Integer:")) 
    
   
   
print("select operation")
print("P.Add")
print("m.substract")
print("t.Multiply")
print("d.Divide")
choise = input("Enter operation(p,m,t,d)") 
    
    


def operation():

   
    while True:

     
        if choise in ("p","m","t","d"):
        

            if choise == "p" :
                print(num1, "+", num2, "=",  (num1+num2) )

            elif choise == "m" :
                print(num1, "-", num2, "=",  (num1-num2) )

            elif choise == "t" :
                print(num1, "*", num2, "=",  (num1*num2) )

            elif choise == "d" :
                print(num1, "/", num2, "=",  (num1/num2) )

            
            process_id_child= os.getpid()
            print("child process id " + str(process_id_child))

            # process_name = current_process().kill
            process_name = current_process().name
            print(process_name)

            break

        else:

            print("invalid input")
  
            break

    
if __name__ == "__main__":
    proc = Process(target=operation)
    proc.start()
    proc.join()
    process_id_parent= os.getpid()
    print("Parent id " +str(process_id_parent))





