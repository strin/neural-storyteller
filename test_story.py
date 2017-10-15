import moxel
import json
import numpy

model = moxel.Model('strin/story-romantic:latest', where='localhost')

sentences = [u'A black and white photo of a man in suit and tie .', u'a large clock on the wall above a radiator', u'A young girl and a woman preparing food in a kitchen .', u'a close up of a person grabbing a pastry in a container', u"A woman glances at a young girl 's cooking on the stovetop"]
passage = model.predict(sentences=sentences)['passage']

print('passage', passage)

