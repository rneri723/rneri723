#use a string to enter the name of the person that will be entered into the list
#the output would be
#name, and the 3 weights needed to score the total amount
#deadlift, squat, and bench
Name = str(input("Please enter new name to score and rank: "))
Bench = int(input("Enter bench PR: "))
Squat = int(input("Enter squat PR: "))
DeadLift = int(input("Enter deadlift PR: "))

with open ("TextFiles/PR.txt", 'a') as PR:
    PR.write(Name)
    PR.write('\n')
    PR.write(str(Bench))
    PR.write('\n')
    PR.write(str(Squat))
    PR.write('\n')
    PR.write(str(DeadLift))
    PR.write('\n')
with open ("TextFiles/PR.txt") as PR:
    contents = PR.read()
    print(contents)
z = Bench + Squat + DeadLift
print(z)
