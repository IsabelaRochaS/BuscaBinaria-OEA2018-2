import struct
import sys
	
registroCEP = struct.Struct("72s72s72s72s2s8s2s")

a = open("novoarq1.txt", "a+")
b = open("novoarq2.txt", "a+")

f = open("cep_ordenado.dat","r")

line = f.read(registroCEP.size).encode('latin1')

for i in range(1, 20):
        f.seek(i*registroCEP.size)
        line = f.read(registroCEP.size).encode('latin1')
        record = registroCEP.unpack(bytes(line))

        if (i % 2 == 0):
                for i in range(0,len(record)):
                    a.write(record[i].decode('latin1')) # .decode('latin1')
                break
                
        else:
                for i in range(0,len(record)):
                    b.write(record[i].decode('latin1')) # .decode('latin1')
                break  
f.close() 
b.close()
a.close()  
