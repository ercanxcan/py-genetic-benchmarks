# encoding: utf-8

"""
     Ercan Can
     Genetic algoritmasi
"""
import functions

__author__ = "ercanc"

# imports
import random

# classes
class Genetic(object):
    def __init__(self, population=None, pop_size=100, maxgenerations=100, crossover_rate=0.90, mutation_rate=0.01, fitnes_function=None):
        self.individual = Individual
        self.size = pop_size
        self.fitnes_function = fitnes_function
        self.population = population or self.create_population()

        for individual in self.population:
            individual.minimum_function(self.fitnes_function)

        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.maxgenerations = maxgenerations
        self.generation = 0
        self.print_ga()

    def create_population(self):
        return [self.individual() for individual in range(self.size)]

    def execute(self):
        while not self.goal():
            self.step()

    def goal(self):
        return self.generation > self.maxgenerations

    def step(self):
        self.population.sort()
        self.crossover()
        self.generation += 1
        self.print_ga()

    def crossover(self):
        next_population = [self.best.copy()]
        while len(next_population) < self.size:
            select1 = self.selection()
            if random.random() < self.crossover_rate:
                select2 = self.selection()
                tmp_select = select1.crossover(select2)
            else:
                tmp_select = [select1.copy()]
            for individual in tmp_select:
                self.mutation(individual)
                individual.minimum_function(self.fitnes_function)
                next_population.append(individual)
        self.population = next_population[:self.size]

    def selection(self):
        return self.tournament()

    def mutation(self, individual):
        for gen in range(individual.genes):
            if random.random() < self.mutation_rate:
                individual.mutate(gen)

    # size turnuvaya gire  birey sayısı,
    def tournament(self, size=8, elitism_rate=0.90):
        competitors = [random.choice(self.population) for i in range(size)]
        competitors.sort()
        if random.random() < elitism_rate:
            return competitors[0]
        else:
            return random.choice(competitors[1:])

    def best():
        def fget(self):
            return self.population[0]

        return locals()

    best = property(**best())

    def print_ga(self):
        print "=" * 150
        print "GENERATION : ", self.generation
        print "BEST       : ", self.best


class Individual(object):
    oneorzero = (0, 1)
    genes = 30
    seperator = ''

    def __init__(self, chromosome=None):
        self.chromosome = chromosome or self.create_chromosome()
        self.score = None

    def create_chromosome(self):
        return [random.choice(self.oneorzero) for gen in range(self.genes)]

    def minimum_function(self, fitnes_function):
        if fitnes_function == 'rosenbrock':
            self.score = functions.fitness_rosenbrock(self.chromosome)
        elif fitnes_function == 'rastrigin':
            self.score = functions.fitness_rastrigin(self.chromosome)
        elif fitnes_function == 'schwefel':
            self.score = functions.fitness_schwefel(self.chromosome)
        else:
            self.score = sum(self.chromosome)

    def crossover(self, other):
        return self.make_crossover(other)

    def mutate(self, gen):
        self.chromosome[gen] = not self.chromosome[gen]  # bit flip

        # sample mutation method

    def pick(self, gen):
        self.chromosome[gen] = random.choice(self.oneorzero)

    def make_crossover(self, other):
        left, right = self.make_rand_for_crossover()

        def select(p0, p1):
            chromosome = p0.chromosome[:]
            chromosome[left:right] = p1.chromosome[left:right]
            child = p0.__class__(chromosome)
            return child

        return select(self, other), select(other, self)


    def make_rand_for_crossover(self):
        left = random.randrange(1, self.genes - 2)
        right = random.randrange(left, self.genes - 1)
        return left, right

    def __repr__(self):
        return 'Individual_="%s" score=%s' % \
               (self.seperator.join(map(str, self.chromosome)), self.score)

    def __cmp__(self, other):
        return cmp(self.score, other.score)

    def copy(self):
        twin = self.__class__(self.chromosome[:])
        twin.score = self.score
        return twin

# genetic = Genetic(min='rosenbrock', maxgenerations=10, pop_size=100, crossover_rate=0.95, mutation_rate=0.01)
# genetic = Genetic(min='rastrigin',maxgenerations=10,pop_size=100, crossover_rate=0.90, mutation_rate=0.01)
genetic = Genetic(fitnes_function='schwefel',maxgenerations=50, pop_size=100, crossover_rate=0.0, mutation_rate=0.001)
genetic.execute()