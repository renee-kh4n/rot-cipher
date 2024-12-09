#rot-cipher in python
#author: Renee Althea F. Khan
#created: 12/09/2024



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

    

