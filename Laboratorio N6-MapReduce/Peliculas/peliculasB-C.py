from mrjob.job import MRJob
from mrjob.job import MRStep

class WatchingsPerDay(MRJob):


    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducerAverage),
            MRStep(reducer=self.reducerMinMax)
        ]

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        yield date, 1

    def reducerAverage(self, date, counts):
        yield None, (sum(counts), date)

    def reducerMinMax(self, _, date_counts):
        dates = list(date_counts)
        max_day = max(dates)
        min_day = min(dates)
        #yield "Min and Max Dates"
        yield "Max day", max_day
        yield "Min day", min_day


if __name__ == '__main__':
    WatchingsPerDay.run()