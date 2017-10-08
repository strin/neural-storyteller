import generate
z = generate.load_all()

def tell_a_story(image):
    passage = generate.story(z, image.to_stream(), bw=1)
    return {
        'passage': passage
    }
