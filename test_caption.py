import moxel
import json
import numpy

model = moxel.Model('strin/coco-caption:latest', where='localhost')

with open('vec.json', 'r') as f:
    data = numpy.array(json.load(f))

sentences = model.predict(feats=data)['sentences']
print('sentences', sentences.to_object())

