from audioop import reverse
from collections import Counter

def analyzeText(text):

    paragraphs = text.split('\n')
    sentences = text.split('.')
    words = text.replace('\n', ' ').split(' ')
    print(f"Liczba akapitów: {len(paragraphs)}")
    print(f"Liczba zdań: {len(sentences)}")
    print(f"Liczba słów: {len(words)}")
    print(f"Liczba znaków: {len(text)}")


    #slowa wystepujace najczesciej z wykluczeniem stop words

    stop_words = {'a','w','z','i','o','the','or','to'}
    filtered_words = filter(lambda word: word not in stop_words, words)

    word_count = Counter(filtered_words)

    most_common = word_count.most_common(3)
    print(f"Najczęstsze słowa: {most_common}")

    #odracanie wyrazow rozpoczynajacych sie na a
    reverseAWords = [word[::-1] if word.startswith('a') else word for word in words]
    print(f"Odwrócone słowo rozpoczynające się na 'a': {' '.join(reverseAWords)}")


text = """
apple
apple
apple
apple
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy 
text ever since the 1500s, when an unknown printer took a galley of type and scrambled it 
to make a type specimen book."""

analyzeText(text)