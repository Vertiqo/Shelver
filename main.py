import json
from funcs import load, new_entry, save, search
from uuid import uuid4


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
            #print("Search selected")
            query = input("What are you searching for?\n")
            result = search(archive, query)
            if len(result) == 0:
                print("nothing found")
            else:
                for movie in result:
                    print(movie)
            break
        else:
            print("wrong entry")

main()