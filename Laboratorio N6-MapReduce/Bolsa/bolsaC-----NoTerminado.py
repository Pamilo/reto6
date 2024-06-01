from mrjob.job import MRJob

class diaDesplome(MRJob):
    def mapper(self,_,line):
        company, price, date = line.strip().split(',')
        yield company, (float(price), date)

    def reducer(self, company, values):
        min_price = float('inf')
        max_price = float('-inf')
        date_min = None
        date_max = None
        countDate = {}
        blackDate = ""
        for price, date in values:
            countDate[date]=0
            if price < min_price:
                countDate[date]+=1
            if countDate[date] == max(countDate):
                blackDate = date
        yield "Black Day:", blackDate







if __name__ == '__main__':
    diaDesplome.run()