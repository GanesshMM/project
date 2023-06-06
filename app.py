from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage
import fpdf
import mimetypes

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('form.html')

@app.route('/apply', methods=['GET', 'POST'])
def index():
    data = request.form
    form_values = list(data.values())
    keys = ["Name", "Registeration Number", "Phone Number", "Email", "Department", "Address", "Leaving Date","Leaving Time", "Arriving Date", "Arriving Time"]

    email = data['email']
    sender = "ganessh7114@gmail.com"
    password = "krvqssopqhulecul"

    pdf_file = "Outing Form.pdf"
    fill_pdf(pdf_file, form_values, keys)

    msg = EmailMessage()
    msg.set_content('This is the email body.')

    mime_type, _ = mimetypes.guess_type(pdf_file)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(pdf_file, 'rb') as pdf_fil:
        msg.add_attachment(pdf_fil.read(), maintype=mime_type, subtype=mime_subtype, filename='file.pdf')


    msg['Subject'] = 'Test Email'
    msg['From'] = sender
    msg['To'] = email

    # Connect to the SMTP server
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()

    # Login to your email account
    smtp.login(sender, password)

    # Send the email
    smtp.send_message(msg)

    # Disconnect from the SMTP server
    smtp.quit()

    return render_template('index.html', data=data, pdf_file=pdf_file)

def fill_pdf(pdf_file, values, keys):
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=21, style='BU')
    pdf.cell(190, 20, txt="R.M.K College Of Engineering And Technology", ln=1, align="C")
    pdf.cell(190, 20, txt="Outing Form", ln=3, align="C")
    pdf.cell(190, 13, txt="", ln=4, align="C")
    for key, value in zip(keys, values):
        pdf.set_font("Times", style='BU', size=17)
        pdf.cell(77, 14, txt=key, ln=0, align="L")
        pdf.set_font("Times", size=15)
        pdf.cell(73, 14, txt=value, ln=1, align="L")
    pdf.cell(220, 50, txt="", ln=3, align="C")
    pdf.set_font("Times", style='B', size=17)
    pdf.cell(50, 13, txt="H.O.D", ln=0, align="C")
    pdf.set_font("Times", style='B', size=17)
    pdf.cell(65, 13, txt="Class Counsellor", ln=0, align="C")
    pdf.set_font("Times", style='B', size=17)
    pdf.cell(75, 13, txt="Branch Co-Ordinator", ln=1, align="C")
    pdf.output(pdf_file, "F")

if __name__ == '__main__':
    app.run(debug=True)


