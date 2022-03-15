import requests


class HolidayDateService:
    @staticmethod
    def get_date(year, holidayName):
        result = requests.get(
            f"https://date.nager.at/api/v3/PublicHolidays/{year}/PL").json()

        for x in result:
            if x['localName'] == holidayName:
                return x['date']

    def SearchingHolidayDates(selectedHoliday, yearFrom, yearTo):
        datesTable = []
        for x in range(yearFrom, yearTo+1):
            date = HolidayDateService.get_date(yearFrom, selectedHoliday)
            datesTable.append(date)
            yearFrom += 1
        return datesTable
