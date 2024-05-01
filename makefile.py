# run_app.py
import os
a = input("Digite se é postman (p) ou aula (a):")
if (a == 'a'):
    a = input("Digite o número da aula:")
    a = './aulaFilipe/aula' + a
    os.system(f'cd {a} && python3 app.py')

elif (a == 'p'):
    os.system('cd postman && python3 app.py')