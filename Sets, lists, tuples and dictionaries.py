Sets, lists, tuples and dictionaries
def store():
     l = "apple banana milk eggs groundbeef kibble"
     w = l.split()
     for word in w:
         print(word.upper())
         #
     print("Alright that should be everything but I can't help but feel like something is missing")
     choice = input("Do you agree (yes/no)").lower().strip()
     if choice == "yes":
         print("Y'know what, I feel we could use some snacks")
     elif choice == "no":
         print("I mean a wise man once said 'If you forgot it, it's not importat'")
     else:
        print("Sure let's just get going")
