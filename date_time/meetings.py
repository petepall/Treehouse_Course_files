from datetime import datetime
import pytz
import random


def create_timezone_list():
    time_zone_list = []
    for _ in range(6):
        time_zone_list.append(pytz.timezone(random.choice(pytz.all_timezones)))

    return time_zone_list


if __name__ == "__main__":
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'

    while True:
        date_input = input(f"When is your meeting? "
                           f"Please use MM/DD/YYYY HH:MM format: ")
        try:
            local_date = datetime.strptime(date_input, '%m/%d/%Y %H:%M')
        except ValueError:
            print(f"{date_input} doesn't seem to be a valid date and time!")
        else:
            local_date = pytz.timezone('US/Pacific').localize(local_date)
            utc_date = local_date.astimezone(pytz.utc)

            output = []
            for timezone in create_timezone_list():
                output.append(utc_date.astimezone(timezone))
            for appointment in output:
                print(appointment.strftime(fmt))
