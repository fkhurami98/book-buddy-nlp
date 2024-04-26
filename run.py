from src.intent_recogniser import IntentRecogniser
from src.cli_handler import CLIHandler
from src.ocr_handler import OpticalCharacterRecogniser
from src.recommendation_engine import RecommendationEngine
from config import SPACY_MODEL_NAME, GENRES
from src.utils.utilities import install_spacy_model, load_json_data


def main_cli():
    install_spacy_model(SPACY_MODEL_NAME)

    intent_recogniser = IntentRecogniser(GENRES, SPACY_MODEL_NAME)
    recommendation_engine = RecommendationEngine("data/books.json")

    cli_handler = CLIHandler(intent_recogniser, recommendation_engine)
    cli_handler.run()


def main_ocr():
    """
    The main entry point for processing text extracted from an image using OCR.
    This function installs the required spaCy model, loads genre data,
    initialises the intent recogniser, performs OCR on an image,
    and processes the extracted text to identify intents and related details.
    """
    install_spacy_model(SPACY_MODEL_NAME)
    genres = load_json_data("data/genres.json")
    intent_recogniser = IntentRecogniser(genres, SPACY_MODEL_NAME)

    ocr_object = OpticalCharacterRecogniser(
        image_path="/Users/farhadkhurami/Developer/book-buddy-nlp/data/images/9060A66E-924F-407C-842C-4D9F7FA50848.heic"
    )
    extracted_text = ocr_object.extract_text()

    preprocessed_tokens = intent_recogniser.identify_entities(extracted_text)
    named_entities = intent_recogniser.identify_entities(extracted_text)
    intents = intent_recogniser.get_query_intents(preprocessed_tokens, named_entities)
    details = {
        "genres": intent_recogniser.extract_intent_details(
            preprocessed_tokens, named_entities, "genres"
        ),
        "authors": intent_recogniser.extract_intent_details(
            preprocessed_tokens, named_entities, "author"
        ),
    }

    print("\nExtracted Text:")
    print(extracted_text)
    print("\nRecognized Intents:")
    print(intents)
    print("\nDetails Extracted:")
    print(details)


if __name__ == "__main__":
    main_ocr()
