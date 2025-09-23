import numpy as np
import matplotlib.pyplot as pl

h = np.array([147, 150, 153, 155, 158, 160, 163, 165, 168, 170, 173, 175, 178, 180, 183])
w = np.array([49, 50, 51, 52, 54, 56, 58, 59, 60, 72, 63, 64, 66, 67, 68])


pl.plot(h, w, 'go-')
pl.xlabel('Chiều cao (cm)')
pl.ylabel('Cân nặng (kg)')
pl.title('Biểu đồ chiều cao – cân nặng')
pl.show()

