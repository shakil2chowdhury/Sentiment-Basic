#NLP - Natural Language Processing - Analysing Emotions/Sentiments

import string
from collections import Counter

import matplotlib.pyplot as plt

#1. Create a text file and read those text from that
text = open('read.txt', encoding='utf-8').read()
#2. Convert all the words into lowercase letters
lower_case = text.lower()
#3. Remove all the punctuations
clean_text = lower_case.translate(str.maketrans('','',string.punctuation))
#4. Tokenize and split the words
tokenized_words = clean_text.split()
#5. Stop words list
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

# NLP Emotion Algorithm

# 1) Checking if words from the final word list are also present in emotion.txt
#    - Opening the emotion file
#    - Looping through each line and parsing it
#    - Extracting the word and emotion using the split operation

# 2) If a word is present, adding the corresponding emotion to the emotion_list
# 3) Finally, counting the occurrences of each emotion in the emotion_list
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

    print(emotion_list)
    w = Counter(emotion_list)
    print(w)

    #Emotions in a graph using MatplotLib
    fig, ax1 = plt.subplots()
    ax1.bar(w.keys(), w.values())
    fig.autofmt_xdate()
    plt.savefig('graph.png')
    plt.show()





