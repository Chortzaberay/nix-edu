
from datetime import datetime

def get_maxday(month):
    d = [31, 28, 31,
         30, 31, 30,
         31, 31, 30,
         31, 30, 31]

    return d[month]


def gmt_time(gmt):
    time_ = datetime.utcnow()
    flag = False

    hr = time_.hour + gmt
    if hr > time_.max.hour:
        time_ = time_.replace(hour = hr - 24)
        flag = True
    else:
        time_ = time_.replace(hour = hr)

    if flag:
        maxday = get_maxday(time_.month)
        day_ = time_.day + 1

        if day_ > maxday:
            time_ = time_.replace(day = 1)
            flag = True
        else:
            time_ = time_.replace(day = day_)
            flag = False

    if flag:
        if time_.month + 1 > 12:
            time_ = time_.replace(month = 1, year = time_.year + 1)
        else:
            time_ = time_.replace(month = time_.month + 1)

    return time_.strftime("[%H:%M:%S] - %d, %B of %Y")
