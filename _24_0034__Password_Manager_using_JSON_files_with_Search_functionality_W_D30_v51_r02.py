from tkinter import *   #imports JUST about everything except for MessageBoxes, etc.. (eveyrthing = classes, constants)
from tkinter import messagebox
import pyperclip
from random import choice, randint, shuffle   #just remove all the places that have 'random.'
import json  #you do NOT need to install json

# Constants:
my_dummy_email = "test@gmail.com"
new_json_data_to_dump = ""

# Cleaner Code:

#---------------------------- SEARCH BUTTON AND FUNCTIONALITY -------------------------------------- #


# --------------------------- FIND PASSWORD -------------------------- #

def find_password_search_button_action_press():
    # nested dictionary format here: dictionary = {website entered: {'email': actual typed email into the field/default email, 'password': generated/created password}, (repeat) next website entry... }
    website = website_entry.get()
    try:
        with open("newest_JSON_data_03.json") as file_to_dump_into:
            data = json.load(file_to_dump_into)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:  #otherwise, if we already found the file, then skip except and implement the code block below!
        # print(data) # just for testing to see what the dictionary prints out as of running this code.
        if website in data:  #if it IS successful (if True) in finding that word inside the dictionary, then we do the following code:  (we need to get ahold of the email and password values)
            #sample result from the dictionary: '552pm 12.27': {'email': 'test@gmail.com', 'password': '#&z%U0cA3KkZVs3'}
            #1 we want to get ahold of the dictionary, and pick out the item with the key that matches the website that we're searching for. #2 once we got ahold of this: data[website], which is equivalent to: {'email': 'test<3sKoalas@gmail.com', 'password': 'jE#Re1h+k2M6h'}, and because this is a nested dictionary (a dict nested inside a dict), you have to look for a key TWICE, in order to get ahold of the final value within both. So, {'this is the newest 03.01': {'email': 'test<3sKoalas@gmail.com', 'password': 'jE#Re1h+k2M6h'} is Key1 = 'this is the newest 03.01', and Key1.1= {'email': so 'test<3sKoalas@gmail.com' is the nested Key data / email 2 layers deep, and 'password': 'jE#Re1h+k2M6h' is the 2nd layer deep data Value. and assign all of that to variable email. data[website] = {'email': 'test<3sKoalas@gmail.com', 'password': 'jE#Re1h+k2M6h'}
            email = data[website]['email']   #to get ahold of the email Value, if True; you have to go 2 Keys deep, so you select the Dictionary you want (data), then the first key of the first dict = website, then the 2nd key = 'email', then that gets the value. So: ( (1st Key = {'this is the newest 03.01': and also 2nd Key = {'email': ), in order to get test<3sKoalas@gmail.com; then assign all of that to variable email.
            password = data[website]['password']   #to get ahold of the password Value, if True, do all above. (get the data dictionary, the 1st Key website, and the 2nd Key 'password, then assign all of that to variable password.
            messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
        else:  #sure, we could make an exception here, but if we can do something very easily with if and else, then stick with if and else. If you can't do it easily, and it's actually an error that would be thrown and you don't have any other way of dealing with that case, then you should be using try except else finally keywords.
            messagebox.showinfo(title="Website not found", message=f'No details for {website} exists.')

'''
    try:  #TRY to open the file and TRY reading the data inside (which will be BOTH the 'with open', 'json.load' & "r" lines
        with open("newest_JSON_data_03.json", mode="r") as file_to_dump_into:  #this is the biggest potential problem that MAY fail, so we want to place the Try block above this line:
            older_data = json.load(file_to_dump_into)   # .load() Method: takes this JSON data and converts it into a Python dictionary.
    except FileNotFoundError:   #if there is NOT a file created quite yet, instead of giving us the FileNotFoundError, instead we will write a new file, titled that, then we dump to save the file again
        with open("newest_JSON_data_03.json", mode="w") as file_to_dump_into:   #creating a new 03 file, in write mode
            # Saving updated data (then write that data back into this file):
            json.dump(new_json_data_to_dump, file_to_dump_into, indent=4)     #new fields that the user typed into the program fields, will be aggragated into a dictionary, which we can process later in the code with that format.

#TODO2: Otherwise do this, IF the file was found and just go ahead and add the new data into the older_data file, and update and save the file:
    # else block will trigger IF the TRY Block was successful (not the except block)

    else:   #if there's no fields empty, then move on to the Confirmation box:
        # with open("newest_JSON_data_03.json", mode="r") as file_to_dump_into:  #(Line 69: Is Optional, because the 03 file already exists from the TRY block OR it created it from the EXCEPT block - remember, this is the Else block, AFTER everything else already succeeds before it.)
            # Reading old data:
            # older_data = json.load(file_to_dump_into)                          #(Line 71: Is Optional, because the 03 file already exists from the TRY block OR it created it from the EXCEPT block - remember, this is the Else block, AFTER everything else already succeeds before it.)
            # Updating old data with new data:
        older_data.update(new_json_data_to_dump)  #.update() will merge the new data into the dictionary along with the old_data displaying before it, within the same dict (NOT APPENDED AFTER THE DICT or in a diff dict)

        #after we've updated the data (just above), we want to be able to open up new_json in "write" mode, and then dump this updated data, into that data file.
        with open("newest_JSON_data_03.json", mode="w") as file_to_dump_into:
            # Saving updated data (then write that data back into this file):
            json.dump(older_data, file_to_dump_into, indent=4) 
'''


