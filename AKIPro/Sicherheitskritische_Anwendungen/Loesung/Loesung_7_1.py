attention_map_safe_background = score_CAM('conv2d_2', prepare_image(img_safe_background), model)

attention_map_safe_coin_hand = score_CAM('conv2d_2', prepare_image(img_safe_coin_hand), model)

attention_map_safe_coin = score_CAM('conv2d_2', prepare_image(img_safe_coin), model)

attention_map_unsafe = score_CAM('conv2d_2', prepare_image(img_unsafe), model)