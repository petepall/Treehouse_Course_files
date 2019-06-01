import datetime
import pytz


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

# def time_tango(given_date, given_time):
#     return datetime.datetime.combine(given_date, given_time)


# date1 = datetime.date(2019, 5, 30)
# time1 = datetime.time(20, 0, 0)
# print(time_tango(date1, time1))

# starter = datetime.datetime(2015, 10, 21, 16, 29)


# def delorean(leap_ahead_hours):
#     global starter
#     starter += datetime.timedelta(hours=leap_ahead_hours)
#     return starter


# print(delorean(2))

# Remember, you can't set "years" on a timedelta!
# Consider a year to be 365 days.

# Example
# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)
# starter = datetime.datetime(2015, 10, 21, 16, 29)


# def time_machine(time_diff, time_type):
#     global starter
#     result = 0

#     if time_type.lower() == 'years':
#         result = starter + datetime.timedelta(days=time_diff * 365)
#     if time_type.lower() == 'days':
#         result = starter + datetime.timedelta(days=time_diff)
#     if time_type.lower() == 'hours':
#         result = starter + datetime.timedelta(hours=time_diff)
#     if time_type.lower() == 'minutes':
#         result = starter + datetime.timedelta(minutes=time_diff)
#     if time_type.lower() == 'seconds':
#         result = starter + datetime.timedelta(seconds=time_diff)
#     return result


# print(time_machine(5, 'minutes'))

# def timestamp_oldest(*args):
#     # posix = []
#     # for item in args:
#     #     posix.append(item)

#     # posix.sort()
#     posix = [item for item in args]
#     posix.sort()
#     return datetime.datetime.fromtimestamp(posix[0])


# timestamp = 1545730073, 1545720073, 1545730078, 1345730073
# print(timestamp_oldest(1545730073, 1545720073, 1545730078, 1345730073))

# pacific = datetime.timezone(datetime.timedelta(hours=-8))
# eastern = datetime.timezone(datetime.timedelta(hours=-5))

# naive = datetime.datetime(2014, 4, 21, 9)
# print(naive)

# aware = datetime.datetime(2014, 4, 21, 9, tzinfo=pacific)
# print(aware)
# print(aware.astimezone(eastern))


# pacific = pytz.timezone('US/Pacific')
# eastern = pytz.timezone('US/Eastern')

# format = '%Y-%m-%d %H:%M:%S %Z%z'

# utc = pytz.utc

# start = pacific.localize(datetime.datetime(2014, 4, 21, 9, 0))
# print(start.strftime(format))

# start_eastern = start.astimezone(eastern)
# print(start_eastern.strftime(format))

# start_utc = datetime.datetime(2014, 4, 21, 1, tzinfo=utc)
# print(start_utc.strftime(format))

# start_pacific = start_utc.astimezone(pacific)
# print(start_pacific.strftime(format))

# auckland = pytz.timezone('Pacific/Auckland')
# mumbai = pytz.timezone('Asia/Calcutta')

# apollo_13_naive = datetime.datetime(1970, 4, 11, 14, 13)
# print(apollo_13_naive.strftime(format))

# apollo_13_eastern = eastern.localize(apollo_13_naive)
# print(apollo_13_eastern.strftime(format))

# apollo_13_utc = apollo_13_eastern.astimezone(utc)
# print(apollo_13_utc.strftime(format))
# print(apollo_13_utc.astimezone(auckland).strftime(format))

# for item in pytz.all_timezones:
#     print(item)

# print(pytz.country_timezones['be'])


# fmt = '%m-%d %H:%M %Z%z'
# starter = datetime.datetime(2015, 10, 21, 4, 29)
# pacific = pytz.timezone('US/Pacific')
# local = pacific.localize(starter)
# print(local)

