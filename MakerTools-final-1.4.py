import PySimpleGUI as sg
import os
import distutils.dir_util
import time
from win32 import win32file
sg.theme('DarkGrey6')


drives = []
drivebits=win32file.GetLogicalDrives()
for d in range(1,26):

    mask=1 << d
    if drivebits & mask:
        drname='%c:\\' % chr(ord('A')+d)
        t=win32file.GetDriveType(drname)
        drives.append(drname)
unidade = 'Alterar Unidade'
menu_def = [[unidade, [drives]],]

# ----------- Layout tela Principal -----------
layout1 = [
    [sg.Menu(menu_def, tearoff=False)],
    [sg.Button('Instalar', key='instalar', size=(11, 2)),
     sg.Text('                                  '),
     sg.Text('            '),sg.Button('TomCat', key='toncat', size=(8, 1))
        , sg.Button('Webserv', key='webservice', size=(8, 1))],
    [sg.Output(size=(65,15), key='-OUTPUT-')],
    [sg.Text('')],
    [sg.Button('Backup&Restore',key='bkprestore', size=(11, 2))],

    [sg.Text('')],

]
# ----------- Layout tela Backup & Restore -----------
layout2 = [
           [sg.Text('Preencher com informações do Banco                                  '),
            ],
           [sg.Text('DBNome', size=(9, 0)), sg.Input('postgres',size=(20, 0), key='dbnome'),
            sg.Text('DBNome2', size=(9, 0)), sg.Input('postgres',size=(20, 0), key='dbnome2')],
           [sg.Text('DBSchema', size=(9, 0)), sg.Input(size=(20, 0), key='schemas'),
            sg.Text('DBSchema2', size=(9, 0)), sg.Input(size=(20, 0), key='schemas2')],
           [sg.Text('DBUsuario', size=(9, 0)), sg.Input('postgres',size=(20, 0), key='dbusuario'),
            sg.Text('DBUsuario2', size=(9, 0)), sg.Input('postgres',size=(20, 0), key='dbusuario2')],
           [sg.Text('DBSenha', size=(9, 0)), sg.Input(size=(20, 0), key='dbsenha'),
            sg.Text('DBSenha2', size=(9, 0)), sg.Input(size=(20, 0), key='dbsenha2')],
           [sg.Text('DBHost', size=(9, 0)), sg.Input('localhost',size=(20, 0), key='dbhost'),
            sg.Text('DBHost2', size=(9, 0)), sg.Input('localhost',size=(20, 0), key='dbhost2')],
           [sg.Text('DBPorta', size=(9, 0)), sg.Input('5432',size=(20, 0), key='dbporta'),
            sg.Text('DBPorta2', size=(9, 0)), sg.Input('5432',size=(20, 0), key='dbporta2')],
           [sg.Text('                              '),sg.Button('Pasta Backup',size=(11,0),key='PastaBKP'),
            sg.Text('                              '),sg.FileBrowse('Carregar BKP',size=(11,0),key='arquivorestore'),
            sg.Text('   ',size=(20, 0))],
          [sg.Text('                            '),sg.Text('                         '),sg.Text('                              '),
           sg.Button('Gravar dados',size=(11,0), key='alterdados')],
          [sg.Text('                                                     '),
            sg.Checkbox('Backup', default=False, key="-BKP-"),sg.Checkbox('Restore', default=False, key="-RES-"),sg.Button('Iniciar', key='-INIC-',size=(9, 1))],
           # [sg.Text('                              '),sg.Button('Backup',size=(11,0),key='BackupDB'),
           #  sg.Text('                               '),sg.Button('Restore',size=(11,0),key='RestoreDB'),
           #  sg.Text('   ',size=(20, 0))],

           [sg.Output(size=(65,7), key='-OUTPUT2-')],
           [sg.Text('')],



           [sg.Text(''),sg.Button('Voltar')]

]

# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, size=(510,460),visible=False, key='-COL2-')],
          [sg.Button('Exit')]]

window =   sg.Window('MAKER TOOLS | Webservice, Backup&Restore', layout)


layout = 1  # The currently visible layout
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break

    ##VARIAVEIS DB
    dbnome = values['dbnome']
    dbusuario = values['dbusuario']
    dbsenha = values['dbsenha']
    dbhost = values['dbhost']
    dbporta = values['dbporta']
    pastabkp = r'C:/MakerTools/postgresql/backup'
    pgdump = r'C:/MakerTools/postgresql/pg_dump.exe'
    pgrestore = r'C:/MakerTools/postgresql/pg_restore.exe'
    arquivorestore = values['arquivorestore']
    schemas = values['schemas']
    urlwebservice = 'http://127.0.0.1:8080/servo/'
