import random

# to define a function with the list of elements in it

def main():
    """Start a periodic table guessing game."""
    print("Guess the element!")

# to tell the function what elements to keep

    elements = [
        "Hydrogen",
        "Helium",
        "Lithium",
        "Beryllium",
        "Boron",
        "Carbon",
        "Nitrogen",
        "Oxygen",
        "Fluorine",
        "Neon",
        "Sodium",
        "Magnesium",
        ]
        
# to choose an element for the player to guess

    answer = random.choice(elements)
    guess = None

# to give the player another chance to answer if the got it wrong until they got it correct

    while answer != guess:
        
        guess = str(input("What element am I thinking of? "))
        
# to tell if the player got it correct
        
        if answer == guess:
            print("Good job you got it right! The answer was", answer, ".".format(guess))
            break

# to tell the player the clues for the correct element

        elif answer == "Hydrogen":
            print("The atomic mass for this element is 1.008. Try again.")
        elif answer == "Helium":
            print("The atomic mass for this element is 4.003. Try again")
        elif answer == "Lithium":
            print("The atomic mass for this element is 6.941. Try again.")
        elif answer == "Beryllium":
            print("The atomic mass for this element is 9.012. Try again.")
        elif answer == "Boron":
            print("The atomic mass for this element is 10.811. Try again.")
        elif answer == "Carbon":
            print("The atomic mass for this element is 12.011. Try again.")
        elif answer == "Nitrogen":
            print("The atomic mass for this element is 14.007. Try again.")
        elif answer == "Oxygen":
            print("The atomic mass for this element is 15.999. Try again.")
        elif answer == "Fluorine":
            print("The atomic mass for this element is 18.998. Try again.")
        elif answer == "Neon":
            print("The atomic mass for this element is 20.180. Try again.")
        elif answer == "Sodium":
            print("The atomic mass for this element is 22.99. Try again.")
        elif answer == "Magnesium":
            print("The atomic mass for this element is 24.305. Try again.")
            
main()

print("Thanks for playing. Goodbye.")


