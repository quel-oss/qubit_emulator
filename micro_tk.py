import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import collections
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import time
import threading
import tkinter as tk
import keyboard
import cv2
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

#12/19: going to do: ax1: q1 control, ax2: q2 control, ax3: read input, ax4: jpa input, 
# ax8->ax6: read output, ax6,7 -> ax7,8: dsp q1+dsp q2

qubit = [1+0j,0+0j]

img = 250 * np.ones(shape=[240, 255, 3], dtype=np.uint8)
for i in range(4):
    for j in range(4):
        p_a = 45 + i*50
        p_b = 35 + j*50
        cv2.rectangle(img, pt1=(p_a,p_b), pt2=(p_a+50,p_b+50), color=(50,50,50), thickness=2)
        if i==0 and j ==0:
            cv2.putText(img,str("{:.2f}".format((qubit[0] * qubit[0].conjugate() * 100).real))+"%",(p_a+5,p_b+30),cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0,0,0),1,cv2.LINE_AA)
        elif i==0 and j ==1:
            cv2.putText(img,str("{:.2f}".format((qubit[1] * qubit[1].conjugate() * 100).real))+"%",(p_a+5,p_b+30),cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0,0,0),1,cv2.LINE_AA)
        else:
            cv2.putText(img,'0.0%',(p_a+5,p_b+30),cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0,0,0),1,cv2.LINE_AA)
cv2.putText(img,'0',(20,70),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),1,cv2.LINE_AA)
cv2.putText(img,'1',(20,120),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),1,cv2.LINE_AA)
cv2.putText(img,'2',(20,170),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),1,cv2.LINE_AA)
cv2.putText(img,'3',(20,220),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),1,cv2.LINE_AA)
cv2.putText(img,'0',(70,20),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),1,cv2.LINE_AA)
cv2.putText(img,'1',(120,20),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),1,cv2.LINE_AA)
cv2.putText(img,'2',(170,20),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),1,cv2.LINE_AA)
cv2.putText(img,'3',(220,20),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),1,cv2.LINE_AA)
imagebox = OffsetImage(img)
ab = AnnotationBbox(imagebox, (0.5, 0.5))

