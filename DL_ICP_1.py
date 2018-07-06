#import tensorflow packages
import tensorflow as tf
#define the matrixes for a , b and c
a = tf.constant([1,2,3,4], name="matrix_a",shape=[2,2])
b = tf.constant([5,6,7,8], name="matrix_b",shape=[2,2])
c = tf.constant([9,10,11,12], name="matrix_c",shape=[2,2])
#define the multiply operation for a*a
x = tf.multiply(a,a)
#define the addition operation for x + b
y=tf.add(x,b)
#define the multiply operation for y * c
z=tf.matmul(y,c)


#create the session for evaluating tensor objects
# opening connection
with tf.Session() as s:

    #print a*a
    print(s.run(x))
    #print (a*a+b)
    print(s.run(y))
    #print (a*a+b)*c
    print(s.run(z))