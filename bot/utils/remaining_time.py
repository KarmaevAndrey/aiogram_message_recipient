from datetime import datetime


def remaining_time(input_datetime):
    try:
        input_date, input_time = input_datetime.split(' ')
        input_date = datetime.strptime(input_date, '%d.%m.%Y')
        input_time = datetime.strptime(input_time, '%H.%M')
        current_datetime = datetime.now()
        input_full_datetime = datetime(input_date.year, input_date.month, input_date.day,
                                       input_time.hour, input_time.minute)
        time_difference = input_full_datetime - current_datetime
        if time_difference.total_seconds() > 0:
            days = time_difference.days
            hours, remainder = divmod(time_difference.seconds, 3600)
            minutes, _ = divmod(remainder, 60)
            result = (days, hours, minutes)
            return [True, result]
        else:
            return [False]
    except ValueError:
        return "Ошибка в формате даты или времени."
