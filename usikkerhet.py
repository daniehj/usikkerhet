from pylab import *


def usikkerhet(x,y,plot=False):
    lin = []
    d = []
    
    n = len(y)
    D = sum(dot(x,x))-(1./n)*(sum(x))**2
    E = sum(dot(x,y))-(1./n)*(sum(x)*sum(y))
    F = sum(dot(y,y))-(1./n)*(sum(y))**2
    
    m = E/D
    c = mean(y)-m*mean(x)
    
    for i in range(len(y)):
        lin.append(x[i]*m + c)
        d.append(lin[i]-y[i])
    
        
    
    deltam = (1./(n-2))*(D*F-E**2)/D**2
    deltac = (1./(n-2))*((D/n) + mean(x)**2)*(D*F-E**2)/D**2
    
    liner = "%fx + %f" % (m,c)
    print "linear regression:",liner
    
    print "Delta m: " , sqrt(deltam)
    print "Delta c: " , sqrt(deltac)
    
    
    if plot:
        figure()
        plot(x,y,'ob',
             x,lin,'-r')
        legend(('$Datapoints$','$linear:$' + '$'+liner+'$',),
        loc='best', fontsize='small', fancybox=True, shadow=True)
        grid(True)
        show()
