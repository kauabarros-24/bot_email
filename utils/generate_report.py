from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from io import BytesIO

def wrap_text(text: str, max_width: float, pdf_canvas: canvas.Canvas, font_name: str = "Times-Roman", font_size: int = 12) -> list:
    pdf_canvas.setFont(font_name, font_size)
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        if pdf_canvas.stringWidth(test_line) <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    return lines

def generate_pdf(title: str, text: str, name_person: str, turma: str) -> BytesIO:
    data = [text, name_person, turma]
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4
    margin_left = 40
    margin_right = 40
    margin_top = 50
    margin_bottom = 80

    # Title: User name
    pdf.setFont("Times-Bold", 16)
    pdf.setFillColor(colors.HexColor("#010101"))
    pdf.drawCentredString(width / 2, height - margin_top, title)

    pdf.setFont("Times-Roman", 12)
    pdf.setFillColor(colors.black)

    x = margin_left
    y = height - margin_top - 40  
    text_width = width - margin_left - margin_right

    # Main text
    for line in wrap_text(data[0], text_width, pdf):
        pdf.drawString(x, y, line)
        y -= 20

        if y < margin_bottom:
            pdf.showPage()
            y = height - margin_top

    y -= 20 

    # Name of person (below the text)
    pdf.setFont("Times-Roman", 12)
    name_line = f"Nome: {data[1]}"
    for line in wrap_text(name_line, text_width, pdf):
        pdf.drawString(x, y, line)
        y -= 20

        if y < margin_bottom:
            pdf.showPage()
            y = height - margin_top

    y -= 20 

    # Adding the class (turma) with a slight space
    pdf.setFont("Times-Roman", 12)
    class_line = f"Turma: {data[2]}"
    for line in wrap_text(class_line, text_width, pdf):
        pdf.drawString(x, y, line)
        y -= 20

        if y < margin_bottom:
            pdf.showPage()
            y = height - margin_top

    pdf.save()
    buffer.seek(0)
    return buffer