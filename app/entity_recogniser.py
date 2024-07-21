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


entities = EntityRecogniser(
    model_name="model_training/v1/trained_models/custom_genre"
).identify_entities("Purple Akhi in a trackie")

print(entities)
