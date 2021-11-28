from scipy.ndimage import morphology
import matplotlib.pyplot as plt
import numpy as np

image, quantity, masks = np.load('ps.npy'), 0, np.array([[[1,1,1,1],
    [1,1,1,1],
    [1,1,0,0],
    [1,1,0,0],
    [1,1,1,1],
    [1,1,1,1]],

    [[1,1,1,1],
    [1,1,1,1],
    [0,0,1,1],
    [0,0,1,1],
    [1,1,1,1],
    [1,1,1,1]],
    
    [[1,1,0,0,1,1],
    [1,1,0,0,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]],
    
    [[1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,0,0,1,1],
    [1,1,0,0,1,1]],
    
    [[1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]]], dtype=object)

for i in masks:
    quantity += np.sum(morphology.binary_hit_or_miss(image, i))
print("Количество объектов на изображении: ", quantity)
plt.figure()
plt.imshow(image, cmap="gray")
plt.show()