#!/usr/bin/env/python3

import os
import sys
from collections import OrderedDict
from datetime import datetime
from pathlib import Path
from time import sleep

from peewee import DateTimeField, Model, SqliteDatabase, TextField
from colorama import Fore, Style, init

db = SqliteDatabase(f"{Path().absolute()}\\diary\\diary.db")


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.now)

    class Meta:
        database = db


def clear_screen():
    """clear the data on the screen
    """
    os.system("cls" if os.name == "nt" else "clear")


def initialize():
    """Create the database and the table if they don't exist
    """
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show the menu
    """
    choice = None
    while choice != 'q':
        clear_screen()
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print(f"{key}) {value.__doc__.strip()}", end="\n")
        choice = input("\nAction:  ").lower().strip()

        if choice in menu:
            clear_screen()
            menu[choice]()


def add_entry():
    """Add an entry
    """
    print("Enter your entry, Press CTRL-Z when finished.")
    data = sys.stdin.read().strip()
    if data:
        if input('Save entry? [Y/n]  ').lower() != 'n':
            Entry.create(content=data)
            print("Saved successfully!")
            sleep(1)


def view_entries(search_query=None):
    """View previous entries
    """
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime("%A %B %d, %Y %I:%M%p")
        clear_screen()
        print(timestamp)
        print('=' * len(timestamp))
        print(entry.content)
        print('\n')
        print('=' * len(timestamp))
        print('n) for next entry')
        print(f'{Fore.RED}d) {Style.RESET_ALL}delete entry')
        print('q) return to main menu')

        next_action = input('Action: [N/d/q]  ').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)


def search_entries():
    """Search for specific entries
    """
    view_entries(input('Search query:  ').strip())


def delete_entry(entry):
    """Delete an entry

    Parameters
    ----------
    entry : record
        Record to be deleted
    """
    if input("Are you sure? [y/N]  ").lower().strip() == 'y':
        entry.delete_instance()
        print('Entry is deleted!')
        sleep(1)
        # clear_screen()


if __name__ == "__main__":
    init(autoreset=True)
    menu = OrderedDict([
        ('a', add_entry),
        ('v', view_entries),
        ('s', search_entries),
    ])

    initialize()
    menu_loop()
