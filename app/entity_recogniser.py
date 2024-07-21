import spacy


class EntityRecogniser:
    def __init__(self, model_name):
        self.nlp = spacy.load(model_name)

    def identify_entities(self, text) -> list:
        doc = self.nlp(text)
        entities = []
        for ent in doc.ents:
            entities.append({"entity": ent.text, "type": ent.label_})
        return entities


if __name__ == "__main__":

    sentences = [
        "2004",
        "this is a bullshit thing" "The fantasy novel was set in a dystopian future.",
        "A thrilling detective story with a complex plot.",
        "Science fiction often explores futuristic technology.",
        "Historical novels provide insight into past events.",
        "Romance novels are often set in contemporary settings.",
        "The author wrote a gripping horror story that was well received.",
    ]

    # Instantiate the entity recognizer
    entity_recogniser = EntityRecogniser(
        model_name="model_training/v1/trained_models/custom_genre"
    )

    # Identify entities in each sentence
    for sentence in sentences:
        entities = entity_recogniser.identify_entities(sentence)
        print(f"Sentence: {sentence}")
        for entity in entities:
            print(f"  Entity: {entity['entity']}, Type: {entity['type']}")
        print()  # Print a newline for better readability
