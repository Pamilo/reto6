from mrjob.job import MRJob
from mrjob.job import MRStep

class RatingDays(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducerAverageRating),
            MRStep(reducer=self.reducerMinMax)
        ]

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        yield date, float(rating)

    def reducerAverageRating(self, date, ratings):
        ratings_list = list(ratings)
        yield None, (sum(ratings_list) / len(ratings_list), date)

    def reducerMinMax(self, _, date_ratings):
        date_ratings_list = list(date_ratings)
        max_rating = max(date_ratings_list)
        min_rating = min(date_ratings_list)
        yield "Best rating day", max_rating
        yield "Worst rating day", min_rating

if __name__ == '__main__':
    RatingDays.run()