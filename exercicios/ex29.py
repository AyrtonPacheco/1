from time import sleep

vel = float(input('Qual é a velocidade atual do carro?' ))
multa = (vel - 80)*7
if vel <= 80:
    print('Tenha um bom dia! Diriga com segurança.')
else:
    sleep(2)
    print(f"""MULTADO!
          Você excedeu o limite de velocidade permitido que é de 80Km/h
          Você deve pagar uma multa de R${multa:.2f}!""")