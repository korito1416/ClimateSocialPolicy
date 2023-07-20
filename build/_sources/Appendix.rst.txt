Appendix A. Computation Method
==============================

Appendix A.1 Upwind Scheme
--------------------------

Appendix A.1.1 Discretized State Space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Suppose we have three controled stochastic process :math:`x_t, y_t, z_t`
as

.. math::

   \begin{aligned}
   d x_t &= \mu^x(x,y,z,\alpha) dt + \sigma^{x}(x,y,z,\alpha) dB^1_t \\
   d y_t &= \mu^y(x,y,z,\alpha) dt + \sigma^{y}(x,y,z,\alpha) dB^2_t \\
   d z_t &= \mu^z(x,y,z,\alpha) dt + \sigma^{z}(x,y,z,\alpha) dB^3_t 
   \end{aligned}

where :math:`B^1_t, B^2_t, B^3_t` are three independent standard
Brownian process.

Let’s consider a generalized three-dimensional HJB equation for a
stationary equilibirum:

.. math::

   \begin{aligned}
   0= & \max_{\alpha} -\delta v(x,y,z) + u(x,y,z,\alpha)\\
       & + \mu^x(x,y,z,\alpha) \partial_x v(x,y,z) + \frac{{\sigma^x}(x,y,z,\alpha)^2}{2}\partial_{xx} v(x,y,z) \\
       &+ \mu^y(x,y,z,\alpha) \partial_y v(x,y,z) + \frac{{\sigma^y}(x,y,z,\alpha)^2}{2}\partial_{yy} v(x,y,z) \\
       & + \mu^z(x,y,z,\alpha) \partial_z v(x,y,z) + \frac{{\sigma^z}(x,y,z,\alpha)^2}{2}\partial_{zz} v(x,y,z)
   \end{aligned}

where :math:`\alpha` is the set of controls in the HJB equation,
:math:`x,y,z` are the state variables of value function :math:`v` and
:math:`u` is the utility function.

Accordingly, we construct equispaced grids for these three state
variable :math:`x,y,z` as

.. math::

   \begin{aligned}
   X &= \{x_1,\ldots,x_N\} \\
   Y &= \{y_1,\ldots,y_N\} \\
   Z &= \{z_1,\ldots,z_N\}
   \end{aligned}

where we set the upper and lower bound as

.. math::

   \begin{aligned}
   x_1 &= \underline{X}, x_N=\bar{X} \\
   y_1 &= \underline{Y}, y_N=\bar{Y} \\
   z_1 &= \underline{Z}, z_N=\bar{Z} \\
   \end{aligned}

and the distance between two grid points are as
:math:`\Delta x, \Delta y, \Delta z`

Appendix A.1.2 Control and Approximation to Value Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that we have discretized the state space, we can approximate value
function on grid points and use short-hand notation
:math:`v(x_i,y_j,z_k) \doteq v_{i,j,k}` and so on.

The partial derivatives :math:`\partial_x v(x,y,z)` can be approximated
with either a forward or backward difference approximation

.. math::

   \begin{aligned}
   \partial_{x,F} v_{i,j,k} &=  \frac{v_{i+1,j,k}-v_{i,j,k}}{\Delta x} \\
   \partial_{x,B} v_{i,j,k} &=  \frac{v_{i,j,k}-v_{i-1,j,k}}{\Delta x} 
   \end{aligned}

For accuracy, we decide to approximate the partial derivatives
:math:`\partial_x v(x,y,z)` via central difference approximation

.. math::

   \begin{aligned}
   \partial_{x,C} v_{i,j,k} &=  \frac{v_{i+1,j,k} - v_{i-1,j,k}}{2\Delta x} 
   \end{aligned}

which can be viewed as an average of forward and backward difference
approximation.

And we also approximate the second-order partial derivatives
:math:`\partial_{xx} v(x,y,z)` with a central difference approximation

.. math::

   \begin{aligned}
   \partial_{xx} v_{i,j,k} &=  \frac{v_{i+1,j,k} + v_{i-1,j,k}- 2v_{i,j,k}}{\Delta x^2} 
   \end{aligned}

