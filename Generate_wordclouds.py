import matplotlib.pyplot as plt
from wordcloud import WordCloud
def generate_wordcoud(data):

    plt.figure(figsize=(20,20))
    plt.imshow(WordCloud().generate(data))
    plt.show()
