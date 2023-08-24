# 1. install pytorch
https://pytorch.org/get-started/locally/

#2 
git clone git@github.com:facebookresearch/segment-anything.git
cd segment-anything
pip install -e .

pip install opencv-python pycocotools matplotlib 
#onnxruntime onnx


from segment_anything import SamPredictor, sam_model_registry
sam = sam_model_registry["vit_l"](checkpoint="../checkpoints/sam_vit_l_0b3195.pth")
predictor = SamPredictor(sam)
predictor.set_image(<your_image>)
masks, _, _ = predictor.predict(<input_prompts>)


python scripts/amg.py --checkpoint ../checkpoints/sam_vit_l_0b3195.pth --model-type vit_l --input ../imgs/test2017/000000000001.jpg --output ../test.jpg

python scripts/amg.py --checkpoint ../checkpoints/sam_vit_l_0b3195.pth --model-type vit_l --input ../../temp/IMG_2465.jpg --output ../out


------------------ ignore, bad now

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

pip install numpy
pip install cython
pip install matplotlib

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



pip install scikit-image