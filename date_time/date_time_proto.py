import datetime


# treehouse_start = datetime.datetime.now()
# print(treehouse_start)

# treehouse_start = treehouse_start.replace(hour=9, minute=0, second=0,
#                                           microsecond=0)
# print(treehouse_start)
# time_worked = datetime.datetime.now() - treehouse_start
# print(time_worked)

# hours_worked = round(time_worked.seconds / 3600)
# print(hours_worked)

# now = datetime.datetime.now()
# print(now)
# now += datetime.timedelta(days=3)
# print(now)
# print(datetime.timedelta(minutes=-5))

# def far_away(time_difference):
#     return datetime.datetime.now() + time_difference

# print(far_away(datetime.timedelta(minutes=-10)))

# def minutes(date1, date2):
#     # difference = date2 - date1
#     return round(datetime.timedelta.total_seconds(date2-date1) / 60)


# date1 = datetime.datetime.now()
# date2 = datetime.datetime.now()

# date1 = date1.replace(hour=22, minute=0, second=0)
# date2 = date2.replace(hour=22, minute=15, second=0)

# print(minutes(date1, date2))

# now = datetime.datetime(2014, 10, 15, 20, 11, 45, 410327)

# print(now.strftime('%m/%d/%y'))

# birthday = datetime.datetime.strptime('2015-04-21', '%Y-%m-%d')
# print(birthday)

# birthday_party = datetime.datetime.strptime('2015-04-21 12:00',
#                                             '%Y-%m-%d %H:%M')
# print(birthday_party)

# def to_string(data):
#     return data.strftime('%d %B %Y')


# def from_string(data, formating):
#     return datetime.datetime.strptime(data, formating)


# now = datetime.datetime(2019, 5, 30, 19, 11, 45, 410327)
# print(to_string(now))

# now = datetime.datetime.now()
# formating = "%Y-%m-%d %H:%M:%S.%f"
# print(from_string(str(now), formating))

def time_tango(given_date, given_time):
    return datetime.datetime.combine(given_date, given_time)


date1 = datetime.date(2019, 5, 30)
time1 = datetime.time(20, 0, 0)
print(time_tango(date1, time1))
