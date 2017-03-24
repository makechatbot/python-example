
import tensorflow as tf

# train set
x_data = [1, 2, 3]
y_data = [1, 2, 3]



W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))


hypothesis = W * x_data + b

cost = tf.reduce_mean(tf.square(hypothesis - y_data))
learning_rate=tf.Variable(0.1)


optimizer = tf.train.GradientDescentOptimizer(learning_rate)

# 비용을 최소화 하는 것이 최종 목표
train_op = optimizer.minimize(cost)


# 세션을 생성하고 초기화합니다.
with tf.Session() as sess:
    # W, b 가 변수인데, 초기화를 안하면 초기화가 안되었다는 에러 메시지가 나타난다.
    # 세션에서 가장 먼저 실행시켜줘야 한다.
    sess.run(tf.global_variables_initializer())

    # 최적화를 100번 수행합니다.
    for step in range(4001):
        sess.run(train_op)

        if step%50==0:
            print(step, sess.run(cost), sess.run(W), sess.run(b))
