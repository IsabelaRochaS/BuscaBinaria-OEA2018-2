import struct
import sys

if len(sys.argv) != 2:
	print ("USO %s [CEP]" % sys.argv[0])
	quit()
	
registroCEP = struct.Struct("72s72s72s72s2s8s2s")
cepColumn = 5

print ("Tamanho da Estrutura: %d" % registroCEP.size)

f = open("cep_ordenado.dat","r")

f.seek(0, 2)
pos = f.tell()
f.seek(0)
tamemarq = pos/registroCEP.size
print ("Tamanho do Arquivo em registros: %d" % tamemarq)

prim = 0
ultimo = tamemarq
meio = int(prim + ((ultimo - prim) / 2))

line = f.read(registroCEP.size).encode('latin1')
counter = 0

while (prim <= ultimo):
    meio = int(prim + ((ultimo - prim) / 2))
    f.seek(meio*registroCEP.size)
    line = f.read(registroCEP.size).encode('latin1')
    record = registroCEP.unpack(bytes(line))
    if int(record[5]) == int(sys.argv[1]):
        for i in range(0,len(record)-1):
            print (record[i].decode('latin1')) # .decode('latin1')
        break
    elif int(record[5]) < int(sys.argv[1]):
        prim = meio + 1
    elif int(record[5]) > int(sys.argv[1]):
        ultimo = meio - 1
    counter += 1
print ("Total de Registros Lidos: %d" % counter)

if prim > ultimo:
	print("Cep nao encontrado")
f.close()
