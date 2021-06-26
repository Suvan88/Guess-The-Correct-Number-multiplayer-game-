import random
a=int(input("enter first number"))
b=int(input("enter second number"))

c = random.randint(a, b)
c1 = random.randint(a, b)
t1=0
t2=0
print("player1 plays")
while(True):

    p1=int(input("enter a number"))

    if p1==c:
        print("player1 is correct")
        print(f"total number of tries are{t1}")
        break
    elif p1>c:
        print("your guess is greater than the answer")
        t1=t1+1
        continue
    elif p1 < c:
        print("your guess is smaller than the answer")
        t1=t1+1
        continue

print("player2 plays\n")

while (True):



    p2 = int(input("enter a number"))

    if p2 == c1:
        print("player2 is correct")
        print(f"total number of tries are{t2}")
        break
    elif p2 > c1:
        print("your guess is greater than the answer")
        t2 = t2 + 1
        continue
    elif p2 < c1:
        print("your guess is smaller than the answer")
        t2 = t2 + 1
        continue
if t1>t2:
    print("player2 wins")
elif t2>t1:
    print("player1 wins")
else:
    print("the game is draw")


