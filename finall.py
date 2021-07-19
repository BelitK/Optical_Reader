#!/usr/bin/env python
# coding: utf-8

# In[64]:


import cv2
import numpy as np
import argparse


# Set threshold level


#image = [coords[0][0]:coords[0][1],coords[-1][0]:coords[-1][1]]


# In[65]:


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
args = vars(ap.parse_args())
# load the image
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# In[55]:


threshold_level = 55

# Find coordinates of all pixels below threshold
coords = np.column_stack(np.where(gray < threshold_level))


# In[56]:


coords


# In[57]:


x1,y1=coords[1]
x2,y2= coords[-1]
x1,y1,x2,y2


# In[59]:


print(coords)

# Create mask of all pixels lower than threshold level
mask = gray < threshold_level

# Color the pixels in the mask
#image[mask] = (204, 119, 250)


# In[ ]:





# In[60]:


cropped_image = image[x1:x2, y1:y2]


# In[61]:


cv2.imshow('image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




