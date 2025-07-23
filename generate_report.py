import pandas as pd
from fpdf import FPDF

# Load data (recreate the assumed CSV)
data = {
    "Date": ["2024-07-01", "2024-07-02", "2024-07-03", "2024-07-04", "2024-07-05"],
    "Sales": [150, 200, 180, 220, 300]
}
df = pd.DataFrame(data)

# Calculate descriptive statistics
sales_stats = df['Sales'].describe()

# Initialize PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Automated Sales Report', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add descriptive statistics
pdf.cell(0, 10, "Descriptive Statistics:", ln=True)

# Placeholder formatting for "Date" (assuming string type; may not be meaningful numerically)
pdf.cell(0, 10,
         f"Date: count={len(df):.2f}, mean=.2f, min=.2f, 25%=.2f, 50%=.2f, 75%=.2f, max=.2f, std=nan", ln=True)

# Real stats for "Sales"
pdf.cell(0, 10,
         f"Sales: count={sales_stats['count']:.2f}, mean={sales_stats['mean']:.2f}, min={sales_stats['min']:.2f}, "
         f"25%={sales_stats['25%']:.2f}, 50%={sales_stats['50%']:.2f}, 75%={sales_stats['75%']:.2f}, "
         f"max={sales_stats['max']:.2f}, std={df['Sales'].std():.2f}", ln=True)

# Save the PDF
pdf.output("final_report.pdf")
print("✅ Report generated successfully: final_report.pdf")
