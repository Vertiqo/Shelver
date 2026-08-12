import json
from funcs import load, new_entry, save, search, print_results, edit_entry
from uuid import uuid4


def main():
    # loading the archive json file
    archive = load()
    2#print(archive)
    

    while True:
        choice = input("1 - New Entry\n2 - Search existing entries\n3 - Edit existing entries\n")

        if choice == "1":
            print("New Entry selected")
            entry = new_entry()
            archive.append(entry)
            save(archive)
            break
        elif choice =="2":
            #print("Search selected")
            query = input("What are you searching for?\n")
            result = search(archive, query)
            print_results(result)
            break

        elif choice == "3":
            query = input("What entry do you want to edit?\n")
            result = search(archive, query)
            print_results(result)
            edit_entry(archive, result)
        else:
            print("wrong entry")

main()