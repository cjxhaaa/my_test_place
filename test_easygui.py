from easygui import *

#
# choices = ['是','否']
# choicebox("Danger, Will Robinson!", choices=choices)

# msgbox("Backup complete!", ok_button="Good job!")

msg = "Do you want to continue?"
title = "Please Confirm"
if ynbox(msg, title):     # show a Continue/Cancel dialog
    pass  # user chose Continue
else:  # user chose Cancel
    sys.exit(0)



# message = "What does she say?"
# title = ""
# if boolbox(message, title, ["She loves me", "She loves me not"]):
#     print("Flowers") # This is just a sample function that you might write.
# else:
#     pass


# msg ="What is your favorite flavor?"
# title = "Ice Cream Survey"
# choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
# choice = choicebox(msg, title, choices)