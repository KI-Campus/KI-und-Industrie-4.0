import json
import numpy as np
import cv2

from helperFunctions import *

dataset_path = 'simple-tools-images-main/'

with open(dataset_path + 'akipro_tool.json') as json_file:
    data = json.load(json_file)

num_imgs = len(data['images']) 
num_classes = len(data['categories']) 

imgs = np.zeros((num_imgs, 144,256, 3 ), dtype=np.uint8)
bboxes = np.zeros((num_imgs, 25, 4))
shapes = np.zeros((num_imgs, 25), dtype=int)
bboxes_rot = np.zeros((num_imgs, 25, 5))
shape_list=[]
shape_template =  np.zeros(num_classes, dtype=int)

bboxes = np.zeros((num_imgs, 4))
scale = 1
i_img = -1
for img in data['images']:
    i_img = i_img + 1

    img_filename = img['file_name']
    # Read Image, 0 = Grayscale, 1 = color
    img_data = cv2.imread(dataset_path + 'images/' + img_filename, 1) 
    b,g,r = cv2.split(img_data)           # get b, g, r
    img_data = cv2.merge([r,g,b])         # switch it to r, g, b
    
    imgs[i_img] = img_data
    i_object = -1
    for annot in data['annotations']:
        if annot['image_id'] == img['id']:
            i_object = i_object + 1
            
            bbox_rot = np.zeros(5)
            bbox_rot = annot['bbox']
            bbox_rot[2] = bbox_rot[2]*2
            bbox_rot[3] = bbox_rot[3]*2
            bbox = getAlignedBBox(bbox_rot)

            scaled_bboxes_rot = [tmp * 1 for tmp in bbox_rot] 
            scaled_bboxes_rot[4] = bbox_rot[4]
            bboxes_rot[i_img, i_object] = scaled_bboxes_rot# [tmp * scale for tmp in bbox_rot] #bbox_rot*scale
            #bboxes[i_img, i_object] = bbox*1 #[x, y, w, h]
            
            bbox[2] = bbox[0]+bbox[2]
            bbox[3] = bbox[1]+bbox[3]
            bboxes[i_img] = bbox*1 #[x, y, w, h]
            class_id = annot['category_id']#shape
            shape_mat = shape_template.copy()
            shape_mat[class_id] = 1
            shape_list.append(shape_mat)
            shapes[i_img, i_object] = annot['category_id']#shape
            pass
    
        #print

shape_labels = ['1', '2', '3']
class_labels = ['Wrench', 'Screwdriver', 'Pliers']
shapes = np.array(shape_list)

#make consistent with structure of synthetic dataset
class_labels = ['Schluessel', 'Schraubenzieher', 'Zange']
classes = np.copy(shapes)
bboxes[:, [1, 3]] = bboxes[:, [3, 1]]

# clip the bounding boxes
h = imgs.shape[1]
b = imgs.shape[2]

bboxes[:,0] = np.clip(bboxes[:,0], 0, b)
bboxes[:,1] = np.clip(bboxes[:,1], 0, h)
bboxes[:,2] = np.clip(bboxes[:,2], 0, b)
bboxes[:,3] = np.clip(bboxes[:,3], 0, h)

print('Realer Datensatz ist bereit.')