import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

# Dati
terms = ["Biosfera Terrestre", "Effetto Serra", "Correnti Oceaniche", "Atmosfera", "Irraggiamento Solare", "Calore Interno"]
colors = ["#66b3b3", "#99cc99", "#cce0ff", "#ffcc66", "#ffcc99", "#ff6666"]
positions = [
    (0, 0),     # Biosfera Terrestre (centro)
    (6, 3),     # Effetto Serra
    (6, -3),    # Correnti Oceaniche
    (-6, 3),    # Atmosfera
    (-6, -3),   # Irraggiamento Solare
    (0, 5)      # Calore Interno
]

circle_radius = 2  # Raggio aumentato per cerchi più grandi

# Creazione della figura
fig, ax = plt.subplots(figsize=(16, 10))

# Funzione per disegnare frecce bidirezionali dai bordi dei cerchi
def draw_bidirectional_arrow(ax, start, end, radius):
    # Calcolo del vettore direzione
    vector = np.array(end) - np.array(start)
    unit_vector = vector / np.linalg.norm(vector)

    # Calcolo dei punti di partenza e arrivo sui bordi dei cerchi
    start_edge = np.array(start) + unit_vector * radius
    end_edge = np.array(end) - unit_vector * radius

    # Disegno della freccia bidirezionale
    arrowprops = dict(arrowstyle="<->", color="black", lw=2)
    arrow = FancyArrowPatch(start_edge, end_edge, connectionstyle="arc3,rad=0.1", **arrowprops)
    ax.add_patch(arrow)

# Disegno delle frecce prima dei cerchi
for i in range(1, len(positions)):
    draw_bidirectional_arrow(ax, positions[0], positions[i], circle_radius)

# Disegno dei cerchi sopra le frecce
for term, color, pos in zip(terms, colors, positions):
    circle = plt.Circle(pos, circle_radius, color=color, zorder=2)  # zorder per mettere i cerchi sopra
    ax.add_artist(circle)
    ax.text(pos[0], pos[1], term, ha="center", va="center", fontsize=14, color="black", zorder=3, wrap=True)

# Impostazioni grafiche
ax.set_xlim(-12, 12)
ax.set_ylim(-7, 7)
ax.set_aspect("equal")
ax.axis("off")

# Salvataggio come immagine con sfondo trasparente
plt.savefig("diagramma_biosfera_trasparente.png", bbox_inches="tight", dpi=300, transparent=True)

# Mostrare il grafico
plt.show()
