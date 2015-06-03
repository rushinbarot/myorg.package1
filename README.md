This directory shows example folder layout for a Python project.

Replace 'myorg' in the leading part of the package name with 
some business function like 'datasci' at your organization, then 
build a number of weakly related packages under that namespace.

Make all edits to the /package1 directory, not the empty /myorg folder above it.

If you make myorg.package1, myorg.package2, etc, they can all live in separate
repositories, each with separate git repos.

Getting Started - Installing Requirements

One choice is conda if you have it installed via the Anaconda Python distribution
from continuum.

Using conda, we create a new environment wherein we install the modules from the requirements.txt

conda create -n new_env --file ./requirements.txt
source activate new_env

Alternatively, we can use pip, either with system pip or virtualenv pip as follows:

pip install -r ./requirements.txt