#rot-cipher in python
#author: Renee Althea F. Khan
#created: 12/09/2024

def calculate_rot(text, rot, direction):
    new_text = []
    # 26 letters in the english allphabet
    rot = rot%26

    for c in text:

        if 97 <= ord(c) <= 122 or 65 <= ord(c) <= 90:
            if 97 <= ord(c) <= 122:
                a_val = 97
                z_val = 122
            if 65 <= ord(c) <= 90:
                a_val = 65
                z_val = 90
            

            if direction == 'a':
                c = ord(c) + rot # get decimal value
            else:
                c = ord(c) - rot # get decimal value
            
            # for out of bounds, (1) get the difference of the excess
            if c < a_val:
                c = z_val - (a_val - c) + 1  # (2) subtract from z_val to go backwards 
                                            # add one to count Z_val
            if c > z_val:
                c = a_val + (c - z_val) - 1  # (2) add to a_val to go forward
                                            # minus one to count a_val
            
            c = chr(c)       # get ascii value

        new_text.append(c)
        
    new_text = ''.join(new_text)
    print(new_text)

if __name__ == "__main__":
    text = str(input("Enter a text: "))
    rot = int(input("Enter number of rotations: "))

    while True:
        print("Choose rotation direction: ")
        print("[a] forward")
        print("[b] backward")
        direction = str(input(""))

        if direction == 'a' or direction == 'b':
            break
        else:
            print("Invalid input")

    calculate_rot(text, rot, direction)
    

