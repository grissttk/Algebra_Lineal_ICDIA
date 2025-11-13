import numpy

print("A en forma de lista Python")
A = [["Gris1", 4, 5],["Gris2", 5, 6]]
print(A)
print("A en forma matricial")
A = numpy.array(A)
print(A)

orden = A.shape
print("orden", str(orden))