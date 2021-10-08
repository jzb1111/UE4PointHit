# -*- coding: utf-8 -*-
import numpy as np
import unreal_engine as ue
from unreal_engine.enums import EPixelFormat
from unreal_engine.classes import ParticleSystem, Material
#[theta,phi]phi:shuzhijiao,theta:shuipingjiao

points=[[0,0],[10,0],[0,90],[20,30],[90,10],[44,0],[300,0],[190,36],[24,40],[90,0],[50,350],[304,4],[186,26],[300,356]]

class GeneratePoint:
    def begin_play(self):
        self.uobject.get_owner().bind_event('OnCalcLocation',self.calc_location)
    def calc_location(self):
        
        Actor=self.uobject.get_owner()
        for i in range(len(points)):
            pt=points[i]
            loc=self.angle2location(pt)
            Actor.LocationX=loc[0]
            Actor.LocationY=-loc[1]
            Actor.LocationZ=loc[2]
            Actor.call_function('AddToTransformArray')
    def angle2location(self,phi_theta):
        r=1000
        phi=phi_theta[1]*(2*np.pi/360)
        theta=phi_theta[0]*(2*np.pi/360)
        x=r*np.cos(phi)*np.cos(theta)
        y=r*np.sin(theta)*np.cos(phi)
        z=r*np.sin(phi)
        return [x,y,z]