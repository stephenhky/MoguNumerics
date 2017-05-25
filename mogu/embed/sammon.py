
import tensorflow as tf

def sammon_embedding(Xmat, initYmat, tol=1e-8, alpha=0.3, nbsteps=1000):
    N = Xmat.shape[0]
    # d = Xmat.shape[1]

    # distance matrix for X
    X = tf.placeholder('float')
    sqX = tf.reduce_sum(X * X, 1)
    sqX = tf.reshape(sqX, [-1, 1])
    sqDX = sqX - 2 * tf.matmul(X, tf.transpose(X)) + tf.transpose(sqX)
    sqDXarray = tf.stack([sqDX[i, j] for i in range(N) for j in range(i + 1, N)])
    DXarray = tf.sqrt(sqDXarray)

    # distance matrix for Y
    Y = tf.Variable(initYmat, dtype='float')
    sqY = tf.reduce_sum(Y * Y, 1)
    sqY = tf.reshape(sqY, [-1, 1])
    sqDY = sqY - 2 * tf.matmul(Y, tf.transpose(Y)) + tf.transpose(sqY)
    sqDYarray = tf.stack([sqDY[i, j] for i in range(N) for j in range(i + 1, N)])
    DYarray = tf.sqrt(sqDYarray)

    # cost function
    Z = tf.reduce_sum(DXarray) * 0.5
    numerator = tf.reduce_sum(tf.divide(tf.square(DXarray - DYarray), DXarray)) * 0.5
    cost = tf.divide(numerator, Z)

    # optimizer (note: do not use Adam, which can lead to overflow)
    train = tf.train.AdagradOptimizer(alpha).minimize(cost)
    init = tf.global_variables_initializer()

    # Tensorflow session
    sess = tf.Session()
    sess.run(init)

    # training
    c = sess.run(cost, feed_dict={X: Xmat})
    print "initial cost = ", c
    converged = False
    i = 0
    while (not converged) and (i < nbsteps):
        sess.run(train, feed_dict={X: Xmat})
        newc = sess.run(cost, feed_dict={X: Xmat})
        print "epoch: ", i, " cost = ", newc
        converged = (abs(newc-c)<tol)
        i += 1
        c = newc

    # result retrieval
    calculated_Y = sess.run(Y, feed_dict={X: Xmat})

    # close session
    sess.close()

    return calculated_Y