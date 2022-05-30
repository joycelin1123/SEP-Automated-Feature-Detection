
# Run this code first to see what this plot looks like
# This plot corresponds to Figures 30-33 of the Paper

# list of locations on x-axis for each errorbar 
locL = [0, 1, 2, 3, 4, 5, 6, 7]

# list of locations on x-axis for labels 
# I set this equal to locL because each label corresponded directly to each errorbar
x_axisL = locL
# list of x-axis labels 
x_ticksL = ["A", "B", "C", "D", "E", "F", "G", "H"]

# list of image names 
im_nameL = ["Image 1", "Image 2", "Image 3", "Image 4", "Image 5"]

# list of the color of each errorbar ("." -  means don't connect the errorbars, "k" - represents the color black)
colorL = [".k", ".k", ".k", ".k", ".k", ".k", ".k", ".k"]

# list j values (should have the same length as locL, jerrL, j_mLL)
# jL = [[j_1, j_2, ...], [...], ...] where j_1, j_2, ... are the j values in each sublist for just one filter band
jL = [[1.0000, -0.4171, 0.7167, -0.7285, 0.1930], [1.0000, -0.4309, 0.7012, -0.7281, 0.1766], [1.0000, -0.4117, 0.7264, -0.7032, 0.1816], [1.0000, -0.4367, 0.7245, -0.7727, 0.1890], [1.0000, -0.4349, 0.6959, -0.7404, 0.1760], [1.0000, -0.3982, 0.6959, -0.6878, 0.1476], [1.0000, -0.3911, 0.7222, -0.7115, 0.1692], [1.0000, -0.4123, 0.6812, -0.6722, 0.1810]]

# list j errorbars
jerrL = [[0.0000, 0.0463, 0.0611, 0.0724, 0.0317], [0.0000, 0.0386, 0.0495, 0.0595, 0.0266], [0.0000, 0.0458, 0.0636, 0.0723, 0.0293], [0.0000, 0.0475, 0.0641, 0.0762, 0.0323], [0.0000, 0.0463, 0.0611, 0.0720, 0.0320], [0.0000, 0.0434, 0.0612, 0.0714, 0.0280], [0.0000, 0.0445, 0.0616, 0.0726, 0.0315], [0.0000, 0.0454, 0.0584, 0.0718, 0.0313]]

# list the most likely value j values
j_mLL = [[1.0000, -0.4186, 0.7153, -0.7293, 0.1932], [1.0000, -0.4308, 0.7002, -0.7279, 0.1774], [1.0000, -0.4130, 0.7256, -0.7031, 0.1824], [1.0000, -0.4384, 0.7237, -0.7735, 0.1898], [1.0000, -0.4354, 0.6944, -0.7416, 0.1770], [1.0000, -0.3996, 0.6948, -0.6895, 0.1480], [1.0000, -0.3923, 0.7199, -0.7120, 0.1704], [1.0000, -0.4134, 0.6798, -0.6724, 0.1823]]

### DO NOT EDIT ANYTHING BELOW THIS LINE ###
################################################################################

# additional setup for reading the test image and displaying plots
import matplotlib.pyplot as plt

# check that locL, colorL, jL, jerrL, j_mLL are all the same length
if (len(locL)!=len(jL)) or (len(locL)!=len(colorL)) or (len(locL)!=len(jerrL)) or (len(locL)!=len(j_mLL)):
    print("Your locL, jL, jerrL, and j_mLL lists are not all the same length!")
    print(0/0)

# loop through every image
for im in range(len(im_nameL)):

    # get the image name
    im_name = im_nameL[im]

    # set up plot
    plt.figure(figsize = (5,5))
    plt.title(im_name + ": $\mathcal{J}$ values")

    # loop through each filter band
    for f in range(len(locL)):

        # get the corresponding location on the x-axis
        loc = locL[f]

        # get the value for the corresponding filter
        j = jL[f]
        jerr = jerrL[f]
        col = colorL[f]

        # set up text styling (latex)
        params = {'mathtext.default': 'regular' } 
        plt.rcParams.update(params)

        # plot data + errorbars for f values
        plt.errorbar(loc, j[im], yerr = jerr[im], fmt=col, capsize = 3)

        # plot the most likely values
        j_mL = j_mLL[f]
        plt.plot(loc, j_mL[im], "r*", fillstyle = "none")

    # plot the xticks and then show 
    plt.xticks(locL, x_ticksL, fontsize = 10)
    plt.show()
