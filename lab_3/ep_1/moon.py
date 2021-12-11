import numpy as np
from PIL import Image

# считаем картинку в numpy array
for i in range(1, 4):
    img = Image.open('lunar0' + str(i) + '_raw.jpg')
    data = np.array(img)

    min_st = np.min(data)
    max_st = np.max(data)
    k = 255 / (max_st - min_st)
    b = 255 - max_st * k

    updated_data = data * k + b

    # запись картинки после обработки
    res_img = Image.fromarray(updated_data)
    if res_img.mode != 'RGB':
        res_img = res_img.convert('RGB')
    res_img.save('lunar1' + str(i) + '_raw.png')
    res_img.save('lunar2' + str(i) + '_raw.jpg')
