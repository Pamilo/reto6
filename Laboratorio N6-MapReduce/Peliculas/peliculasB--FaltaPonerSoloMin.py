from mrjob.job import MRJob

class DayWithLeastMovies(MRJob):

    def mapper(self, _, line):
        user, movie, rating, genre,date = line.split(',')
        yield date, 1

    def reducer(self, date, values):
        # Find the date with the most movies
        count= sum(values)

        yield date, count  # Yield date with most movies and its count

if __name__ == '__main__':
    DayWithLeastMovies.run()
