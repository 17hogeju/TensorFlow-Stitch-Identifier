import tensorflow as tf, sys
#image_path = sys.argv[1]

def test_function(image_path):
    # Read in the image_data
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line in tf.gfile.GFile("./output_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("./output_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
        
    # Feed the image_data as input to the graph and get first prediction
    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        f= open("output.txt","w+")
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            
            f.write('%s (score = %.5f)\n' % (human_string, score))
            
            print('%s (score = %.5f)' % (human_string, score))
        f.close()