import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2, 2, 100)
y1 = x**2
y2 = x**3
plt.plot(x, y1, color='blue', label='$y = x^2$')
plt.plot(x, y2, color='red', label='$y = x^3$')
plt.title('Do thi ham so')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()