##VERIFICAR COMO ACIONAR INSTALAÇÃO COM A OPÇÃO DO CHECKBOX:
    checkBox = ''
    if values["-BKP-"] == True:
        checkBox = 'Backup-CK'

    if values["-RES-"] == True:
        checkBox = 'Restore-CK'

    if event == '-INIC-' and checkBox == 'Backup-CK':
        print('Checkbox Backup')



    if event == 'alterdados':
        print('Nome do banco: '+dbnome,'\nUsuario: '+dbusuario,'\nSenha: '+dbsenha,'\nHost/IP:'+dbhost,'\nPorta: '+dbporta)
    if unidade == 'Alterar Unidade':
        pastaSoftwell = r'C:\Program Files (x86)\Softwell Solutions'
        pastaSoftwellWeb = r'C:\Program Files (x86)\Softwell Solutions\Webrun Enterprise'
        system32 = r'C:\Windows\System32'
        tomcat = r'C:\Program Files\Tomcat-7.0.55'
        src = r'C:\MakerTools\Webrun Enterprise'
        srcTomcat = r'C:\MakerTools\Tomcat-7.0.55'
        dst = pastaSoftwellWeb
        srcIni = r'C:\MakerTools\Webrun-ini'
        dstIni = r'C:\Windows\System32'

    else:
        pastaSoftwell = r''+unidade+'Program Files (x86)\Softwell Solutions'
        pastaSoftwellWeb = r''+unidade+'Program Files (x86)\Softwell Solutions\Webrun Enterprise'
        system32 = r''+unidade+'Windows\System32'
        tomcat = r''+unidade+'Program Files\Tomcat-7.0.55'
        src = r''+unidade+'MakerTools\Webrun Enterprise'
        srcTomcat = r''+unidade+'MakerTools\Tomcat-7.0.55'
        dst = pastaSoftwellWeb
        srcIni = r''+unidade+'MakerTools\Webrun-ini'
        dstIni = r''+unidade+'Windows\System32'



    if event == 'bkprestore':
        window[f'-COL2-'].update(visible=True)
        window[f'-COL1-'].update(visible=False)
    if event == 'Voltar':
        window[f'-COL1-'].update(visible=True)
        window[f'-COL2-'].update(visible=False)


    if event == 'Cycle Layout':
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout + 1 if layout < 3 else 1
        window[f'-COL{layout}-'].update(visible=True)

    if event == 'instalar':
        print('')
        print("********* Iniciando instalacao do Webrun do Servo ************* ")
        print('')
        # CRIANDO PASTA SOFTWELL
        if os.path.exists(pastaSoftwell):
            print('Pasta ' + pastaSoftwell + '   já existe.\n >>> Inciando cópia de arquivos. . .')
            print('')
        else:
            os.makedirs(pastaSoftwell)
            print(' Pasta Softwell Solution criada com sucesso . . .')
            print('')
        # COPIANDO ARQUIVOS PARA PASTA SOFTWELL
        if os.path.exists(pastaSoftwell):
            print('')
            print("Copiando. . . ")
            print("Favor aguardar. . . ")
            print('')
            distutils.dir_util.copy_tree(src, dst)
            print('Arquivos copiados para:  ' + pastaSoftwellWeb + ' . . .')
            print('')
            print('')
        # CRIANDO PASTA TOMCAT
        if os.path.exists(tomcat):
            print('Pasta ' + tomcat + '   já existe.\n >>> Inciando cópia de arquivos. . .')
            print('')
        else:
            os.makedirs(tomcat)
            print('Diretório Tomcat 7.0.55 criado com sucesso . . .')
            print('')
        # COPIANDO ARQUIVOS PARA PASTA TOMCAT
        if os.path.exists(tomcat):
            print('')
            print("Copiando. . . ")
            print('')
            distutils.dir_util.copy_tree(srcTomcat, tomcat)
            print('Arquivos copiados para:  ' + tomcat + '  . . .')
            print('')
            print('')
        # COPIANDO ARQUIVOS PARA PASTA SYSTEM32
        if os.path.exists(system32):
            print('Copiando webrun.ini para  ' + system32 + '   . . .')
            print('')
            distutils.dir_util.copy_tree(srcIni, dstIni)
            print('webrun.ini copiado!')
            print('')
            print('Cópia de arquivos finalizada . . ')
            print('')
            print('')
            print('')
            print('                       Instalação concluida com sucesso!')
            print('')
            print('        ')

    if event == 'toncat':

        os.system(r'start cmd /k   cd '+unidade+r'Program Files\Tomcat-7.0.55\bin\ ^&^& pause ^&^& startup.bat')

    if event == 'webservice':
        os.system('start chrome '+urlwebservice+'')

    if event == 'BackupDB':

        backup = 'SET "datetime=%date%" && SET "datetime=%datetime:~6,4%%datetime:~3,2%%datetime:~0,2%" && SET "PGPASSWORD=' + dbsenha + '" && SET "PGUSER=' + dbusuario + '" && SET "PGHOST=' + dbhost + '" && SET "PGDATABASE=' + dbnome + '" &&  ' + pgdump + ' -Fc -Z  -f --schema '+schemas+' > '+pastabkp+'/bkp-'+dbnome+'-'+schemas+'.sql'


        os.system(backup)

        print('Realizando backup do banco de dados ' + dbnome + ' . . .')
        time.sleep(3)
        print('Backup do Banco de Dados ' + dbnome + ' realizado!')

    if event == 'RestoreDB':
        restore = 'SET "PGPASSWORD='+dbsenha+'" && pg_restore.exe --host ' + dbhost + ' --port ' + dbporta + ' --username ' + dbusuario + ' --dbname ' + dbnome + '  ' + arquivorestore + ''

        os.system(restore)

        print('Realizando Restore do Banco de Dados ' + dbnome + '  . . .')
        time.sleep(3)
        print('Restore do Banco de Dados ' + dbnome + ' realizado com sucesso!')

    if event == 'PastaBKP':
        os.system(r'start '+pastabkp+'')

    if event:
        for x in drives:
            if event == x:
                unidade = x
                print(unidade)

#window.close()