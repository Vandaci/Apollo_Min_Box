# -*- coding:utf-8 -*-
import numpy as np  

def GetCloudMinMax3D(cloud,min_point,max_point):
    min_point[0]=np.min(cloud.x)
    min_point[1]=np.min(cloud.y)
    min_point[2]=np.min(cloud.z)
    max_point[0]=np.max(cloud.x)
    max_point[1]=np.max(cloud.y)
    max_point[2]=np.max(cloud.z)
    