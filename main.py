import pygad
import utils
from fitness import calculate_fitness
from population import generate_population

# Define the parameters
population_size = 20
num_generations = 10
num_parents_mating = 2
num_genes = utils.CHROMOSOME_COUNT
crossover_probability = 0.8
mutation_probability = 0.1

# Create an instance of the GA class
ga_instance = pygad.GA(
    initial_population=generate_population(population_size),
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    num_genes=num_genes,
    parent_selection_type="rws",
    crossover_type="two_points",
    mutation_type="scramble",
    crossover_probability=crossover_probability,
    mutation_probability=mutation_probability,
    fitness_func=calculate_fitness,
    save_solutions=True
)

if __name__ == "__main__":
    # Run the GA
    # print(f'Generation num {ga_instance.num_generations},\n Initial Pop: {ga_instance.initial_population}')
    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    # print(f'Result pop {ga_instance.population}')

    # Binary solution otherwise as a result we are going to get float vector values
    binary_solution = [1 if x >= 0.5 else 0 for x in solution]

    # Print the best solution
    print(f"Best binary solution: {binary_solution}")
    print("Fitness score:", solution_fitness)

    # list comprehension to sum value of all items
    total_items_value = sum(
        [
            utils.INPUT_DATA_DICT.get(i).price
            for i in range(len(binary_solution))
            if binary_solution[i] == 1
               and utils.INPUT_DATA_DICT.get(i).price is not None
        ]
    )
    print(f"Total value of items: {total_items_value}")

    # list comprehension to sum total weight of all items
    total_weight_value = sum(
        [
            utils.INPUT_DATA_DICT.get(i).weight
            for i in range(len(binary_solution))
            if binary_solution[i] == 1
               and utils.INPUT_DATA_DICT.get(i).weight is not None
        ]
    )
    print(f"Total weigth of items: {total_weight_value}")

    # Generate plot for visualization
    # ga_instance.plot_fitness(save_dir=f"results/Generation{GENERATIONS}")
    # Prepare for nextgen
    ga_instance.plot_fitness(save_dir=f"Generation-Fitness")
    ga_instance.plot_genes(save_dir="Genes", plot_type="bar")
