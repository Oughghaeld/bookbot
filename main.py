import sys
from stats import count_words, count_chars, sort_counts


def main():
    # Se non è specificato alcun argomento, esci
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book_path = sys.argv[1]

    # Specifica il percorso relativo al file frankenstein.txt
    # book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f'============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print(f'----------- Word Count ----------')
    print(f'Found {num_words} total words')

    # Printa i caratteri e il loro conteggio in lowercase
    counts = count_chars(text)
    sorted_counts = sort_counts(counts)
    print('--------- Character Count -------')
    for char, count in sorted_counts.items():
        if char.isalpha():
            print(f'{char}: {count}')
    print('============= END ===============')


def get_book_text(book_path):
    # Apre il file in lettura
    with open(book_path, 'r') as file:
        # Legge il contenuto del file
        text = file.read()
    return text

main()

