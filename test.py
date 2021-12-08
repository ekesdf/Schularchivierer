import tensorflow as tf
def matmul_manual_transpose(x, y):
    return tf.matmul(x, tf.transpose(y, (1, 0)))
def get_args(i=1024, j=1024, k=1024):
    return tf.random.normal((i, j)), tf.random.normal((k, j))
def benchmark_matmul_impl(f, **kwargs):
    with tf.Graph().as_default() as graph:
        x, y = get_args(**kwargs)
        output = f(x, y)
        with tf.compat.v1.Session(graph=graph) as sess:
            bm = tf.test.Benchmark()
            bm_result = bm.run_op_benchmark(sess, output)
    return bm_result
# passing matmul_manual_transpose which is a function as a argument
results = benchmark_matmul_impl(matmul_manual_transpose)
print(results)
