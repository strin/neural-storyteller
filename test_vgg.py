import moxel

model = moxel.Model('strin/coco-vgg:latest', where='localhost')
image = moxel.space.Image.from_file('images/ex2.jpg')
result = model.predict(image=image)['feats']
print(result.to_numpy())
