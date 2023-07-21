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
$:raw-latex:`\partial`\ *{xx} v*\ {i,j,k} $.

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

Now, to decide when to stop, we hope to see the difference between two
subsequent iterations very tiny, meaning we have obtained a convergent
solution to the equation. In other words, we wish to see

.. math::


   |v^{n+1}-v^{n}| < \epsilon

where :math:`\epsilon` is set to be :math:`10^{-7}`.

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

Appendix A.2.1 A Deep Look into First Order Condition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are HJB equations with simple control dynamics. For example, this
HJB equation, describing heterogenous agents model in
Aiyagari-Bewley-Huggett Economy,

.. math::


   \rho v(a, z)=\max _c u(c)+\partial_a v(a, z)(z+r a-c)+\mu(z) \partial_z v(a, z)+\frac{\sigma^2(z)}{2} \partial_{z z} v(a, z)

has a very straight-forward optimal consumption choice as

.. math::


   c^* = u^{\prime-1}\left(\partial_a v(a, z)\right)

However, our HJB equations doesn’t contain such simple dynamics. To
solve a very complex system, we resort to a special algorithm called
Cobweb algorithm. As it will show, the key idea is to reduce the
non-linearity of the first order condition by progressively solving it
in multiple steps.

Appendix A.2.2 Progressive Algorithm against Strong Non-linearity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We take the HJB equation for post technology jump as an example.

.. math::

   \begin{aligned}
   0= & \max_{i_k}\min_{h_k} \left(\frac{\delta}{1-\rho}\right)\left[\left(\frac{\alpha-i_k}{\exp (v)} \exp(k)\right)^{1-\rho}-1\right] \\
   & +\frac{d v}{dk}\left[\mu_k+i_k-\frac{\kappa}{2} i_k^2-\frac{\left|\sigma_k\right|^2}{2}+\sigma_k h_k\right]+\frac{d^2 v}{d k^2} \frac{\left|\sigma_k\right|^2}{2} \\
   & +\xi_k \frac{\left|h_k\right|^2}{2}
   \end{aligned}

First order condition for :math:`i_k` writes

.. math::


   \delta\left(\frac{\alpha-i_k}{\exp (v)} \exp (k)\right)^{-\rho} \frac{\exp (k)}{\exp (v)} = \frac{d v}{dk}\left(1-\kappa i_k\right)

which is a highly nonlinear equation of :math:`i_k`.

To get around the nonlinearity, the Cobweb algorithm states that we
define a new term :math:`mu` as

.. math::


   m u=\frac{d v}{dk}\left(1-\kappa i_k\right)

Then we solve the equation in multiple steps. Starting with a initial
guess of :math:`i_k` as :math:`i_k^0`, we update :math:`i_k^n`,
:math:`n=1,2,\ldots,N` according to

.. math::


   mu^{n}= \frac{d v}{dk}\left(1-\kappa i_k^{n+1}\right)

where

.. math::


   mu^{n} = \delta\left(\frac{\alpha-i_k^n}{\exp (v)} \exp (k)\right)^{-\rho} \frac{\exp (k)}{\exp (v)}

Now, to decide when to stop, we hope to see the difference between two
subsequent iterations very tiny, meaning we have obtained a convergent
solution to the equation. In other words, we wish to see

.. math::


   |i_k^n-i_k^{n-1}| < \epsilon

where :math:`\epsilon` is set to be :math:`10^{-7}`.

Appendix A.2.3 Further Improvement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While the Cobweb algorithm can alleviate our computational burden of
dealing with complex first order conditions a lot, there is still much
room for further improvement on efficiency of our algorithm. For
example, as we notice that the main purpose is to deliver a convergent
solution to the value function in the HJB equation, we can alternate the
Cobweb algorithm in a way that it’s iterating not over control, such as
:math:`i_k`, but directly over value function.

In other words, we start with initial guess of :math:`v`, :math:`i_k` as
:math:`v^0`, :math:`i_k^0` and complete a inner iteration over
:math:`i_k` and an outer iteration over :math:`v`.

In the inner iteration, we take value function :math:`v^n` as given and
attempt to update :math:`i_k^n` according to

.. math::


   mu^{n}= \frac{d v^{n}}{dk}\left(1-\kappa {i_k^{n+1}}'\right)

where

.. math::


   mu^{n}= \delta\left(\frac{\alpha-i_k^{n}}{\exp (v^{n})} \exp (k)\right)^{-\rho} \frac{\exp (k)}{\exp (v^{n})}

Here we progressively update :math:`i_k^n` to :math:`i_k^{n+1}` by a
convex combination of :math:`i_k^n` and :math:`{i_k^{n+1}}'` with a
relaxation parameter :math:`\chi` as

.. math::


   i_k^{n+1}= \chi i_k^n + (1-\chi) {i_k^{n+1}}'.

Once we have updated :math:`i_k^{n+1}`, we can turn to outer iteration
that updating :math:`v^{n+1}` according to

.. math::

   \begin{aligned}
   0= &  \left(\frac{\delta}{1-\rho}\right)\left[\left(\frac{\alpha-i_k^{n+1}}{\exp (v^{n})} \exp(k)\right)^{1-\rho}-1\right] \\
   & +\frac{d v^{n+1}}{dk}\left[\mu_k+{i_k^{n+1}}-\frac{\kappa}{2} {i_k^{n+1}}^2-\frac{\left|\sigma_k\right|^2}{2}+\sigma_k {h_k^{n+1}}\right]+\frac{d^2 v^{n+1}}{d k^2} \frac{\left|\sigma_k\right|^2}{2} \\
   & +\xi_k \frac{\left|{h_k^{n+1}}\right|^2}{2}
   \end{aligned}

To sum up, this alternated Cobweb algorithm aims at achieving a very
tiny difference between two subsequent iterations over value function
:math:`v` more directly,

.. math::


   |v^{n+1}-v^{n}| < \epsilon

which improved the efficiency and stability gallantly.

Appendix A.3 List of Parameters Chosen in Algorithm
---------------------------------------------------

========================== ======
Parameter                  Value
========================== ======
:math:`\chi`               0.0025
:math:`\Delta t`           0.0025
:math:`\underline{\log K}` 4.0
:math:`\overline{\log K}`  9.0
:math:`\underline{Y}`      0.0
:math:`\overline{Y}`       4.0
:math:`\underline{\log J}` 1.0
:math:`\overline{\log J}`  6.0
:math:`\Delta \log K`      0.2
:math:`\Delta Y`           0.1
:math:`\Delta \log J`      0.1
========================== ======


