import json
from pprint import pprint
import spacy
from spacy.training import Example
from spacy.util import minibatch, compounding

with open("model_training/training_data/genre_training_data.json", "r") as f:
    TRAIN_DATA = json.load(f)

nlp = spacy.blank("en")
nlp.add_pipe("transformer", source=spacy.load("en_core_web_trf"))
ner = nlp.add_pipe("ner")

ner.add_label("GENRE")

examples = []
for text, annotations in TRAIN_DATA:
    doc = nlp.make_doc(text)
    examples.append(Example.from_dict(doc, annotations))

optimizer = nlp.begin_training()

for iteration in range(9):  
    losses = {}
    batches = minibatch(examples, size=compounding(4.0, 32.0, 1.001))
    for batch in batches:
        nlp.update(batch, drop=0.5, losses=losses)
    print(f"Iteration {iteration + 1}: Losses {losses}")

nlp.to_disk("model_training/trained_models/custom_genre_v1")
