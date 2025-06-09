import random 
n=random.randint(50,100)
a=49
guess=1
while(a!=n):
  
    a=int(input("Guess the number : "))
    if(a>n):
        print("Lower Number Please")
        guess+=1
    elif(a<n):
        print("Higher number please : ")
        guess+=1
  
print(f"You have guessed the number {n} correctly in {guess} attempts")
