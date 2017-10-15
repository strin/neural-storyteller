import coremltools

coreml_model = coremltools.converters.caffe.convert(('vgg/VGG_ILSVRC_19_layers.caffemodel', 'vgg/VGG_ILSVRC_19_layers_deploy.prototxt'))

coreml_model.save('vgg19.mlmodel')
