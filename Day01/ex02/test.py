from vector import Vector

vec = Vector([0.0, 1.0, 2.0, 4.0, 5.0])
vec2 = Vector.by_size(4)
vec3 = Vector.by_range(10, 15)


print('Value of Vec BEFORE add SCALAR: %s\n' % format(vec.values))
print('Value of Vec2 BEFORE add SCALAR: %s\n' % format(vec2.values))
print('Value of Vec3 BEFORE add SCALAR: %s\n' % format(vec3.values))

vec3 / 4.0

print('Value of Vec3 / vec : %s\n' % format(vec3.values))
