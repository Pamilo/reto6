from mrjob.job import MRJob
from mrjob.job import MRStep

class RatingGenre(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducerGetRatings),
            MRStep(reducer=self.reducerMinMax)
        ]

    def mapper(self, _, line):
        user, movie, rating, genre, date = line.split(',')
        yield genre, (movie, float(rating))

    def reducerGetRatings(self, genre, movie_ratings):
        movie_ratings_list = list(movie_ratings)
        ratings_dict = {}
        for movie, rating in movie_ratings_list:
            if movie in ratings_dict:
                ratings_dict[movie].append(rating)
            else:
                ratings_dict[movie] = [rating]
        for movie, ratings in ratings_dict.items():
            yield genre, (movie, sum(ratings) / len(ratings))

    def reducerMinMax(self, genre, movie_ratings):
        movie_ratings_list = list(movie_ratings)
        max_rating = max(movie_ratings_list, key=lambda x: x[1])
        min_rating = min(movie_ratings_list, key=lambda x: x[1])
        yield genre, ("Best rated", max_rating)
        yield genre, ("Worst rated", min_rating)

if __name__ == '__main__':
    RatingGenre.run()
