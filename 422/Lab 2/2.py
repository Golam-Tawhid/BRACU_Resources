import random

# Function to generate a random chromosome
def generate_chromosome(N, T):
    chromosome = [random.choice([0, 1]) for _ in range(N * T)]
    return chromosome

# Function to calculate fitness
def calculate_fitness(chromosome, N, T):
    penalty_overlap = 0
    penalty_consistency = 0

    # Calculate overlap penalty
    for t in range(T):
        timeslot = chromosome[t * N:(t + 1) * N]
        penalty_overlap += max(0, sum(timeslot) - 1)

    # Calculate consistency penalty
    for n in range(N):
        course_count = sum(chromosome[n + t * N] for t in range(T))
        penalty_consistency += abs(course_count - 1)

    total_penalty = penalty_overlap + penalty_consistency
    fitness = -total_penalty
    return fitness

# Function to select two parents randomly based on fitness
def select_parents(population, fitnesses):
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    parents = random.choices(population, probabilities, k=2)
    return parents

# Function to perform single-point crossover
def crossover(parent1, parent2, N, T):
    point = random.randint(1, N * T - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Function to perform mutation
def mutate(chromosome, mutation_rate=0.01):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]  # Flip bit
    return chromosome

# Function to run the genetic algorithm
def genetic_algorithm(N, T, course_codes, population_size=100, generations=1000, mutation_rate=0.01):
    # Initialize population
    population = [generate_chromosome(N, T) for _ in range(population_size)]

    for generation in range(generations):
        fitnesses = [calculate_fitness(chromosome, N, T) for chromosome in population]

        # Check for the best fitness
        best_fitness = max(fitnesses)
        best_chromosome = population[fitnesses.index(best_fitness)]

        # Print the best chromosome and its fitness in the current generation
        print(f"Generation {generation}: Best Fitness = {best_fitness}")

        # Selection and Crossover
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population, fitnesses)
            child1, child2 = crossover(parent1, parent2, N, T)
            new_population.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])

        population = new_population[:population_size]

    return best_chromosome, best_fitness

# Sample Input
N = 3
T = 3
course_codes = ["CSE110", "MAT110", "PHY112"]

# Run the genetic algorithm
best_chromosome, best_fitness = genetic_algorithm(N, T, course_codes)

# Print the result
print("Best Chromosome:", "".join(map(str, best_chromosome)))
print("Best Fitness:", best_fitness)
