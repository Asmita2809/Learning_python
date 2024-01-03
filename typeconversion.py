x=1
y=2.8
z=1j
a=float(x)
b=int(y)
c=complex(z)
print(a)
print(b) #2.8 was converted to '2' the values after decimal was "trencated"
print(c)
print(type(a))
print(type(b))
print(type(c))

d=('apple', 'ban','che')
e="hello world"
f=33
m=type(d)
n=type(e)
p=type(f)
print(m,n,p)

#print(oct(12)) #see output 0o14
#print(hex(255)) #0xff