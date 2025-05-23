import csv

def save_to_csv(rows, path):
    """
    Salva várias linhas em CSV.
    
    Parâmetros:
    - rows: lista de listas/tuplas, onde cada item interno representa as colunas de uma linha.
    - path: caminho do arquivo CSV.
    """
    with open(path, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)