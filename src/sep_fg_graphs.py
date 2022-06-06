
# Run this code first to see what this plot looks like
# This plot corresponds to Figures 24-26 of the Paper

# list of locations on x-axis for each errorbar (CHANGE THIS)
locL = [0, 1, 2, 2.825, 3.175, 3.825, 4.175, 4.825, 5.175, 5.825, 6.175, 6.825, 7.175]

# list of locations on x-axis for labels (CHANGE THIS)
x_ticksL = [0, 1, 2, 3, 4, 5, 6, 7]
# list of x-axis labels (CHANGE THIS)
x_labelsL = ["A", "B", "C", "D", "E", "F", "G", "H"]

# list of image names (CHANGE THIS)
im_nameL = ["Image 1", "Image 2", "Image 3"]

# list of the color of each errorbar ("." -  means don't connect the errorbars, "k" - represents the color black, "b" - represents the color blue), (CHANGE THIS)
colorL = [".k", ".k", ".k", ".k", ".b", ".k", ".b", ".k", ".b", ".k", ".b", ".k", ".b"]

# list of markers for each errorbar for the most likely value ("rx" - red x, "ro" - red o), (CHANGE THIS)
markerL = ["rx", "rx", "rx", "rx", "ro", "rx", "ro", "rx", "ro", "rx", "ro", "rx", "ro"]

# list the f and f error bars (CHANGE THIS)
# fL = [[f_1, f_2, ...], [...], ...] where f_1, f_2, ... are the f values for one filter band
fL = [[1.0000, 1.9522, 0.7196], [1.0000, 1.8727, 0.7604], [1.0000, 1.3862, 0.9335], [1.0000, 1.0664, 1.2033], [1.0000, 1.0240, 1.0151], [1.0000, 1.5350, 1.0154], [1.0000, 1.2773, 0.9832], [1.0000, 1.5185, 0.7845], [1.0000, 1.4305, 0.7386], [1.0000, 1.6813, 0.7604], [1.0000, 1.4230, 0.7662], [1.0000, 2.0257, 0.8816], [1.0000, 1.4774, 0.8894]]
ferrL = [[0.0000, 2.5274, 0.1555], [0.0000, 1.2105, 0.1209], [0.0000, 0.9163, 0.2780], [0.0000, 0.7954, 2.8832], [0.0000, 0.3103, 0.7566], [0.0000, 2.8381, 0.3939], [0.0000, 0.5357, 0.2670], [0.0000, 0.3127, 0.0889], [0.0000, 0.2535, 0.0714], [0.0000, 0.4377, 0.0900], [0.0000, 0.2532, 0.0780], [0.0000, 6.4108, 0.2545], [0.0000, 0.8520, 0.1936]]

# list the g_1 and g_1 error bars (L stands for list) (CHANGE THIS)
g1L = [[-0.5345, -2.3362, 0.0840], [-0.5342, -2.1574, 0.0564], [-0.6976, -1.6582, -0.2632], [-0.8521, -1.2995, -0.7091], [-0.7993, -1.3409, -0.4874], [-0.7037, -1.7549, -0.3323], [-0.7469, -1.5254, -0.3522], [-0.6111, -1.8110, 0.0026], [-0.6013, -1.8029, 0.0051], [-0.5530, -1.9990, 0.0661], [-0.6154, -1.7532, -0.0092],[-0.5778, -2.4636, -0.0808], [-0.6512, -1.8574, -0.1559]]
g1errL = [[0.1631, 2.9594, 0.2665], [0.1378, 1.3460, 0.2014], [0.1946, 1.0480, 0.5048], [0.2176, 0.7954, 2.8832], [0.1637, 0.3588, 1.2495], [0.2251, 3.1424, 0.6919], [0.1704, 0.5923, 0.4789], [0.0876, 0.3449, 0.1456], [0.0733, 0.2875, 0.1199], [0.1050, 0.4986, 0.1554], [0.0792, 0.2879, 0.1331], [0.2130, 7.5682, 0.4514], [0.1627, 1.0118, 0.3468]]

# list the g_2 values and g_2 error bars (L stands for list) (CHANGE THIS)
g2L = [[-0.1222, 0.1639, 0.1263], [-0.1549, 0.0358, 0.1048], [-0.0754, 0.0888, 0.0820], [-0.1002, -0.0100, -0.0339], [-0.1550, -0.0181, -0.0128], [-0.0572, 0.1478, 0.0534], [-0.0926, 0.1157, 0.0518], [-0.1015, 0.1760, 0.1335], [-0.1460, 0.1744, 0.1339], [-0.0903, 0.1078, 0.1234], [-0.1253, 0.1073, 0.1247], [-0.1425, 0.1800, 0.0342], [-0.1746, 0.1143, 0.0339]]
g2errL = [[0.0384, 0.5316, 0.0806], [0.0324, 0.2068, 0.0693], [0.0422, 0.2273, 0.1111], [0.0486, 0.1961, 0.9058], [0.0470, 0.1384, 0.3698], [0.0477, 0.6372, 0.1116], [0.0460, 0.2004, 0.1021], [0.0242, 0.1096, 0.0440], [0.0241, 0.1062, 0.0424], [0.0220, 0.0988, 0.0417], [0.0221, 0.0872, 0.0415], [0.0460, 0.2876, 0.0991], [0.0468, 1.5213, 0.1052]]

