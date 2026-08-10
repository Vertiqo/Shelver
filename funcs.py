import json

def load():
    with open('archive.json') as arch:
            archive = json.load(arch)
            return archive

def new_entry():
    new = {}
    title = input("Enter the Title\n").strip()
    while title =="":
         print("Title cant be blank!")
         title = input("Enter the Title\n").strip()
    new["title"] = title
    new["director"] = input("Enter the Director\n").strip()
    new["year"] = input("Enter the Release Year\n").strip()
    cast = []
    while True:
         actor = input("Enter Actors, leave blank when done\n").strip()
         if actor =="":
              break
         cast.append(actor)
    new["cast"] = cast
    new["genre"] = input("Enter Genre\n").strip()

    return new

def save(archive):
     with open("archive.json", "w") as arch:
        json.dump(archive, arch, indent=2)