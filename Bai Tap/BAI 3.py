import json
data = {
    "book1": "30k",
    "book2": "50k",
    "book3": "100k"
}
with open("books.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)