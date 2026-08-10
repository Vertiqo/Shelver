import json
from funcs import load, new_entry, save


def main():
    # loading the archive json file
    archive = load()
    2#print(archive)
    

    while True:
        choice = input("1 - New Entry\n2 - Search existing Entries\n")

        if choice == "1":
            print("New Entry selected")
            entry = new_entry()
            archive.append(entry)
            save(archive)
            break
        elif choice =="2":
            print("Search selected")
            
            #for entry in archive:
            #    print(entry)
            #search()
            break
        else:
            print("wrong entry")

main()