#!/usr/bin/env python

import math
import pantilthat
from gps3 import gps3
import time

pantilthat.tilt(0)
pantilthat.pan(0)
time.sleep(1)

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()


#Math for calculating angles
#L = Longitude, theta= latitude, beta= pan angle, R=earth's radius
#Beta=atan2(X,Y)
#X=cos(theta2)*sin(delta L)
#Y=cos(theta1)*sin(theta2)-sin(theta1)*cos(theta2)*cos(delta L)

for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        print('Altitude = 1.07 m')
        print('Latitude = ', data_stream.TPV['lat'])
        print('Longitude = ', data_stream.TPV['lon'])
        theta1=data_stream.TPV['lat']
        L1=data_stream.TPV['lon']
        a1=1.07
        theta2=float(input("What is the latitude of the object? "))
        L2=float(input("What is the longitude of the object? "))
        a2=float(input("What is the altitude of the object? "))
        print(type(L1))

        if (type(L1) is float):
            try:
                delta_L=L2-L1
                delta_theta=theta2-theta1
                delta_a=a2-a1 

                X=math.cos(theta2*math.pi/180)*math.sin(delta_L*math.pi/180)
                Y=math.cos(theta1*math.pi/180)*math.sin(theta2*math.pi/180)-math.sin(theta1*math.pi/180)*math.cos(theta2*math.pi/180)*math.cos(delta_L*math.pi/180)
                beta=math.atan2(X,Y)*180/math.pi #degrees

                #a=haversine,c=scalar, d=distance,R= Earth's radius, alpha=tilt angle
                R=6371*10^3 #meters
                a=math.sin(delta_theta/2*math.pi/180)**2+math.cos(theta1*math.pi/180)*math.sin(delta_L/2*math.pi/180)**2
                c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
                d=R*c
                alpha=math.atan2(d,delta_a)*180/math.pi #degrees

                alpha_int=round(alpha)+50
                beta_int=round(beta)+30

                if alpha_int > 90:
                    alpha_int=alpha_int-180
                if alpha_int < -90:
                    alpha_int=alpha_int+180

                if beta_int > 90:
                    beta_int=beta_int-180
                if beta_int < -90:
                    beta_int=beta_int+180
                    
                print(alpha_int)
                print(beta_int)
                #pan and tilt    
                pantilthat.tilt(alpha_int)
                pantilthat.pan(beta_int)
            except KeyboardInterrupt:
                continue




