#! /usr/bin/python

# See README.txt for information and build instructions.

import addressbook_pb2
import sys

# Iterates though all people in the AddressBook and prints info about them.
def ListPeople(address_book):
  for person in address_book.person:
    print "Person ID:", person.id
    print "  Name:", person.name
    if person.HasField('email'):
      print "  E-mail address:", person.email

    for phone_number in person.phone:
      if phone_number.type == addressbook_pb2.Person.MOBILE:
        print "  Mobile phone #:",
      elif phone_number.type == addressbook_pb2.Person.HOME:
        print "  Home phone #:",
      elif phone_number.type == addressbook_pb2.Person.WORK:
        print "  Work phone #:",
      print phone_number.number

# Main procedure:  Reads the entire address book from a file and prints all
#   the information inside.
filename = raw_input("Please input the filename:")
address_book = addressbook_pb2.AddressBook()

# Read the existing address book.
f = open(filename, "rb")
address_book.ParseFromString(f.read())
f.close()

ListPeople(address_book)