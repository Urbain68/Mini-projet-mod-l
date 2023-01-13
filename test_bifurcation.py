import numpy as np
import matplotlib.pyplot as plt


alpha = 0.05
beta = 0.08
gamma = 0.05

rho = 0.08
sigma = 0.08
nu = 0.04

def new_prey_pop(alpha, x_n, y_n):
    return x_n + (alpha*x_n - beta * np.multiply(x_n, y_n) - alpha*np.multiply(x_n, x_n))
def new_pred_pop(alpha, x_n, y_n):
    return y_n + (-rho*y_n + 0.1*alpha* np.multiply(x_n, y_n) - nu * np.multiply(y_n, y_n))


n = 10000
r = np.linspace(1, 3, n)

iterations = 1000
last = 100

x = 1.1 * np.ones(n)
y = 1 * np.ones(n)

fig, (ax1, ax2) = plt.subplots(1, 2,
                               sharey=False)
for i in range(iterations):
    x = new_prey_pop(r, x, y)
    y = new_pred_pop(r, x, y)
    # We display the bifurcation diagram.
    if i >= (iterations - last):
        ax1.plot(r, x, ',k', alpha=.25)
        ax2.plot(r, y, ',k', alpha=.25)
ax1.set_xlabel(f"$\\alpha \in [1, 3]$")
ax2.set_xlabel(f"$\\alpha \in [1, 3]$")
ax1.set_title("Analyse pour les proies (x_n)")
ax2.set_title("Analyse pour les prédateurs (y_n)")
plt.xlim(1, 3)
fig.suptitle("Diagramme de bifurcation")
plt.show()