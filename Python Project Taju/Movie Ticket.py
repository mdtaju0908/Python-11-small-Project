#movie ticket
age = int (input("Enter Your age :"))
ticket = True 
if age > 18:
    print("You can watch tha movie")
if ticket == True :
    print("you  can go inside ")
elif age < 15:
    print ("You can watch the movie with parents ")
else:
    print("Not allowed")