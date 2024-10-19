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
    pass

def delete_contact():
    pass

def search_contact():
    pass

def display_contacts():
    for index, (contact_num, contact_details) in enumerate(contact_dict.items()):
        print(f"{Fore.GREEN}{index + 1} - Title:{Style.RESET_ALL} {contact_details['Title']}")
        print(f"{Fore.GREEN}Name:{Style.RESET_ALL} {contact_details['Name']}")
        print(f"{Fore.GREEN}Phone Number:{Style.RESET_ALL} {contact_num}")
        print(f"{Fore.GREEN}Email:{Style.RESET_ALL} {contact_details['Email']}")
        print(f"{Fore.GREEN}Notes:{Style.RESET_ALL} {contact_details['Notes']}")
        print("-" * 50)

def export_contacts():
    pass

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