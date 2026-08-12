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
    new["id"] = str(uuid4())

    return new

# saving the archive
def save(archive):
     with open("archive.json", "w") as arch:
        json.dump(archive, arch, indent=2)

# searching for an entry in the archive based on it being already open as a list

def search(archive, query):
     result = []
     #making the search word lowercase
     q = query.lower()
     for entry in archive:
          #getting information per entry from the archive in lowercase
          #converting to str is important for the "year"
          title = str(entry.get("title", "")).lower()
          director = str(entry.get("director", "")).lower()
          year = str(entry.get("year", "")).lower()
          genre = str(entry.get("year, ")).lower()

          #cast is a list, any returns true if any list entry matches
          cast_list = entry.get("cast", [])
          if isinstance(cast_list, list):
               cast_match = any(q in actor.lower() for actor in cast_list)
          else:
               cast_match = q in str(cast_list).lower()

          if (q in title or
              q in director or
              q in year or
              q in genre or cast_match):
               result.append(entry)

     return result

def print_results(results):
     if not results:
          print("\nNo entries have been found.\n")
          return

     print(f"\n*** Found {len(results)} entries ***")
     for i, item in enumerate(results, start = 1):
          cast = item.get("cast", [])
          cast_str = ", ".join(cast) if isinstance(cast, list) else str(cast)

          print(f"\n[{i}] {item.get('title', 'Unknown Title')} ({item.get('year', 'N/A')})")
          print(f"  Director: {item.get('director', 'N/A')}")
          print(f"  Genre:    {item.get('genre', 'N/A')}")
          print(f"  Cast:     {cast_str}")
     print("\n********************")
