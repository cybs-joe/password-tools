print(r"""
/$$                                               
| $$                                               
 /$$$$$$$ /$$   /$$| $$$$$$$   /$$$$$$$        /$$  /$$$$$$   /$$$$$$ 
/$$_____/| $$  | $$| $$__  $$ /$$_____//$$$$$$|__/ /$$__  $$ /$$__  $$
| $$      | $$  | $$| $$  \ $$|  $$$$$$|______/ /$$| $$  \ $$| $$$$$$$$
| $$      | $$  | $$| $$  | $$ \____  $$       | $$| $$  | $$| $$_____/
|  $$$$$$$|  $$$$$$$| $$$$$$$/ /$$$$$$$/       | $$|  $$$$$$/|  $$$$$$$
 \_______/ \____  $$|_______/ |_______/        | $$ \______/  \_______/
           /$$  | $$                      /$$  | $$                    
          |  $$$$$$/                     |  $$$$$$/                    
           \______/                       \______/
""")









password = input("Enter password to check strength")

if (password):
    print(len(password))
    up = any(c.isupper() for c in password) #this to check for any capital charc using isupper 
    low = any(c.islower() for c in password) #this to check for any capital charc using islower
    num = any(c.isdigit() for c in password)
    alphanum  = any(not c.isalnum() and not c.isspace() for c in password) #this excludes spaces and checks for special charcaters @ ,! ,/ 
    

rate = 0
if(len(password) >= 8):
    rate +=1
    if(up):
        rate+=1
        if(low):
            rate+=1
            if(num):
                rate+=1
                if(alphanum):
                    rate+=1
score =" "
if (rate <=2):
    score = "weak"
elif(rate <=4):
    score = "Medium"
elif(rate >=5):
    score = "Strong"

print("== Password Analysis ===")
print("Length      :" , len(password))
print("Uppercase   :" , up)
print("Lowercase   :" , low)
print("Numbers     :" , num)
print("Special     :" , alphanum)
print("Rating      :" , rate , "/5")
print("Score       :" , score)

choice = int(input("Enter 1 if You want a wordlist or 2 to exit program"))
if (choice == 1):
    word = input("enter anything that you want to be used in the wordlist")
    year = input("enter a year that can be used in wordlist")
    variations = [
        word + "123",
        word + "!@><L",
        word + "#@$%&__+",
        word.capitalize(),
        word.capitalize() + "!@@$#%$%^T$<OIU",
        word + "~!2\]=';lkxw!@&()*&^+",
        word + year,
        word + "YphTdItflq",
        word + "eDA6R6Ikm6",
        word + year + "eDA6R6Ikm6"
    ]
    with open("wordlist.txt", "a") as file:
        for i in variations:
            file.write(i + '\n')
else:
    print(" ")