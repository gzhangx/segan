initial setup: 
conda install pip
https://conda.io/projects/conda/en/latest/user-guide/install/index.html


https://towardsdatascience.com/master-the-coco-dataset-for-semantic-image-segmentation-part-1-of-2-732712631047

### Enter the below in your Conda Command Prompt ###
# Create a new environment
conda create -n <envName>
# Activate the environment
conda activate <envName>
# Install cython
pip install cython
# Install git
conda install -c anaconda git
# Install pycocotools from this GitHub rep
pip install git+https://github.com/philferriere/cocoapi.git#egg=pycocotools^&subdirectory=PythonAPI



conda create -n coco
conda activate coco
# run outside conda
# pip install cython
conda install -c anaconda git
# Install pycocotools from this GitHub rep
pip install git+https://github.com/philferriere/cocoapi.git#egg=pycocotools^&subdirectory=PythonAPI