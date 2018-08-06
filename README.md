# Machine Learning with Python and TensorFlow

**2018 CQS Summer Institute course in machine learning**

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/fonnesbeck/cqs_machine_learning)

This intermediate-level course will provide students with hands-on experience applying practical machine learning methods in Python. I will provide an introduction to several core Python data science tools for data manipulation (pandas), statistical learning (scikit-learn), probabilistic programming (PyMC3), and neural networks (TensorFlow). The course content will be presented using Jupyter notebooks, which allow for interactive, hands-on learning. **The course will assume familiarity with Python and with basic statistics** but does not require previous experience with machine learning methods or any of the specific Python packages

## Syllabus

### Day 1: Data Preparation

* Introduction to the NumPy `ndarray`
* Introduction to Pandas `Series` and `DataFrame` objects
* Importing and exporting data
* Data processing
* Merging, joining and reshaping

### Day 2: Unsupervised Learning with scikit-learn

* The scikit-learn API
* Principal components analysis
* Clustering methods
* Model checking

### Day 3: Supervised Learning with scikit-learn

* Regression models
* Decision trees and random forests
* Gradient boosted trees
* Cross-validation

### Day 4: Probabilistic Programming with PyMC3

* Introduction to probabilistic programming and Bayesian inference
* Specifying probabilistic models in PyMC3
* Model fitting
* Model checking

### Day 5: Neural Networks with TensorFlow

* Introduction to programming in TensorFlow
* Data preparation
* Training neural networks
* Building models with Keras


## Software Installation

This course requires a working Python3 interpreter, preferably Python 3.6. A complete Python installation for Mac OSX, Linux and Windows can most easily be obtained by downloading and installing the free [`Anaconda Python Distribution`](https://www.continuum.io/downloads) by ContinuumIO. **If possible, please have your Python environment set up prior to the course.**

We will primarily be using four packages:

- pandas
- scikit-learn
- PyMC3
- TensorFlow

These can all be installed using `conda`, a package management tool that is bundled with Anaconda. Each package also depends on several third-party Python packages which will be automatically installed when installing via `conda`. You can install everything you need by cloning this repository:

```bash
git clone https://github.com/fonnesbeck/cqs_machine_learning.git
```

If you are unfamiliar with Git, you can download and unzip a zip file of the course contents from the "Clone or download" button in the upper right part of the GitHub page.

Then move into the directory created by the clone, and install the required packages using `conda`:

```bash
cd cqs_machine_learning
conda env create -f environment.yml
```

This will create a *virtual environment* called `cqsml` that includes everything that you need, and that is completely separate from any other Python installations you may have on your machine. To activate this environment to run the course materials, you can run the following command from the terminal:

```bash
source activate cqsml
```

**If you would rather not install the software yourself, you can use the MyBinder.org link at the top of the page to run the course materials on a remote server**

If you have used Git to download the course materials,you can update the course materials at any time by pulling from the course repository. From your course directory, type:

```bash
git pull
```

Note that this will overwrite any changes you have made to notebooks that need to be updated.
