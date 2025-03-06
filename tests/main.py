from language_checkers.pos_tagger import POSTagger
from language_checkers.spell_checker import SpellChecker

def main():
    test_POSTagger = POSTagger('the dog is running')
    test_SpellChecker = SpellChecker()

if __name__ == "__main__":
    main()