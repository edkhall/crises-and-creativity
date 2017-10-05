~~In~~ Th~~e Beg~~inning: of Species
-----

Python code associated with a Global Challenge Research Team (GCRT) project.The central task of the team is to create and implement algorithms that translates processes of species loss and species invasion to works of literature, music, and art. These processes are simulated to give an ecological context to erasure studies of art, music, and literature.

### Contributors
[Dr. Ken Locey](http://kenlocey.weecology.org/): Postdoctoral Fellow in the Lennon Lab, Indiana University, Bloomington.

[Dr. Ed Hall](http://www.nrel.colostate.edu/hall-lab/): Assistant Professor, Natural Resource Ecology Laboratory - Colorado State University  

### Purpose  

**Code in this repository will be built to simulate:**

1. **Extinction:** To represent the impact of species loss, individual nouns in well‐known works of literature are removed according to an algorithm mimicking species extinction. As each noun is removed all other parts of speech referring to that noun (e.g. adjective, pronouns) disappear simultaneously. This process represents the collapse of ecological interactions that occur when species are lost from an ecosystem.2. **Invasion:** To represent the impact of species invasions, all adjectives expressing a similar modification (e.g. augmentative adjectives such as: larger, obese, robust, rotund) are replaced with a single adjective that represents augmentation (e.g. huge). Allowing the alterations to fill a “functional niche” while decreasing the diversity of prose.**Code in this repository will eventually be expanded to visual and musical works of art. Examples will be:**

1. Melodies with introduced notes (invasion) and melodies with notes removed (extinction).
2. Paintings with introduced pixels and colors (invasion) and paintings with pixels and colors that are removed (extinction).

### Directories and Files

**Directory:** Bible\_KingJamesVersion  
**Files**:  

* Bible, King James Version  
downloaded from http://www.sacred-texts.com/bib/osrc/

**Directory:** Epic\_of\_Gilgamesh  
**Files**: 

* Epic\_of\_Gilgamesh.txt  
downloaded from https://archive.org/stream/TheEpicofGilgamesh_201606/eog_djvu.txt

**Directory:** Hesiods\_Theogony  
**Files**: 

* Hesiods\_Theogony.txt  
downloaded from http://www.sacred-texts.com/cla/hesiod/theogony.htm
* Hesiods\_Theogony\_EndNotes.txt  
downloaded from http://www.sacred-texts.com/cla/hesiod/theogony.htm

**Directory:** Native\_American\_Trickster\_Myths  
**Files**: 

* Native\_American\_Trickster\_Myths.txt  
downloaded from: http://arcadiasystems.org/academia/printtrickster.html


### Suggested software

This source code is developed on the Enthought Canopy Python distribution (version 1.5.5) available here: https://store.enthought.com/

This source code will implements unit testing using pytest version 2.8.1; see: http://pytest.org/latest/getting-started.html#getstarted

Output files will be able to be imported into Python and R environments as dataframes. For this reason, the R friendly user may want to install RStudio: https://www.rstudio.com/products/rstudio/download/ and/or R: https://www.r-project.org/