# most likely value lists  (mL - most likely) (CHANGE THIS)
f_mLL = [[1.0000, 1.7075, 0.6842], [1.0000, 1.6914, 0.7382], [1.0000, 1.2856, 0.8535], [1.0000, 1.0141, 1.0458], [1.0000, 0.9958, 0.9328], [1.0000, 1.3509, 0.9090], [1.0000, 1.2178, 0.9082], [1.0000, 1.4846, 0.7727], [1.0000, 1.4072, 0.7319], [1.0000, 1.6214, 0.7454], [1.0000, 1.3960, 0.7572], [1.0000, 1.5885, 0.8145], [1.0000, 1.3525, 0.8391]]
g1_mLL = [[-0.5163, -2.0513, 0.1479], [-0.5272, -1.9566, 0.0929], [-0.6688, -1.5428, -0.1129], [-0.8204, -1.2410, -0.4217], [-0.7760, -1.3082, -0.3293], [-0.6753, -1.5508, -0.1406], [-0.7217, -1.4576, -0.2131], [-0.6057, -1.7730, 0.0185], [-0.5974, -1.7760, 0.0185], [-0.5456, -1.9298, 0.0924], [-0.6122, -1.7218, 0.0067], [-0.5504, -1.9499, 0.0413], [-0.6291, -1.7096, -0.0628]]
g2_mLL = [[-0.1214, 0.1200, 0.1474], [-0.1536, 0.0145, 0.1202], [ -0.0750, 0.0700, 0.1173], [-0.1001, -0.0209, 0.0274], [-0.1554, -0.0262, 0.0317], [-0.0577, 0.1066, 0.0860], [-0.0933, 0.0990, 0.0826], [-0.1016, 0.1670, 0.1394], [-0.1460, 0.1672, 0.1384], [-0.0901, 0.0989, 0.1310], [-0.1248, 0.1010, 0.1302], [-0.1421, 0.0863, 0.0634], [-0.1731, 0.0793, 0.0616]]

### DO NOT EDIT ANYTHING BELOW THIS LINE ###
################################################################################

# additional setup for reading the test image and displaying plots
import matplotlib.pyplot as plt

# check that all of the inputted lists are of equal size
if (len(locL)!=len(fL)) or (len(locL)!=len(ferrL)) or (len(locL)!=len(g1L)) or (len(locL)!=len(g1errL)) or (len(locL)!=len(g2L)) or (len(locL)!=len(g2errL)) or (len(locL)!=len(f_mLL)) or (len(locL)!=len(g1_mLL)) or (len(locL)!=len(g2_mLL)):
    print("Your locL, fL, ferrL, g1L, g1errL, g2L, g2errL, f_mLL, g1_mLL, g2_mLL are not all of the same size!")
    print(0/0)

# loop through each image
for im in range(len(im_nameL)):
    im_name = im_nameL[im]

    # set up text styling (latex)
    params = {'mathtext.default': 'regular' } 
    plt.rcParams.update(params)

    # set up the figure to graph
    fig, axes = plt.subplots(1, 3, figsize=(10, 5), sharex=False, sharey=False)
    fig.suptitle(im_name)

    # set up the axes and figure
    ax1 = axes[0]
    ax2 = axes[1]
    ax3 = axes[2]

    ax1.set_title("f values")
    ax1.set_xticks(x_ticksL)
    ax1.set_xticklabels(x_labelsL, fontsize = 10)

    ax2.set_title("$g_1$ values")
    ax2.set_xticks(x_ticksL)
    ax2.set_xticklabels(x_labelsL, fontsize = 10)

    ax3.set_title("$g_2$ values")
    ax3.set_xticks(x_ticksL)
    ax3.set_xticklabels(x_labelsL, fontsize = 10)

    ax1.tick_params(axis='y', labelsize= 8)
    ax2.tick_params(axis='y', labelsize= 8)
    ax3.tick_params(axis='y', labelsize= 8)
    
    # loop through each filter
    for i in range(len(locL)):
        # get the location value
        loc = locL[i]

        # get the f, g1, and g2 values for the plot
        f = fL[i][im]
        fvar = ferrL[i][im]
        g1 = g1L[i][im]
        gvar1 = g1errL[i][im]
        g2 = g2L[i][im]
        gvar2 = g2errL[i][im]

        col = colorL[i]
        # plot data + errorbars for f values
        ax1.errorbar(loc, f, yerr = fvar, fmt=col, capsize = 3)

        # plot data + errorbars for g1 values
        ax2.errorbar(loc, g1, yerr = gvar1, fmt=col, capsize = 3)

        # plot data + errorbars for g2 values
        ax3.errorbar(loc, g2, yerr = gvar2, fmt=col, capsize = 3)

        # get the most likely values
        f_mL = f_mLL[i][im]
        g1_mL = g1_mLL[i][im]
        g2_mL = g2_mLL[i][im]

        # mark the most likely value for each errorbar
        mark = markerL[i]
        ax1.plot(loc, f_mL, mark, fillstyle = "none")
        ax2.plot(loc, g1_mL, mark, fillstyle = "none",)
        ax3.plot(loc, g2_mL, mark, fillstyle = "none",)

    plt.show()

