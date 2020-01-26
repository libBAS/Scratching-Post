def detect_labels(path):
    """Detects labels in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    return labels

def is_dog(labels):
    for label in labels:
        if label.description == "Dog":
            return True
    return False

def is_cat(labels):
    for label in labels:
        if label.description == "Cat":
            return True
    return False




labels = detect_labels("cat.jpg")
for label in labels:
    print(label.description)
print(is_dog(labels))
print(is_cat(labels))
# print("next")
# detect_labels("dog.jpg")

