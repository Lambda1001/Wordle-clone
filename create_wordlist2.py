def filter_five_letter_words(input, output):
    with open(input, 'r', encoding="utf-8") as f_in:
        words = [word.strip() for word in f_in.readlines() if len(word.strip()) == 6]
    with open(output, 'w', encoding="utf-8")as f_out:
        f_out.write('\n'.join(words))
input = "complete.txt"
output = "wordlist2.txt"

filter_five_letter_words(input, output)