def update_img():
    '''global cont_test
    cont_test += 50
    img = cont_test * np.ones(shape=[256, 256, 3], dtype=np.uint8)'''
    global qubit 
    img = 250 * np.ones(shape=[240, 255, 3], dtype=np.uint8)
    for i in range(4):
        for j in range(4):
            p_a = 45 + i*50
            p_b = 35 + j*50
            cv2.rectangle(img, pt1=(p_a,p_b), pt2=(p_a+50,p_b+50), color=(50,50,50), thickness=2)
            if i==0 and j ==0:
                cv2.putText(img,str("{:.2f}".format((qubit[0] * qubit[0].conjugate() * 100).real))+"%",(p_a+5,p_b+30),cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0,0,0),1,cv2.LINE_AA)
            elif i==0 and j ==1:
                cv2.putText(img,str("{:.2f}".format((qubit[1] * qubit[1].conjugate() * 100).real))+"%",(p_a+5,p_b+30),cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0,0,0),1,cv2.LINE_AA)
            else:
                cv2.putText(img,'0.0%',(p_a+5,p_b+30),cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(img,'0',(20,70),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(img,'1',(20,120),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(img,'2',(20,170),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(img,'3',(20,220),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(img,'0',(70,20),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(img,'1',(120,20),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(img,'2',(170,20),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(img,'3',(220,20),cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0),1,cv2.LINE_AA)
    imagebox = OffsetImage(img)
    ab = AnnotationBbox(imagebox, (0.5, 0.5))
    ax5.add_artist(ab)

def apply_gate(phi,t):
    global qubit, qubit_h
    if len(qubit_h)>0:
        qubit=qubit_h[-1]
    qubit2 = [1+0j,0+0j]
    I = np.cos(phi)
    Q = np.sin(phi)
    theta = np.pi * t/26
    U = [[np.cos(theta/2)+0j,-Q*np.sin(theta/2)-I*(np.sin(theta/2))*1j],[Q*np.sin(theta/2)-I*(np.sin(theta/2))*1j,np.cos(theta/2)+0j]]
    qubit2[0] = U[0][0]*qubit[0] + U[0][1]*qubit[1]
    qubit2[1] = U[1][0]*qubit[0] + U[1][1]*qubit[1]
    qubit_h.append(qubit2)
    return(qubit2)

def basic_pulse(event):
    global input_sys_i, input_sys_q, output_sys_i,output_sys_q, qubit, qubit_h
    global pulse_on,ctrl_in,input_read,read_in,read_out,ms,pump_in, pump_on, jpa_pump
    global theta1,theta

    while('true'):
        if event.is_set():
            break
        input_sys_i.popleft()
        input_sys_q.popleft()
        output_sys_i.popleft()
        output_sys_q.popleft()
        input_read.popleft()
        jpa_pump.popleft()
        
        if len(read_in)>1:
            input_read.append(read_in[0][1])
            read_in = read_in[1:]
        else:
            input_read.append(0)
            read_in = []
    
        if len(read_out)>1:
            if read_out[-1][1]!=0:
                output_sys_i.append(read_out[0][1])
                output_sys_q.append(read_out[0][2])
                if theta<0.5:
                    theta += 0.01
                read_out = read_out[1:]
                test = (2*((1-(read_in[0][1])**2)**.5)*read_out[0][1] + (4*(read_in[0][1]**2 - read_out[0][1]**2))**.5)/2
                
                if ms != 1:
                    theta1 = theta * (-1)
                else:
                    theta1 = theta    
            else:     
                output_sys_i.append(0)
                output_sys_q.append(0)
        else:
            output_sys_i.append(0.0)
            output_sys_q.append(0.0)
            read_out = []
            theta = theta1 = 0

        if pulse_on==0:
            input_sys_i.append(0)
            input_sys_q.append(0)
        else:
            if len(ctrl_in)>0:
                input_sys_i.append(ctrl_in[0][1])
                input_sys_q.append(ctrl_in[0][2])
                ctrl_in = ctrl_in[1:]
                #Bloch
                if len(qubit_h)>0:
                    plotq = qubit_h[0]
                    qubit_h = qubit_h[1:]
                    dmatrix = [[1,1],[1,1]]
                    dmatrix[0][0] = plotq[0]*plotq[0].conjugate()
                    dmatrix[1][1] = plotq[1]*plotq[1].conjugate()
                    dmatrix[0][1] = plotq[0] * plotq[1].conjugate()
                    dmatrix[1][0] = plotq[0].conjugate() * plotq[1]
                    exp_data_record.append([2*dmatrix[0][1].real, 2*dmatrix[1][0].imag, dmatrix[0][0] - dmatrix[1][1]])
            else: 
                pulse_on = 0
                input_sys_i.append(0)
                input_sys_q.append(0)

        if pump_on==0:
            jpa_pump.append(0)            
        else:
            if len(pump_in)>0:
                jpa_pump.append(pump_in[0])
                pump_in = pump_in[1:]
            else:
                pump_on = 0
        
        global theta2,xa,ya
        theta2 = theta1+((np.random.rand()-0.5)**3)*1.5
        xa = np.cos(theta2)
        ya = np.sin(theta2)
        time.sleep(0.05)


def simple_pulse():
    global input_sys_i, input_sys_q,pulse_on,ctrl_in,qubit
    pulse_on=1
    for i in range(53):
        if (i>=0 and i<52):
            if(i>=0 and i<26):    
                phi = 0
            else:
                phi = np.pi/2
            a = np.sin(phi+(i/6.5)*np.pi)
            b = np.cos(phi+(i/6.5)*np.pi)
            qubit = apply_gate(phi,1)
            
        else:
            a = b = 0
        ctrl_in.append([i,a,b])
    update_img()
        #time.sleep(0.1)
        #qubit = apply_gate(0,1) #RX-gate
        #qubit = apply_gate(np.pi/2,1) #RY-gate

def long_pulse():
    global input_sys_i, input_sys_q,pulse_on,ctrl_in, qubit
    pulse_on=1
    for i in range(160):
        if (i>=0 and i<160-1):   
            phi = 0
            a = np.sin(phi+(i/26)*np.pi)
            b = np.cos(phi+(i/26)*np.pi)
            qubit = apply_gate(phi,1)
        else:
            a = b = 0
        ctrl_in.append([i,a,b])
    update_img()
        #qubit = apply_gate(0,1) #RX-gate
        #qubit = apply_gate(np.pi/2,1) #RY-gate
        
def plot_data(input_wave):
    time = input_wave[0]
    i = input_wave[1]
    q = input_wave[2]
    ctrl_in.append([time,i,q])
    
def readout(output):
    global qubit, read_in, read_out
    time = output[0]
    inpt = output[1]
    i = output[2]
    q = output[3]
    read_in.append([time, inpt])
    read_out.append([time,i,q])
    
def measurement():    
    global ms,qubit
    r = np.random.random()
    if (r>abs(qubit[0])):
        ms = 1
        zure = np.pi/4
    else:
        ms = 0
        zure = -np.pi/4
    print(ms)
    for i in range(60):
        inpt = np.sin(4*i*np.pi/30)
        a = i/60 * np.sin(4*i*np.pi/30 + zure)
        b = i/60 * np.cos(4*i*np.pi/30 + zure)
        out = [i, inpt, a, b]
        readout(out)
        #time.sleep(0.1)
        #time.sleep(0.1)
        
def x_gate():
    global qubit
    for i in range(27):
        if(i>=0 and i<26):
            phi = 0
            a = np.sin(phi+(i/26)*np.pi)
            b = np.cos(phi+(i/26)*np.pi)
            qubit = apply_xgate(1)
        else:
            a=b=0
        input_wave = [i, a, b]
        plot_data(input_wave)
        
def y_gate():
    global qubit
    for i in range(27):
        if(i>=0 and i<26):
            phi = np.pi/2
            a = np.sin(phi+(i/26)*np.pi)
            b = np.cos(phi+(i/26)*np.pi)
            qubit = apply_ygate(1)
        else:
            a=b=0
        input_wave = [i, a, b]
        plot_data(input_wave)

def z_gate():
    global qubit
    for i in range(27):
        if(i>=0 and i<26):
            phi = np.pi/4
            a = np.sin(phi+(i/26)*np.pi)
            b = np.cos(phi+(i/26)*np.pi)
            qubit = apply_zgate(1)
        else:
            a=b=0
        input_wave = [i, a, b]
        plot_data(input_wave)

def h_gate():
    global qubit
    for i in range(40):
        if(i>=0 and i<13):
            phi = np.pi/4
            a = np.sin(phi+(i/26)*np.pi)
            b = np.cos(phi+(i/26)*np.pi)
            qubit = apply_zgate(1)
        elif(i>=13 and i<26):
            phi = 0
            a = np.sin(phi+(i/26)*np.pi)
            b = np.cos(phi+(i/26)*np.pi)
            qubit = apply_xgate(1)
        elif(i>=26 and i<39):
            phi = np.pi/4
            a = np.sin(phi+(i/26)*np.pi)
            b = np.cos(phi+(i/26)*np.pi)
            qubit = apply_zgate(1)
        else:
            a=b=0
        input_wave = [i, a, b]
        plot_data(input_wave)
        
def apply_xgate(t):
    global qubit
    if len(qubit_h)>0:
        qubit=qubit_h[-1]
    qubit2 = [1+0j,0+0j]
    theta = np.pi * t/26
    U = [[np.cos(theta/2)+0j,-(np.sin(theta/2))*1j],[-(np.sin(theta/2))*1j,np.cos(theta/2)+0j]]
    qubit2[0] = U[0][0]*qubit[0] + U[0][1]*qubit[1]
    qubit2[1] = U[1][0]*qubit[0] + U[1][1]*qubit[1]
    return qubit2

def apply_ygate(t):
    global qubit
    if len(qubit_h)>0:
        qubit=qubit_h[-1]
    qubit2 = [1+0j,0+0j]
    theta = np.pi * t/26
    U = [[np.cos(theta/2)+0j,-np.sin(theta/2)+0j],[np.sin(theta/2)+0j,np.cos(theta/2)+0j]]
    qubit2[0] = U[0][0]*qubit[0] + U[0][1]*qubit[1]
    qubit2[1] = U[1][0]*qubit[0] + U[1][1]*qubit[1]
    return qubit2

def apply_zgate(t):
    global qubit
    if len(qubit_h)>0:
        qubit=qubit_h[-1]
    qubit2 = [1+0j,0+0j]
    theta = np.pi * t/26
    U = [[np.exp(-(theta/2)*1j)+0j,0+0j],[0+0j,np.exp((theta/2)*1j)+0j]]
    qubit2[0] = U[0][0]*qubit[0] + U[0][1]*qubit[1]
    qubit2[1] = U[1][0]*qubit[0] + U[1][1]*qubit[1]
    return qubit2

def pump():
    global pump_in, pump_on
    pump_on = 1
    for i in range(128):
        if(i>=0 and i<127):
            phi = np.pi/2
            a = np.sin(phi+(i/26)*np.pi)
        else:
            a=0
        pump_in.append(a)

exp_data_record = []
qubit_h = []
# function to update the data
pulse_on = 0
pump_on = 0
ctrl_in = []
read_in = []
read_out = []
pump_in = []
theta = 0
theta1 = 0
theta2 = 0
signal_range = 0.5
ms = 0 #measurement

#fig = plt.figure()
fig = plt.figure(figsize=(10,8), facecolor='#DEDEDE', tight_layout=True)
                   
#ブロッホ球の描写
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

sin_u = np.zeros(100)
cos_u = np.zeros(100)
sin_v = np.zeros(100)
cos_v = np.zeros(100)

for i in range(100):
    sin_u[i]=(np.sin(u[i]))
    cos_u[i]=(np.cos(u[i]))
    sin_v[i]=(np.sin(v[i]))
    cos_v[i]=(np.cos(v[i]))
    
x = 1 * np.outer(np.cos(u), np.sin(v))
y = 1 * np.outer(np.sin(u), np.sin(v))
z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))

k = np.linspace(-np.pi, np.pi, 100)

l=np.zeros(100)
m=np.zeros(100)

for i in range(100):
    l[i] = np.sin(k[i])
    m[i] = np.cos(k[i])


def animation_plot(i):
    global signal_range, read_in, read_out, theta, m,pump_in, jpa_pump,qubit
        
    # clear axis
    ax1.cla()
    ax2.cla()
    ax3.cla()
    ax4.cla()
    
    ax1.set_title("Input Control Wave")
    ax2.set_title("Input Readout Wave")
    ax3.set_title("Output Readout Wave")
    ax4.set_title("Input JPA Pump")
    
    # plot input1
    ax1.plot(input_sys_i,color="blue")
    ax1.scatter(99, input_sys_i[-1],color="blue")
    ax1.set_ylim(-1,1)
    ax1.plot(input_sys_q,color="red")
    ax1.scatter(99, input_sys_q[-1],color="red")

    # plot input2
    ax2.plot(input_read,color="blue")
    ax2.scatter(len(input_read)-1, input_read[-1],color="blue")
    ax2.set_ylim(-1,1)

    # plot output
    ax3.plot(output_sys_i,color="blue")
    ax3.scatter(len(output_sys_i)-1, output_sys_i[-1],color="blue")
    ax3.set_ylim(-1,1)
    ax3.plot(output_sys_q,color="red")
    ax3.scatter(len(output_sys_q)-1, output_sys_q[-1],color="red")

    # plot jpa input
    ax4.plot(jpa_pump,color="blue")
    ax4.scatter(len(jpa_pump)-1,jpa_pump[-1],color="blue")
    ax4.set_ylim(-1,1)
    
    '''
    #plot Bloch sphere
    ax5.set_box_aspect([1,1,1])

    #目盛りとラベル
    ax5.set_xlabel('X')
    ax5.set_ylabel('Y')
    ax5.set_zlabel('Z')
    ax5.set_xlim(-1,1)
    ax5.set_ylim(-1,1)
    ax5.set_zlim(-1,1)
    ax5.set_xticks([-1,-0.5,0,0.5,1])
    ax5.set_yticks([-1,-0.5,0,0.5,1])
    ax5.clear()  
    ax5.grid(None)
    ax5.plot_surface(x, y, z,  rstride=4, cstride=4, color='lightblue', linewidth=0, alpha=0.25)

    ax5.plot(sin_u,cos_u,0,color='gray',linewidth=1.2)
    ax5.plot(np.linspace(0,0,100),sin_u,cos_u,color='gray',linewidth=1.2)
    ax5.plot(sin_u,np.linspace(0,0,100),cos_u,color='gray',linewidth=.5)

    for i in range(-4,5,1):
        if i!=0:
            d = .25 * i
        s = ((1-d**2)**.5)
        ax5.plot(sin_u*s,cos_u*s,d,color='gray',linewidth=.3)
        ax5.plot(np.linspace(d,d,100),sin_u*s,cos_u*s,color='gray',linewidth=.3)
    
    if (len(exp_data_record) > 0):
        if (exp_data_record[-1][0] <= 1.00001):
            ax5.plot(exp_data_record[-1][0], exp_data_record[-1][1], exp_data_record[-1][2], "o", c="blue")
        else:
            ax5.plot(0, 0, 1, "o", c="blue") 
    else:
        ax5.plot(0, 0, 1, "o", c="blue")
    '''
    #Digital Signal Processing Graph
    global theta2,xa,ya
    ax6.clear()
    ax6.set_title("Digital Signal Processing")
    ax6.plot(l,m,linestyle='dotted', color="gray")
    ax6.plot([0,xa],[0,ya], color="red")
    if len(jpa_pump)>0:
        if (jpa_pump[-1] != 0):
            if(signal_range>0.15):
                signal_range-=0.01
        else:
            if(signal_range<0.5):
                signal_range+=0.01
    cc = plt.Circle((xa,ya),signal_range,color="red")
    ax6.add_artist( cc ) 
    ax6.spines['left'].set_position('zero')
    ax6.spines['bottom'].set_position('zero') 
    ax6.plot(0.85,0.5,"o",color="orangered")  
    #ax6.text(0.5, 0.85, 'θ1')
    ax6.plot(0.85,-0.5,"o",color="deepskyblue")
    #ax6.text(0.85, 0.5, 'θ0')
    ax6.set_xlim(-1.5,1.5)
    ax6.set_ylim(-1.2,1.2)
    
    ax7.clear()
    ax7.set_title("Output Wave I-Q")
    xx = output_sys_i[-1]
    yy = output_sys_q[-1]
    cc2 = plt.Circle((xx,yy),0.2,color="red")
    ax7.add_artist( cc2 ) 
    ax7.spines['left'].set_position('zero')
    ax7.spines['bottom'].set_position('zero') 
    ax7.plot(0.85,0.5,"o",color="orangered")  
    ax7.plot(0.85,-0.5,"o",color="deepskyblue")
    ax7.set_xlim(-1.5,1.5)
    ax7.set_ylim(-1.2,1.2)
    
    # Info
    ax8.clear()
    textstr = 'Hamiltonian = ωa†a+α/2 a†a†aa \n|ψ> = \n[δ(p3)=0\n γ(p2)=0\n α(p0)='+'{:.3g}'.format(qubit[0])+'\n β(p1)='+'{:.3g}'.format(qubit[1])+']'
    ax8.text(0.3, 0.3, textstr)

# start collections with zeros
input_sys_i = collections.deque(np.zeros(100))
input_sys_q = collections.deque(np.zeros(100))
input_read = collections.deque(np.zeros(100))
output_sys_i  = collections.deque(np.zeros(100))
output_sys_q  = collections.deque(np.zeros(100))
output_read  = collections.deque(np.zeros(100))
jpa_pump = collections.deque(np.zeros(100))

# define and adjust figure
gs = fig.add_gridspec(4,4)
from mpl_toolkits.axisartist.axislines import Subplot 
ax1 = fig.add_subplot(gs[0, 0:2], facecolor="white")
ax2 = fig.add_subplot(gs[1, 0:2], facecolor="white")
ax3 = fig.add_subplot(gs[2, 0:2], facecolor="white")
ax4 = fig.add_subplot(gs[3, 0:2], facecolor="white")
ax5 = Subplot(fig, 222)
fig.add_subplot(ax5)
#fig.add_subplot(gs[0:2, 2:4])
ax5.axis["left"].set_visible(False)
ax5.axis["bottom"].set_visible(False)
ax5.add_artist(ab)
#ax5 = fig.add_subplot(gs[0:2, 2:4], projection='3d')
ax6 = fig.add_subplot(gs[2, 2:3], facecolor="white")
ax7 = fig.add_subplot(gs[2, 3:4], facecolor="white")
ax8 = fig.add_subplot(gs[3, 2:4], facecolor="white")

#グリッドと最初の表示
#ax5.view_init(elev = 17, azim = 12)

# animate
ani = FuncAnimation(fig, animation_plot, interval=50)

def _destroyWindow():
    root.quit()
    root.destroy()

def btn_simple():
    threading.Thread(target=simple_pulse).start()
    #canvas.get_tk_widget().pack()

def btn_long():
    threading.Thread(target=long_pulse).start()
    #canvas.get_tk_widget().pack()

def btn_measure():
    threading.Thread(target=measurement).start()
    #canvas.get_tk_widget().pack()

def btn_pump():
    threading.Thread(target=pump).start()
    #canvas.get_tk_widget().pack()

# Tkinter Class
root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)  # When you close the tkinter window.
event = threading.Event()
threading.Thread(target=basic_pulse, args=(event,)).start()

# Canvas
canvas = FigureCanvasTkAgg(fig, master=root)  # Generate canvas instance, Embedding fig in root
canvas.draw()
canvas.get_tk_widget().pack()

btn1=tk.Button(root,text="Simple Pulse",command=btn_simple)
btn1.pack()
btn2=tk.Button(root,text="Long Pulse",command=btn_long)
btn2.pack()
btn3=tk.Button(root,text="Measurement",command=btn_measure)
btn3.pack()
btn4=tk.Button(root,text="JPA Pump",command=btn_pump)
btn4.pack()
#canvas._tkcanvas.pack()

# root
root.update()
root.deiconify()
root.mainloop()
event.set()