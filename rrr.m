clc 
clear all
num=[1.5];                  %ingresa numerador del sistema
den=[20 1];                %ingresa denominador del sistema 
ret=3;                    %ingresa retardo del sistema
T=5;
gs=tf(num,den,'inputdelay',ret)%generacion de la funcion de trasferencia
gz=c2d(gs,T,'zoh')
figure(1)
margin(gz)
[Gm,Pm,Wog,Wop]=margin(gz)