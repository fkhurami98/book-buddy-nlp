import json


# This could be a SQL databse in the future?
GENRES = [
    "sci-fi", "science fiction", "sci fi", "SF", "fantasy", "fiction",
    "mystery", "psychological thriller", "thriller", "horror", "historical fiction",
    "historical", "western", "dystopian", "utopian", "speculative fiction",
    "cyberpunk", "steampunk", "biopunk", "romantic comedy", "romance",
    "contemporary romance", "romcom", "comedy", "drama", "tragedy", "contemporary fiction"
    "crime", "detective", "adventure", "action", "non-fiction", "biography",
    "autobiography", "memoir", "self-help", "guide", "travel", "true crime",
    "religious", "spiritual", "new age", "science", "history", "math",
    "mathematics", "philosophy", "poetry", "essay", "anthology", "short story",
    "young adult", "YA", "children's", "children's fiction",  "picture book", "graphic novel", "manga",
    "light novel", "erotica", "LGBTQ+", "literature", "queer literature",
    "classical", "american literature", "classic fiction", "classic american literature", "chick lit",
    "paranormal", "urban fantasy", "magical realism", "saga", "epic", "political",
    "war", "apocalyptic", "post-apocalyptic", "space opera", "hard science fiction",
    "soft science fiction", "military science fiction", "pulp fiction", "gothic",
    "fairy tale", "folk tale", "mythology", "educational", "health", "fitness",
    "cooking", "cookbook", "art", "photography", "diy", "do it yourself", "gardening",
    "sports", "technology", "computer science", "business", "economics", "finance",
    "law", "psychology", "sociology", "anthropology", "academic", "reference",
    "dictionary", "encyclopedia", "manual", "textbook", "journal", "humor",
    "alternative history", "amateur sleuth", "animal", "anime", "apocalyptic thriller",
    "arthurian", "bildungsroman", "biographical novel", "body horror", "campus novel",
    "chivalric romance", "cozy mystery", "crafts", "creative non-fiction", "cyber thriller",
    "dark fantasy", "dark humor", "disaster", "domestic fiction", "eco thriller",
    "epistolary", "erotic thriller", "espionage", "experimental", "fable", "feminist",
    "flash fiction", "folklore", "food literature", "game", "gay fiction", "gender studies",
    "ghost story", "glbt", "graphic memoir", "hardboiled", "high fantasy", "historical mystery",
    "historical romance", "historical thriller", "interactive", "international",
    "invasion literature", "investigative journalism", "legal thriller", "lesbian fiction",
    "literary fiction", "love story", "magic realism", "maritime", "medieval", "metaphysical",
    "military history", "modernist", "music", "narrative non-fiction", "nature", "neo-noir",
    "new adult", "noir", "occult", "oral history", "paranormal romance", "philosophical fiction",
    "pirate", "political thriller", "postmodern", "lovecraftian horror", "cosmic horror", "prehistory", "comedy horror", "gothic horror","psychological horror",
    "pulp noir", "queer fiction", "quest", "quick reads", "quirky", "regency romance",
    "road novel", "robotics", "rural", "satire", "science fantasy", "self-improvement",
    "serial killer", "slipstream", "socio-political", "space western", "spy thriller",
    "supernatural", "surrealist", "survival", "suspense", "sword and sorcery",
    "techno-thriller", "time travel", "transgressive", "travelogue", "urban", "vampire",
    "victorian", "video game", "virtual reality", "weird fiction", "werewolf",
    "wilderness", "witchcraft", "women's fiction", "world history", "zombie", "teen romance"
]

def generate_training_data(genres):
    training_data = []
    for genre in genres:
        sentence = f"This book falls into the {genre} genre."
        start_idx = sentence.find(genre)
        end_idx = start_idx + len(genre)
        entities = [(start_idx, end_idx, "GENRE")]
        training_data.append((sentence, {"entities": entities}))
    
    return training_data

def save_training_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

training_data = generate_training_data(GENRES)
save_training_data("model_training/training_data/genre_training_data.json", training_data)