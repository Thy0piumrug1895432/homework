If/else basics.py
def start_game():
...     print("You went camping and wanted to explore, so you went exploring until you find a fork.")
choice = input("Do you go left or right? (left/right): ").lower().strip()
if choice == "left" :
  print("end up in a huge flower field that seems to beautiful to be real")
  choice = input("another fork, left or right? (left/right)?: ").lower().strip()
    if choice == "left":
      print("You see a lovely, calm river that looks like it would be nice to splash in")
    elif choice == "right":
      print("Wow that's a cool rock, you thought to yourself before heading back")
elif choice == "right":
  print("You find a large cave taht looks sketchy, so you run back to the campsite)
else:
  print("That's enough exploring for today, you think and go back")
  