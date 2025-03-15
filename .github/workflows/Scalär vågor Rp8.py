import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parametrar för RP8
pi = np.pi
sqrt_pi = np.sqrt(pi)
scale_factor = 1.618  # Gyllene snittet

# Funktion för RP8-mönster
def rp8_pattern(x, y, t):
    return np.sin(x * sqrt_pi + t) * np.cos(y * sqrt_pi - t) + \
           np.sin(scale_factor * x - t) * np.cos(scale_factor * y + t)

# Skapa rutnät
size = 300
x = np.linspace(-2 * pi, 2 * pi, size)
y = np.linspace(-2 * pi, 2 * pi, size)
X, Y = np.meshgrid(x, y)

# Initiera figuren
fig, ax = plt.subplots(figsize=(8, 8))
im = ax.imshow(rp8_pattern(X, Y, 0), extent=[-2 * pi, 2 * pi, -2 * pi, 2 * pi], cmap='viridis')
plt.colorbar(im, label='Intensitet')
plt.title("RP8 Harmoniska Mönster - Animation")

# Uppdatera för animation
def update(frame):
    Z = rp8_pattern(X, Y, frame * 0.1)  # Ändra tiden för varje frame
    im.set_array(Z)
    return [im]

# Skapa animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Visa animationen
plt.show()
