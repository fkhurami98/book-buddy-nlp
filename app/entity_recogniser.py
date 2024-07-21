import spacy

class EntityRecogniser:
    def __init__(self, model_name):
        self.nlp = spacy.load(model_name)

    def identify_entities(self, text):
        doc = self.nlp(text)
        entities = []
        for ent in doc.ents:
            entities.append({"entity": ent.text, "type": ent.label_})
        return entities