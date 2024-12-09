#rot-cipher in python
#author: Renee Althea F. Khan
#created: 12/09/2024

def calculate_rot(text, rot, direction):
    new_text = []
    
    rot = rot%26 # 26 letters in the english allphabet

    for c in text:

        if 97 <= ord(c) <= 122 or 65 <= ord(c) <= 90:
            if 97 <= ord(c) <= 122:
                a_val = 97
            if 65 <= ord(c) <= 90:
                a_val = 65

            z_val = a_val + 26 - 1            

            # get shifted decimal value
            c = ord(c) + rot if direction == 'a' else ord(c) - rot 
            
            # for out of bounds, (1) get the difference of the excess
            if c < a_val:
                c = z_val - (a_val - c) + 1  # (2) subtract from z_val to go backwards 
                                             # add one to count Z_val
            if c > z_val:
                c = a_val + (c - z_val) - 1  # (2) add to a_val to go forward
                                             # minus one to count a_val
            
            c = chr(c)                       # get ascii value

        new_text.append(c)
        
    new_text = ''.join(new_text)

    return new_text

if __name__ == "__main__":
    text = str(input("Enter a text: "))

    while True:
        rot_input = input("Enter number of rotations: ")
        
        try:
            rot = (int(rot_input))
            if rot >= 0:
                break
            else:
                print("Invalid Input: Enter a non-negative integer")
        except ValueError:
            print("Invalid input: Enter a non-negative integer")


    while True:
        print("Choose rotation direction: ")
        print("[a] forward")
        print("[b] backward")
        direction = str(input(""))

        if direction == 'a' or direction == 'b':
            break
        else:
            print("Invalid input")

    output = calculate_rot(text, rot, direction)
    print(output)