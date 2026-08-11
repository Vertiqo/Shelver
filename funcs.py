import json
from uuid import uuid4

# loading the json based archive
def load():
     with open('archive.json') as arch:
          archive = json.load(arch)
     
     changed = False
     for movie in archive:
          if "id" not in movie:
               movie["id"] = str(uuid4())
               changed = True
     if changed:
          save(archive)

     return archive


# Adding a new entry to the archive by asking for user input
def new_entry():
    new = {}
    new["id"] = str(uuid4())
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

# saving the archive
def save(archive):
     with open("archive.json", "w") as arch:
        json.dump(archive, arch, indent=2)

# searching for an entry in the archive based on it being already open as a list

def search(archive, query):
     result = []
     for entry in archive:
          if query in entry["title"] or query in entry["director"] or query in entry["year"] or query in entry["cast"] or query in entry["genre"]:
               result.append(entry)
     return result
