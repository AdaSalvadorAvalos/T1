# Ada Salvador Avalos

# Exercici 1
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd      
from numpy.fft import fft     
# Amb 4kHz
T= 2.5                               
fm=8000                              
fx=4000                              
A=4                                  
pi=np.pi                            
L = int(fm * T)                      
Tm=1/fm                              
t=Tm*np.arange(L)                    
x = A * np.cos(2 * pi * fx * t)      
sf.write('nom_fitxer1.wav', x, fm)   
Tx=1/fx                                   
Ls=int(fm*5*Tx)                           

plt.figure(111)                            
plt.plot(t[0:Ls], x[0:Ls])                
plt.xlabel('t en segons')                 
plt.title('fx= 4kHz, 5 periodes de la sinusoide')   
plt.show()                                

sd.play(x, fm)    


N=5000                       
X=fft(x[0 : Ls], N)           
k=np.arange(N)                       
plt.figure(112)                         
plt.subplot(211)                      
plt.plot(k,abs(X))                    
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                  
plt.subplot(212)                      
plt.plot(k,np.unwrap(np.angle(X)))    
plt.xlabel('Index k')                 
plt.ylabel('$\phi_x[k]$')             
plt.show() 

# Amb 523Hz 
T= 2.5                              
fm=8000                            
fx=523                              
A=4                               
pi=np.pi                            
L = int(fm * T)                      
Tm=1/fm                              
t=Tm*np.arange(L)                    
x = A * np.cos(2 * pi * fx * t)     
sf.write('nom_fitxer2.wav', x, fm)   
Tx=1/fx                                  
Ls=int(fm*5*Tx)                          

plt.figure(121)                             
plt.plot(t[0:Ls], x[0:Ls])                
plt.xlabel('t en segons')                
plt.title('fx= 523Hz,5 periodes de la sinusoide')   
plt.show()                              

sd.play(x, fm)    


N=5000                        
X=fft(x[0 : Ls], N)           
k=np.arange(N)                      
plt.figure(122)                        
plt.subplot(211)                      
plt.plot(k,abs(X))                   
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')               
plt.subplot(212)                     
plt.plot(k,np.unwrap(np.angle(X)))  
plt.xlabel('Index k')                 
plt.ylabel('$\phi_x[k]$')             
plt.show() 

#--------------------------------------------------------------------

# Exercici 2

x_r, fm=sf.read('nom_fitxer1.wav')         #agafo la senyal del segon fitxer creat en el exercici anterior, agafo la seva
#informació i la fm
Tm=1/fm                            
t=Tm* np.arange(len(x_r))               
sf.write('nom_fitxerej2.wav', x_r, fm)   

#  - Insereix a continuació una gràfica que mostri 5 períodes del senyal i la seva transformada.
fx=4000
Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(21)                             
plt.plot(t[0:Ls], x_r[0:Ls])                
plt.xlabel('t en segons')              
plt.title('Exercici 2, 5 periodes de la sinusoide')   
plt.show()                              

sd.play(x_r, fm)    

N=5000                       
X=fft(x_r[0 : Ls], N)         
k=np.arange(N)                        
plt.figure(22)                        
plt.subplot(211)                     
plt.plot(k,abs(X))                   
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                 
plt.subplot(212)                      
plt.plot(k,np.unwrap(np.angle(X)))   
plt.xlabel('Index k')               
plt.ylabel('$\phi_x[k]$')             
plt.show()    

#---------------------------------------------------------------------------------------
#Exercici 3

T= 2.5                               
fm=8000                             
fx=440                               
A=4                                  
pi=np.pi                           
L = int(fm * T)                     
Tm=1/fm                              
t=Tm*np.arange(L)                   
x = A * np.cos(2 * pi * fx * t)     
sf.write('nom_fitxerej3.wav', x, fm)  
Tx=1/fx                                   
Ls=int(fm*Tx*5)                           

plt.figure(31)                             
plt.plot(t[0:Ls], x[0:Ls])               
plt.xlabel('t en segons')                 
plt.title('Exercici 3')  
plt.show()                                

sd.play(x, fm)    


N=5000                        
X=fft(x[0 : Ls], N)          
k=np.arange(N)                       
FK=k/N * fm                           #Calcul de la fk, pels valors de l'eix d'abscisses
plt.figure(32)                         
plt.subplot(211)                     
plt.plot(FK/2,abs(20*np.log10(X/max(X))))  # Representació del mòdul de la transformada en dB y de 0 a FK/2
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                
plt.subplot(212)                     
plt.plot(k,np.unwrap(np.angle(X)) )   
plt.xlabel('Index k')                
plt.ylabel('$\phi_x[k]$')             
plt.show() 

#--------------------------------------------------------------------------------------

#Exercici 4
T= 0.025                               
data, fm =sf.read('luzbel44.wav')       
L = int(fm * T)                     
Tm=1/fm                            
t=Tm*np.arange(L)                  
sf.write('nom_fitxerej4.wav', data, fm)  

plt.figure(41)                          
plt.plot(t[0:L],data[0:L])              
plt.xlabel('t en segons')               
plt.title('Exercici 4')  
plt.show()                             


N=5000                        
X=fft(data[0 : L], N)       
k=np.arange(N)                        
FK=k/N * fm
k2=np.arange(len(FK/2),len(FK))                       
plt.figure(42)                         
plt.subplot(211)                      
plt.plot(k2,abs(20*np.log10(int(X[fm/2:fm])/max(int(X[fm/2:fm]))))) 
plt.title(f'Transformada del senyal de Ls={L} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                 
plt.subplot(212)                      
plt.plot(k2,np.unwrap(np.angle(X)) )   
plt.xlabel('Index k')                  
plt.ylabel('$\phi_x[k]$')            
plt.show() 
