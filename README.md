# Persistent Homology
##  <a href="https://ximenafernandez.github.io/">  _Ximena Fernandez_ </a>
## <a href="https://eutopia.unitn.eu/eutopia-summer-school/"> EUTOPIA 2022 </a>

<!--<img src="figures/filtration_circle.gif" width="300" height="300" class="center"/>-->

This repository contains all the lectures and code related to the course Persistent Homology, as part of the EUTOPIA Summer School 2022.

### Lecture 1.1: Topological Data Analysis
This lecture is about a general exposition of Persistent Homology and some applications. The slides of the lecture are available <a href="https://ximenafernandez.github.io/reveal.js-presentations/slides/PersistentHomology_EUTOPIA.html#/"> here</a>.
The demo of the software Ripser can be found at <a href="https://live.ripser.org/"> this link</a>. The synthetic point clouds to test the software are available at the folder _data_: cicle, sphere and torus.


### Lecture 1.2: Hands on: computational topology in action
This lecture is a live-coding/hands-on exposition of the use of the software Ripser to compute Persistent Homology, and some real applications with concrete data.

 All the datasets are available at the folder _data_.

 To run the notebooks, it is required to have installed ```jupyter```, as well as the following:
 ``` 
Python (>= 3.6)
pip
NumPy (>= 1.19.1)
SciPy (>= 1.5.0)
scikit-learn (>= 0.23.1)
matplotlib
seaborn
pandas

```

The specific libraries for TDA we use are:
```
Fermat
ripser
tadasets
persim
biopython
```

The notebook _Intro_Persistent_Homology.ipynb_ provides a complete description and implementation of tools related to the computation of persistent homology with the software ```Ripser```. It also contains  some simulations in synthetic point clouds to describe properties of persistent homology. The notebook _Beyond_Persistent_Homology.ipynb_ describes how to infer other topological features from a sample (such as orientability, singularities, local dimension and low domensional representation).
Some exercises to familiarize yourself with the techniques can be found at the notebook _Exercises_Persistent_Homology.ipynb_

### Lecture 2: 
This lecture is about concrete applications of the study of topological descriptors in real data. The slides of the lecture are available <a href="https://ximenafernandez.github.io/reveal.js-presentations/slides/Data_Sets_Persistent_Homology.html#/"> here</a>.

*  We will apply all the topological methods already learned to study the topology of one of the following real datasets:
2.1. **Cyclo Octane**
2.2 **Grid Cells**

* We will apply all we have learned in a concrete problem of _classification of the secondary structure of proteins_, using persistent homology to construct topological features to feed a ML algorithm. The guided implementation can be found at the notebook
 _Proteins_Structure_Classification.ipynb_ 


