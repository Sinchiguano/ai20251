
import numpy as np


a=np.array([1,2,3,4,5])

print(a.shape)
print('Element extracted of index 2: ',a[2])

b=np.array([[1,2,3],[11,22,33]])
print(b.shape)
print('Extracted element of row 1 and column 2: ',b[1,2])


print(b)

print('ok!!!')


c=np.zeros((5,4))

print("the matrix x is: ")
print(c)


d=np.ones((3,4))
print('matrix of values ones:')
print(d)


e=np.full((3,4),8)
print("matrix of a unique value:")
print(e)


f=np.random.randint(1,11,size=(5,5))
print(f)
 

print("Matrix G")
g=np.random.random((5,5))
print(g)

print('IDENTITY MATRIX')
h=np.eye(10)
print(h)


print('SUBMATRIX')
f=np.random.randint(1,21,size=(3,4))
print(f)
 
m=f[:2,:2]
print(m)

print('***********************')
n=np.random.randint(1,101,size=(7,5))
print(n)

# p=n[4:6,2:4]
# print(p)
# 0,0
# 6,0
# 6,4
# 0,4

h=n[[0,6,6,0],[0,0,4,4]]
print(h)
print(type(h))
print(h.shape)
print(h.ndim)


print('/////////////////////////')
p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(p)
b=np.array([0,2,0,1])
a=np.arange(4) 
# print(a)
print('--')
print(np.arange(4),b)
p[a,b]+=100
print(p)


print('/////////////////////////')
p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(p)
filter=(p>5)
print(filter)
print(type(filter))
print(filter.ndim)
print(filter.shape)
z=p[filter]
print(type(z))
print(z.shape)
print(z.ndim)

print(z)

print('FILTER VALUES FROM 40 TO 50')
f=np.random.randint(1,101,size=(7,7))
print(f)
print('************')
filter1=(f>40)
filter2=(f<60)
print('filter 1')
print(filter1)
print("filter 2")
print(filter2)
print('----------------')
f[filter1 & filter2]=0
print(f)
print(f.shape)
print(type(f))


# array_30x30[(array_30x30 >= 40) & (array_30x30 <= 50)] = 0


print('///////////////////////////')
a=np.random.randint(1,10,size=(2,2))
b=np.random.randint(1,10,size=(2,2))
print(' MATRIX A')
print(a)
print('MATRIX B')
print(b)

print('ADDING MATRICES')
adding_matrices=np.add(a,b)
print(adding_matrices)
print(a+b)
print(a-b)
print(a/b)
print(a*b)

aux1=np.subtract(a,b)
aux2=np.multiply(a,b)
aux3=np.divide(a,b)
aux3=np.sqrt(a)

print(aux3)


print('///////////////////////////')
a=np.random.randint(1,10,size=(3,3))
b=np.random.randint(1,10,size=(3,3))

c=a.dot(b)
print(c)
print(c.shape)
print(c.ndim)



a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(a)
print(b)

w=np.array([9,10])
v=np.array([11,12])


tmp1=np.dot(w,v)
tmp2=w.dot(v)

print(tmp1)
print(tmp2)
print(type(tmp1))
print(type(tmp2))

print(tmp2.shape)
print(tmp1.ndim)

print('DOT PRODUCT BETWEEN A VECTOR AND MATRIX')
tmp3=a.dot(v)
tmp4=np.dot(a,v)
print(type(tmp3))
print(tmp3.ndim)
print(tmp3.shape)


a=np.array([[1,2],[3,4]])

print(a)

# result=np.sum(a)
print('THE RESULT OF THE SUM THE WHOLE ELEMENTS INSIDE THE MATRIX IS: ', np.sum(a))

f=np.random.randint(1,21,size=(10,10))
print(f)
columns_sum=np.sum(f,axis=0)
print('sum each elements of a columns: ',columns_sum)
print(columns_sum.shape)
print('The total elements of my column sum is: ',len(columns_sum))
print(columns_sum.ndim)
print("THE AVERAGE OF EACH COLUMN ARE: ",np.sum(f,axis=0)/len(np.sum(f,axis=0)))

print("THE MEAN OF EACH COLUMN ARE: ",np.mean(f,axis=0))

print("THE AVERAGE OF EACH COLUMN ARE: ",np.average(f,axis=0))

print('TRANSPOSE MATRIX')
f=np.random.randint(1,21,size=(4,4))
print(f)
print(f.T)

x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v=np.array([1,0,1])
emptyMatrix=np.empty_like(x)


print(x)
print(v)
print(x.shape)
print('rows: ',x.shape[0])
# print('columns: ',x.shape[1])
for i in range(x.shape[0]):
    emptyMatrix[i,:]=x[i,:]+v
    # print(i)
print(emptyMatrix)


vv=np.tile(v,(4,1))
print(vv)
print(x+vv)

print(x+v)

# hstack
# vstack