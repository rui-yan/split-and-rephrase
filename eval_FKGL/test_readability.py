import unittest
from readability import Readability


fname="/Users/ruiyan/Documents/GitHub/NLP/pred_ref_eval/pred_websplit2_clean.txt"

with open(fname, 'r') as file:
    text = file.read()

readability = Readability(text)

def test_ari():
    r = readability.ari()
    print(r)
    assertEqual(9.551245421245422, r.score)
    assertEqual(['10'], r.grade_levels)
    assertEqual([15, 16], r.ages)

def test_coleman_liau():
    r = readability.coleman_liau()
    print(r)
    assertEqual(10.673162393162393, r.score)
    assertEqual('11', r.grade_level)

def test_dale_chall():
    r = readability.dale_chall()
    print(r)
    assertEqual(9.32399010989011, r.score)
    assertEqual(['college'], r.grade_levels)

def test_flesch():
    r = readability.flesch()
    print(r)
    assertEqual(51.039230769230784, r.score)
    assertEqual(['10', '11', '12'], r.grade_levels)
    assertEqual('fairly_difficult', r.ease)

def test_flesch_kincaid():
    r = readability.flesch_kincaid()
    print(r)

def test_gunning_fog():
    r = readability.gunning_fog()
    print(r)
    assertEqual(12.4976800976801, r.score)
    assertEqual('12', r.grade_level)

def test_linsear_write():
    r = readability.linsear_write()
    print(r)
    assertEqual(11.214285714285714, r.score)
    assertEqual('11', r.grade_level)

def test_smog():
    text = """
    In linguistics, the Gunning fog index is a readability test for English writing. The index estimates the years of formal education a person needs to understand the text on the first reading. For instance, a fog index of 12 requires the reading level of a United States high school senior (around 18 years old). The test was developed in 1952 by Robert Gunning, an American businessman who had been involved in newspaper and textbook publishing.
    The fog index is commonly used to confirm that text can be read easily by the intended audience. Texts for a wide audience generally need a fog index less than 12. Texts requiring near-universal understanding generally need an index less than 8.
    """
    text = ' '.join(text for i in range(0, 5))

    readability = Readability(text)
    r = readability.smog()

    print(r)
    assertEqual(12.516099999999998, r.score)
    assertEqual('13', r.grade_level)

def test_spache():
    r = readability.spache()
    print(r)
    assertEqual(7.164945054945054, r.score)
    assertEqual('7', r.grade_level)

def test_print_stats():
    stats = readability.statistics()
    print(stats['num_sentences'])
    # assertEqual(562, stats['num_letters'])
    # assertEqual(117, stats['num_words'])
    # assertEqual(7, stats['num_sentences'])
    # assertEqual(20, stats['num_polysyllabic_words'])

test_flesch_kincaid()
