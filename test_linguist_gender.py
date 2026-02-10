
import spacy

try:
    nlp = spacy.load("es_core_news_sm")
    print("Loaded model")
except:
    print("Model not found")
    exit()

text = "Tengo la camisa negra y el amor duele. La pena es grande."
doc = nlp(text)

print(f"Analyzing: {text}")
for token in doc:
    if token.pos_ == "NOUN":
        gender = token.morph.get("Gender")
        print(f"Noun: {token.text}, Gender: {gender}, Lemma: {token.lemma_}")
