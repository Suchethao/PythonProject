# Import the necessary libraries
from peewee import *

# Connect to the database
db = PostgresqlDatabase(
    'contacts',
    user='',
    password='',
    host='localhost',
    port=8000)
db.connect()

# Define the database model
class BaseModel(Model):
    class Meta:
        database = db

# Define the ContactBook model
class ContactBook(BaseModel):
    id = AutoField()
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    phone = IntegerField()

# Drop the ContactBook table if it already exists, then create a new table
# db.drop_tables([ContactBook])
db.create_tables([ContactBook])

# Add a new contact to the ContactBook table
def create_contact():
    create = True
    while create:
        first_name = input('What is the first name? ')
        last_name = input('What is the last name? ')
        email = input('Enter an email address: ')
        phone = int(input('Enter a phone number: '))
        new_contact = ContactBook(
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            phone=phone)
        new_contact.save()
        print('----------////----------')
        user_input = str(input('Would you like to add another contact? (yes/no) '))
        if user_input.lower() == 'yes':
            create = True
        else:
            create = False
            break

# List all contacts in the ContactBook table
def list_all_contacts():
    list_all = ContactBook.select()
    print('All contacts: ')
    for contact in list_all:
        print('----------////----------')
        print(
            f'First Name: {contact.first_name}\nLast Name: {contact.last_name}\nEmail: {contact.email}\nPhone: {contact.phone}\n')

# Find a contact in the ContactBook table by first name
def list_one_contact():
    search_contact = input('Enter the first name: ').lower()
    try:
        list_one = ContactBook.get(ContactBook.first_name == search_contact)
        print('----------////----------')
        print(
            f'First Name: {list_one.first_name}\nLast Name: {list_one.last_name}\nEmail: {list_one.email}\nPhone Number: {list_one.phone}\n')
    except ContactBook.DoesNotExist:
        print('No contact found with the given first name.')

# Update a contact in the ContactBook table by ID
def update_contact():
    update = True
    while update:
        contact_id = input('Enter contact ID to update a contact: ')
        try:
            update_contact = ContactBook.get(ContactBook.id == contact_id)
            print('----------////----------')
            print(
                f'This is the contact you want to update:\nFirst Name: {update_contact.first_name}\nLast Name: {update_contact.last_name}\nEmail: {update_contact.email}\nPhone Number: {update_contact.phone}')
            print('----------////----------')
            user_input = str(input('What would you like to update? First Name(f), Last Name(l), Email(e), Phone(p), All(a), or Quit(q)...'))
            if user_input.lower() == 'f':
                new_first_name = str(input('Enter the first name: '))
                update_contact.first_name = new_first_name
            elif user_input.lower() == 'l':
                new_last_name = str(input('Enter the last name: '))
                update_contact.last_name = new_last_name
            elif user_input.lower() == 'e':
                new_email = str(input('Enter
