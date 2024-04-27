from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def create_pdf(filename, data):
    # Create a PDF document
    pdf = SimpleDocTemplate(filename, pagesize=letter)
    
    # Add data to the table
    table_data = []
    for row in data:
        table_data.append(row)
    
    # Define table style
    table_style = TableStyle([('BACKGROUND', (0,0), (-1,0), colors.grey),
                              ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                              ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                              ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                              ('BOTTOMPADDING', (0,0), (-1,0), 12),
                              ('BACKGROUND', (0,1), (-1,-1), colors.beige),
                              ('GRID', (0,0), (-1,-1), 1, colors.black)])
    
    # Create table object
    table = Table(table_data)
    table.setStyle(table_style)
    
    # Add table to the PDF document
    pdf.build([table])

#Example data for the table
# data = [
#     ['Name', 'Age', 'Country'],
#     ['John Doe', 30, 'USA'],
#     ['Jane Smith', 25, 'Canada'],
#     ['Ahmed Khan', 35, 'Pakistan']
# ]

# # Create the PDF
# create_pdf("table.pdf", data)

# Example timetable data


# Create the PDF for the timetable
#create_timetable_pdf("timetable.pdf", timetable_data)
