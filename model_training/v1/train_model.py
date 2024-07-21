import json
from pprint import pprint
import spacy
from spacy.training import Example
from spacy.util import minibatch, compounding


with open(
    "/Users/farhadkhurami/Developer/book-buddy-nlp/model_training/v1/training_data/genre_intent_training_data.json",
    "r",
) as f:
    TRAIN_DATA = json.load(f)

nlp = spacy.load("en_core_web_trf")

if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
else:
    ner = nlp.get_pipe("ner")

ner.add_label("GENRE")


examples = []
for text, annotations in TRAIN_DATA:
    doc = nlp.make_doc(text)
    examples.append(Example.from_dict(doc, annotations))


optimizer = nlp.resume_training()


for iteration in range(50):
    losses = {}
    batches = minibatch(examples, size=compounding(4.0, 32.0, 1.001))
    for batch in batches:
        nlp.update(batch, drop=0.5, losses=losses)
    print(f"Iteration {iteration + 1}: Losses {losses}")

nlp.to_disk(
    "/Users/farhadkhurami/Developer/book-buddy-nlp/model_training/v1/trained_models/custom_genre_with_trf"
)