'''
def find_password_search_button_action_press():
    website_name = website_entry.get()
    try:  # TRY to open the file and TRY reading the data inside (which will be BOTH the 'with open', 'json.load' & "r" lines
        with open("newest_JSON_data_03.json", mode="r") as file_to_dump_into:
            older_data = json.load(file_to_dump_into)

        # if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:  # if the 1st or 3rd box is empty, then give an error popup:

    except FileNotFoundError:
        messagebox.showerror(title=f"{website_name}", message=f"Sorry, but {website_name} was not found inside this file.")
        # with open("newest_JSON_data_03.json", mode="w") as file_to_dump_into:  # creating a new 03 file, in write mode
            # Saving updated data (then write that data back into this file):
            # json.dump(new_json_data_to_dump, file_to_dump_into, indent=4)  # new fields that the user typed into the program fields, will be aggragated into a dictionary, which we can process later in the code with that format.

    # TODO2: Otherwise do this, IF the file was found:
    # else block will trigger IF the TRY Block was successful (not the except block)

    else:  # if there's no fields empty, then move on to the Confirmation box:
        # with open("newest_JSON_data_03.json", mode="r") as file_to_dump_into:  #(Line 69: Is Optional, because the 03 file already exists from the TRY block OR it created it from the EXCEPT block - remember, this is the Else block, AFTER everything else already succeeds before it.)
        # Reading old data:
        # older_data = json.load(file_to_dump_into)                          #(Line 71: Is Optional, because the 03 file already exists from the TRY block OR it created it from the EXCEPT block - remember, this is the Else block, AFTER everything else already succeeds before it.)
        # Updating old data with new data:
        older_data.update(new_json_data_to_dump)

        # after we've updated the data (just above), we want to be able to open up new_json in "write" mode, and then dump this updated data, into that data file.
        with open("newest_JSON_data_03.json", mode="w") as file_to_dump_into:
            # Saving updated data (then write that data back into this file):
            json.dump(older_data, file_to_dump_into, indent=4)  # (MUST IMPORT JSON METHOD 1ST) json.dump(obj=things you want to dump, IO[str]=file you want to dump it to). The data we want to put in should be in the form of a dict. ; instead of this: data_file.write(f"{get_website_url}, {get_email_username}, {get_password}\n")
            # not the NEW data, but the data that we updated           #spacing for easier learning above                                          # json.dump(..., ..., (optional: indent=4) will help with the human readability of the spaced out fields within the json file.
    # website_entry.delete(0, END)  # or (0, 'end')
    # password_entry.delete(0, END)  # or (0, 'end')
'''
# def search_if_inside_file():
    # website_name = website_entry.get()
    # if website_name not in older_data:
    #     # if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:  # if the 1st or 3rd box is empty, then give an error popup:
    #     messagebox.showerror(title=f"{website_name}",
    #                          message=f"Sorry, but {website_name} was not found inside this file.")



######################### SEARCH button functionality ###############################

'''

def is_the_word_found_within_dictionary_keys_and_values(dictionary, website_entry):
    for key, value in file_to_dump_into.items():
        if website_entry in key or website_entry in value:
            return True
    return False


def is_word_in_dict(dictionary, word):
    for key, value in dictionary.items():
        if word in key or word in value:
            return True
    return False

# Example usage
my_dict = {'key1': 'value1', 'key2': 'value2'}
word = 'key1'
print(is_word_in_dict(my_dict, word))  # Returns True if 'key1' is in any key or value


'''

# ---------------------------- PASSWORD GENERATOR FUNCTION AND BUTTON------------------------------- #

def generate_secure_password():
    from random import shuffle, randint, choice

    #Password Generator function:

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, string=password)

    pyperclip.copy(password)

    # print(f"Your new secure Generated Password is: {password}")
    # return password

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    get_website_url = website_entry.get()
    get_email_username = email_username_entry.get()
    get_password = password_entry.get()
    new_json_data_to_dump = {
        get_website_url: {    #the website key (itself, is also going to contain a dictionary)
            "email": get_email_username,
            "password": get_password,
        }
    }

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:  #if the 1st or 3rd box is empty, then give an error popup:
        messagebox.showerror(title="Oops", message="Please fill in ALL of the blanks before clicking the Add button!")

#TODO1: IF the file doesn't exist yet, do this: (create a new file)

    try:  #TRY to open the file and TRY reading the data inside (which will be BOTH the 'with open', 'json.load' & "r" lines
        with open("newest_JSON_data_03.json", mode="r") as file_to_dump_into:  #this is the biggest potential problem that MAY fail, so we want to place the Try block above this line:
            older_data = json.load(file_to_dump_into)   # .load() Method: takes this JSON data and converts it into a Python dictionary.
    except FileNotFoundError:   #if there is NOT a file created quite yet, instead of giving us the FileNotFoundError, instead we will write a new file, titled that, then we dump to save the file again
        with open("newest_JSON_data_03.json", mode="w") as file_to_dump_into:   #creating a new 03 file, in write mode
            # Saving updated data (then write that data back into this file):
            json.dump(new_json_data_to_dump, file_to_dump_into, indent=4)     #new fields that the user typed into the program fields, will be aggragated into a dictionary, which we can process later in the code with that format.

