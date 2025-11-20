x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# print(x,y,z)

m="hello"
x=1.1
a=12
print(type(m))
print(type(x))
print(type(a))

bike=['honda','suzuki','yamaha']
print(type(bike))
print(bike[1])
a,b,c= bike
# print(a)

one="i"
two="am"
three="python"

print(one , two,three)

z= frozenset([3,2])
print(z)

ba = bytearray(b"hello")
#
print(ba)
# ba[0] = 72      # change first byte

mv = memoryview(b"hello")
print(mv)
print(mv.tobytes())
