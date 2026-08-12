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
    cast_input = input("Enter actors seperated by comma\n").strip()
    cast =[actor.strip() for actor in cast_input.split(",") if actor.strip()]
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

def edit_entry(archive, search_result):
     if not search_result:
          print("No entries matched the search")
          return
     selection = input("\nEnter the number of the entry to edit:").strip()

     if selection.isdigit():
          index = int(selection) - 1
          if index >= 0 and index < len(search_result):
               #get the dict from the results
               item = search_result[index]
               #updating the fields
               print(f"\nEditing title '{item.get('title')}'...")
               new_title = input(f"Title - current title is: [{item.get('title')}]:").strip()
               if new_title:
                    item["title"] = new_title

               print(f"\nEditing director '{item.get('director')}'...")
               new_director = input(f"Director - current director is: [{item.get('director')}]:").strip()
               if new_director:
                    item["director"] = new_director

               print(f"\nEditing year '{item.get('year')}'...")
               new_year = input(f"Year - current year is: [{item.get('year')}]:").strip()
               if new_year:
                    item["year"] = new_year

               print(f"\nEditing genre '{item.get('genre')}'...")
               new_genre = input(f"Genre - current genre is: [{item.get('genre')}]:").strip()
               if new_genre:
                    item["genre"] = new_genre

               print(f"\nEditing cast '{item.get('cast')}'...")
               current_cast = item.get("cast", [])
               #converting list of cast members to a string
               current_cast_str = ", ".join(current_cast) if isinstance(current_cast, list) else str(current_cast)
               new_cast = input(f"Title - current cast is: [{current_cast_str}]:").strip()
               if new_cast:
                    new_cast_list = [actor.strip() for actor in new_cast.split(",")]
                    item["cast"] = new_cast_list

               save(archive)

          else:
               print("Invalid entry number.")
     else:
          print("Invalid input")

