
# This example is for Images 1,2,3,4,5 of CL0024

# get the fits info using the relative path of the FITS file
filename = "hst_10325_c7_acs_wfc_f475w_drz.fits"

# Image names (e.g. Image A, Image B, Image C)
imL = ["Image 1", "Image 2", "Image 3", "Image 4", "Image 5"]

# row and column lists (we suggest a 128x128 image)
# e.g. rowL = [(r0,r1)] where r0 is the lower row and r1 is the higher row of each image
rowL = [(1637, 1765), (1765, 1893), (2149, 2277), (2405, 2533), (2149, 2277)]
colL = [(1535, 1663), (1407, 1535), (1279, 1407), (2283, 2411), (2057, 2185)]

# backgound patch paramters (we suggest a 64x64 bkg patch)
# e.g. bkg_rowL = [(br0,br1)] where br0 is the lower row and br1 is the higher row of each image and are a 'width' apart (br1 - br0 = width)
width = 64
bkg_rowL = [(1701, 1765), (1765, 1829), (2213, 2277), (2405, 2469), (2213, 2277)]
bkg_colL = [(1599, 1663), (1471, 1535), (1279, 1343), (2283, 2347), (2121, 2185)]

# OPTIONAL - color limit for each image (set True if you want to manually set the color limit otherwise set False)
clim_bool = True
climL = [(0.03,0.182), (0.038,0.13), (0.038,0.16), (0.03,0.195), (0.035,0.155)]

# Do you want to outline the background patch in the image? (True - Yes, False - No)
bkg_bool = True

### DO NOT EDIT ANYTHING BELOW THIS LINE ###
################################################################################

# import needed packages (Download these first if you haven't done so)
import numpy as np
import sep
import astropy.io.fits as pyfits
import matplotlib.pyplot as plt

# check that the imL, rowL, colL, bkg_rowL, bkg_colL, and climL are all the same length
if (len(imL)!=len(rowL)) or (len(imL)!=len(colL)) or (len(imL)!=len(bkg_rowL)) or (len(imL)!=len(bkg_colL)) or (len(imL)!=len(climL) and clim_bool):
    print("Your imL, rowL, colL, bkg_rowL, bkg_colL, and climL are not all the same length!")
    print(0/0)

# open up the fits file
hdul = pyfits.open(filename)

# create lists to hold the bkg and rms value
bkgL = []
rmsL = []

# go through each image
for i in range(len(imL)):

    # get the row and column from the list
    (r0,r1) = rowL[i]
    (c0,c1) = colL[i]
    data = hdul[1].data[r0:r1, c0:c1]
    data = np.ascontiguousarray(data, dtype=np.float32)

    # set up the figure and plot
    fig, ax = plt.subplots()
    plt.imshow(data, cmap='gray', origin='lower')

    im = imL[i]
    plt.title(im)

    # get the background information
    (br0,br1) = bkg_rowL[i]
    (bc0,bc1) = bkg_colL[i]
    bkg_data = hdul[1].data[br0:br1, bc0:bc1]
    bkg_data = np.ascontiguousarray(bkg_data, dtype=np.float32)

    # have to check that the background patch has the same size as the width
    if ((br1-br0 == width) and (bc1-bc0 == width)):
        bkg = sep.Background(bkg_data, bw = width, bh = width)
        bkg_image = bkg.back()
        bkg_rms = bkg.rms()

        # print the background values and add them to their corresponding lists
        print()
        print(im)
        print(bkg.globalback)
        print(bkg.globalrms)
        bkgL += [bkg.globalback]
        rmsL += [bkg.globalrms]
    else:
        print("Your difference in your background lists are not a 'width' apart.")

    # outline the background patch in the image  
    if bkg_bool:
        plt.vlines(bc0 - c0, br0 - r0, br1 - r0 - 1, color = "r", linewidths = 0.75)
        plt.vlines(bc1 - c0 - 1, br0 - r0, br1 - r0 - 1, color = "r", linewidths = 0.75)
        plt.hlines(br0 - r0, bc0 - c0, bc1 - c0 - 1, color = "r", linewidths = 0.75)
        plt.hlines(br1 - r0 - 1, bc0 - c0, bc1 - c0 - 1, color = "r", linewidths = 0.75)

    # optional manual color limits
    if clim_bool:
        (clim0, clim1) = climL[i]
        plt.clim(clim0,clim1)
    
    plt.colorbar()
    plt.show()

# print the background and rms lists used in the sep_graphs_area.py, sep_graphs_location.py, sep_location_3D.py, sep_view.py
print()
print("bkgL = ")
print(bkgL)
print("rmsL = ")
print(rmsL)
