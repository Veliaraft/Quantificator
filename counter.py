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

    [[1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
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

def type_of_mask(j):
    stringa = ''
    for n in j[::2]:
        stringa += str(n[::2]).replace('[', '').replace(']', '').replace(', ', '')
        stringa += '\n'
    return stringa

for i in masks:
    result = np.sum(morphology.binary_hit_or_miss(image, i))
    print('Объекты типа: \n', type_of_mask(i), 'Их количество = ', result, sep = '', end = '\n\n')
    quantity += result
print("Количество объектов на изображении: ", quantity)

plt.figure()
plt.imshow(image, cmap="gray")
plt.show()