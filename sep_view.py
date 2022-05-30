
# get the fits info (CHANGE THIS)
filename = "hst_data/CL0024_data/hst_10325_c7_acs_wfc_f475w_drz.fits"

# write down the image names in order (CHANGE THIS)
imL = ["Image 1", "Image 2", "Image 3", "Image 4", "Image 5"]

# row and column lists (CHANGE THIS)
rowL = [(1637, 1765), (1765, 1893), (2149, 2277), (2405, 2533), (2149, 2277)]
colL = [(1535, 1663), (1407, 1535), (1279, 1407), (2283, 2411), (2057, 2185)]

# OPTIONAL - color limit for each image (set True if you want to manually set the color limit otherwise set False)
clim_bool = True
climL = [(0.03,0.182), (0.038,0.13), (0.038,0.16), (0.03,0.195), (0.035,0.155)]

# get the background and rms values for each image (CHANGE THIS)
bkgL = [0.04627720266580582, 0.046375613659620285, 0.04566671699285507, 0.04507363587617874, 0.04775523394346237]
rmsL = [0.00323042762465775, 0.0031234666239470243, 0.003028792329132557, 0.0035166656598448753, 0.0033184518106281757]

# parameters (CHANGE THIS)
# num is the index of the image (Note: lists start at index 0)
# n : referred to n_I in the paper
num = 0
n = 7
deblend_num = 0.005

### DO NOT EDIT ANYTHING BELOW THIS LINE ###
################################################################################

# import relevant packages
import numpy as np
import sep
import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# safety check
if ((len(rowL)!=len(colL)) or ((len(rowL)!=len(climL)) and clim_bool) or (len(rowL)!=len(bkgL)) or (len(rowL)!=len(rmsL)) or (len(rowL)!=len(imL))):
    print("You're lists are not all the same length!")
    print(0/0)

# open up the fits file
hdul = pyfits.open(filename)

# get the image info
im = imL[num]
(r0, r1) = rowL[num]
(c0, c1) = colL[num]
rows = r1 - r0
cols = c1 - c0

# get the data from fits data
data = hdul[1].data[r0:r1, c0:c1]
# make data a contiguous array
data = np.ascontiguousarray(data, dtype=np.float32)

# create an array using the background value 
bkg_val = bkgL[num]
bkg = np.full((rows,cols), bkg_val)

# subtract the background
data_sub = data - bkg

# get objects using sep
objects = sep.extract(data_sub, n, err=rmsL[num], clean = False, deblend_cont = deblend_num)

# create figure
fig, ax3 = plt.subplots()

# OPTIONAL: set colorbar limits
if clim_bool:
    # get the colorbar limits
    (c0, c1) = climL[num]

    # show the image without background
    img = ax3.imshow(data, cmap='gray', origin='lower', vmin = c0, vmax = c1)

else: img = ax3.imshow(data, cmap='gray', origin='lower')

# set the colorbar
fig.colorbar(img)

# list for center pixels
xpoints = []
ypoints = []
points = []

# list for peak points
xpeaks = []
ypeaks = []

# plot an ellipse for each object
for i in range(len(objects)):
    # create ellipse using object parameters
    e = Ellipse(xy=(objects['x'][i], objects['y'][i]),
                width=6*objects['a'][i],
                height=6*objects['b'][i],
                angle=objects['theta'][i] * 180. / np.pi)

    # add the center of the object into the center lists defined above
    xPoint = round(objects['x'][i], 2)
    yPoint = round(objects['y'][i], 2)
    xpoints += [xPoint]
    ypoints += [yPoint]
    points += [xPoint, yPoint]

    # add the peak of the object into the peak lists defined above
    xPeak = objects['xpeak'][i]
    yPeak = objects['ypeak'][i]
    peak = (xPeak, yPeak)
    xpeaks += [xPeak]
    ypeaks += [yPeak]

    # print out all of the points (adj - adjusted to the actual location in the data)
    centerPoint = (xPoint, yPoint)
    adjPoint = (xPoint + c0, yPoint + r0)
    adjPeak = (xPeak + c0, yPeak + r0)
    print(peak, adjPeak, centerPoint, adjPoint)

    # draw the ellipses onto plot
    e.set_facecolor('none')
    e.set_edgecolor('red')
    ax3.add_artist(e)

# set up latex text setting
params = {'mathtext.default': 'regular' } 
plt.rcParams.update(params)

# set up title, axes labels, etc.
plt.title(im)
plt.plot(xpoints, ypoints, color = 'm', linestyle = "", marker = ".")
plt.plot(xpeaks, ypeaks, color = 'b', linestyle = "", marker = ".")
plt.xlabel("$x_1$ [px]")
plt.ylabel("$x_2$ [px]")

# show plot
plt.show()
