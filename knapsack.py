import pygad

# Define the data
weights = [12, 8, 15, 2, 9, 17, 36, 8, 14, 9]
values = [25, 32, 5, 8, 16, 12, 19, 2, 14, 3]
max_weight = 89


# Define the fitness function
def fitness(solution, solution_idx):
    # Calculate the total weight and value of the solution
    total_weight = 0
    total_value = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_weight += weights[i]
            total_value += values[i]
    # Penalize solutions that exceed the maximum weight
    if total_weight > max_weight:
        fitness = -1 * (max_weight - total_weight)
    else:
        # Add a penalty for solutions that do not exceed the maximum weight
        penalty = 0.1 * (total_weight - max_weight)
        fitness = total_value - penalty if penalty <= 0 else penalty
    return fitness


# Define the parameters
num_generations = 2
num_parents_mating = 10
sol_per_pop = 20
num_genes = len(weights)
crossover_probability = 0.8
mutation_probability = 0.1

# Create an instance of the GA class
ga_instance = pygad.GA(
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    crossover_probability=crossover_probability,
    mutation_probability=mutation_probability,
    fitness_func=fitness,
)

# Run the GA
ga_instance.run()

# Print the best solution
solution, solution_fitness, solution_idx = ga_instance.best_solution()
binary_solution = [1 if x >= 0.5 else 0 for x in solution]

print("Best solution (binary):", binary_solution)

print(
    "Total value: ",
    sum([values[i] for i in range(len(binary_solution)) if binary_solution[i] == 1]),
)
print(
    "Total weight: ",
    sum([weights[i] for i in range(len(binary_solution)) if binary_solution[i] == 1]),
)

print("Best solution fitness:", solution_fitness)
