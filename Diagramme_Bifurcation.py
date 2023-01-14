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
# plt.show()





# Vérification des conditions de stabilité : 
alpha_lim = 2.2  # obtenu par lecture graphique donc avec incertitude
beta_lim = 0.08
gamma_lim = alpha_lim
rho_lim = 0.08
sigma_lim = 0.1*alpha_lim
nu_lim = 0.04

# Calcul des points d'équilibre pour les paramètres donnés :
y_star = (sigma_lim*alpha_lim - rho_lim*gamma_lim)/(beta_lim*sigma_lim + nu_lim*gamma_lim)
x_star = (alpha_lim - beta_lim*y_star)/gamma_lim
print("Point d'équilibre :")
print("x*=",x_star,", y*=", y_star)

# Coefficient de la jacobienne : J(x*, y*) = [[a1, a2], [a3, a4]]
a1 = 1 + alpha_lim - beta_lim*y_star - 2*gamma_lim*x_star
a2 = - beta_lim*x_star
a3 = sigma_lim*y_star
a4 = 1 - rho_lim + sigma_lim*x_star + 2*nu_lim*y_star
print("Coefficients de la matrice jacobienne au point d'équilibre :")
print("J(x*, y*) =")
print("[ [", a1, "  ", a2, "]\n","  [", a3, "  ", a4, "] ]")

# Coefficients du polynôme caractéristique de la jacobienne : chi(X) = X^2 + b1*X + b2
b1 = - (a1 + a4)
b2 = a1*a4 - a2*a3
print("Polynôme caractéristique de la jacobienne :")
print(f"X^2 + {b1}*X + {b2}")

# Critère de Jury pour des polynômes d'ordre 2 :
cond1 = b2 + b1 + 1
cond2 = b2 - b1 + 1
cond3 = abs(b2) - 1
print("Valeurs des conditions du critère de Jury pour des polynômes de degré 2 :")
print("Valeur de la condition 1 :",cond1)
if cond1 > 0:
    print("Condition vérifiée")
else:
    print("Condition NON vérifiée")

print("Valeur de la condition 2 :",cond2)
if cond2 > 0:
    print("Condition vérifiée")
else:
    print("Condition NON vérifiée")

print("Valeur de la condition 3 :",cond3)
if cond3 < 0:
    print("Condition vérifiée")
else:
    print("Condition NON vérifiée")

# Variante : avec numpy pour obtenir l'expression des valeurs propres de la matrice :
J_star = np.array([[a1, a2], [a3, a4]])
print("Liste des valeurs propres de la matrice linéarisée tangente \n au point critique (obtenu avec numpy.linalg.eigvals) :")
print(np.linalg.eigvals(J_star))