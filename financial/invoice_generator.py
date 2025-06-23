from fpdf import FPDF
from datetime import datetime

class InvoicePDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "INVOICE", ln=True, align="C")
        self.ln(10)

    def add_invoice_details(self, client, invoice_no, date):
        self.set_font("Arial", "", 12)
        self.cell(0, 10, f"Client: {client}", ln=True)
        self.cell(0, 10, f"Invoice No: {invoice_no}", ln=True)
        self.cell(0, 10, f"Date: {date}", ln=True)
        self.ln(10)

    def add_items(self, items):
        self.set_font("Arial", "B", 12)
        self.cell(80, 10, "Item", border=1)
        self.cell(40, 10, "Quantity", border=1)
        self.cell(40, 10, "Price", border=1)
        self.cell(30, 10, "Total", border=1, ln=True)

        self.set_font("Arial", "", 12)
        total_cost = 0
        for item in items:
            name, qty, price = item
            total = qty * price
            total_cost += total
            self.cell(80, 10, name, border=1)
            self.cell(40, 10, str(qty), border=1)
            self.cell(40, 10, f"₹{price:.2f}", border=1)
            self.cell(30, 10, f"₹{total:.2f}", border=1, ln=True)

        self.ln(5)
        self.set_font("Arial", "B", 12)
        self.cell(160, 10, "Grand Total:", border=0)
        self.cell(30, 10, f"₹{total_cost:.2f}", border=1, ln=True)

def get_invoice_data():
    client = input("Enter client name: ")
    invoice_no = input("Enter invoice number: ")
    date = input("Enter date (YYYY-MM-DD): ") or datetime.now().strftime("%Y-%m-%d")

    items = []
    while True:
        name = input("Item name (or 'done'): ")
        if name.lower() == 'done':
            break
        try:
            qty = int(input("Quantity: "))
            price = float(input("Price per unit (₹): "))
            items.append((name, qty, price))
        except ValueError:
            print(" Invalid quantity or price. Try again.")

    return client, invoice_no, date, items

def generate_invoice_pdf(client, invoice_no, date, items):
    pdf = InvoicePDF()
    pdf.add_page()
    pdf.add_invoice_details(client, invoice_no, date)
    pdf.add_items(items)

    filename = f"invoice_{invoice_no}.pdf"
    pdf.output(filename)
    print(f"\n Invoice saved as '{filename}'")

if __name__ == "__main__":
    print(" Invoice Generator CLI")
    print("-" * 30)
    client, invoice_no, date, items = get_invoice_data()
    generate_invoice_pdf(client, invoice_no, date, items)
