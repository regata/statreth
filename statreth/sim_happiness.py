import numpy as np
import pandas as pd

__all__ = ["sim_happiness"]

# Automatically converted by ChatGPT3 with some tweaks.
# https://github.com/rmcelreath/rethinking/blob/ac1b3b2cda83f3e14096e2d997a6e30ad109eeee/R/sim_happiness.R
def sim_happiness(seed=1977, N_years=1000, max_age=65, N_births=20, aom=18):
    # Set random seed
    np.random.seed(seed)

    # Initialize lists for ages, happiness, and marriage status
    A = []  # Ages of individuals
    H = []  # Happiness of individuals
    M = []  # Marriage status of individuals (0 = not married, 1 = married)

    for t in range(N_years):
        # Increment the age of existing individuals
        A = [age + 1 for age in A]

        # Add new births
        A.extend([1] * N_births)

        # Add happiness for newborns (uniform distribution from -2 to 2)
        H.extend(np.linspace(-2, 2, N_births))

        # Add marriage status for newborns (0 = not married)
        M.extend([0] * N_births)

        # Try to get married for each individual who is over the age of maturity (aom) and not married
        for i in range(len(A)):
            if A[i] >= aom and M[i] == 0:
                # Simulate marriage with Bernoulli distribution (based on happiness)
                prob_marriage = 1 / (1 + np.exp(-(H[i] - 4)))  # Logistic function
                M[i] = np.random.binomial(1, prob_marriage)

        # Remove individuals older than max_age (mortality)
        deaths = set((i for i, age in enumerate(A) if age > max_age))
        if deaths:
            A = [age for i, age in enumerate(A) if i not in deaths]
            H = [happiness for i, happiness in enumerate(H) if i not in deaths]
            M = [marriage for i, marriage in enumerate(M) if i not in deaths]

    # Create a DataFrame to return the results
    df = pd.DataFrame({"age": A, "married": M, "happiness": H})

    return df