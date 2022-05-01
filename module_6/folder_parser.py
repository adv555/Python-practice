import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []

MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []

AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []

DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []

ARCHIVES = []

OTHER = []

REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES
}

EXTENSIONS = set()
UNKNOWN = set()

FOLDERS = []

def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:

    # print(f"folder:", folder)

    for item in folder.iterdir():
        if item.is_dir():
            # print(f"item: {item}, item.name: {item.name}")

            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        # print(f"item: {item}, item.name: {item.name}")

        ext = get_extension(item.name)
        fullname = folder / item.name

        # print(f"ext: {ext}, fullname: {fullname}")

        if not ext:
            OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSIONS[ext]

                # print(f"REGISTER_EXTENSIONS  {REGISTER_EXTENSIONS}")

                # print(f"container: {container}")

                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                OTHER.append(fullname)


if __name__ == '__main__':
    folder_for_scan = sys.argv[1]

    print(f'Start in folder {folder_for_scan}')
    scan(Path(folder_for_scan))
    # print(f'Images jpeg: {JPEG_IMAGES}')
    # print(f'Images jpg: {JPG_IMAGES}')
    # print(f'Images svg: {SVG_IMAGES}')
    # print(f'Audio mp3: {MP3_AUDIO}')
    # print(f'Archives: {ARCHIVES}')

    print(f'Types of files in folder: {EXTENSIONS}')
    print(f'Unknown files of types: {UNKNOWN}')
    print(f'Folders files of types: {FOLDERS}')
    # print(f'Other files of types:: {OTHER}')

    # print(FOLDERS[::-1])  

