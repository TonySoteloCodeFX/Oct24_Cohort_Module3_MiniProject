import os
import re
from colorama import Fore, Back, Style
from art import intro, outro

contact_dict = {}

number_pattern = r"^\d{3}-\d{3}-\d{4}$"
name_pattern = r"([\bA-Z]{1}[A-Za-z.']+)\s([A-Z]{1}[A-Za-z]+)"
email_pattern = r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[a-z]{3,}"

def clr():
    '''This clears the terminal.'''
    os.system('cls' if os.name == 'nt' else 'clear')

def add_contact():
    '''Adds contact to contact dictionary & returns confirmation.'''
    clr()
    print("-" * 50)
    keep_running = True
    while keep_running:
        try:
            print(f"{Fore.GREEN}To add a new contact enter the following:{Style.RESET_ALL}")
            print("-" * 50)

            contact_number = input(f"{Fore.GREEN}Enter phone number: ex: xxx-xxx-xxxx{Style.RESET_ALL}\n")
            print("-" * 50)
            if not re.match(number_pattern, contact_number):
                clr()
                print("-" * 50)
                print(f"{Fore.RED}Invalid Number.{Style.RESET_ALL} Try again. ex: xxx-xxx-xxxx")
                print("-" * 50)
                continue

            contact_name = input(f"{Fore.GREEN}Enter full name: ex: John Doe{Style.RESET_ALL}\n")
            print("-" * 50)
            if not re.match(name_pattern, contact_name):
                clr()
                print("-" * 50)
                print(f"{Fore.RED}Invalid Name.{Style.RESET_ALL} Try again. ex: John Doe")
                print("-" * 50)
                continue

            contact_email = input(f"{Fore.GREEN}Enter email: ex: john_doe@gmail.com{Style.RESET_ALL}\n")
            print("-" * 50)
            if not re.match(email_pattern, contact_email):
                clr()
                print("-" * 50)
                print(f"{Fore.RED}Invalid Email.{Style.RESET_ALL} Try again. ex: john_doe@gmail.com")
                print("-" * 50)
                continue

            contact_title = input(f"{Fore.GREEN}Personal or Professional:{Style.RESET_ALL}\n")
            print("-" * 50)
            contact_notes = input(f"{Fore.GREEN}Enter Notes:{Style.RESET_ALL}\n")

            contact_dict[contact_number] = {
                "Name": contact_name,
                "Title": contact_title,
                "Email": contact_email,
                "Notes": contact_notes
            }

            clr()
            print("-" * 50)
            print(f"{Fore.GREEN}The following contact was added.{Style.RESET_ALL}")
            print("-" * 50)
            print(f"{Fore.GREEN}Title:{Style.RESET_ALL} {contact_title}\n{Fore.GREEN}Name:{Style.RESET_ALL} {contact_name}\n{Fore.GREEN}Phone Number:{Style.RESET_ALL} {contact_number}\n{Fore.GREEN}Email:{Style.RESET_ALL} {contact_email}\n{Fore.GREEN}Notes:{Style.RESET_ALL} {contact_notes}")
            print("-" * 50)

            keep_running = False
        except Exception as e:
            clr()
            print("-" * 50)
            print(f"{Fore.RED}Error:{Style.RESET_ALL} {e}")
            
