import peewee

class Contact(peewee.Model):
    first_name = peewee.CharField()
    last_name = peewee.CharField()
    phone_number = peewee.CharField()
    email = peewee.CharField()

    class Meta:
        database = peewee.SqliteDatabase('contacts.db')