#TODO2: Otherwise do this, IF the file was found and just go ahead and add the new data into the older_data file, and update and save the file:
    # else block will trigger IF the TRY Block was successful (not the except block)

    else:   #if there's no fields empty, then move on to the Confirmation box:
        # with open("newest_JSON_data_03.json", mode="r") as file_to_dump_into:  #(Line 69: Is Optional, because the 03 file already exists from the TRY block OR it created it from the EXCEPT block - remember, this is the Else block, AFTER everything else already succeeds before it.)
            # Reading old data:
            # older_data = json.load(file_to_dump_into)                          #(Line 71: Is Optional, because the 03 file already exists from the TRY block OR it created it from the EXCEPT block - remember, this is the Else block, AFTER everything else already succeeds before it.)
            # Updating old data with new data:
        older_data.update(new_json_data_to_dump)  #.update() will merge the new data into the dictionary along with the old_data displaying before it, within the same dict (NOT APPENDED AFTER THE DICT or in a diff dict)

        #after we've updated the data (just above), we want to be able to open up new_json in "write" mode, and then dump this updated data, into that data file.
        with open("newest_JSON_data_03.json", mode="w") as file_to_dump_into:
            # Saving updated data (then write that data back into this file):
            json.dump(older_data, file_to_dump_into, indent=4)  # (MUST IMPORT JSON METHOD 1ST) json.dump(obj=things you want to dump, IO[str]=file you want to dump it to). The data we want to put in should be in the form of a dict. ; instead of this: data_file.write(f"{get_website_url}, {get_email_username}, {get_password}\n")
            # not the NEW data, but the data that we updated           #spacing for easier learning above                                          # json.dump(..., ..., (optional: indent=4) will help with the human readability of the spaced out fields within the json file.
    finally:
        website_entry.delete(0, END)  # or (0, 'end')
        password_entry.delete(0, END)  # or (0, 'end')

    #OR you can use:
    # finally:  (in this indent position)
    #     website_entry.delete(0, END)  # or (0, 'end')
    #     password_entry.delete(0, END)  # or (0, 'end')

'''
The finally block is indeed allowed and is typically used in Python, but it must be part of a try...except...finally structure. The finally block is executed no matter whether the try block raises an error or not. It's commonly used for cleanup actions, like closing files or clearing resources, that need to be executed under all circumstances.

In your code, the finally block is correctly placed as part of the try...except...finally structure in the save() function. This means it will execute whether or not the try block (reading the JSON file) or the except block (handling a FileNotFoundError) is executed.

Here's a brief explanation of what happens in your save() function:

You attempt to open and read a JSON file in a try block.
If the file doesn't exist (FileNotFoundError), the except block creates a new file.
After the try or except block finishes, the finally block executes, deleting the contents of the website_entry and password_entry widgets.
This is the correct usage of the finally block. If you're encountering issues, they may be due to other parts of your code or the specific context in which this function is being used. If there's a specific error or issue you're facing, please provide more details for further assistance.

'''

# ---------------------------- UI SETUP ------------------------------- #


# Window Setup:
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Canvas Widget:
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(107, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Website label:
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

# Website Entry:
website_entry = Entry(width=33)
website_entry.insert(END, string="Enter website URL Search here!")
website_entry.grid(row=1, column=1)    #columnspan=2 is a keyword argument.
website_entry.focus() #If you want to start the blinking cursor on the first Entry text box field, then you would get ahold of the website_entry and use a Method on it called: .focus() and you would place it right after the .grid() method, of the Entry block we want it to Only apply to.

search_button = Button(text="Search", command=find_password_search_button_action_press, width=15)   #place before the width and after text=: command=search_button_action_press. #width= does not have to be after the other parameters, it can be before as well, and it will work just fine.
search_button.grid(row=1, column=2)    #optional= , columnspan=2

#############

# Email/Username label:
email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)

# Email/Username Entry:
email_username_entry = Entry(width=52)
email_username_entry.insert(END, my_dummy_email)
email_username_entry.grid(row=2, column=1, columnspan=2)

#############

# Password label:
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Password Entry:
password_entry = Entry(width=33)
# password_entry.insert(END, string="Enter your Password here, or --> ")
password_entry.grid(row=3, column=1)

# Generate Password button:
# def generate_secure_password():
    # email_username_entry = Entry(width=52)
    # email_username_entry.insert(END, my_dummy_email)
    # email_username_entry.grid(row=2, column=1, columnspan=2)
    # print(password)


generate_password_button = Button(text="Generate Password", command=generate_secure_password, width=15)
generate_password_button.grid(row=3, column=2, columnspan=2)


################ Add button #############################
add_button = Button(text="Add", command=save, width=45)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()