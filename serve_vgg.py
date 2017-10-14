import generate

net = generate.load_vgg()

def predict(image):
    _, im = generate.load_image(image.to_stream())

    # Run image through convnet
    feats = generate.compute_features(net, im).flatten()
    feats /= generate.norm(feats)

    return {
        'feats': feats
    }
