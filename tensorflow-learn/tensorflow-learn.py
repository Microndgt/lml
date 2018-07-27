import tensorflow as tf

c = tf.constant("Hello World")
with tf.Session() as sess:
    print(sess.run(c))
