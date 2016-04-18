import datetime

with open('date.txt', 'r') as f:
    INPUT = [s.strip() for s in f.readlines()]


if __name__ == '__main__':
    for row in INPUT:
        data_set = [int(d) for d in row.split('/')]
        year, month, date = [None] * 3

        if max(data_set) >= 2000:
            year = max(data_set)

        possibly_month = [d for d in data_set if 0 < d <= 12]
        if len(possibly_month) == 3:
            year, month, date = sorted(possibly_month)
            year += 2000
        elif len(possibly_month) == 2:
            if min(data_set) == 0 or max(data_set) > 31:
                month, date = sorted(possibly_month)
                del data_set[data_set.index(month)]
                del data_set[data_set.index(date)]
                year = data_set[0] if data_set[0] >= 2000 else 2000 + data_set[0]
            else:
                year, month = sorted(possibly_month)
                del data_set[data_set.index(month)]
                del data_set[data_set.index(year)]
                year += 2000
                date = data_set[0]
        elif len(possibly_month) == 1:
            if max(data_set) >= 2000:
                year = max(data_set)
                del data_set[data_set.index(year)]
            month = possibly_month[0]
            del data_set[data_set.index(month)]
            for digit in data_set:
                if digit == 0 or digit > 31:
                    year = digit
                else:
                    if year:
                        if year:
                            if year == 0 or year > 31:
                                date = digit
                            else:
                                date = year
                                year = digit
                        else:
                            date = digit
                    else:
                        if date:
                            if date < digit:
                                year = date
                                date = digit
                            else:
                                year = digit
                        else:
                            date = digit
            year = year + 2000 if year < 2000 else year

        # Check is this date is a valid date
        try:
            full_date = datetime.datetime(year, month, date)
            print('{} => {}'.format(row, full_date.strftime('%Y-%m-%d')))
        except ValueError:
            print('{} is illegal'.format(row))
