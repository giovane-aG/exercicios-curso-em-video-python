class Computador:
  def __init__(self, marca, memoria_ram, placa_de_video):
    self.marca = marca
    self.memoria_ram = f'{memoria_ram}gb'
    self.placa_de_video = placa_de_video
  pass

  def ligar(self):
    print('Sistema online')

  def desligar(self):
    print('Desligando sistema')
  
computador1 = Computador('Asus', 64, 'Nvidia')
computador2 = Computador('Samsung', 8, 'Nvidia')

print(computador1.marca)
print(computador1.memoria_ram)
print(computador1.placa_de_video)

print(computador2.marca)
print(computador2.memoria_ram)
print(computador2.placa_de_video)

computador2.desligar()