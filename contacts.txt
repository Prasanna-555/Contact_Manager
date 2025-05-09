def save_to_txt():
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")
