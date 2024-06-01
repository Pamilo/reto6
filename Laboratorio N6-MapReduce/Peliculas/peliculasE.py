from mrjob.job import MRJob

class MovieRatings(MRJob):

    def mapper(self, _, line):
        # Extract user ID, movie rating, and genre
        user_id, movie, rating, genre, date = line.split(',')
        # Emit key-value pair: (user_id, (movie_rating, genre))
        yield date, (user_id,rating)

    def reducer(self, date, user_ratings):
        total_rating = 0
        movie_count = 0
        max_rating = 0
        max_date = ''
        dateCounts = {}
        # Calculate total rating and movie count
        for user_id, rating in user_ratings:
            total_rating += int(rating)
            movie_count += 1
        # Calculate average rating
        average_rating = total_rating / movie_count

        dateCounts[date] = average_rating
        if dateCounts[date] > max_rating:
            max_rating = average_rating
            max_date = date

        yield max_date, max_rating

if __name__ == '__main__':
    MovieRatings.run()