def edit_contact():
    '''deletes given contact and creates a new one.'''
    clr()
    print("-" * 50)
    keep_running = True
    while keep_running:
        try:
            print(f"{Fore.GREEN}Enter number to edit for ex: xxx-xxx-xxxx{Style.RESET_ALL}")
            contact_edit = input(f"{Fore.GREEN}Enter Number:{Style.RESET_ALL} ")
            print("-" * 50)

            if contact_edit in contact_dict:
                clr()
                print("-" * 50)
                del contact_dict[contact_edit]

            correct_number = input(f"{Fore.GREEN}Enter correct phone number: ex: xxx-xxx-xxxx{Style.RESET_ALL}\n")
            print("-" * 50)
            if not re.match(number_pattern, correct_number):
                clr()
                print("-" * 50)
                print(f"{Fore.RED}Invalid Number.{Style.RESET_ALL} Try again. ex: xxx-xxx-xxxx")
                print("-" * 50)
                continue

            correct_name = input(f"{Fore.GREEN}Enter correct full name: ex: John Doe{Style.RESET_ALL}\n")
            print("-" * 50)
            if not re.match(name_pattern, correct_name):
                clr()
                print("-" * 50)
                print(f"{Fore.RED}Invalid Name.{Style.RESET_ALL} Try again. ex: John Doe")
                print("-" * 50)
                continue

            correct_email = input(f"{Fore.GREEN}Enter correct email: ex: john_doe@gmail.com{Style.RESET_ALL}\n")
            print("-" * 50)
            if not re.match(email_pattern, correct_email):
                clr()
                print("-" * 50)
                print(f"{Fore.RED}Invalid Email.{Style.RESET_ALL} Try again. ex: john_doe@gmail.com")
                print("-" * 50)
                continue

            correct_title = input(f"{Fore.GREEN}Personal or Professional:{Style.RESET_ALL}\n")
            print("-" * 50)
            correct_notes = input(f"{Fore.GREEN}Enter Notes:{Style.RESET_ALL}\n")

            contact_dict[correct_number] = {
                "Name": correct_name,
                "Title": correct_title,
                "Email":correct_email,
                "Notes": correct_notes
            }

            clr()
            print("-" * 50)
            print(f"{Fore.GREEN}The following contact was edited.{Style.RESET_ALL}")
            print("-" * 50)
            print(f"{Fore.GREEN}Title:{Style.RESET_ALL} {correct_title}\n{Fore.GREEN}Name:{Style.RESET_ALL} {correct_name}\n{Fore.GREEN}Phone Number:{Style.RESET_ALL}{correct_number}\n{Fore.GREEN}Email:{Style.RESET_ALL} {correct_email}\n{Fore.GREEN}Notes:{Style.RESET_ALL} {correct_notes}")
            print("-" * 50)

            keep_running = False
        except Exception as e:
            clr()
            print("-" * 50)
            print(f"{Fore.RED}Error:{Style.RESET_ALL} {e}")

def delete_contact():
    '''Deletes given number contact from contact dictionary and prints confirmation.'''
    try:
        clr()
        print("-" * 50)
        print(f"{Fore.GREEN}Enter number to delete for ex: xxx-xxx-xxxx{Style.RESET_ALL}")
        contact_delete = input(f"{Fore.GREEN}Enter Number:{Style.RESET_ALL} ")

        if contact_delete in contact_dict:
            clr()
            print("-" * 50)
            contact_details = contact_dict[contact_delete]
            print(f"{Fore.GREEN}The following contact has been deleted.{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Title:{Style.RESET_ALL} {contact_details['Title']}")
            print(f"{Fore.GREEN}Name:{Style.RESET_ALL} {contact_details['Name']}")
            print(f"{Fore.GREEN}Phone Number: {Style.RESET_ALL}{contact_delete}")
            print(f"{Fore.GREEN}Email:{Style.RESET_ALL} {contact_details['Email']}")
            print(f"{Fore.GREEN}Notes:{Style.RESET_ALL} {contact_details['Notes']}")
            del contact_dict[contact_delete]
            print("-" * 50)
        else:
            clr()
            print("-" * 50)
            print(f"{Fore.GREEN}The number:{Style.RESET_ALL} {contact_delete}. {Fore.GREEN}Does not exist. Try again.{Style.RESET_ALL}")

    except ValueError:
        clr()
        print("-" * 50)
        print(f"{Fore.RED}Error:{Style.RESET_ALL} Incorrect input")

