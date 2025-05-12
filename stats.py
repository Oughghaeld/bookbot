def count_words(text):
    # Divide il testo in parole
    words = text.split()
    return len(words)

def count_chars(text):
    # Conta i caratteri nel testo
    counts = {}
    for char in text:
        # Converte il carattere in minuscolo
        char_lower = char.lower()
        counts[char_lower] = counts.get(char_lower, 0) + 1
    return counts

def sort_counts(counts):
    # Ordina i conteggi in ordine decrescente
    sorted_keys = sorted(counts.keys())
    sorted_counts = {key: counts[key] for key in sorted_keys}
    return sorted_counts