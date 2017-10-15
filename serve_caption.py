import generate
import numpy
from generate import Timer

z = generate.load_caption()

def predict(feats):
    ''' Given feature vector retrieve coco-embeddings.
    '''
    k = 5

    feats = feats.to_numpy().astype('float32')

    # Embed image into joint space
    with Timer('Encode image into caption space'):
        feats = generate.embedding.encode_images(z['vse'], feats[None,:])

    # Compute the nearest neighbours
    with Timer('Retrieve captions'):
        scores = numpy.dot(feats, z['cvec'].T).flatten()
        sorted_args = numpy.argsort(scores)[::-1]
        sentences = [z['cap'][a] for a in sorted_args[:k]]

    return {
        'sentences': sentences
    }
