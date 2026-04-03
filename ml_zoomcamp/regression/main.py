from zipfile import ZipFile
from pathlib import Path
import os

def main():
    os.system("clear")

    ROOT = Path(__file__).parent
    caminho_zip = ROOT / "data.csv.zip"

    #Acessando os arquivos do zip
    with ZipFile(caminho_zip,"r") as zip:
        for file in zip.namelist():
            print(file)
    
    #Desempacotando o zip
    with ZipFile(caminho_zip,"r") as zip:
        zip.extractall(ROOT)

if __name__ == "__main__":
    main()