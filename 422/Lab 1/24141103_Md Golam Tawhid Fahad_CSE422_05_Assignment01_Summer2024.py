import heapq

input_txt_file = open("Input file.txt", "r")

def organizing_heuristic_values(input_txt_file):
    self_heuristic_vlaues = {}
    neighbor_heuristic_values = {}
    temporary_heuristic_holder = {}

    for ith_line in input_txt_file:
        listOfConnectedCities = ith_line.strip().split()

        self_heuristic_vlaues[listOfConnectedCities[0]] = int(listOfConnectedCities[1])

        for neighbor_city_index in range(2, len(listOfConnectedCities), 2):
            temporary_heuristic_holder[listOfConnectedCities[neighbor_city_index]] = int(listOfConnectedCities[neighbor_city_index+1])

        neighbor_heuristic_values[listOfConnectedCities[0]] = temporary_heuristic_holder
        temporary_heuristic_holder = {}

    return (self_heuristic_vlaues, neighbor_heuristic_values)

def aStarSearchAlgo(starting_city, destination_city, neighbor_heuristic_values, self_heuristic_values):
    listOfVisitedCities = []
    heapq.heappush(listOfVisitedCities, (0, starting_city))
    optimized_final_path = {}
    travel_cost = {}
    optimized_final_path[starting_city] = None
    travel_cost[starting_city] = 0

    while listOfVisitedCities:
        current_visiting_city = heapq.heappop(listOfVisitedCities)[1]

        if current_visiting_city == destination_city:
            break

        for ith_neighbor_city in neighbor_heuristic_values[current_visiting_city]:
            new_travel_cost = travel_cost[current_visiting_city] + neighbor_heuristic_values[current_visiting_city][ith_neighbor_city]
            if ith_neighbor_city not in travel_cost or new_travel_cost < travel_cost[ith_neighbor_city]:
                travel_cost[ith_neighbor_city] = new_travel_cost
                priority = new_travel_cost + self_heuristic_values[ith_neighbor_city]
                heapq.heappush(listOfVisitedCities, (priority, ith_neighbor_city))
                optimized_final_path[ith_neighbor_city] = current_visiting_city

    return optimized_final_path, travel_cost

def generatingOutput(optimized_final_path, travel_cost, starting_city, destination_city):
    current_visiting_city = destination_city
    final_path = []

    while current_visiting_city is not starting_city:
        final_path.append(current_visiting_city)
        new_city = optimized_final_path[current_visiting_city]
        current_visiting_city = new_city

    final_path.append(starting_city)

    if len(final_path) == 1:
        return "NO PATH FOUND"
    else:
        final_path =  final_path[::-1]
        print("Path: ", end = "")
        print(*final_path, sep = " --> ")

    print(f"Total distance: {travel_cost[destination_city]} km.")

starting_city = input("Enter Start node: ")
destination_city = input("Enter Destination: ")

self_heuristic_vlaues, neighbor_heuristic_values = organizing_heuristic_values(input_txt_file)

if starting_city in self_heuristic_vlaues and destination_city in self_heuristic_vlaues:
    optimized_final_path, travel_cost = aStarSearchAlgo(starting_city, destination_city, neighbor_heuristic_values, self_heuristic_vlaues)
    generatingOutput(optimized_final_path, travel_cost, starting_city, destination_city)
else:
    print("Star or destination city do not exist.")