import math
import seaborn as sns
import matplotlib.pyplot as plt

def f(v):
  """
  Function to evaluate the given function at a specific value.

  Parameters:
  - v (float): The value at which to evaluate the function.

  Returns:
  - float: The result of evaluating the function at the given value.
  """
  return 0.5*1.225+math.cos(v)*v**2*15.165*(2*(math.pi)*0.0872665)/(1+(2/7.32)); #Function, replace A/R

def biseccion(a,b,tol):
  """
  Bisection method for finding the root of a function within a given interval.

  Parameters:
  - a (float): The left endpoint of the interval.
  - b (float): The right endpoint of the interval.
  - tol (float): Tolerance level to determine the convergence of the method.

  Returns:
  None
  """
  
  #Initialize Max number of iterations, Left and Right Endpoint, Number of ITerations, Error and Empty lists to graph x,y  
  niter=100
  m1=float(a);
  m=float(b);
  k=0
  err=1+tol
  approximations = []
  f_values = []
  
  #Bisection Procedure  
  if (f(a)*f(b)>0):
    print("Function won't change sign")
  fev=f((a+b)/2)
  fint=f(fev)
  while (abs(m1-m)> tol) and k<niter and fint!=0 :
    k=k+1
    m1=m;
    m=(a+b)/2;
    if (f(a)*f(m)<0): #Sign changes in (a,m)
      b=m;
    if (f(a)*f(m)>0): #Sign changes in (m,b)
      a=m;
    err=abs(m1-m)#error, if Corr Dec
    #err=abs((m1-m)/m1) #error, if Sig Fig
    
    #Append x and y values
    approximations.append(m)
    f_values.append(f(m))
    
    #Print iterations
    print("N:",k, "xn:", m, "fm:", f(m), "Error:", err )
  print("\n"'On iteration:',k, 'x=',m, 'was found to be a good approach for the root of the function')

  # Plotting the function and approximations
  sns.set(style='darkgrid')
  plt.plot(approximations, f_values, 'ro-', label='Approximations')
  v = [i/10 for i in range(-50, 51)]  # Range of v values for the function plot
  plt.plot(v, [f(x) for x in v], label='Function f(v)')
  plt.axhline(y=0, color='black', linestyle='--', label='y=0')
  plt.xlabel('v')
  plt.ylabel('f(v)')
  plt.title('Bisection Method')
  plt.legend()
  plt.show()

  
biseccion(-2,2,0.5e-5)