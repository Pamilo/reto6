from mrjob.job import MRJob

class MovimientoDeAcciones(MRJob):
    def mapper(self, _,line):
        company, price, date = line.strip().split(',')
        yield(company, (price, date))

    def reducer(self, company, values):
        prev_price = None
        healthyMovement = True

        for price, date in values:
            if prev_price is not None and price < prev_price:
                healthyMovement = False
                break

            prev_price = price

        yield company, healthyMovement

if __name__ == '__main__':
    MovimientoDeAcciones.run()