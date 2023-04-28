contacts = [    {        'first_name': 'John',        'last_name': 'Doe',        'phone_number': '555-555-5555',        'email': 'john.doe@example.com'    },    {        'first_name': 'Jane',        'last_name': 'Doe',        'phone_number': '555-555-1234',        'email': 'jane.doe@example.com'    }]

for contact in contacts:
    new_contact = Contact(
        first_name=contact['first_name'],
        last_name=contact['last_name'],
        phone_number=contact['phone_number'],
        email=contact['email']
    )
    new_contact.save()
