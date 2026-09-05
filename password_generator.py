import string
import secrets
import math

print("\nlength must be between 15-65 characters")
try:
    length= int(input("enter the length of password: "))
    if (length < 15 or length> 65):
        print("invalid input")
    else:
        data=[]
        character = string.ascii_letters + string.digits + string.punctuation
        for i in range(length):
            data.append(secrets.choice(character))

        password=''.join(data)

        entropy= length * math.log2(len(character))

        print("you password is: ",password)   
        print("length of your password is: ",len(password))
        print("entropy is:", round(entropy,2))

except ValueError:
    print("you can only enter a number") 