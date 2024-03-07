import numpy as np
import tensorflow as tf

def get_angles_test(target):
    position = 4
    d_model = 16
    pos_m = np.arange(position)[:, np.newaxis]
    dims = np.arange(d_model)[np.newaxis, :]

    result = target(pos_m, dims, d_model)

    assert type(result) == np.ndarray, "You must return a numpy ndarray"
    assert result.shape == (position, d_model), f"Wrong shape. We expected: ({position}, {d_model})"
    assert np.sum(result[0, :]) == 0
    assert np.isclose(np.sum(result[:, 0]), position * (position - 1) / 2)
    even_cols =  result[:, 0::2]
    odd_cols = result[:,  1::2]
    assert np.all(even_cols == odd_cols), "Submatrices of odd and even columns must be equal"
    limit = (position - 1) / np.power(10000,14.0/16.0)
    assert np.isclose(result[position - 1, d_model -1], limit ), f"Last value must be {limit}"

    print("\033[92mAll tests passed")
    
def positional_encoding_test(target, get_angles):
    position = 8
    d_model = 16

    pos_encoding = target(position, d_model)
    sin_part = pos_encoding[:, :, 0::2]
    cos_part = pos_encoding[:, :, 1::2]

    assert tf.is_tensor(pos_encoding), "Output is not a tensor"
    assert pos_encoding.shape == (1, position, d_model), f"Wrong shape. We expected: (1, {position}, {d_model})"

    ones = sin_part ** 2  +  cos_part ** 2
    assert np.allclose(ones, np.ones((1, position, d_model // 2))), "Sum of square pairs must be 1 = sin(a)**2 + cos(a)**2"
    
    angs = np.arctan(sin_part / cos_part)
    angs[angs < 0] += np.pi
    angs[sin_part.numpy() < 0] += np.pi
    angs = angs % (2 * np.pi)
    
    pos_m = np.arange(position)[:, np.newaxis]
    dims = np.arange(d_model)[np.newaxis, :]

    trueAngs = get_angles(pos_m, dims, d_model)[:, 0::2] % (2 * np.pi)
    
    assert np.allclose(angs[0], trueAngs), "Did you apply sin and cos to even and odd parts respectively?"
 
    print("\033[92mAll tests passed")
    
def scaled_dot_product_attention_test(target):
    q = np.array([[1, 0, 1, 1], [0, 1, 1, 1], [1, 0, 0, 1]]).astype(np.float32)
    k = np.array([[1, 1, 0, 1], [1, 0, 1, 1 ], [0, 1, 1, 0], [0, 0, 0, 1]]).astype(np.float32)
    v = np.array([[0, 0], [1, 0], [1, 0], [1, 1]]).astype(np.float32)

    attention, weights = target(q, k, v, None)
    assert tf.is_tensor(weights), "Weights must be a tensor"
    assert tuple(tf.shape(weights).numpy()) == (q.shape[0], k.shape[1]), f"Wrong shape. We expected ({q.shape[0]}, {k.shape[1]})"
    assert np.allclose(weights, [[0.2589478,  0.42693272, 0.15705977, 0.15705977],
                                   [0.2772748,  0.2772748,  0.2772748,  0.16817567],
                                   [0.33620113, 0.33620113, 0.12368149, 0.2039163 ]]), "Wrong unmasked weights"

    assert tf.is_tensor(attention), "Output must be a tensor"
    assert tuple(tf.shape(attention).numpy()) == (q.shape[0], v.shape[1]), f"Wrong shape. We expected ({q.shape[0]}, {v.shape[1]})"
    assert np.allclose(attention, [[0.74105227, 0.15705977],
                                   [0.7227253,  0.16817567],
                                   [0.6637989,  0.2039163 ]]), "Wrong unmasked attention"

    mask = np.array([[[1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1]]])
    attention, weights = target(q, k, v, mask)

    assert np.allclose(weights, [[0.30719590187072754, 0.5064803957939148, 0.0, 0.18632373213768005],
                                 [0.3836517333984375, 0.3836517333984375, 0.0, 0.2326965481042862],
                                 [0.3836517333984375, 0.3836517333984375, 0.0, 0.2326965481042862]]), "Wrong masked weights"
    assert np.allclose(attention, [[0.6928040981292725, 0.18632373213768005],
                                   [0.6163482666015625, 0.2326965481042862], 
                                   [0.6163482666015625, 0.2326965481042862]]), "Wrong masked attention"
    
    print("\033[92mAll tests passed")
    
def EncoderLayer_test(target):
    q = np.array([[[1, 0, 1, 1], [0, 1, 1, 1], [1, 0, 0, 1]]]).astype(np.float32)
    tf.keras.utils.set_random_seed(42)
    encoder_layer1 = target(4, 2, 8)
    encoded = encoder_layer1(q, True, np.array([[1, 0, 1]]))
    
    assert tf.is_tensor(encoded), "Wrong type. Output must be a tensor"
    assert tuple(tf.shape(encoded).numpy()) == (1, q.shape[1], q.shape[2]), f"Wrong shape. We expected ((1, {q.shape[1]}, {q.shape[2]}))"

    assert np.allclose(encoded.numpy(), [[ 0.50068265, -1.7271469, 0.52905715, 0.69740695],
                            [-1.2686021, 0.0331768, -0.2840655, 1.519491],
                            [0.88460815, -1.4898368, -0.33562618, 0.94085467]]), "Wrong values when training=True"
    
    encoded = encoder_layer1(q, False, np.array([[1, 1, 0]]))
    assert np.allclose(encoded.numpy(), [[0.19307354, -1.685749, 0.6874707, 0.80520487],
                            [-1.4838818, 0.04238091, 0.105391, 1.33611],
                            [0.7177963, -1.5438266, -0.20350842, 1.0295385 ]]), "Wrong values when training=False"
    print("\033[92mAll tests passed")
    
def Encoder_test(target):
    tf.keras.utils.set_random_seed(42)
    
    embedding_dim=4
    
    encoderq = target(num_layers=2,
                      embedding_dim=embedding_dim,
                      num_heads=2,
                      fully_connected_dim=8,
                      input_vocab_size=32,
                      maximum_position_encoding=5)
    
    x = np.array([[2, 1, 3], [1, 2, 0]])
    
    encoderq_output = encoderq(x, True, None)
    
    assert tf.is_tensor(encoderq_output), "Wrong type. Output must be a tensor"
    assert tuple(tf.shape(encoderq_output).numpy()) == (x.shape[0], x.shape[1], embedding_dim), f"Wrong shape. We expected ({x.shape[0]}, {x.shape[1]}, {embedding_dim})"
    assert np.allclose(encoderq_output.numpy(), 
                       [[[-0.7971118, 0.85400605, -1.1759804, 1.1190861],
                          [-0.64581424, -0.25346905, -0.7982203, 1.6975037],
                          [0.2252863, -1.2023212, 1.4950882, -0.5180533]],
                        [[-1.3417134, 1.479414, -0.09762204, -0.04007855],
                          [-1.6554903, 1.0217665, 0.40211105, 0.23161274],
                          [0.06369102, -1.0942822, 1.580056, -0.5494647 ]]]), "Wrong values case 1"
    
    encoderq_output = encoderq(x, True, np.array([[[[1., 1., 1.]]], [[[1., 1., 0.]]]]))
    assert np.allclose(encoderq_output.numpy(), 
                       [[[-1.2117493, -0.30997747, 1.5601575, -0.03843075],
                        [-0.00764149, -1.5612948, 1.1916014, 0.3773347],
                        [-0.14200436, -1.150779, 1.6003035, -0.3075202 ]],
                        [[-1.3067628, 1.4991512, -0.2111016, 0.01871333],
                        [0.14493492, -1.5634681, 1.2232896, 0.19524363],
                        [0.2534179, -1.3456379, 1.4203416, -0.32812166]]]), "Wrong values case 2"
    
    encoderq_output = encoderq(x, False, np.array([[[[1., 1., 1.]]], [[[1., 1., 0.]]]]))
    assert np.allclose(encoderq_output.numpy(), 
                       [[[-1.3025213, 1.3020152, -0.55119544, 0.55170155],
                          [0.03750244, -1.5926285, 1.1331725, 0.4219535 ],
                          [0.07615094, -1.2685362, 1.5111033, -0.31871796]],
                        [[-1.3577062, 1.4475601, -0.21398903, 0.12413511],
                          [0.31797162, -1.7108289, 0.72747874, 0.66537863],
                          [0.17300025, -1.3473498, 1.4430861, -0.26873654]]]), "Wrong values case 3"
    
    print("\033[92mAll tests passed")
    
def DecoderLayer_test(target, create_look_ahead_mask):
    
    num_heads=8
    tf.keras.utils.set_random_seed(42)
    
    decoderLayerq = target(
        embedding_dim=4, 
        num_heads=num_heads,
        fully_connected_dim=32, 
        dropout_rate=0.1, 
        layernorm_eps=1e-6)
    
    encoderq_output = tf.constant([[[-0.40172306,  0.11519244, -1.2322885,   1.5188192 ],
                                   [ 0.4017268,   0.33922842, -1.6836855,   0.9427304 ],
                                   [ 0.4685002,  -1.6252842,   0.09368491,  1.063099  ]]])
    
    q = np.array([[[1, 0, 1, 1], [0, 1, 1, 1], [1, 0, 0, 1]]]).astype(np.float32)
    
    look_ahead_mask = create_look_ahead_mask(q.shape[1])
    
    padding_mask = None
    out, attn_w_b1, attn_w_b2 = decoderLayerq(q, encoderq_output, True, look_ahead_mask, padding_mask)
    
    assert tf.is_tensor(attn_w_b1), "Wrong type for attn_w_b1. Output must be a tensor"
    assert tf.is_tensor(attn_w_b2), "Wrong type for attn_w_b2. Output must be a tensor"
    assert tf.is_tensor(out), "Wrong type for out. Output must be a tensor"
    
    shape1 = (q.shape[0], num_heads, q.shape[1], q.shape[1])
    assert tuple(tf.shape(attn_w_b1).numpy()) == shape1, f"Wrong shape. We expected {shape1}"
    assert tuple(tf.shape(attn_w_b2).numpy()) == shape1, f"Wrong shape. We expected {shape1}"
    assert tuple(tf.shape(out).numpy()) == q.shape, f"Wrong shape. We expected {q.shape}"

    assert np.allclose(attn_w_b1[0, 0, 1], [0.42892298,  0.571077, 0.], atol=1e-2), "Wrong values in attn_w_b1. Check the call to self.mha1"
    assert np.allclose(attn_w_b2[0, 0, 1], [0.36948738, 0.3800445, 0.25046816]),  "Wrong values in attn_w_b2. Check the call to self.mha2"
    assert np.allclose(out[0, 0], [1.2285516, -0.06560415, 0.3698757, -1.5328231]), "Wrong values in out"
    

    # Now let's try a example with padding mask
    padding_mask = np.array([[[1, 1, 0]]])
    out, attn_w_b1, attn_w_b2 = decoderLayerq(q, encoderq_output, True, look_ahead_mask, padding_mask)
    assert np.allclose(out[0, 0], [1.2627907, 0.2749473, -0.01142518, -1.5263128]), "Wrong values in out when we mask the last word. Are you passing the padding_mask to the inner functions?"

    print("\033[92mAll tests passed")
    
def Decoder_test(target, create_look_ahead_mask, create_padding_mask):
    tf.keras.utils.set_random_seed(42)
        
    num_layers=7
    embedding_dim=4 
    num_heads=3
    fully_connected_dim=8
    target_vocab_size=33
    maximum_position_encoding=6
    
    x_array = np.array([[3, 2, 1], [2, 1, 0]])

    
    encoderq_output = tf.constant([[[-0.40172306,  0.11519244, -1.2322885,   1.5188192 ],
                         [ 0.4017268,   0.33922842, -1.6836855,   0.9427304 ],
                         [ 0.4685002,  -1.6252842,   0.09368491,  1.063099  ]],
                        [[-0.3489219,   0.31335592, -1.3568854,   1.3924513 ],
                         [-0.08761203, -0.1680029,  -1.2742313,   1.5298463 ],
                         [ 0.2627198,  -1.6140151,   0.2212624 ,  1.130033  ]]])
    
    look_ahead_mask = create_look_ahead_mask(x_array.shape[1])
    
    decoderk = target(num_layers,
                    embedding_dim, 
                    num_heads, 
                    fully_connected_dim,
                    target_vocab_size,
                    maximum_position_encoding)
    x, attention_weights = decoderk(x_array, encoderq_output, False, look_ahead_mask, None)
    assert tf.is_tensor(x), "Wrong type for x. It must be a dict"
    assert np.allclose(tf.shape(x), tf.shape(encoderq_output)), f"Wrong shape. We expected { tf.shape(encoderq_output)}"
    assert np.allclose(x[1, 1], [1.6465435, -1.0554001, -0.2834093, -0.30773413]), "Wrong values in x"
    
    keys = list(attention_weights.keys())
    assert type(attention_weights) == dict, "Wrong type for attention_weights[0]. Output must be a tensor"
    assert len(keys) == 2 * num_layers, f"Wrong length for attention weights. It must be 2 x num_layers = {2*num_layers}"
    assert tf.is_tensor(attention_weights[keys[0]]), f"Wrong type for attention_weights[{keys[0]}]. Output must be a tensor"
    shape1 = (x_array.shape[0], num_heads, x_array.shape[1], x_array.shape[1])
    assert tuple(tf.shape(attention_weights[keys[1]]).numpy()) == shape1, f"Wrong shape. We expected {shape1}"
    assert np.allclose(attention_weights[keys[0]][0, 0, 1], [0.48481178, 0.5151882, 0.]), f"Wrong values in attention_weights[{keys[0]}]"
    
    x, attention_weights = decoderk(x_array, encoderq_output, True, look_ahead_mask, None)
    assert np.allclose(x[1, 1], [1.2481778, -1.5399985, 0.2639646, 0.02785601]), "Wrong values in x when training=True"

    x, attention_weights = decoderk(x_array, encoderq_output, True, look_ahead_mask, create_padding_mask(x_array))
    assert np.allclose(x[1, 1], [1.1812904, -1.5843581, 0.28254977, 0.12051809]), "Wrong values in x when training=True and use padding mask"
    
    print("\033[92mAll tests passed")
    
def Transformer_test(target, create_look_ahead_mask, create_padding_mask):
    
    tf.keras.utils.set_random_seed(42)


    num_layers = 6
    embedding_dim = 4
    num_heads = 4
    fully_connected_dim = 8
    input_vocab_size = 30
    target_vocab_size = 35
    max_positional_encoding_input = 5
    max_positional_encoding_target = 6

    trans = target(num_layers, 
                        embedding_dim, 
                        num_heads, 
                        fully_connected_dim, 
                        input_vocab_size, 
                        target_vocab_size, 
                        max_positional_encoding_input,
                        max_positional_encoding_target)
    # 0 is the padding value
    sentence_lang_a = np.array([[2, 1, 4, 3, 0]])
    sentence_lang_b = np.array([[3, 2, 1, 0, 0]])

    enc_padding_mask = create_padding_mask(sentence_lang_a)
    dec_padding_mask = create_padding_mask(sentence_lang_b)

    look_ahead_mask = create_look_ahead_mask(sentence_lang_a.shape[1])

    translation, weights = trans(
        sentence_lang_a,
        sentence_lang_b,
        True,  # Training
        enc_padding_mask,
        look_ahead_mask,
        dec_padding_mask
    )
    
    
    assert tf.is_tensor(translation), "Wrong type for translation. Output must be a tensor"
    shape1 = (sentence_lang_a.shape[0], max_positional_encoding_input, target_vocab_size)
    assert tuple(tf.shape(translation).numpy()) == shape1, f"Wrong shape. We expected {shape1}"

    assert np.allclose(translation[0, 0, 0:8],
                       [0.01598642, 0.03246542, 0.02865042, 0.03237151, 
                        0.0384616,  0.01717172, 0.01019837, 0.02168636]), "Wrong values in translation"
    
    keys = list(weights.keys())
    assert type(weights) == dict, "Wrong type for weights. It must be a dict"
    assert len(keys) == 2 * num_layers, f"Wrong length for attention weights. It must be 2 x num_layers = {2*num_layers}"
    assert tf.is_tensor(weights[keys[0]]), f"Wrong type for att_weights[{keys[0]}]. Output must be a tensor"

    shape1 = (sentence_lang_a.shape[0], num_heads, sentence_lang_a.shape[1], sentence_lang_a.shape[1])
    assert tuple(tf.shape(weights[keys[1]]).numpy()) == shape1, f"Wrong shape. We expected {shape1}"
    assert np.allclose(weights[keys[0]][0, 0, 1], [0.47521198, 0.52478796, 0.0, 0.0, 0.0]), f"Wrong values in weights[{keys[0]}]"
    
    translation, weights = trans(
        sentence_lang_a,
        sentence_lang_b,
        False, # Training
        enc_padding_mask,
        look_ahead_mask,
        dec_padding_mask
    )
    assert np.allclose(translation[0, 0, 0:8],
                       [0.042736, 0.02721556, 0.0233324, 0.03952922, 
                        0.02491077, 0.01355808, 0.0224883, 0.01778231]), "Wrong values in outd"
    
    print(translation)
    
    print("\033[92mAll tests passed")