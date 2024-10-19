import os
import re
from colorama import Fore, Back, Style
from art import intro, outro

contact_dict = {}

number_pattern = r"[\d]{3}-[\d]{3}-[\d]{4}"
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
            print("To add a new contact enter the following:")

            contact_number = input("Enter phone number: ex: xxx-xxx-xxxx\n")
            if not re.match(name_pattern, contact_number):
                print("Invalid Number. Try again. ex: xxx-xxx-xxxx")
                continue

            contact_name = input("Enter full name: ex: John Doe\n")
            if not re.match(name_pattern, contact_name):
                print("Invalid Name. Try again. ex: John Doe")
                continue

            contact_email = input("Enter email: ex: john_doe@gmail.com\n")
            if not re.match(email_pattern, contact_email):
                print("Invalid Email. Try again. ex: john_doe@gmail.com")
                continue

            contact_notes = input("Enter Notes:\n")

            keep_running = False
        except Exception as e:
            clr()
            print("-" * 50)
            print(f"Error: {e}")
            

def edit_contact():
    pass

def delete_contact():
    pass

def search_contact():
    pass

def display_contacts():
    pass

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
print(f"{Fore.GREEN}Welcome to the Contact Management System{Style.RESET_ALL}\n")

run_program()