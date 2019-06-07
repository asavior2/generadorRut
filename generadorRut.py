def digito_verificador(rut):
	value = 11 - sum([ int(a)*int(b)  for a,b in zip(str(rut).zfill(8), '32765432')])%11
	return {10: 'K', 11: '0'}.get(value, str(value))	
archivoRut = open('rut', 'r')
archivoFinal = open('rut2', 'w')
for linea in archivoRut.readlines():
	archivoFinal.write(linea.rstrip('\n')+digito_verificador(linea)+"\n") 
print "Termino"
archivo.close() 
archivoFinal.close() 
