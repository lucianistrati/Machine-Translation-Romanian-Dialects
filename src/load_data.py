"""
here there should be functions on how to read pdfs, txts and then parse them and clean them so that they are good to
go in the other components
"""
import os

books_folderpath = "data/books"

videos_folderpath = "data/videos"

classes = ["crisanean", "maramuresean", "banatean", "ardelean", "oltean", "moldovean", "muntean"]

class_to_book = {'crisanean': [''],
                 'maramuresean': ["dstef_antologie-de-folclor-din-maramures.pdf"],
                 'banatean': ['Poezi-in-grai-banatean-vol1.pdf'],
                 'ardelean': ['Ion_Pop_Reteganul_Poveti_ardeleneti_Ba.pdf'],
                 'oltean': ['Dilibau. Povesti oltenesti - Cristiana Belodan.pdf'],
                 'moldovean': ['Moldovan_in_Ukraine_01.pdf'],
                 'muntean': ['']}

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
                  'timoc': ['About our village and our language – Timok Romanian (Vlach) Collection.mp4']}

