from app.cli_handler import CLIHandler
from app.intent_recogniser import IntentRecogniser
from app.entity_recogniser import EntityRecogniser
from app.recommendation_engine import RecommendationEngine
from config import SPACY_MODEL_NAME
from app.utils.utilities import install_spacy_model


def main():
    """Runs book buddy from the CLI"""
    install_spacy_model(SPACY_MODEL_NAME)

    entity_recogniser = EntityRecogniser(SPACY_MODEL_NAME)
    intent_recogniser = IntentRecogniser(entity_recogniser)
    recommendation_engine = RecommendationEngine("data/books.json")

    cli_handler = CLIHandler(intent_recogniser, recommendation_engine)
    cli_handler.run()


if __name__ == "__main__":
    main()
