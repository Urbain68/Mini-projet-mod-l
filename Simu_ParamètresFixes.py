import numpy as np
import matplotlib.pyplot as plt

alpha = 2.2
beta = 0.08
gamma = 2.2

rho = 0.08
sigma = 0.22
nu = 0.04

def intraspecies_competition(x_0, y_0, observation):

    # modèle à temps discret du système proie-prédateur
    def new_prey_pop(x_n, y_n):
        return max(0, (alpha + 1)*x_n - beta * x_n * y_n - gamma * x_n**2)
    def new_pred_pop(x_n, y_n):
        return max(0, (1 - rho)*y_n + sigma * x_n * y_n - nu * y_n**2)
    
    # expression des points d'équilibre non nuls du système
    def equilibre():
        y_eq = (sigma*alpha - rho*gamma) / (beta*sigma + nu*gamma)
        x_eq = (alpha - beta*y_eq)/gamma
        return max(0, x_eq), max(0, y_eq)

    x_eq, y_eq = equilibre()
    Prey_eq = [x_eq]*len(observation)
    Pred_eq = [y_eq]*len(observation)

    Prey = [x_0]
    Pred = [y_0]
    for _ in observation[1::]:
        old_pop = Prey[-1], Pred[-1]
        Prey.append(new_prey_pop(old_pop[0], old_pop[1]))
        Pred.append(new_pred_pop(old_pop[0], old_pop[1]))
    
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
    ax1.plot(observation, Prey, "b", label="prey")
    ax1.plot(observation, Pred, "r", label="predator")
    ax1.plot(observation, Prey_eq, color="green", label="prey lim")
    ax1.plot(observation, Pred_eq, color="orange", label="predator lim")
    ax1.set_xlabel("Temps")
    ax1.set_ylabel("Population")
    ax1.legend(fontsize="small")
    ax2.plot(Prey, Pred)
    ax2.set_xlabel("Proies")
    ax2.set_ylabel("Prédateurs")
    ax2.set_title("Portrait de phase")
    plt.show()

    return x_eq, y_eq


print(intraspecies_competition(1.1, 1, [i for i in range(1000)]))