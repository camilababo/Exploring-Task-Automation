import PySimpleGUI as sg
import pandas as pd

excel_file = 'data/bank-additional-full.xlsx'
df = pd.read_excel(excel_file, )

sg.theme('Black')

layout = [
    [sg.Text('Please fill out the following fields while contacting the client:')],
    [sg.Text('Age',
             size=(3, 1)), sg.InputText(key='age')],
    [sg.Text('Job', size=(15, 1)),
     sg.Combo(["admin.", "blue-collar", "entrepreneur", "housemaid", "management", "retired",
               "self-employed", "services", "student", "technician", "unemployed", "unknown"],
              key='job')],
    [sg.Text('Marital Status', size=(15, 1)),
     sg.Combo(["divorced", "married", "single", "unknown"],
              key='marital')],
    [sg.Text('Education', size=(15, 1)),
     sg.Combo(["basic.4y", "basic.6y", "basic.9y", "high.school", "illiterate",
               "professional.course", "university.degree", "unknown"],
              key='education')],
    [sg.Text('Has credit?', size=(15, 1)),
     sg.Combo(["no", "yes", "unknown"], key='default')],
    [sg.Text('Has housing loan?', size=(15, 1)),
     sg.Combo(["no", "yes", "unknown"], key='housing')],
    [sg.Text('Has personal loan?', size=(15, 1)),
     sg.Combo(["no", "yes", "unknown"], key='loan')],
    [sg.Text('Type of Contact', size=(15, 1)),
     sg.Combo(["cellular", "telephone"], key='contact')],
    [sg.Text('Month', size=(15, 1)),
     sg.Combo(["jan", "fev", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dez"], key='month')],
    [sg.Text('Day of the Week', size=(15, 1)),
     sg.Combo(["mon", "tue", "wed", "thu", "may", "fri"], key='day_of_week')],
    [sg.Text('Term deposit?', size=(15, 1)),
     sg.Combo(["yes", "no"], key='y')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('Simple data entry form', layout)


def clear_input():
    for key in values:
        window[key]('')
    return None


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        values['age'] = int(values['age'])
        new_data = pd.DataFrame([values])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_excel(excel_file, index=False)
        sg.popup('Data Saved!')
        clear_input()

window.close()
