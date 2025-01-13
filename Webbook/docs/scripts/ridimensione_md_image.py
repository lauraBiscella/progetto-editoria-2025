import os
import re
from PIL import Image

def ridimensiona_immagini(markdown_file, larghezza_nuova, altezza_nuova):
    # Apri il file markdown
    with open(markdown_file, 'r', encoding='utf-8') as file:
        contenuto = file.read()

    # Trova tutte le immagini nel markdown usando regex
    immagini = re.findall(r'!\[.*?\]\((.*?)\)', contenuto)

    # Itera sulle immagini trovate
    for immagine in immagini:
        if os.path.exists(immagine):
            # Apri l'immagine
            with Image.open(immagine) as img:
                # Ridimensiona l'immagine alla larghezza e altezza specificate
                img = img.resize((larghezza_nuova, altezza_nuova))
                # Salva l'immagine con lo stesso nome
                img.save(immagine)
                print(f"Immagine {immagine} ridimensionata a {larghezza_nuova}x{altezza_nuova} px")
        else:
            print(f"Immagine {immagine} non trovata!")

    # Salva il contenuto markdown modificato (se necessario)
    # with open("modified_" + markdown_file, 'w') as file:
    #     file.write(contenuto)

# Esegui lo script
if __name__ == "__main__":
    markdown_file = 'index.md'  # Sostituisci con il tuo file markdown
    larghezza_nuova = 1000 # La larghezza desiderata per le immagini (in pixel)
    altezza_nuova = 100 # L'altezza desiderata per le immagini (in pixel)
    ridimensiona_immagini(markdown_file, larghezza_nuova, altezza_nuova)
