"""
Configuration for the generate module
"""

#-----------------------------------------------------------------------------#
# Flags for running on CPU
#-----------------------------------------------------------------------------#
FLAG_CPU_MODE = True

#-----------------------------------------------------------------------------#
# Paths to models and biases
#-----------------------------------------------------------------------------#
paths = dict()

# Skip-thoughts
paths['skmodels'] = 'skipthoughts/'
paths['sktables'] = 'skipthoughts/'

# Decoder
paths['decmodel'] = 'decoder/romance.npz'
paths['dictionary'] = 'decoder/romance_dictionary.pkl'

# Image-sentence embedding
paths['vsemodel'] = 'decoder/coco_embedding.npz'

# VGG-19 convnet
paths['vgg'] = 'vgg19.pkl'
paths['pycaffe'] = '/u/yukun/Projects/caffe-run/python'
paths['vgg_proto_caffe'] = 'vgg/VGG_ILSVRC_19_layers_deploy.prototxt'
paths['vgg_model_caffe'] = 'vgg/VGG_ILSVRC_19_layers.caffemodel'


# COCO training captions
paths['captions'] = 'decoder/coco_train_caps.txt'

# Biases
paths['negbias'] = 'decoder/caption_style.npy'
paths['posbias'] = 'decoder/romance_style.npy'
