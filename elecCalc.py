# -*- coding: utf-8 -*-
#electrical calculator
import math
import cmath
import numpy as np
import matplotlib.pyplot as plot
from matplotlib.offsetbox import AnchoredText



#three phase power calculations
def singlePhaseLoad( powerConsumed, powerFactor, leadLag):
    #powerConsumed in kW
    #power factor
    #leadLag = 0 - lead, 1 - lag

    #get the angle from the pf
    angle = math.acos(powerFactor)

    #change angle depending on leading or lagging pf.
    if(leadLag == 1):
        angle = 0-angle; 

    #calculate the apparent power
    #S*pf = P
    apparentPower = powerConsumed/powerFactor;
    
    #get reactive Power
    reactivePower = apparentPower*math.sin(angle);

    #display values
    print("Angle is: {} rad / {} degrees").format(angle, math.degrees(angle))
    print("Apparent Power: {} VA").format(apparentPower)
    print("Reactive Power is: {} VAR").format(reactivePower);
    
def threePhaseLoad( powerConsumed, powerFactor, leadLag, voltagel2l):
    """
    Para: powerConsumed - power consumed by the 3phase load in W
          powerFactor - pf
          leadLag - leading pf - 0, lagging pf - 1
          voltage121 - line to line voltage across the 3 phase load
    """
    
    #powerConsumed in kW
    #power factor
    #leadLag = 0 - lead, 1 - lag

    #get the angle from the pf
    angle = math.acos(powerFactor)

    #change angle depending on leading or lagging pf.
    if(leadLag == 1):
        angle = 0-angle; 

    #calculate the apparent power
    #S*pf = P
    apparentPower = powerConsumed/powerFactor;
    
    #get reactive Power
    reactivePower = apparentPower*math.sin(angle);

    #get the line to line current
    currentl2l = apparentPower/(math.sqrt(3)*voltagel2l);
    #display values
    print("Angle is: {} rad / {} degrees").format(angle, math.degrees(angle))
    print("Apparent Power: {} VA").format(apparentPower)
    print("Reactive Power is: {} VAR").format(reactivePower);
    print("l2l Current is: {} A").format(currentl2l);

    
def polarRec(mod, angleDeg):
    """ 
       Converts from polar to rectangular coordinates
       return complexNumber
    """
    return cmath.rect(mod,math.radians(angleDeg))
    
def recPolar(complexNumber):
    """
       Converts from rectangular to polar coordinates.
       return (mod, angle in deg)
    """
    ans = cmath.polar(complexNumber)
    return (ans[0], math.degrees(ans[1]))

def paraImp(number1, number2):
    """
        Calculates the total impedence of 2 impedences in parallel
    """
    return (number1*number2)/(number1 + number2)

def impBaseConv(voltageRating, powerRating, voltageBase, powerBase, impedenceValue):
    """
        Parameters of equipment are given using the power rating of the equipment as the MVA base.
        This function converts Z values from old rating to new rating
        voltageRating - voltage rating of the equipment
        powerRating - powerRating of the equipment
        powerBase - the power base of where the equipment is being used
        voltageBase - the voltage base of where the equipmment is being used
        impedenceValue - the value to be converted between bases

        The formula for Zbase = Vbase**2/Sbase
        
    """
    return impedenceValue*((voltageRating**2/powerRating)/(voltageBase**2/powerBase))




def smibTransCalc(Egen, Vpoc, Xeq, EgenPost, VpocPost, XeqPost):

    #pre fault graph
    delta = np.arange(0, 3.14, 0.1);
    Pe = (abs(Egen)*abs(Vpoc)*np.sin(delta))/abs(Xeq)

    #post fault graph
    Pepost = (abs(EgenPost)*abs(VpocPost)*np.sin(delta))/abs(XeqPost)

    f,ax = plot.subplots(1,1)
    ax.plot(delta, Pe) #pre fault 
    ax.plot(delta, Pepost) #post fault
    ax.plot(delta, [ abs(Vpoc) for i in delta]) #mechanical power input
    
    plot.title("Power Curve")
    plot.xlabel("Power Angle Delta (rad)")
    plot.ylabel("Power (p.u or W)")
    plot.grid(True, which='both')
    #plot.text("Pe = {}sin(del)").format((abs(Egen)*abs(Vpoc))/abs(Xeq))

    anchored_text = AnchoredText("Pe = {}sin(del)".format((abs(Egen)*abs(Vpoc))/abs(Xeq)), loc=2)
    ax.add_artist(anchored_text)

    d0 = math.asin(Vpoc/((abs(Egen)*abs(Vpoc))/abs(Xeq)))
    d1 = math.asin(Vpoc/((abs(EgenPost)*abs(VpocPost))/abs(XeqPost)))
    print(d0)
    print(d1)

    plot.show()
    
