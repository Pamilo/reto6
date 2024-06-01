from mrjob.job import MRJob
from mrjob.step import MRStep

class BlackDay(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        yield company, (float(price), date)

    def reducerMinPrice(self, company, values):
        min_price_date = min(values)
        yield min_price_date[1], 1

    def reducerBlackDayDate(self, date, counts):
        yield "Black Day", (sum(counts), date)

    def reducerBlackDayData(self, _, date_counts):
        max_black_day = max(date_counts)
        yield "# of companies and day", max_black_day

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducerMinPrice),
            MRStep(reducer=self.reducerBlackDayDate),
            MRStep(reducer=self.reducerBlackDayData)
        ]

if __name__ == '__main__':
    BlackDay.run()