#English alphabet
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


while True: 

    #Question asked for encryption, decryption or quit.
    mode= input("Select mode (Encryption(e)/Decryption(d)/Quit(q)): ").lower()

    #Encryption  
    if mode=="e":
        text=input("Enter text: ").lower()
        shift=int(input("Enter shift number: "))
        result=""

        #Loop through each letter in the text
        for letter in text:
            if letter in alphabet:
                position=alphabet.index(letter)
                new_position=(position+shift)%26
                result+=alphabet[new_position]
                result=result.capitalize()
            
            #If the character is not in the alphabet (like spaces or punctuation), keep it unchanged
            else:
                result+=letter
                result=result.capitalize()
        print("Encrypted text:",result)

    #Decryption
    elif mode=="d":
        text=input("Enter text: ").lower()
        shift=int(input("Enter shift number: "))
        shift = -abs(shift)
        result=""
        for letter in text:

            #Loop through each letter in the text
            if letter in alphabet:
                position=alphabet.index(letter)
                new_position=(position+shift)%26
                result+=alphabet[new_position]
                result=result.capitalize()
            #If the character is not in the alphabet (like spaces or punctuation), keep it unchanged
            else:
                result+=letter
                result=result.capitalize()
        print("Decrypted text:",result)

    #Quit
    elif mode=="q":
        print("Exiting the program.")
        break

    #Invalid input handling
    else:
        print("Invalid mode. Please choose Encryption, Decryption, or Quit.") 