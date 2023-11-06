def define_bee():
    import numpy as np

    # make an empty numpy array for storing the image
    image_mat = np.full((16, 16, 3), 1.0)

    # define some colours
    black = [0, 0, 0]
    yellow = [1.0, 0.85, 0]
    grey = [0.65] * 3

    # specify which pixels are which colour
    image_mat[7:11, 2] = black
    image_mat[6:12, 3:5] = black
    image_mat[6:12, 5:7] = yellow
    image_mat[6:12, 7:9] = black
    image_mat[6:12, 9:11] = yellow
    image_mat[6:12, 11:13] = black
    image_mat[7:11, 13] = black
    image_mat[4:6, 5:11] = grey
    image_mat[3, 6:10] = grey

    return image_mat

def define_bee_pink():
    import numpy as np

    # make an empty numpy array for storing the image
    image_mat = np.full((16, 16, 3), 1.0)

    # define some colours
    grey = [0.65] * 3
    pink = [1,0,1]
    pink_diff = [1,0.85,1]


    # specify which pixels are which colour
    image_mat[7:11, 2] = pink
    image_mat[6:12, 3:5] = pink
    image_mat[6:12, 5:7] = pink_diff
    image_mat[6:12, 7:9] = pink
    image_mat[6:12, 9:11] = pink_diff
    image_mat[6:12, 11:13] = pink
    image_mat[7:11, 13] = pink
    image_mat[4:6, 5:11] = grey
    image_mat[3, 6:10] = grey
    
    return image_mat
    
def define_butterfly():
    import numpy as np

    # make an empty numpy array for storing the image
    image_mat = np.full((16, 16, 3), 1.0)

    # define some colours
    pink = [1, 0, 1]
    different_pink = [1, 0.85, 1]

    # specify which pixels are which colour
    c = 8
    # centre of butterfly
    image_mat[2:13, c] = pink
    
    # generate mirror image at the same time
    for i in [-1, 1]:
        # outline
        image_mat[1, i*1+c] = pink
        image_mat[0, i*2+c] = pink
        image_mat[4, i*1+c] = pink
        image_mat[3, [i*j+c for j in [2, 3]]] = pink
        image_mat[2, [i*j+c for j in [4, 5]]] = pink
        image_mat[3, i*6+c] = pink
        image_mat[4:7, i*7+c] = pink
        image_mat[7, [i*j+c for j in [6, 5]]] = pink
        image_mat[8, [i*j+c for j in [4, 3, 2]]] = pink
        image_mat[7, i*1+c] = pink
        image_mat[9, i*5+c] = pink
        image_mat[10:12, i*6+c] = pink
        image_mat[12, i*5+c] = pink
        image_mat[13, [i*j+c for j in [4, 3]]] = pink
        image_mat[12, i*2+c] = pink
        image_mat[11, i*1+c] = pink
        
        # fill in the centre line by line
        image_mat[3, [i*j+c for j in [4, 5]]] = different_pink
        image_mat[4, [i*j+c for j in range(2,7)]] = different_pink
        image_mat[5:7, [i*j+c for j in range(1,7)]] = different_pink
        image_mat[7, [i*j+c for j in range(2,5)]] = different_pink
        image_mat[8, i*1+c] = different_pink
        image_mat[9, [i*j+c for j in range(1,5)]] = different_pink
        image_mat[10, [i*j+c for j in range(1,6)]] = different_pink
        image_mat[11, [i*j+c for j in range(2,6)]] = different_pink
        image_mat[12, [i*j+c for j in range(3,5)]] = different_pink
    
    return image_mat



def plot_image(image):
    import matplotlib.pyplot as plt

    plt.axis('off')
    plt.imshow(image)
    plt.show()
    

bee = define_bee()
plot_image(bee)
barbee = define_bee_pink()
plot_image(barbee)
butterfly = define_butterfly()
plot_image(butterfly)
