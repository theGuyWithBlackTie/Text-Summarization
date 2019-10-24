#from rogue.rogue import rouge_n_sentence_level
from rouge.rouge import rouge_l_sentence_level,rouge_n_sentence_level,rouge_w_sentence_level

file = open('summary.txt', 'r')
summary_sentence = file.read().split()

file = open('data\summary\\005.txt', 'r')
reference_sentence = file.read().split()

# Calculate ROUGE-2
recall, precision, rouge = rouge_n_sentence_level(summary_sentence, reference_sentence, 1)
print('ROUGE-2-R', recall)
print('ROUGE-2-P', precision)
print('ROUGE-2-F', rouge)

ans = rouge_l_sentence_level(summary_sentence, reference_sentence)
print(ans)

ans2 = rouge_w_sentence_level(summary_sentence, reference_sentence, 2)
print(ans2)