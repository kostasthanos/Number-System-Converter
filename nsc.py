#===========================#
#  NUMBER SYSTEM CONVERTER  #
#   Convert a number from   #
#   one system to another   #
#===========================#
#    Konstantinos Thanos    #
#     Mathematician, Msc    #
#===========================#

# Function to remove extra characters ('0b', '0o', '0x') from a printed result
def remove(result):
    my_list = ["0b", "0o", "0x"]
    for char in my_list:
        if char in result:
            result = result.replace(char, "").strip()
    return result

# Function to invert 0 to 1 and 1 to 0
def invert(let):
    if let=="0":
        return "1"
    elif let=="1":
        return "0"

# convert() : Function to convert numbers from one system to another
def convert():
    num = input("\nEnter your number : ") # User input of the desired number to be converted
    print("\nIn which system does your number belong (type the number) ?")
    print("[1] : Binary \n[2] : Decimal \n[3] : Octal \n[4] : Hexadecimal")
    print(18*"=")
    
    my_system = int(input("Choice : "))   # User inputs the number of his 'system'
    print("\nChoose the system you want to convert your number")

    # Transform user's number and show the options of systems
    if my_system == 1:   # User input in binary
        temp = int(num, 2)
        print("[1] : Decimal \n[2] : Octal \n[3] : Hexadecimal \n[4] : Decimal, Octal, Hexadecimal (non negative)")        
    elif my_system == 2: # User input in decimal
        temp = int(num)
        print("[1] : Binary \n[2] : Octal \n[3] : Hexadecimal \n[4] : Binary, Octal, Hexadecimal (non negative)")
    elif my_system == 3: # User input in octal
        temp = int(num, 8)
        print("[1] : Binary \n[2] : Decimal \n[3] : Hexadecimal \n[4] : Binary, Decimal, Hexadecimal (non negative)")
    elif my_system == 4: # User input in hexadecimal
        temp = int(num, 16)
        print("[1] : Binary \n[2] : Decimal \n[3] : Octal \n[4] : Binary, Decimal, Octal (non negative)")
    print(50*"=")

    # User inputs the number of the desired system
    system_choice = int(input("System choice : ")) 

    # Transformations from Binary to (Decimal or Octal or Hexadecimal or all)
    if my_system == 1:
        if system_choice == 1:
            result = temp
        elif system_choice == 2:
            result = oct(temp)
        elif system_choice == 3:
            result = hex(temp)
        elif system_choice == 4 :
            result = "dec : {}, oct : {}, hex : {}".format(temp, oct(temp), hex(temp))
            
    # Transformations from Decimal to (Binary or Octal or Hexadecimal or all)
    elif my_system == 2:
        if temp >= 0: # Check if decimal >= 0
            if system_choice == 1:
                result = bin(temp)    
            elif system_choice == 2:
                result = oct(temp)
            elif system_choice == 3:
                result = hex(temp)
            elif system_choice == 4 :
                 result = "bin : {}, oct : {}, hex : {}".format(bin(temp), oct(temp), hex(temp))
        else: # Check if decimal < 0
            a = remove(bin(temp*(-1)))
            b = ''
            if len(a) < 8:
                a = '0'*(8-len(a)) + a
            for let in a:
                b += invert(let) # Apply invert() function for the binary number
            c = remove(bin(int(b, 2) + int('1', 2)))
            if system_choice == 1:
                result = c 
            elif system_choice == 2:
                result = oct(int(c, 2))
            elif system_choice == 3:
                result = hex(int(c, 2))
            result = remove(result) # Apply remove() function to the result
            if len(result) < 8: 
                result = 'F'*(8-len(result)) + result # Add F's to fill the '8-digits number'
                
    # Transformations from Octal to (Binary or Decimal or Hexadecimal or all)
    elif my_system == 3:
        if system_choice == 1:
            result = bin(temp)    
        elif system_choice == 2:
            result = temp
        elif system_choice == 3:
            result = hex(temp)
        elif system_choice == 4 :
            result = "bin : {}, dec : {}, hex : {}".format(bin(temp), temp, hex(temp))

    # Transformations from Hexadecimal to (Binary or Decimal or Octal or all)
    elif my_system == 4:
        if system_choice == 1:
            result = bin(temp)    
        elif system_choice == 2:
            result = temp
        elif system_choice == 3:
            result = oct(temp)
        elif system_choice == 4 :
            result = "bin : {}, dec : {}, oct : {}".format(bin(temp), temp, oct(temp))
            
    # Check for correct inputs (numbers only)
    else:
        print("Choose a correct number")
    result = str(result) # Trasform result to string
    result = remove(result).strip() # Apply remove() function to remove extra characters
    print("\nResult: ", result.upper())
        
if __name__ == "__main__":
    print("\n# Number System Converter #")
    while True:
        convert()
        # Ask user if wants to continue with another new number
        choice = input("\nContinue with another number (Y/N) : ")
        if choice == "Y" or choice == "y":
            continue
        else:
            break
