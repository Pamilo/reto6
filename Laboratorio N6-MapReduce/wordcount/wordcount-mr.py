from mrjob.job import MRJob
from mrjob.job import MRStep

class MRWordFrequencyCount(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]


    def mapper(self, _, line):
#       for w in line.decode('utf-8', 'ignore').split():
        for w in line.split():
            yield w,1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MRWordFrequencyCount.run()