def search_contact():
    '''Searches contact dictionary and returns given number's contact details.'''
    try:
        clr()
        print("-" * 50)
        print(f"{Fore.GREEN}Enter number to search for ex: xxx-xxx-xxxx{Style.RESET_ALL}")
        contact_search = input(f"{Fore.GREEN}Enter Number:{Style.RESET_ALL} ")
        
        if contact_search in contact_dict:
            clr()
            print("-" * 50)
            contact_details = contact_dict[contact_search]
            print(f"{Fore.GREEN}Title:{Style.RESET_ALL} {contact_details['Title']}")
            print(f"{Fore.GREEN}Name:{Style.RESET_ALL} {contact_details['Name']}")
            print(f"{Fore.GREEN}Phone Number: {Style.RESET_ALL}{contact_search}")
            print(f"{Fore.GREEN}Email:{Style.RESET_ALL} {contact_details['Email']}")
            print(f"{Fore.GREEN}Notes:{Style.RESET_ALL} {contact_details['Notes']}")
            print("-" * 50)
        else:
            clr()
            print("-" * 50)
            print(f"{Fore.GREEN}The number:{Style.RESET_ALL} {contact_search}. {Fore.GREEN}Does not exist. Try again.{Style.RESET_ALL}")

    except ValueError:
        clr()
        print("-" * 50)
        print(f"{Fore.RED}Error:{Style.RESET_ALL} Incorrect input")

def display_contacts():
    '''Displays all contacts in dictionary.'''
    clr()
    print("-" * 50)
    for index, (contact_num, contact_details) in enumerate(contact_dict.items()):
        print(f"{Fore.GREEN}{index + 1} - Title:{Style.RESET_ALL} {contact_details['Title']}")
        print(f"{Fore.GREEN}Name:{Style.RESET_ALL} {contact_details['Name']}")
        print(f"{Fore.GREEN}Phone Number:{Style.RESET_ALL} {contact_num}")
        print(f"{Fore.GREEN}Email:{Style.RESET_ALL} {contact_details['Email']}")
        print(f"{Fore.GREEN}Notes:{Style.RESET_ALL} {contact_details['Notes']}")
        print("-" * 50)

def export_contacts():
    with open('contact_file.txt', 'w') as file:
        for contact, details in contact_dict.items():
            file.write(f"{contact}: Name: {details.get('Name', 'N/A')},"
                       f"Phone Number: {details.get('Phone Number', 'N/A')},"
                       f"Email: {details.get('Email', 'N/A')},"
                       f"Notes: {details.get('Notes', 'N/A')}\n")

def import_contacts():
    pass

def run_program():
    '''Runs Menu Options. Serves as the Main Program.'''
    keep_running = True
    while keep_running:
        print(f"{Fore.GREEN}Menu:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}1.{Style.RESET_ALL} Add a new contact")
        print(f"{Fore.GREEN}2.{Style.RESET_ALL} Edit an existing contact")
        print(f"{Fore.GREEN}3.{Style.RESET_ALL} Delete a contact")
        print(f"{Fore.GREEN}4.{Style.RESET_ALL} Search for a contact")
        print(f"{Fore.GREEN}5.{Style.RESET_ALL} Display all contacts")
        print(f"{Fore.GREEN}6.{Style.RESET_ALL} Export contacts to a text file")
        print(f"{Fore.GREEN}7.{Style.RESET_ALL} Import contacts from a text file *BONUS*")
        print(f"{Fore.GREEN}8.{Style.RESET_ALL} Quit")
        option = int(input(f"{Fore.GREEN}Enter Option Number: {Style.RESET_ALL}"))

        clr()
        try:
            if option == 1:
                add_contact()
            elif option == 2:
                edit_contact()
            elif option == 3:
                delete_contact()
            elif option == 4:
                search_contact()
            elif option == 5:
                display_contacts()
            elif option == 6:
                export_contacts()
            elif option == 7:
                import_contacts()
            elif option == 8:
                clr()
                print("-" * 50)
                print(f"{Fore.GREEN}{outro}{Style.RESET_ALL}")
                keep_running = False
            else:
                clr()
                print("-" * 50)
                print(f"{Fore.RED}Error:{Style.RESET_ALL} Not a valid option. Try again!")
                print("-" * 50)
        except ValueError:
            clr()
            print("-" * 50)
            print(f"{Fore.RED}Error:{Style.RESET_ALL} Enter a number.")
            print("-" * 50)

clr()
print("-" * 50)
print(f"{Fore.GREEN}{intro}{Style.RESET_ALL}")
print(f"{Fore.GREEN}Welcome To The\nContact Management System{Style.RESET_ALL}\n")

run_program()