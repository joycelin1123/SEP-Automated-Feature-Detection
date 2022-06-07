
# Run this code first to see what this plot looks like
# Required to run sep_bkg_rms.py first to obtain the bkgL and rmsL
# The first plot corresponds to Figure 6 of the Paper

# get the fits info using the relative path of the FITS file
filename = "data/hst_data/CL0024_data/hst_10325_c7_acs_wfc_f475w_drz.fits"

# Image names (e.g. Image A, Image B, Image C)
imL = ["Image 1", "Image 2", "Image 3", "Image 4", "Image 5"]

# row and column lists (we suggest a 128x128 image)
# e.g. rowL = [(r0,r1)] where r0 is the lower row and r1 is the higher row of each image
rowL = [(1637, 1765), (1765, 1893), (2149, 2277), (2405, 2533), (2149, 2277)]
colL = [(1535, 1663), (1407, 1535), (1279, 1407), (2283, 2411), (2057, 2185)]

# background and rms lists calculated using sep_bkg_rms.py
bkgL = [0.04627720266580582, 0.046375613659620285, 0.04566671699285507, 0.04507363587617874, 0.04775523394346237]
rmsL = [0.00323042762465775, 0.0031234666239470243, 0.003028792329132557, 0.0035166656598448753, 0.0033184518106281757]

# set lower and upper bound for n (what we refer to as signal strength, n_I, in the paper)
n_Lower = 5
n_Upper = 20
incr = 1
# deblend_num is by default 0.005
deblend_num = 0.005

### DO NOT EDIT ANYTHING BELOW THIS LINE ###
################################################################################

import numpy as np
import sep
import astropy.io.fits as pyfits
import matplotlib.pyplot as plt

# check that imL, rowL, colL, bkgL, rmsL, and climL are all the same length
if (len(rowL)!=len(colL)) or (len(rowL)!=len(bkgL)) or (len(rowL)!=len(rmsL)) or (len(rowL)!=len(imL)):
    print("Your imL, rowL, colL, bkg_rowL, and bkg_colL are not all the same length!")
    print(0/0)

# open up the fits file
hdul = pyfits.open(filename)

# loop through each image
for num in range (len(imL)):

    # get the info for the current image
    im = imL[num]
    (y0,y1) = rowL[num]
    (x0,x1) = colL[num]
    rows = y1 - y0
    cols = x1 - x0

    # get the data from fits data
    data = hdul[1].data[y0:y1, x0:x1]
    data = np.ascontiguousarray(data, dtype=np.float32)

    # create an array using the corresponding background value
    bkg_val = bkgL[num]
    bkg = np.full((rows,cols), bkg_val)

    # subtract the background
    data_sub = data - bkg

    # create empty dictionaries and lists
    # d keeps track of all of the areas
    d = dict()
    # dsig keeps track of all of the sigma values that the point occurs in
    dsig = dict()
    # this list is to keep track of all of the points so that we can use the dictionaries later
    pointList = []

    # get number of steps (+1 to include the upper limit)
    steps = int((n_Upper - n_Lower)/incr) + 1

    # loop through each sigma
    for step in range(steps):
        # get the corresponding sigma to the step
        n = n_Lower + (step*incr)
        objects = sep.extract(data_sub, n, err=rmsL[num], clean = False, deblend_cont = deblend_num)

        # loop through all of the objects and add them to the dictionaries
        for i in range(len(objects)):

            # get the xpeak pixel and ypeak pixel
            xpeak = objects['xpeak'][i]
            ypeak = objects['ypeak'][i]
            point = (xpeak, ypeak)

            # calculate the area to insert into dictionary
            area = round(np.pi*objects['b'][i]*objects['a'][i]*4, 2)

            # if point is already in dictionary, add new area point to both dictionaries
            if (point in d):
                d[point] += [area]
                dsig[point] += [n]
            # else add newpoint to pointList and add it to both dictionaries
            else: 
                pointList +=[point]
                d[point] = [area]
                dsig[point] = [n]

    # plot all of the points in the dictionary
    for p in range(len(pointList)):
        point = pointList[p]
        plt.plot(dsig[point], d[point],"o-" , label=point)

    # set up styling of text
    params = {'mathtext.default': 'regular' } 
    plt.rcParams.update(params)

    # plot the data and show titles, axes labels, etc.
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1))
    plt.title(im)
    plt.ylabel("$Area~[px]$")
    plt.xlabel("$n_I$")
    plt.show()
