from pprint import pprint

class CLIHandler:
    def __init__(self, intent_recogniser, recommendation_engine):
        self.intent_recogniser = intent_recogniser
        self.recommendation_engine = recommendation_engine


    def display_extracted_info(self, named_entities, intents, details):
        print(f"\n[RESULT] Identified Named Entities: {named_entities}")
        print(f"[RESULT] Identified Intents: {intents}")
        pprint(f"[RESULT] Output Dictionary: {details}")
        
    def display_recommendations(self, recommendations):
        recommendations
        if recommendations:
            print("\n[RECOMMENDATIONS]")
            # for book in recommendations:
            #     print(
            #         f"Title: {book.get('title')}\nAuthor: {', '.join(book.get('authors', []))}\n"
            #     )
        else:
            print("\nNo recommendations found based on your query.")

    def run(self):
        print("\nWelcome to Book-Buddy. Please enter your query.")
        try:
            while True:
                user_input = input("\nYour query: ").lower()
                if user_input == "exit":
                    break
                named_entities, intents, details = self.intent_recogniser.process_query(
                    user_input
                )
                self.display_extracted_info(named_entities, intents, details)
                recommendations = self.recommendation_engine.recommend(details)
                self.display_recommendations(recommendations)
        except KeyboardInterrupt:
            print("\nExiting Book-Buddy...")