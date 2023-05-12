import pickle


def generate_population(length):
    def generate(prefix, remaining):
        if prefix.count(0) >= length - 2:
            return
        if len(prefix) == length:
            population.append(prefix)
            return
        for i in range(3):
            new_prefix = prefix + [i]
            new_remaining = remaining - 1
            generate(new_prefix, new_remaining)

    population = []
    generate([], length)
    return population

p = generate_population(6)

with open('../file_ignore/population.pickle', 'wb') as f:
    pickle.dump(p, f)
