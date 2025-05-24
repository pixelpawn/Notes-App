while True:
    print("\nWelcome to the Notes App!")
    choice = input("\nChoose: Add, Remove, View, Exit: ").lower()
    
    # Debug: Show what choice was input
    print(f"User chose: {choice}")

    if choice == "add":
        add_task = input("\nEnter your note: ").strip()  # Stripped to remove extra spaces
        if add_task:  # Check if add_task is not empty
            with open("notes.txt", "a") as file:
                file.write(add_task + "\n")  # Write to file
            print(f"\nNote added: {add_task}")
        else:
            print("\nYou cannot add an empty note!")

    elif choice == "remove":
        remove_task = input("\nEnter the note to remove: ").strip()

        # Debug: Check if removing is happening
        print(f"Attempting to remove: {remove_task}")
        
        with open("notes.txt", "r") as file:
            notes = file.readlines()  # Read all notes
        
        if remove_task + "\n" in notes:
            notes.remove(remove_task + "\n")  # Remove the note
            with open("notes.txt", "w") as file:
                file.writelines(notes)  # Rewrite file without the removed note
            print(f"\nYou have removed: {remove_task}")
        else:
            print("\nNote not found...")

    elif choice == "view":
        print("\nYour Notes:")
        with open("notes.txt", "r") as file:
            notes = file.readlines()  # Read notes from file
            if notes:
                for note in notes:
                    print(f"- {note.strip()}")  # Strip newlines and extra spaces
            else:
                print("\nNo notes found.")

    elif choice == "exit":
        print("\nGoodbye!")
        exit()

    else:
        print("\nInvalid choice! Please choose Add, Remove, View, or Exit.")
