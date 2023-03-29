import pygad
import utils
from fitness import calculate_fitness
from population import generate_population

# Define the parameters
population_size = 6
num_generations = 2
num_parents_mating = 2
sol_per_pop = 20
num_genes = len(utils.INPUT_DATA_DICT)
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
    fitness_func=calculate_fitness,
)

# Run the GA
ga_instance.run()

# Print the best solution
solution, solution_fitness, solution_idx = ga_instance.best_solution()
binary_solution = [1 if x >= 0.5 else 0 for x in solution]
ga_instance.plot_fitness()
print("Best solution (binary):", binary_solution)

print(
    "Total value: ",
    sum(
        [
            utils.INPUT_DATA_DICT.get(i).price
            for i in range(len(binary_solution))
            if binary_solution[i] == 1
            and utils.INPUT_DATA_DICT.get(i).price is not None
        ]
    ),
)
print(
    "Total weight: ",
    sum(
        [
            utils.INPUT_DATA_DICT.get(i).weight
            for i in range(len(binary_solution))
            if binary_solution[i] == 1
            and utils.INPUT_DATA_DICT.get(i).weight is not None
        ]
    ),
)

print("Best solution fitness:", solution_fitness)
