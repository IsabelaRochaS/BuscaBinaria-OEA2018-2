import struct
import os
from operator import itemgetter

s = struct.Struct('72s72s72s72s2s8s2s')
f = open('cep.dat', 'rb')
n = 0
linha = f.read(s.size)
tamanho = 100000

while linha != b'':
	k = 0

	listaEntradas = []

	while k < tamanho and linha != b'':
		k += 1
		dados = s.unpack(linha)
		listaEntradas.append(dados)
		linha = f.read(s.size)

	listaEntradas.sort(key=itemgetter(5))
	
	n += 1

	nF = open('cep' + str(n) + '.dat', 'ab')

	for i in range(k):
		nF.write(s.pack(listaEntradas[i][0],
                        listaEntradas[i][1],
                        listaEntradas[i][2],
                        listaEntradas[i][3],
                        listaEntradas[i][4],
                        listaEntradas[i][5],
                        listaEntradas[i][6]))
	nF.close()

n = 1

while n != 1 or os.path.isfile('cep' + str(n + 1) + '.dat'):
        
	if os.path.isfile('cep' + str(n) + '.dat') and os.path.isfile('cep' + str(n + 1) + '.dat'):

		f1 = open('cep' + str(n) + '.dat', 'rb')
		linha1 = f1.read(s.size)

		f2 = open('cep' + str(n + 1) + '.dat', 'rb')
		linha2 = f2.read(s.size)

		f3 = open('merge.dat', 'ab')

		while linha1 != b'' and linha2 != b'':
			dados1 = s.unpack(linha1)
			dados2 = s.unpack(linha2)

			if dados1[5] < dados2[5]:
				f3.write(s.pack(dados1[0],
                                dados1[1],
                                dados1[2],
                                dados1[3],
                                dados1[4],
                                dados1[5],
                                dados1[6]))
				linha1 = f1.read(s.size)
			else:
				f3.write(s.pack(dados2[0],
                                dados2[1],
                                dados2[2],
                                dados2[3],
                                dados2[4],
                                dados2[5],
                                dados1[6]))
				linha2 = f2.read(s.size)

		while linha1 != b'':
			dados1 = s.unpack(linha1)
			f3.write(s.pack(dados1[0],
                            dados1[1],
                            dados1[2],
                            dados1[3],
                            dados1[4],
                            dados1[5],
                            dados1[6]))
			linha1 = f1.read(s.size)

		while linha2 != b'':
			dados2 = s.unpack(linha2)
			f3.write(s.pack(dados2[0],
                            dados2[1],
                            dados2[2],
                            dados2[3],
                            dados2[4],
                            dados2[5],
                            dados1[6]))
			linha2 = f2.read(s.size)

		f3.close()

		os.remove('cep' + str(n) + '.dat')
		os.remove('cep' + str(n + 1) + '.dat')
		os.rename('merge.dat', 'cep' + str((n + 1) // 2) + '.dat')

		n += 2
	else:
		if os.path.isfile('cep' + str(n) + '.dat') and n != 1:
			os.rename('cep' + str(n) + '.dat', 'cep' + str((n + 1) // 2) + '.dat')

		n = 1

print(time() - ti)
