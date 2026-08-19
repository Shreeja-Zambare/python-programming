substring = input("Enter a secret msg :")
string = input ("Enter te coded msg :")

found = False 
for i in range(len(string)-len(substring)+1):
    if string[i:i + len(substring)] == substring:
        found = True 
        break

if found :
    print("Secret msg found!")
else:
    print("Secret msg not found!")
