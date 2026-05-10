import os   

while True:
    print("\n==== DREAMS FILE MANAGER ====")
    print("1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        file = open("dreams.txt", "r")
        print("=========================")
        print("--- Inspiring Messages ---")
        print("=========================")
        content = file.read()
        print(content)
        file.close()
        print("=========================")

        file = open("dreams.txt", "w")
        file.write(":Help yourself first so you can help others.")
        file.write("\n:You only live once so be careful in every decision you make.")
        file.write("\n:Keep grinding until you succeed in life.")
        file.write("\n:Love your health and Love your soul.\n\n") 
        file.close()

    elif choice == "2":
        new = input("\nEnter your new inspiring line: ")
        file = open("dreams.txt", "a")
        print("=========================")
        file.write(new + "\n")
        file.close()
        print("Your inspiration has been added!")
        print("=========================")


    elif choice == "3":
        print("Warning: This will overwrite the file.")
        confirm = input("Type \"Yes\" to continue: ")
        if confirm == "Yes":
            new_text = input("Enter your new set of inspiring messages:\n")
            file = open("dreams.txt", "w")
            print("=========================")
            file.write(new_text)
            file.close()
            print("File has been overwritten.")
            print("=========================")

    elif choice == "4":
        print("=========================")
        print("BYE.")
        print("=========================")
        os._exit(0)
        break 

    else:
        print("Invalid choice!")
