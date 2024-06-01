from mrjob.job import MRJob
from mrjob.step import MRStep

class MinPriceByDate(MRJob):

    def mapper(self, _, line):
        company, price, date = line.strip().split(",")
        price = float(price)
        yield company, (price, date)

    def reducer(self, company, price_dates):
        min_price = min(price for price, _ in price_dates)
        for price, date in price_dates:
            if price == min_price:
                yield date, 1

    def reducer_count_dates(self, date, counts):
        # Get the final count for each date
        yield None, (date, sum(counts))

    def reducer_find_max(self, _, dates_with_counts):
        # Find the date with the most companies at minimum price
        max_count = max(count for _, count in dates_with_counts)
        for date, count in dates_with_counts:
            if count == max_count:
                yield "Date with Most Minimum Prices:", date

if __name__ == "__main__":
    MinPriceByDate.run()