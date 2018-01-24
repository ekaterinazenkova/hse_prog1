
import random
def get_word(filename):
    word=""
    with open ("filename", "r", encoding="utf-8") as f:
        word = f.readline()
        word = word.split()
        word = random.choice(word)
        return word
print(get_word("Line_1_verb.txt")+" "+get_word("Line_1_prep.txt")+" "+get_word("Line_1_noun.txt")+'\n'+get_word("Line_2_verb.txt")+" "+get_word("Line_2_prep.txt")+" "+get_word("Line_2_noun.txt")+'\n'+get_word("Line_3_verb.txt")+" "+get_word("Line_3_noun.txt"))

