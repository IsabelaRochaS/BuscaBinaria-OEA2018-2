import struct
import sys
	
registroCEP = struct.Struct("72s72s72s72s2s8s2s")

a = open("novoarq1.dat", "wb")
b = open("novoarq2.dat", "wb")

f = open("cep_ordenado.dat","rb")

for i in range(0, 40):
        f.seek(i*registroCEP.size)
        line = f.read(registroCEP.size)

        if (i % 2 == 0):
                a.write(line)
        else:
                b.write(line)
          
f.close() 
b.close()
a.close()
