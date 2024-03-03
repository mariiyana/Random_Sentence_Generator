import random

names = ["Rocky", "Lucky", "Archie", "Lola"]
places = ["Mallorca", "Madrid", "Sofia", "Vienna"]
verbs = ["eats", "drinks", "plays with", "study"]
nouns = ["computer", "apple", "ball", "scissors", "bikes"]
adverbs = ["perfectly", "rapidly", "warmly", "quickly", "loudly"]
details = ["at the stadium", "at home", "in the dog park", "on the road", "on mars"]


def get_random_sentence(words):
    return random.choice(words)


input("Hello this is you first random sentence.")
while True:
    random_name = get_random_sentence(names)
    random_places = get_random_sentence(places)
    random_verbs = get_random_sentence(verbs)
    random_nouns = get_random_sentence(nouns)
    random_adverbs = get_random_sentence(adverbs)
    random_details = get_random_sentence(details)

    print(f"{random_name} from {random_places} {random_verbs} {random_nouns} {random_adverbs} {random_details}.")
    input("Click [Enter] to generate a new one.")