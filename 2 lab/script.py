import json
import pandas as pd

with open("data.json", "r") as i:
    data = json.load(i)

# for item in data:
#     print(item["name"], item["quantity"], item["price"])

# df = pd.DataFrame(data)

# df.to_excel("data.xlsx", index=False)

# df = pd.read_excel("data.xlsx")

# df = df.sort_values(by="price", ascending=False)

# df.to_excel("sorted.xlsx", index=False)

# print("Файл products.xlsx отсортирован")

# from docx import Document

# doc = Document()

# doc.add_heading("Исходные данные", level=1)

# table = doc.add_table(rows=1, cols=3)
# table.style = "Table Grid"
# table.rows[0].cells[0].text = "Name"
# table.rows[0].cells[1].text = "Quantity"
# table.rows[0].cells[2].text = "Price"

# for item in data:
#     cells = table.add_row().cells
#     cells[0].text = str(item["name"])
#     cells[1].text = str(item["quantity"])
#     cells[2].text = str(item["price"])

# doc.add_heading("Итоги", level=1)

# total = sum(i["quantity"] * i["price"] for i in data)
# doc.add_paragraph(f"Общая сумма: {total}")

# max_item = max(data, key=lambda x: x["price"])
# doc.add_paragraph(f"Самая дорогая позиция: {max_item['name']} ({max_item['price']})")

# doc.save("report.docx")

from datetime import date
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader, PdfWriter
import io


TEMPLATE = "report.pdf"
OUTPUT   = "filled_report.pdf"

total = sum(i["quantity"] * i["price"] for i in data)
max_item = max(data, key=lambda x: x["price"])

total_value = str(total)
expensive_item = f"{max_item['name']} ({max_item['price']})"
today = date.today().strftime("%Y-%m-%d")

packet = io.BytesIO()
c = canvas.Canvas(packet, pagesize=A4)
c.setFont("Helvetica-Bold", 12)

c.drawString(50, 400, total_value)
c.drawString(50, 130, expensive_item)
c.drawString(50, 110, f"Date: {today}")

c.save()
packet.seek(0)

reader = PdfReader(TEMPLATE)
writer = PdfWriter()
page = reader.pages[0]
overlay = PdfReader(packet).pages[0]
page.merge_page(overlay)
writer.add_page(page)

with open(OUTPUT, "wb") as f:
    writer.write(f)

print(f"Создан {OUTPUT}")