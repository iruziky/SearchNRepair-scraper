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

def save_product_data(product_data_list, path="products.csv"):
    fields = [
        "link", "title", "price", "category", "brand", "model",
        "condition", "memory", "color", "battery_life", "description", "images"
    ]

    with open(path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(fields)

        for product_data in product_data_list:
            images = product_data.get("images", [])
            images_str = ";".join(images) if images else ""

            row = [
                product_data.get(field, "").replace("\n", " ") if field != "images" else images_str
                for field in fields
            ]

            writer.writerow(row)
