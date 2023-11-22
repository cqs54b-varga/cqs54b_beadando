# kodolas.py

def karakterkonvertalas(tartalom, forras_encoding, cel_encoding):
    try:
        dekodolas = tartalom.encode(forras_encoding).decode(cel_encoding, errors='ignore')
        return dekodolas
    except UnicodeDecodeError:
        print("Hiba a karakterkódolás konverziójában.")
        return None
