"""
here there should be functions on how to read pdfs, txts and then parse them and clean them so that they are good to
go in the other components
"""
import os

books_folderpath = "data/books"

videos_folderpath = "data/videos"

classes = ["crisanean", "maramuresean", "banatean", "ardelean", "oltean", "moldovean", "muntean", "timocean"]

class_to_book = {'crisanean': [''],
                 'maramuresean': ["dstef_antologie-de-folclor-din-maramures.pdf"],
                 'banatean': ['Poezi-in-grai-banatean-vol1.pdf'],
                 'ardelean': ['Ion_Pop_Reteganul_Poveti_ardeleneti_Ba.pdf'],
                 'oltean': ['Dilibau. Povesti oltenesti - Cristiana Belodan.pdf'],
                 'moldovean': ['Moldovan_in_Ukraine_01.pdf'],
                 'muntean': [''],
                 "timocean": [""]}

class_to_video = {'crisanean': [''],
                  'maramuresean': [''],
                  'banatean': [''],
                  'ardelean': ['Curs de dialect ardelenesc!.mp4',
                               'Curs de dialect ardelenesc!suduieli si blesteme!.mp4'],
                  'oltean': [''],
                  'moldovean': ["Stirile in limba moldoveneasca.mp4",
                                'Igor Dodon explică strategia prin care doreşte să mute graniţa dintre România şi Republica Moldova.mp4',
                                "Vox pop Unirea cu România şi preţul ei.mp4",
                                "Vox populi Tinerii despre România şi Unire.mp4"],
                  'muntean': [''],
                  'timocean': ['About our village and our language – Timok Romanian (Vlach) Collection.mp4']}


video_to_alias = {'Curs de dialect ardelenesc!.mp4': 'ardelenesc.txt',
                  'Curs de dialect ardelenesc!suduieli si blesteme!.mp4': 'ardelenesc_suduieli.txt',
                  'Stirile in limba moldoveneasca.mp4': 'stiri_moldoveneasca.txt',
                  'Igor Dodon explică strategia prin care doreşte să mute graniţa dintre România şi Republica Moldova.mp4': 'dodon.txt',
                  'Vox pop Unirea cu România şi preţul ei.mp4': 'vox_pop_pretul_unirii.txt',
                  'Vox populi Tinerii despre România şi Unire.mp4': 'vox_pop_romania_unire.txt',
                  'About our village and our language – Timok Romanian (Vlach) Collection.mp4': 'timok.txt'}

def remove_diacritics(text: str):
    diacritics = "ăâîșțĂȘȚÎÂ"
    for d in diacritics:
        text = text.replace(d, "")
    return text


def load_data(filepath: str, to_str: bool = False, strip: bool = False, no_diacritics: bool = False):
    print(filepath)
    if filepath.endswith('.txt'):
        texts = []
        if "vatis" in filepath:
            with open(filepath, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if len(line) > 0 and line.startswith("[") is False:
                        if strip:
                            line = line.strip()
                            while "  " in line:
                                line = line.replace("  ", "")
                            line = line.replace("\n", "")
                        if no_diacritics:
                            line = remove_diacritics(line)
                        texts.append(line)
        elif "sonix" in filepath:
            with open(filepath, "r") as f:
                lines = f.readlines()
                # print(len(lines))
                for line in lines:
                    line = line[line.find(" "):]
                    tokens = [token for token in line.split()
                              if token.startswith("[") is False
                              and token.endswith("]") is False]
                    line = " ".join(tokens)
                    if strip:
                        line = line.strip()
                        while "  " in line:
                            line = line.replace("  ", "")
                        line = line.replace("\n", "")
                    if no_diacritics:
                        line = remove_diacritics(line)
                    texts.append(line)
        elif "annotations" in filepath:
            with open(filepath, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if len(line) > 0:
                        if strip:
                            line = line.strip()
                            while "  " in line:
                                line = line.replace("  ", "")
                            line = line.replace("\n", "")
                        if no_diacritics:
                            line = remove_diacritics(line)
                        texts.append(line)
        if to_str:
            return " ".join(texts)
        return texts
    elif filepath.endswith('.pdf'):
        # importing required modules
        from PyPDF2 import PdfReader
        # creating a pdf reader object
        reader = PdfReader(filepath)
        # printing number of pages in pdf file
        whole_text = []
        for page in reader.pages:
            # extracting text from page
            text = page.extract_text()
            # print(text)
            whole_text.append(text)
        if to_str:
            return " ".join(whole_text)
        # print(len(whole_text))
        return whole_text
    else:
        raise Exception("Unsupported format!")


def main():
    books_contents = []
    for file in sorted(os.listdir("data/books")):
        filepath = os.path.join("data/books", file)
        texts = load_data(filepath)
        books_contents.append(texts)

    print(len(books_contents))

    with open("data/all_books_contents.txt", "w") as f:
        f.write(str(books_contents))

    sonix_transcriptions = []
    for file in sorted(os.listdir("data/transcriptions/sonix")):
        filepath = os.path.join("data/transcriptions/sonix/", file)
        texts = load_data(filepath)
        sonix_transcriptions.append(texts)

    print(len(sonix_transcriptions))

    with open("data/transcriptions/sonix_transcriptions.txt", "w") as f:
        f.write(str(sonix_transcriptions))

    vatis_transcriptions = []
    for file in sorted(os.listdir("data/transcriptions/vatis_tech")):
        filepath = os.path.join("data/transcriptions/vatis_tech/", file)
        texts = load_data(filepath)
        vatis_transcriptions.append(texts)

    print(len(vatis_transcriptions))

    with open("data/transcriptions/vatis_transcriptions.txt", "w") as f:
        f.write(str(vatis_transcriptions))


if __name__ == "__main__":
    main()
