import random

def generatingRandomChromosome(numberOfCourses, totalTimeSlots):
    generatedChromosome = [random.choice([0, 1]) for a in range(numberOfCourses * totalTimeSlots)]
    return generatedChromosome

def calculatingFitness(chromosome, numberOfCourses, totalTimeSlots):
    penaltyOfOverlap = 0
    penaltyOfConsistency = 0

    for times in range(totalTimeSlots):
        timeslot = chromosome[times * numberOfCourses:(times + 1) * numberOfCourses]
        penaltyOfOverlap += max(0, sum(timeslot) - 1)

    for num in range(numberOfCourses):
        totalCourseCount = sum(chromosome[num + times * numberOfCourses] for times in range(totalTimeSlots))
        penaltyOfConsistency += abs(totalCourseCount - 1)

    totalCalculatedPenalty = penaltyOfOverlap + penaltyOfConsistency
    CalculatedFitness = -totalCalculatedPenalty
    return CalculatedFitness

def selectingRandomParents(generatedInitialPopulation, fitnessofInitialPopulation):
    totalFitness = sum(fitnessofInitialPopulation)
    probabilities = [o / totalFitness for o in fitnessofInitialPopulation]
    selectedParents = random.choices(generatedInitialPopulation, probabilities, k=2)
    return selectedParents

def crossoverFunction(selectedParent1, selectedParent2, numberOfCourses, totalTimeSlots):
    selectedRamdomPoint = random.randint(1, numberOfCourses * totalTimeSlots - 1)
    firstChild = selectedParent1[:selectedRamdomPoint] + selectedParent2[selectedRamdomPoint:]
    secondChild = selectedParent2[:selectedRamdomPoint] + selectedParent1[selectedRamdomPoint:]
    return firstChild, secondChild

def mutate(chromosome):
    rateOfMutation=0.01
    for s in range(len(chromosome)):
        if random.random() < rateOfMutation:
            chromosome[s] = 1 - chromosome[s]
    return chromosome

def twoPointCrossOver(firstSelectedParent, secondSelectedParent):
    numberOfCourses = len(firstSelectedParent)
    point1, point2 = sorted(random.sample(range(1, numberOfCourses), 2))
    
    child1 = firstSelectedParent[:point1] + secondSelectedParent[point1:point2] + firstSelectedParent[point2:]
    child2 = secondSelectedParent[:point1] + firstSelectedParent[point1:point2] + secondSelectedParent[point2:]
    
    return child1, child2

def genetic_algorithm(numberOfCourses, totalTimeSlots, numberOfInitialPopulation, totalGenerations, generatedInitialPopulation):
    
    for generation in range(totalGenerations):
        fitnessofInitialPopulation = [calculatingFitness(chromosome, numberOfCourses, totalTimeSlots) for chromosome in generatedInitialPopulation]

        bestFitness = max(fitnessofInitialPopulation)
        bestChromosome = generatedInitialPopulation[fitnessofInitialPopulation.index(bestFitness)]

        newPopulation = []
        while len(newPopulation) < numberOfInitialPopulation:
            selectedParent1, selectedParent2 = selectingRandomParents(generatedInitialPopulation, fitnessofInitialPopulation)
            firstChild, secondChild = crossoverFunction(selectedParent1, selectedParent2, numberOfCourses, totalTimeSlots)
            newPopulation.extend([mutate(firstChild), mutate(secondChild)])

        generatedInitialPopulation = newPopulation[:numberOfInitialPopulation]

    return bestChromosome, bestFitness

with open('Assignment 2\input.txt', 'r') as file:
    numberOfCourses, totalTimeSlots = map(int, file.readline().strip().split())

numberOfInitialPopulation=10
totalGenerations=1000
generatedInitialPopulation = [generatingRandomChromosome(numberOfCourses, totalTimeSlots) for q in range(numberOfInitialPopulation)]
bestChromosome, bestFitness = genetic_algorithm(numberOfCourses, totalTimeSlots, numberOfInitialPopulation, totalGenerations, generatedInitialPopulation)

print("Best Chromosome:", "".join(map(str, bestChromosome)))
print("Best Fitness:", bestFitness)


firstSelectedParent, secondSelectedParent = random.sample(generatedInitialPopulation, 2)

child1, child2 = twoPointCrossOver(firstSelectedParent, secondSelectedParent)

print("Parent 1: ", "".join(map(str, firstSelectedParent)))
print("Parent 2: ", "".join(map(str, secondSelectedParent)))
print("Child 1:  ", "".join(map(str, child1)))
print("Child 2:  ", "".join(map(str, child2)))