from docx import Document
from docx.shared import Pt
from docx.enum.style import WD_STYLE_TYPE
import subprocess

def testPrint():
    print("Connected to formatter")

def formatDocument(userInfo):
    doc = Document("CivilReviewEN.docx")
    styles = doc.styles
    style = styles.add_style('Insertion', WD_STYLE_TYPE.PARAGRAPH)
    style = doc.styles['Insertion']
    font = style.font
    font.name = 'Helvetica'
    font.size = Pt(18)

    print("Creating Document using this info")
    print(userInfo)
    
    for paragraph in doc.paragraphs:
        
        if '[DATE]' in paragraph.text:
            paragraph.style = 'Insertion'
            paragraph.text = '4/08/21'


        if '[NAME]' in paragraph.text:
            paragraph.style = 'Insertion'
            paragraph.text = 'Applicant: {}'.format(userInfo["userName"])

        if '[QUALIFYSTATUS]' in paragraph.text:
            paragraph.style = 'Insertion'
            paragraph.text = 'Result : QUALIFY'

        if '[Q1Part1]' in paragraph.text:
            paragraph.text = "You {} know or {} heard of any of the suspects and witnesses.".format("Do", "Have")


        if '[Q2]' in paragraph.text:
            paragraph.text = "You think the U.S. is {} in the racial constructs of the D.R..".format(userInfo["a2"])

        if '[Q3]' in paragraph.text:
            q3Answer = 'How other see and identify you'
            paragraph.text = "For you, {} affects your material conditions.".format(userInfo["a3"])

        if '[Q4]' in paragraph.text:
            q4Answer = 'High'
            paragraph.text = "Your weekly sugar intake is {}.".format(userInfo["sugarIntake"])

        if '[XX%]' in paragraph.text:
            paragraph.style = 'Insertion'
            populationPercentage = 38
            paragraph.text = '{}% White Population'.format(populationPercentage)

        if '[YY%]' in paragraph.text:
            paragraph.style = 'Insertion'
            populationPercentage = '55'
            paragraph.text = '{}% Median Income'.format(populationPercentage)


        if '[ZZ%]' in paragraph.text:
            paragraph.style = 'Insertion'
            unemploymentRate = '15'
            paragraph.text = '{}% Unemployment rate'.format(unemploymentRate)




    doc.save('{}.docx'.format(userInfo["userName"]))
    subprocess.run(["libreoffice","--headless","--convert-to","pdf","{}.docx".format(userInfo["userName"])])
    subprocess.run(["lp","-d","myprinter","{}.pdf".format(userInfo["userName"])])
if __name__ == "__main__":
   formatDocument({
  "userName": "Bertram Ross",
  "userId": "",
  "a1": "",
  "a2": "How other see and identify you",
  "a3": "Material Conditions",
  "zipcode": "",
  "sugarIntake":"High",
  "archivePermission":""
})