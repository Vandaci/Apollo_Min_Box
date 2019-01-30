# -*- coding:utf-8 -*-
import numpy as np 
from geometry_util import *

def ComputePolygon2dxy(obj):
    min_point=np.zeros(4)
    max_point=np.zeros(4)
    cloud=obj.cloud # class pointcloud Obj contains pointcloud
    SetDefaultValue(cloud,obj,min_point,max_point)


def SetDefaultValue(cloud,obj,min_point,max_point):
    GetCloudMinMax3D(cloud,min_point,max_point)
    obj.length=max_point[0]-min_point[0]
    obj.width=max_point[1]-min_point[1]
    if obj.length>obj.width:
        obj.length,obj.width=obj.width,obj.length
        obj.direction=[0,1,0]
    else:
        obj.direction=[1,0,0]
    obj.height=max_point[2]-min_point[2]
    obj.center=(max_point+min_point)/2
    obj.center=obj.center[:3]
    if cloud.size < 4:
        obj.polygon.x[0]=min_point[0]
        obj.polygon.x[1]=max_point[0]
        obj.polygon.x[2]=max_point[0]
        obj.polygon.x[3]=min_point[0]
        obj.polygon.y[0]=min_point[1]
        obj.polygon.y[1]=min_point[1]
        obj.polygon.y[2]=max_point[1]
        obj.polygon.y[3]=max_point[1]
        obj.polygon.z[0]=min_point[2]
        obj.polygon.z[1]=min_point[2]
        obj.polygon.z[2]=min_point[2]
        obj.polygon.z[3]=min_point[2]

