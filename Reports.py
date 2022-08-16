import webbrowser
from reportlab.pdfgen import canvas

class Reports():
    def show_pdf(self):
        webbrowser.open('client.pdf')

    def client_pdf(self):
        self.canvas = canvas.Canvas('client.pdf')

        self.num = self.number_entry.get() 
        self.name = self.name_entry.get() 
        self.phone = self.phone_entry.get() 
        self.city = self.city_entry.get()
        self.status = self.status_var.get()
        self.age = self.age_entry.get()  

        self.canvas.setFont('Helvetica-Bold', 24)
        self.canvas.drawString(200, 790, 'Client Report')

        self.canvas.setFont('Helvetica-Bold', 18)
        self.canvas.drawString(50, 700, 'Number:')
        self.canvas.drawString(50, 670, 'Name:')
        self.canvas.drawString(50, 640, 'Phone:')
        self.canvas.drawString(50, 610, 'City:')
        self.canvas.drawString(50, 580, 'Marital Status:')
        self.canvas.drawString(50, 550, 'Age:')

        self.canvas.setFont('Helvetica', 18)
        self.canvas.drawString(130, 700, self.num)
        self.canvas.drawString(120, 670, self.name)
        self.canvas.drawString(120, 640, self.phone)
        self.canvas.drawString(100, 610, self.city)
        self.canvas.drawString(180, 580, self.status)
        self.canvas.drawString(100, 550, self.age)

        self.canvas.rect(20, 490, 550, 5, False, True)
        self.canvas.rect(20, 750, 550, 5, False, True)

        self.canvas.showPage()
        self.canvas.save()
        self.show_pdf()
