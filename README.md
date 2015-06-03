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

Using conda, we create a new environment wherein we install the modules from the requirements.txt. We activate that environment and then run setup.py.
<pre>
<code>
conda create -n new_env --file ./requirements.txt
source activate new_env
python setup.py install
</code>
</pre>
Alternatively, we can use pip, either with system pip or virtualenv pip as follows.  
<pre>
<code>
pip install ./
</code>
</pre>
If using pip and the code has been modified since a previous installation, use the upgrade flag and force reinstall.
<pre>
<code>
pip install -U --force-reinstall ./
</code>
</pre>

A script was installed and we need to find where it is.  Try to figure out where the scripts get installed after you install it.  Here's a bash helper:
<pre>
<code>
echo $(dirname $(which python))
</code>
</pre>
In the parent of that directory, look for lib/python2.7/site-packages/<package_name>. For me this means I run the REST API handler script with this:
<pre>
<code>
python  /Users/psteinberg/anaconda/envs/new_env/lib/python2.7/site-packages/myorg/package1/scripts/rest_api_handler.py
</code>
</pre>
The setup.py script defines several entry_points.  Look at setup.py and see if you can figure out where the installed entry points are.  



