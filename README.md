# SEP Automated Feature Detection
This repository contains code to detect features using SEP (Sextractor in Python)

# Required packages
- Numpy      (For handling arrays)
- Matplotlib (For plotting mechanisms)
- Astropy    (To handle FITS file)
- SEP        (Available at https://github.com/kbarbary/sep)
- ptmatch    (Available at https://github.com/ntessore/imagemap)

The codes use an FITS data file as an example. The dataset is "hst_10325_c7_acs_wfc_f475w.fits" and you can download it via Hubble Legacy Archive (Proposal ID: 10325, PI: Ford, Visit num: c7). 

## Contents:
-   [**`sep_bkg_rms.py`**] - calculates the background and rms value of an image
-   [**`sep_fg_graphs.py`**] - plots all of the f, g1, and g2 values on one plot
-   [**`sep_graphs_area.py`**] - plots the area of the detected objects over $n_I$
-   [**`sep_graphs_location.py`**] - plots the location of each detected object over two plots, x1 and x2
-   [**`sep_j_graphs.py`**] -  plots all of the j values on one plot
-   [**`sep_3D_location.py`**] - a 3D version of sep_graphs_location.py
-   [**`sep_view.py`**] - a tool to look at the image at a single $n_I$

## Manual

### sep_bkg_rms.py
Input: 
- filename - location of FITS file that you want to use
- imL - list for image names
- rowL - list of tuples of rows for each image e.g. (r0,r1) where r0 is the lower row and r1 is the higher row
- colL - list of tuples of columns for each image e.g. (c0,c1) where r0 is the lower row and r1 is the higher row
- width - the size of the background patch 
- bkg_rowL - list of tuples of rows for each background patch
- bkg_colL - list of tuples of columns for each background patch

Optional Inputs: 
- clim_bool - boolean, set True if you want to manually input colorbar limits
- climL - list of tuples for colorbar limits e.g. (clim0, clim1) where clim0 is the lower limit and clim1 is the higher limit for an image
- bkg_bool - boolean, set True if you want to see the background patch outlined in the image

Output: 
- a plot of each image (along with the background patch if bkg_bool = True)
- printed statements of background and rms values of each image
- bkgL and rmsL

### sep_fg_graphs.py
Input:
- locL - list of the locations on the x-axis of each errorbar plotted
- x_ticksL - list of the location of the x-labels 
- x_labelsL - list of labels for the x-axis
- im_nameL - list of image names (what you want the title of the plot to be)
- colorL - list of colors for the errorbars e.g. ".k" --> black and disconnected errorbars
- markerL - list of markers for the most likely value of each errorbar e.g. "ro" --> red circles
- fL - list of the f values, each sublist is for one waveband [f_1, f_2, ...] where f_1 is the f value for Image 1, etc.
- ferrL - list of the error values corresponding to each f in fL
- g1L - list of the g1 values
- g1errL - list of the error values corresponding to each g1 in g1L
- g2L - list of the g2 values
- g2errL - list of the error values corresponding to each g2 in g1L
- f_mLL - list of the most likely values corresponding to each f in fL
- g1_mLL - list of the most likely values corresponding to each g1 in g1L
- g2_mLL - list of the most likely values corresponding to each g2 in g2L

Output:
- plots of the f, g1, and g2 values for each image

### sep_graphs_area.py
Input:
- filename - location of FITS file that you want to use
- imL - list for image names
- rowL - list of tuples of rows for each image e.g. (r0,r1) where r0 is the lower row and r1 is the higher row
- colL - list of tuples of columns for each image e.g. (c0,c1) where r0 is the lower row and r1 is the higher row
- bkgL - list of the background values for each image calculated using sep_bkg_rms.py
- rmsL - list of the rms values for each image calculated using sep_bkg_rms.py
- n_Lower - lower bound for the signal strength, $n_I$
- n_Upper - upper bound for the signal strength, $n_I$
- incr - increment for the signal strength, $n_I$
- deblend_num - the deblend parameter as defined in SEP (by deafult is 0.005)

Output:
- a plot of the Area of each detected object vs. $n_I$ for each image with a legend of the peak location of the detected objects

### sep_graphs_location.py
Input: 
- filename - location of FITS file that you want to use
- imL - list for image names
- rowL - list of tuples of rows for each image e.g. (r0,r1) where r0 is the lower row and r1 is the higher row
- colL - list of tuples of columns for each image e.g. (c0,c1) where r0 is the lower row and r1 is the higher row
- bkgL - list of the background values for each image calculated using sep_bkg_rms.py
- rmsL - list of the rms values for each image calculated using sep_bkg_rms.py
- n_Lower - lower bound for the signal strength, $n_I$
- n_Upper - upper bound for the signal strength, $n_I$
- incr - increment for the signal strength, $n_I$
- deblend_num - the deblend parameter as defined in SEP (by deafult is 0.005)

Output:
- a plot of the x1 and x2 locations of each object detected vs. $n_I$ for each imagewith a legend of the peak location of the detected objects

### sep_j_graphs.py
Input:
- locL - list of the locations on the x-axis of each errorbar plotted
- x_ticksL - list of the location of the x-labels 
- x_labelsL - list of labels for the x-axis
- im_nameL - list of image names (what you want the title of the plot to be)
- colorL - list of colors for the errorbars e.g. ".k" --> black and disconnected errorbars
- markerL - list of markers for the most likely value of each errorbar e.g. "ro" --> red circles
- jL - list of the f values, each sublist is for one waveband [f_1, f_2, ...] where f_1 is the f value for Image 1, etc.
- jerrL - list of the error values corresponding to each j in jL
- j_mLL - list of the most likely values corresponding to each j in jL

Output:
- plots of the j values for each image

### sep_3D_location.py
Input: 
- filename - location of FITS file that you want to use
- imL - list for image names
- rowL - list of tuples of rows for each image e.g. (r0,r1) where r0 is the lower row and r1 is the higher row
- colL - list of tuples of columns for each image e.g. (c0,c1) where r0 is the lower row and r1 is the higher row
- bkgL - list of the background values for each image calculated using sep_bkg_rms.py
- rmsL - list of the rms values for each image calculated using sep_bkg_rms.py
- n_Lower - lower bound for the signal strength, $n_I$
- n_Upper - upper bound for the signal strength, $n_I$
- incr - increment for the signal strength, $n_I$
- deblend_num - the deblend parameter as defined in SEP (by deafult is 0.005)

Output:
- a 3D plot of the x1 and x2 locations of each object detected for each imagewith a legend of the peak location of the detected objects

### sep_view.py
Input: 
- filename - location of FITS file that you want to use
- imL - list for image names
- rowL - list of tuples of rows for each image e.g. (r0,r1) where r0 is the lower row and r1 is the higher row
- colL - list of tuples of columns for each image e.g. (c0,c1) where r0 is the lower row and r1 is the higher row
- bkgL - list of the background values for each image calculated using sep_bkg_rms.py
- rmsL - list of the rms values for each image calculated using sep_bkg_rms.py
- num - integer that indexes into the list, use to choose which image you want to access
- n - signal strength, $n_I$
- deblend_num - the deblend parameter as defined in SEP (by deafult is 0.005)

Optional Inputs: 
- clim_bool - boolean, set True if you want to manually input colorbar limits
- climL - list of tuples for colorbar limits e.g. (clim0, clim1) where clim0 is the lower limit and clim1 is the higher limit for an image

Output: 
- a plot of the selected image with red ellipses plotted around each SEP detected object (magenta point: center point, blue point: peak point)
- printed statements of information of each detected object in the plot (order: (peak, adjPeak, center, adjCenter) where adj stands for adjusted to the actual location in the data array)

