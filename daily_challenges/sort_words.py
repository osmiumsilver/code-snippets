def sort_words(sequence):
    listo = sequence.split(' ')
    listo.sort(key=str.casefold())
    return ' '.join(listo)