Suppose we have a initial guess for value function, we can employ the
first-order-condition to express our control :math:`\alpha` on a grid
point :math:`x_i, y_j, z_k` as a nonlinear function of value function
approximations :math:`\partial_{x,C} v_{i,j,k}`,
:math:`\partial_{xx} v_{i,j,k}`.

In other words, we write our control, drift and diffusion term as

.. math::

   \begin{aligned}
   \alpha(x_i,y_j,z_k) &= \alpha_{i,j,k} \\
   u(x_i,y_j,z_k,\alpha_{i,j,k}) &= u_{i,j,k} \\
   \mu^w(x_i,y_j,z_k,\alpha_{i,j,k}) &= \mu^w_{i,j,k}, \quad w=x,y,z\\
   \sigma^w(x_i,y_j,z_k,\alpha_{i,j,k}) &= \sigma^w_{i,j,k}, \quad w=x,y,z\\
   \end{aligned}

Appendix A.1.3 Viscosity in False Transient Algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To improve the stability of our algorithm, we add an extra term
:math:`\partial_t v(x,y,z)` in our HJB equation, which can be
approximated as

.. math::

   \begin{aligned}
   \partial_t v(x,y,z) = \frac{v^{n+1}_{i,j,k} - v^{n}_{i,j,k}}{\Delta t}
   \end{aligned}

where :math:`\Delta t` is the time step.

Suppose we start with a initial guess :math:`v^{0}_{i,j,k}` and then
update :math:`v^{n}_{i,j,k}` according to

.. math::

   \begin{aligned}
   \frac{v^{n+1}_{i,j,k} - v^{n}_{i,j,k}}{\Delta t} = &  -\delta v^{n+1}_{i,j,k} + u_{i,j,k}^{n}\\
       & + {\mu^{x,n}_{i,j,k}}^{+} \partial_x v^{n+1,F}_{i,j,k} + {\mu^{x,n}_{i,j,k}}^{-}  \partial_x v^{n+1,B}_{i,j,k}+ \frac{{\sigma^{x,n}_{i,j,k}}^2}{2}\partial_{xx} v_{i,j,k}^{n+1}\\
       & + {\mu^{y,n}_{i,j,k}}^{+} \partial_y v^{n+1,F}_{i,j,k} + {\mu^{y,n}_{i,j,k}}^{-}  \partial_y v^{n+1,B}_{i,j,k}+ \frac{{\sigma^{y,n}_{i,j,k}}^2}{2}\partial_{yy} v_{i,j,k}^{n+1}\\
       & + {\mu^{z,n}_{i,j,k}}^{+} \partial_x v^{n+1,F}_{i,j,k} + {\mu^{z,n}_{i,j,k}}^{-}  \partial_z v^{n+1,B}_{i,j,k}+ \frac{{\sigma^{z,n}_{i,j,k}}^2}{2}\partial_{zz} v_{i,j,k}^{n+1}\\
   \end{aligned}

which can be written in matrix notation as

.. math::

   \begin{aligned}
   \frac{1}{\Delta t} (v^{n+1}-v^{n}) + \delta v^{n+1} = u^{n} + A^{n} v^{n+1}
   \end{aligned}

This system can in turn be written as

.. math::

   \begin{aligned}
   B^{n} v^{n+1} = b^{n}
   \end{aligned}

where

.. math::

   \begin{aligned}
   B^{n} &= \left(\frac{1}{\Delta t} + \delta\right) I - A^{n} \\
   b^n &= u^n + \frac{1}{\Delta t} v^{n}
   \end{aligned}

Appendix A.1.4 Intuition
~~~~~~~~~~~~~~~~~~~~~~~~

Finally, it’s instructive to consider the case with an infinitely large
time step :math:`\Delta t`, which leads to a vanishing
:math:`\frac{1}{\Delta t}`. In other words, the aforementioned system
can be written as

.. math::

   \begin{aligned}
    \delta v^{n+1} = u^{n} + A^{n} v^{n+1}.
   \end{aligned}

which is immediately another way of writing our HJB equation in matrix
form. In particula, :math:`A^n` encodes the evolution of the stochastic
process :math:`x_t,y_t,z_t`.

Appendix A.2 Cobweb Relaxation
------------------------------


