#taking totla amount as input from user
Amount = int(input("Please Enter Amount for Withdraw"))
#calculating the number of notes of different denominations
note1 = Amount//100
note2 = (Amount%100)//50
note3 = ((Amount%100)%50)//10
print("notes of 100 ruppee", note1)
print("notes of 50 ruppee", note2)
print("notes of 10 ruppee", note3 )