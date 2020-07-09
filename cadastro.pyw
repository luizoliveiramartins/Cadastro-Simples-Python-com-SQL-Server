import PySimpleGUI as tela
import pyodbc
connection = pyodbc.connect('DRIVER={SQL Server};server=localhost\sqlexpress;database=CADASTRO;uid=sa;pwd=Senha123')
sql=connection.cursor()

layout=[
    [tela.Text('Nome',size=(7,0)),tela.Input(),tela.Text('Endereço',size=(7,0)),tela.Input()],
    [tela.Text('Número',size=(7,0)),tela.Input(size=(10,0)),tela.Text('Telefone',size=(7,0)),tela.Input(size=(12,0)),tela.Text('E-Mail',size=(7,0)),tela.Input()],
    [tela.Text('Cidade',size=(7,0)),tela.Input(),tela.Text('Estado',size=(7,0)),tela.Input(size=(3,0))],
    [tela.Text('Cep',size=(7,0)),tela.Input(size=(8,0))],
    [tela.Button('Salvar',button_color=('white','green')),tela.Button('Limpar',button_color=('white','blue')),tela.Button('Buscar',button_color=('black','yellow')),tela.Button('Fechar',button_color=('white','red'))],
    [tela.Output(size=(120,20),key='Output')]
    ]
    
window=tela.Window('CADASTRO DE CLIENTE',layout)

while True:    
    event,values=window.read()
    if event=='Salvar':
        sql.execute("INSERT INTO CLIENTE VALUES (?,?,?,?,?,?,?,?)",(values[0].title(),values[1].title(),values[2],\
        values[3],values[4].lower(),values[5].title(),values[6].upper(),values[7]))
        connection.commit()
        window[0].update('')
        window[1].update('')
        window[2].update('')
        window[3].update('')
        window[4].update('')
        window[5].update('')
        window[6].update('')
        window[7].update('')

    elif event=='Limpar':
        window[0].update('')
        window[1].update('')
        window[2].update('')
        window[3].update('')
        window[4].update('')
        window[5].update('')
        window[6].update('')
        window[7].update('')
        window.FindElement('Output').update('')

    elif event=='Buscar':
        sql.execute("SELECT * FROM CLIENTE WHERE NOME LIKE '%'+?+'%'",values[0])
        for s in sql:
            print(s)

    elif event=='Fechar':
        break

sql.close()
window.close()
