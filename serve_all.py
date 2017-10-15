import moxel

model_vgg = moxel.Model('strin/coco-vgg:latest')
model_caption = moxel.Model('strin/coco-caption:latest')
model_story_romantic = moxel.Model('strin/story-romantic:latest')

def predict(image):
    feats = model_vgg.predict(image=image)['feats']
    captions = model_caption.predict(feats=feats)['sentences'].to_object()
    return model_story_romantic.predict(sentences=captions)
