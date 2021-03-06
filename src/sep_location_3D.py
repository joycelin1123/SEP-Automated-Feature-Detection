
# Run this code first to see what this plot looks like and what is outputted in the terminal
# Required to run sep_bkg_rms.py first to obtain the bkgL and rmsL

# get the fits info using the relative path of the FITS file
filename = "data/hst_10325_c7_acs_wfc_f475w_drz.fits"

# list of image names 
imL = ["Image 1", "Image 2", "Image 3", "Image 4", "Image 5"]

# row and column lists (we suggest a 128x128 image)
# e.g. rowL = [(r0,r1)] where r0 is the lower row and r1 is the higher row of each image
rowL = [(1637, 1765), (1765, 1893), (2149, 2277), (2405, 2533), (2149, 2277)]
colL = [(1535, 1663), (1407, 1535), (1279, 1407), (2283, 2411), (2057, 2185)]

# background and rms lists calculated using sep_bkg_rms.py
bkgL = [0.04627720266580582, 0.046375613659620285, 0.04566671699285507, 0.04507363587617874, 0.04775523394346237]
rmsL = [0.00323042762465775, 0.0031234666239470243, 0.003028792329132557, 0.0035166656598448753, 0.0033184518106281757]

# set lower and upper bound for sigma
sgmLower = 3
sgmUpper = 20
incr = 1.0
deblend_num = 0.005

### DO NOT EDIT ANYTHING BELOW THIS LINE ###
################################################################################

import numpy as np
import sep
import astropy.io.fits as pyfits
import matplotlib.pyplot as plt

# check that imL, rowL, colL, bkgL, and rmsL are all the same length
if (len(imL)!=len(rowL)) or (len(imL)!=len(colL)) or (len(imL)!=len(bkgL)) or (len(imL)!=len(rmsL)):
    print("Your imL, rowL, colL, bkgL, and rmsL are not all the same length!")
    print(0/0)

# open up the fits file
hdul = pyfits.open(filename)

# get number of steps (+1 to include the upper limit)
steps = int((sgmUpper - sgmLower)/incr) + 1

# loop through each image
for num in range(len(rowL)):

    # print the image name
    im_num = imL[num]
    print(im_num)

    # get the image parameters
    (y0,y1) = rowL[num]
    (x0,x1) = colL[num]
    rows = y1 - y0
    cols = x1 - x0

    # get the data from fits data
    data = hdul[1].data[y0:y1, x0:x1]
    # make data a contiguous array
    data = np.ascontiguousarray(data, dtype=np.float32)
    
    # create a bkg array using the background value
    bkg_val = bkgL[num]
    bkg = np.full((rows,cols), bkg_val)

    # subtract the background
    data_sub = data - bkg

    # create empty dictionaries and lists
    # d keeps track of all of the points (by peak pixel)
    # dx keeps track of all of the x points while dy keeps track of all of the y points
    d = dict()
    dx = dict()
    dy = dict()

    # dsig keeps track of all of the sigma values that the point occurs in
    dsig = dict()
    # this list is to keep track of all of the points so that we can use the dictionaries later
    pointList = []

    # loop through each sigma
    for step in range(steps):
        # get the corresponding sigma to the step
        sgm = sgmLower + (step*incr)
        # extract objects using sep
        objects = sep.extract(data_sub, sgm, err=rmsL[num], clean = False, deblend_cont = deblend_num)

        # loop through all of the objects and add them to the dictionaries
        for i in range(len(objects)):

            # get the xpeak pixel and ypeak pixel
            xpeak = objects['xpeak'][i]
            ypeak = objects['ypeak'][i]
            point = (xpeak, ypeak)

            # get the x and y pixels of each object
            xpoint = round(objects['x'][i], 2)
            ypoint = round(objects['y'][i], 2)

            # if point is already in dictionary, add new area point to both dictionaries
            if (point in dx):
                dx[point] += [xpoint]
                dy[point] += [ypoint]
                dsig[point] += [sgm]

            # else add newpoint to pointList and add it to both dictionaries
            else: 
                pointList += [point]
                dx[point] = [xpoint]
                dy[point] = [ypoint]
                dsig[point] = [sgm]

    # create figure
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Go through each point and plot both x and y point
    for i in range(len(pointList)):
        point = pointList[i]
        print(point)

        # get x and y point lists
        xpoints = dx[point]
        ypoints = dy[point]
        sigPoints = dsig[point]

        # plot data as 3D scatter plot
        ax.scatter(xpoints, ypoints, sigPoints)

    # set up latex text setting
    params = {'mathtext.default': 'regular' } 
    plt.rcParams.update(params)

    # set up title, axes labels, etc.
    fig.suptitle("Image " + str(im_num) + ": $x_1$ and $x_2$ coordinates")
    ax.set_xlabel('$x_1$ [px]')
    ax.set_ylabel('$x_2$ [px]')
    ax.set_zlabel('$n_I$')
    plt.show()



