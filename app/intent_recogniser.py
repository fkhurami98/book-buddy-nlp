class IntentRecogniser:
    def __init__(self, genres, entity_recogniser):
        self.genres = genres
        self.entity_recogniser = entity_recogniser

    def get_query_intents(self, entities):
        intents = []
        entity_types = {ent["type"] for ent in entities}

        # Check for genres in entities
        for ent in entities:
            if ent["entity"].lower() in self.genres:
                intents.append("genre_recommendation")
                break

        intent_mappings = {
            "PERSON": "author_query",
            "ORG": "author_query",
            "WORK_OF_ART": "work_of_art_query",
            "DATE": "date_query",
            "LANGUAGE": "language_query",
            "GPE": "location_query",
            "LOC": "location_query",
            "NORP": "group_query",
            "FAC": "facility_query",
            "PRODUCT": "product_query",
            "EVENT": "event_query",
            "LAW": "law_query",
            "PERCENT": "percent_query",
            "MONEY": "money_query",
            "QUANTITY": "quantity_query",
            "ORDINAL": "ordinal_query",
            "CARDINAL": "cardinal_query",
            "TIME": "time_query",
        }

        for entity_type, intent in intent_mappings.items():
            if entity_type in entity_types:
                intents.append(intent)

        if not intents:
            intents.append("unknown")

        return intents

    def extract_intent_details(self, entities, detail_type):
        details = set()
        detail_mapping = {
            "genres": lambda ent: ent["entity"].lower() in self.genres,
            "author": lambda ent: ent["type"] == "PERSON",
            "work_of_art": lambda ent: ent["type"] == "WORK_OF_ART",
            "date": lambda ent: ent["type"] == "DATE",
            "language": lambda ent: ent["type"] == "LANGUAGE",
        }
        for ent in entities:
            if detail_mapping[detail_type](ent):
                details.add(ent["entity"])
        return details

    def process_query(self, input_string):
        """
        ENTRY POINT: Processes the input query to extract intents and relevant details.
        """
        entities = self.entity_recogniser.identify_entities(input_string)
        intents = self.get_query_intents(entities)

        details = {
            "genres": set(),
            "authors": set(),
            "works_of_art": set(),
            "dates": set(),
            "language": set(),
        }

        for intent in intents:
            if intent == "genre_recommendation":
                details["genres"].update(
                    self.extract_intent_details(entities, "genres")
                )
            elif intent == "author_query":
                details["authors"].update(
                    self.extract_intent_details(entities, "author")
                )
            elif intent == "work_of_art_query":
                details["works_of_art"].update(
                    self.extract_intent_details(entities, "work_of_art")
                )
            elif intent == "date_query":
                details["dates"].update(self.extract_intent_details(entities, "date"))
            elif intent == "language_query":
                details["language"].update(
                    self.extract_intent_details(entities, "language")
                )

        return entities, intents, details
