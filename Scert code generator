# Secret Code Generator - Caesar Cipher

def encode(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decode(message, shift):
    return encode(message, -shift)


def main():
    while True:
        print("\n=== Secret Code Generator ===")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            msg = input("Enter message to encode: ")
            shift = int(input("Enter shift number: "))
            print("Encoded Message:", encode(msg, shift))
        
        elif choice == "2":
            msg = input("Enter message to decode: ")
            shift = int(input("Enter shift number: "))
            print("Decoded Message:", decode(msg, shift))
        
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
