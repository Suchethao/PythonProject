import peewee
from database import Contact
import argparse

parser = argparse.ArgumentParser(description='Contact Book')
subparsers = parser.add_subparsers(dest='command')

add_parser = subparsers.add_parser('add', help='Add a new contact')
add_parser.add_argument('first_name', type=str, help='First name')
add_parser.add_argument('last_name', type=str, help='Last name')
add_parser.add_argument('phone_number', type=str, help='Phone number')
add_parser.add_argument('email', type=str, help='Email')

list_parser = subparsers.add_parser('list', help='List all contacts')

find_parser = subparsers.add_parser('find', help='Find a contact by first name')
find_parser.add_argument('first_name', type=str, help='First name')

args = parser.parse_args()

if args.command == 'add':
    new_contact = Contact(
        first_name=args.first_name,
        last_name=args.last_name,
        phone_number=args.phone_number,
        email=args.email
    )
    new_contact.save()
    print('Contact added successfully.')

elif args.command == 'list':
    contacts = Contact.select()
    for contact in contacts:
        print(f'{contact.first_name} {contact.last_name} ({contact.phone_number}, {contact.email})')

elif args.command == 'find':
    contact = Contact.get(Contact.first_name == args.first_name)
    print(f'{contact.first_name} {contact.last_name} ({contact.phone_number}, {contact.email})')
