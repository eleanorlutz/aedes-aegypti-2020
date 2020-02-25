# Distinct navigation behaviors in *Aedes*, *Anopheles*, and *Culex* mosquito larvae
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](http://doge.mit-license.org)
[![Data License: CC0-1.0](https://img.shields.io/badge/Data%20License-CC0--1.0-lightgrey)](http://creativecommons.org/publicdomain/zero/1.0/)
[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

**Authors and Affiliations:** Eleanor K. Lutz<sup>a</sup>, Kim T. Ha<sup>b</sup>, [Jeffrey A. Riffell](http://faculty.washington.edu/jriffell/)<sup>a†</sup>

  - **a**. Department of Biology, University of Washington, Seattle, WA 98195, USA.
  - **b**. University of Washington, Seattle, WA 98195, USA
  - **†** To whom all correspondence should be addressed</sup>

Code used to analyze and visualize data for this manuscript is provided in this Github repository under the [MIT license](https://choosealicense.com/licenses/mit/). Note that the code and data required to create the concentration map for the arena is provided in the [open-source code of a previous paper](https://github.com/eleanorlutz/aedes-aegypti-2019). A brief explanation of each code file is provided below.

This paper was originally submitted to the Journal of Experimental Biology on January 4, 2020. Comments from two anonymous reviewers were received on February 11, 2020, and the manuscript was revised and resubmitted on February 21, 2020. Both versions are available in the `manuscript` folder.

### Data Analysis Code:
#### 0_inspect_data.ipynb
- Output number of live and dead animals for each species and treatment
- Remove dead larvae from experiment master file
- Check that manually annotated files all exist and are spelled correctly

#### 1_convert_hdf5_to_csv.ipynb
- Translate Multitracker hdf5 files into Pandas dataframes and save to CSV
- Find videos with quiescent animals at beginning of video
- Manually correct videos with quiescent animals at beginning of video

#### 2_calculate_trajectory_properties.ipynb
- Add the size of each larvae into the trajectory CSV file
- Convert pixel locations to mm
- Zero out any off-screen values to the limits of the behavior arena
- Calculate instantaneous speed in mm per second
- Calculate instananeous angle (from horizontal, countercounterclockwise, in degrees)
- Calculate instantaneous change in heading (angle)
- Calculate the predicted concentration of chemical in the arena experienced by the larva at each time point
- Calculate the change in concentration relative to the previous timestep

#### 3_calculate_acclimation_values_per_larvae.ipynb
- Calculates each of the ten navigation variables for each animal and outputs the results as a separate data file
	1. Time spent moving
	2. Total distance traveled
	3. Mean speed when moving
	4. Maximum speed
	5. Mean speed during the first minute 
	6. Difference in mean speed (first and last minute)
	7. Number of sharp turns (>45 degrees)
	8. Number of spiral movements
	9. Number of continuous paths that are not spirals
	10. Longest rest period (in seconds)

#### 4_calculate_experiment_values_per_larvae.ipynb
- Calculate the median concentration preferred by the larvae (normalized to the acclimation period)
- Calculate the discovery time for each larvae (normalized to the acclimation period)
- Calculate the speed in areas of high concentration, compared to speed in areas of low concentration, normalized to behavior during the acclimation period. 
- Output all of these values into a separate spreadsheet. 

#### 5_calculate_acclimation_experiment_changes_per_larvae.ipynb
- Calculate the change in each of the ten navigation variables for each animal between the acclimation period and the experiment period. Save the results as a separate data file. 
	1. Time spent moving
	2. Total distance traveled
	3. Mean speed when moving
	4. Maximum speed
	5. Mean speed during the first minute 
	6. Difference in mean speed (first and last minute)
	7. Number of sharp turns (>45 degrees)
	8. Number of spiral movements
	9. Number of continuous paths that are not spirals
	10. Longest rest period (in seconds)

#### 6_statistical_analyses.ipynb
- Calculate if there are any differences among the six species for each of the ten navigational variables (Kruskal test)
- Calculate if the larvae of each species prefer each of the different treatment odors
- Check if data gathered has a normal distribution (to inform the types of statistical tests that can be conducted)
- Calculate if there are mortality differences across the larval species (Fisher's exact test for binary data)
- Calculate pairwise perMANOVA for each species against each other species (navigation variables) as well as pairwise tests of multivariate dispersion (ANOVA) for all of the ten navigation variables during the acclimation period.

### Figure Generation Code:
Each figure code file generates the figure(s) named in the title (`S` marks supplemental figures)
- **F_1_plot_gradient_map.ipynb**
- **F_1_plot_trajectories.ipynb**
- **F_2_describe_trajectories.ipynb**
- **F_2_make_barplots_acclimation.ipynb**
- **F_3_make_PCA_plots.R**
- **F_4_angular_distributions.ipynb**
- **F_4_make_barplots_experiment.ipynb**
- **F_S1_plot_distance_matrix.ipynb**
- **F_S2_make_barplots_acclimation_changes.ipynb**
- **F_S3_larvae_size_across_species.ipynb**
- **F_S3_PCA_acclimation_changes.ipynb**
- **F_S4_combined_trajectories.ipynb**
- **colors.py** (colors used in all figures)
