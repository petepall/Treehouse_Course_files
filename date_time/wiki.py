import datetime


answer_format = "%m/%d"
link_format = "%b_%d"
link = "https://en.wikipedia.org/wiki/{}"

while True:
    answer = input(f"What date would you like? "
                   f"Please use the MM/DD format. Enter 'quit'to exit: ")
    if answer.upper() == 'QUIT':
        break

    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        print(output)
    except ValueError:
        print("That's not a valid date, please try again.")
