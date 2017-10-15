import generate
import numpy
from generate import Timer, skipthoughts, decoder

z = generate.load_story()

def predict(sentences):
    beam_width = 20

    sentences = sentences.to_object()

    # Compute skip-thought vectors for sentences
    with Timer('Compute skip-thought vector'):
        svecs = skipthoughts.encode(z['stv'], sentences, verbose=False)

    # Style shifting
    shift = svecs.mean(0) - z['bneg'] + z['bpos']

    # Generate story conditioned on shift
    with Timer('Decoding'):
        passage = decoder.run_sampler(z['dec'], shift, beam_width=beam_width)

    return {
        'passage': passage
    }
