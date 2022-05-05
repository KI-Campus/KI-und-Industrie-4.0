# Helper Functions:
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def rotatePointAroundOrigin(x,y, omega):
    import numpy as np
    omega = omega * -1 
    new_x = x*np.cos(omega) - y*np.sin(omega)
    new_y = y*np.cos(omega) + x*np.sin(omega)
    return new_x, new_y

def setNewMinMaxValue(new_x, x_min, x_max):
    if new_x > x_max:
        x_max = new_x
    if new_x < x_min:
        x_min = new_x
    return x_min, x_max

def getCornerPointsBBox(bbox):
    import numpy as np
    center_x = bbox[1] + bbox[3]/2
    center_y = bbox[0] + bbox[2]/2

    center_x = bbox[1]
    center_y = bbox[0]
    
    new_x, new_y = rotatePointAroundOrigin(bbox[2]/2,bbox[3]/2, bbox[4])
    p1 = [center_x + new_x, center_y + new_y]

    new_x, new_y = rotatePointAroundOrigin(-bbox[2]/2,bbox[3]/2, bbox[4])
    p2 = [center_x + new_x, center_y + new_y]

    new_x, new_y = rotatePointAroundOrigin(-bbox[2]/2,-bbox[3]/2, bbox[4])
    p3 = [center_x + new_x, center_y + new_y]
    
    new_x, new_y = rotatePointAroundOrigin(bbox[2]/2,-bbox[3]/2, bbox[4])
    p4 = [center_x + new_x, center_y + new_y]

    pts = np.array([p1, p2, p3, p4], np.int32)
    
    return pts.reshape((-1, 1, 2))

def getAlignedBBox(bbox):
    import numpy as np
    
    center_x = bbox[1]
    center_y = bbox[0]

    x_min = 10^6
    x_max = -10^6
    y_min = 10^6
    y_max = -10^6
    
    new_x, new_y = rotatePointAroundOrigin(bbox[2]/2,bbox[3]/2, bbox[4])
    x_min, x_max = setNewMinMaxValue(new_x, x_min, x_max)
    y_min, y_max = setNewMinMaxValue(new_y, y_min, y_max)

    new_x, new_y = rotatePointAroundOrigin(-bbox[2]/2,bbox[3]/2, bbox[4])
    x_min, x_max = setNewMinMaxValue(new_x, x_min, x_max)
    y_min, y_max = setNewMinMaxValue(new_y, y_min, y_max)

    new_x, new_y = rotatePointAroundOrigin(-bbox[2]/2,-bbox[3]/2, bbox[4])
    x_min, x_max = setNewMinMaxValue(new_x, x_min, x_max)
    y_min, y_max = setNewMinMaxValue(new_y, y_min, y_max)
    
    new_x, new_y = rotatePointAroundOrigin(bbox[2]/2,-bbox[3]/2, bbox[4])
    x_min, x_max = setNewMinMaxValue(new_x, x_min, x_max)
    y_min, y_max = setNewMinMaxValue(new_y, y_min, y_max)
    
    bbox = np.zeros(4)
    bbox[0] = center_x + x_min
    bbox[1] = center_y + y_min
    bbox[2] = x_max - x_min
    bbox[3] = y_max - y_min

    return bbox #[x, y, w, h]

def addSaltAndPepperNoiseSolution(img):
    import numpy as np

    row,col,ch = img.shape
    s_vs_p = 0.5
    amount = 0.01
    out = np.copy(img)
    # Salt mode
    num_salt = np.ceil(amount * img.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
          for i in img.shape]
    out[coords] = 1
    # Pepper mode
    num_pepper = np.ceil(amount* img.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
          for i in img.shape]
    out[coords] = 0

    return out

def getROIfromBbox(img, bbox, bbox_deviation = [-20,-20,20,20]):
        x_start = int( bbox[0]  + bbox_deviation[0] )
        y_start = int( bbox[1]  + bbox_deviation[1] )
        x_end   = int( bbox[0] + bbox[2] + bbox_deviation[2] )
        y_end   = int( bbox[1] + bbox[3] + bbox_deviation[3] )

        x_start = int( bbox[0]  + bbox_deviation[0] )
        y_start = int( bbox[1]  + bbox_deviation[1] )
        x_end   = int( bbox[2] + bbox_deviation[2] )
        y_end   = int( bbox[3] + bbox_deviation[3] )
        roi = img[y_start:y_end, x_start:x_end, :]
        
        return roi

def insertROIintoImg(img, roi, bbox_deviation = [-20,-20,20,20]):
    y_start = 10
    x_start = 20
    y_end   = y_start + roi.shape[0]
    x_end   = x_start + roi.shape[1]

    img[y_start:y_end, x_start:x_end] = roi
    x = x_start - bbox_deviation[0]
    y = y_start - bbox_deviation[1]
    xe = x_end - bbox_deviation[2]
    ye = y_end - bbox_deviation[3]
    bbox = [x,y,xe,ye]
    
    return img, bbox

def addBboxToImg(img,bbox):
    import numpy as np
    import cv2 as cv
    if isinstance(bbox, list):
        bbox = np.array(bbox)
    if len(bbox.shape) == 1:
      if len(bbox) == 4:
        bbox = bbox.astype(int)
        img = cv.rectangle(img, (bbox[0],bbox[1]), (bbox[2],bbox[3]), (200,1,1), 3)
      if len(bbox) == 5:
        pts = getCornerPointsBBox(bbox)
        img = cv.fillPoly(img, [pts], (200,100,50) )
    else:
      raise NotImplementedError

    return img

def insertTshapeSolution(img, x,y,w,h,r):
    import numpy as np
    import cv2 as cv

    b = w/2
    center_x = x+b
    center_y = y

    img = np.ones((img_size,img_size,3), np.uint8) * 255
    center_p = [center_x, center_y]
    p1 = [center_x-r, center_y] 
    p2 = [center_x-r, center_y+h-2*r] 
    p3 = [center_x-r-b, center_y+h-2*r] 
    p4 = [center_x-r-b, center_y+h]
    p5 = [center_x+r+b, center_y+h]  
    p6 = [center_x+r+b, center_y+h-2*r] 
    p7 = [center_x+r, center_y+h-2*r] 
    p8 = [center_x+r, center_y]  

    pts = np.array([p1,p2,p3,p4,p5,p6,p7,p8],  np.int32)
    cv.fillPoly(img, [pts], (200,100,50))

    return img

def add_label(img, label):
    import cv2 as cv

    font                   = cv.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10, 10)
    fontScale              = 0.75
    fontColor              = (1,1,1)
    lineThickness          = 1
    lineType               = cv.LINE_AA
    bottomLeftOrigin       = True

    cv.putText(img, label, 
        bottomLeftCornerOfText, 
        font, fontScale, fontColor,
        lineThickness, lineType,
        bottomLeftOrigin)
    return img

def plot_cv_img(img, bbox = None, label = None, show = True):
    import matplotlib.pyplot as plt

    if bbox is not None:
        img = addBboxToImg(img,bbox)
    if label is not None:
        img = add_label(img, label)

    plt.imshow(img, interpolation='none',origin='lower', extent=[0, img.shape[1], 0, img.shape[0]])
    if show:
        plt.show()

    return img
