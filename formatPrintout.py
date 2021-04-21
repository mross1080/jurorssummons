from docx import Document
from docx.shared import Pt
from docx.enum.style import WD_STYLE_TYPE
import subprocess
import json
import datetime
import random


def testPrint():
    print("Connected to formatter")


answer_lookup = {
    "en": {
        "a1": {
            "1": "Do",
            "2": "Have",
            "Yes!": "Do",
            "No!": "Have"
        },
        "a2": {
            "1": "Fully Implicated",
            "2": "Modestly Implicated",
            "3": "Slightly Implicated",
            "4": "Not Implicated At All"
        },
        "a3": {
            "1": "How you see and identify yourself",
            "2": "How others see and identify you",
            "3": "How you see yourself and how others see you",
            "4": "nothing"
        },
        "sugarIntake": {
            "1": "High",
            "2": "Medium",
            "3": "Low",
            "4": "None"
        }
    },
    "es": {
        "a1": {
            "1": "conoce o ha oído",
            "2": "no conoce y no ha oído",
            "Yes!": " conoce o ha oído",
            "No!": " no conoce y no ha oído"
        },
        "a2": {
            "1": "Totalmente implicado",
            "2": "Modestamente implicado",
            "3": "Ligeramente implicado",
            "4": "Para nada implicado"
        },
        "a3": {
            "1": "Cómo te ves e identificas",
            "2": "Como otres te ven e identifican",
            "3": "Todo lo anterior",
            "4": "Ninguna de las anteriores"
        },
        "sugarIntake": {
            "1": "Alto",
            "2": "Medio",
            "3": "Bajo",
            "4": "Ninguno"
        }
    }
}


zipcode_data_lookup = {}


with open('/home/pi/zipcode_data.txt') as json_file:
    zipcode_data_lookup = json.load(json_file)


def formatDocument(userInfo):
    print("Startomg")

    doc = Document("/home/pi/CivilReviewEN.docx")
    lang = userInfo["lang"]
    if userInfo["lang"] == "es":
        doc = Document("/home/pi/CivilReviewES.docx")

    data_for_zip = zipcode_data_lookup[userInfo["zipcode"]]
    print(data_for_zip)
    styles = doc.styles
    style = styles.add_style('Insertion', WD_STYLE_TYPE.PARAGRAPH)
    style = doc.styles['Insertion']
    font = style.font
    font.name = 'Helvetica'
    font.size = Pt(18)

    print("Creating Document using this info")
    print(userInfo)
    random_data_points = random.sample(range(1, len(data_for_zip)), 3)
    print(random_data_points)
    for paragraph in doc.paragraphs:
        # print(paragraph.text)

        if '[DATE]' in paragraph.text:
            paragraph.style = 'Insertion'
            paragraph.text =f"{datetime.datetime.now():%m-%d-%Y}" 

        if '[NAME]' in paragraph.text:
            paragraph.style = 'Insertion'
            paragraph.text = 'Applicant: {}'.format(userInfo["userName"])

        if '[QUALIFYSTATUS]' in paragraph.text:
            paragraph.style = 'Insertion'
            paragraph.text = 'Result : DISQUALIFY'

        if '[Q1Part1]' in paragraph.text:
            q1Answer = answer_lookup[lang]["a1"][userInfo["a1"]]
            q1Part1Answer = "[Do]" if q1Answer == "1" else "[Don't]"
            q1Part2Answer = "[Have]" if q1Answer == "1" else ""


            if lang == "en":
                paragraph.text = "You {} know or have {} heard of any of the suspects and witnesses.  An impartial reviewer wouldn’t know or heard of the suspects and witnesses.".format(
                    q1Part1Answer, q1Part2Answer)
            else:
                q1Answer = answer_lookup[lang]["a1"][userInfo["a1"]]
                paragraph.text = "Usted [{}] de los testigos o los sospechosos.".format(q1Answer)

        if '[Q2]' in paragraph.text:
            questionTwoAnswer = answer_lookup[lang]["a2"][userInfo["a2"]]

            paragraph.text = "You think the U.S. is [{}] in the racial constructs of the D.R..  An impartial would recognize that the U.S.A. is a cultural, economic, and political hegemonic imperial power.".format(
                questionTwoAnswer)
            if lang == "es":
                paragraph.text = "Usted cree que los Estados Unidos está [{}] en las construcciones raciales de R.D.".format(questionTwoAnswer)

        if '[Q3]' in paragraph.text:
            questionThreeAnswer = answer_lookup[lang]["a3"][userInfo["a3"]]

            paragraph.text = "For you, [{}] affects your material conditions.  An impartial reviewer will understand the 'othering' mechanisms as tools of control. ".format(questionThreeAnswer)
            if lang == "es":
                paragraph.text = "Para usted, [{}] afecta sus condiciones materiales.".format(questionThreeAnswer)

        if '[Q4]' in paragraph.text:
            questionFourAnswer = answer_lookup[lang]["sugarIntake"][userInfo["sugarIntake"]]
            paragraph.text = "Your weekly sugar intake is {}.  An impartial reviewer would not consume any sugar.".format(
                answer_lookup[lang]["sugarIntake"][userInfo["sugarIntake"]])
            if lang == "es":
                paragraph.text = "Su consumo semanal de azúcar es [{}].".format(questionFourAnswer)

        if '[XX%]' in paragraph.text:
            print("Setting Random Value 1")
            paragraph.style = 'Insertion'

            print(data_for_zip[random_data_points[0]])
            paragraph.text = data_for_zip[random_data_points[0]]


        if '[$YY]' in paragraph.text:
            print("Setting Random Value 2")
            paragraph.style = 'Insertion'
            paragraph.text = data_for_zip[random_data_points[1]]

        if '[ZZ%]' in paragraph.text:
            print("Setting Random Value 3")
            paragraph.style = 'Insertion'
            paragraph.text = data_for_zip[random_data_points[2]]

    doc_name = '{}.docx'.format(userInfo["userName"])
    doc.save(doc_name)
    print("Formatted And Saved Document with name {}".format(doc_name))
    subprocess.run(["libreoffice", "--headless", "--convert-to",
                   "pdf", "{}.docx".format(userInfo["userName"])])
    subprocess.run(
        ["lp", "-d", "myprinter", "{}.pdf".format(userInfo["userName"])])


if __name__ == "__main__":
    try:
        formatDocument({'userName': 'sbb', 'userId': 'd63142d7cf6f53a093ebc32ae1448f18', 'a1': '1', 'a2': '1',
                       'a3': '1', 'zipcode': '11222', 'sugarIntake': '1', 'archivePermission': '1', 'lang': 'es'})
    except Exception as e:
        print(e)
