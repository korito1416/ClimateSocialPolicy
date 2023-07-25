Appendix A. Computation Method
==============================

Appendix A.1 Overview
---------------------

Let’s take the HJB equation for pre technology and pre damage jump as an
example

.. math::

   \begin{aligned}
   0 & = \max_{i_k, i_j, \mathcal{E}} \min_{h_k, h_y, h_j, g, f_\ell}\left(\frac{\delta}{1-\rho}\right)\left[\left(\frac{\alpha-i_k-i_j-\alpha \phi_0\left[1-\frac{\mathcal{E}}{\beta_t \alpha \exp(k)}\right]^{\phi_1}}{\exp (\Phi)} \exp(k)\right)^{1-\rho}-1\right] \\
   & +\frac{\partial \Phi}{\partial k}\left[\mu_k+i_k-\frac{\kappa}{2} i_k^2-\frac{\left|\sigma_k\right|^2}{2}+\sigma_k h_k\right]+\frac{\partial^2 \Phi}{\partial k^2} \frac{\left|\sigma_k\right|^2}{2} \\
   & +\frac{\partial \Phi}{\partial y}\left(\frac{1}{M} \sum_m^M q(x \mid m) \theta(m)+\varsigma h_y\right) \mathcal{E}+\frac{\partial^2 \Phi}{\partial y^2} \frac{|\varsigma|^2}{2} \mathcal{E}^2 \\
   & -\left(\left[\lambda_1+\lambda_2 y\right]\left(\frac{1}{M} \sum_m^M q(x \mid m) \theta(m)+\varsigma h_y\right) \mathcal{E}+\lambda_2 \frac{|\varsigma|^2}{2} \mathcal{E}^2\right) \\
   & +\frac{\partial \Phi}{\partial j}\left(-\zeta+\psi_0\left(i_j\right)^{\psi_1} \exp \left(\psi_1 \log K-\psi_1 \log J\right)-\frac{\left|\sigma_j\right|^2}{2}+\sigma_j h_j\right)+\frac{\partial^2 \Phi}{\partial j^2} \frac{\left|\sigma_j\right|^2}{2} \\
   & +\xi_g I_g(J)(1-g+g \log g)+I_g(J) g\left(\Phi^{II}-\Phi\right) \\
   & +\xi_d I_n(y) \sum_{\ell=1}^L \pi_d^{\ell}\left(1-f_{\ell}+f_{\ell} \log f_{\ell}\right)+I_n(y) \sum_{\ell=1}^L \pi_d^{\ell} f_{\ell}\left(\Phi^{\ell}-\Phi\right) \\
   & +\xi_k \frac{\left|h_k\right|^2}{2}+\xi_c \frac{\left|h_y\right|^2}{2}+\xi_j \frac{\left|h_j\right|^2}{2}+\xi_a \frac{1}{M} \sum_m^M q(x \mid m) \log q(x \mid m)
   \end{aligned}

which satisfies conditions to switch the order of max and min operator.

Then, after exchanging the order of max and min operator, we deliver the
solution, i.e. value function :math:`\Phi`, to this HJB equation
resursively according to

-  Start with current value function :math:`\Phi^n` where
   :math:`n \in \{0,1, 2,\ldots\}` is called iteration step.
   Specifically, :math:`\Phi^0` is the initial guess of value function,
   which can be vital to success of algorithm. We solve the HJB equation
   and update value function :math:`\Phi^n` to :math:`\Phi^{n+1}` in two
   steps.

   1. Take current value function :math:`\Phi^n` as given, let’s start
      with current distortion and jump misspecification
      :math:`h_k^n, h_y^n, h_j^n, g^n, f_\ell^n` and solve optimal
      distortion and jump misspecification in two sub-steps.

      1. Take value function :math:`\Phi^n` and current distortion and
         jump misspecification
         :math:`h_k^n, h_y^n, h_j^n, g^n, f_\ell^n` as given, we update
         optimal actions from :math:`i_k^{n}, i_j^{n}, \mathcal{E}^{n}`
         to :math:`i_k^{n+1}, i_j^{n+1}, \mathcal{E}^{n+1}` in a
         maximization problem.

      2. With updated robustly optimal actions
         :math:`i_k^{n+1}, i_j^{n+1}, \mathcal{E}^{n+1}` in hand, we
         update optimal distortion
         :math:`h_k^{n+1}, h_y^{n+1}, h_j^{n+1}, g^{n+1}, f_\ell^{n+1}`
         by solving a minimization problem.

   2. With updated robustly optimal actions and probability distortion,
      we finally can update value function :math:`\Phi^{n+1}` via upwind
      scheme.

-  We obtain a convergent solution to the HJB equation when the
   difference between two subsequent iterations is very tiny as

.. math::


   |\Phi^{n+1}-\Phi^{n}| < \epsilon

where :math:`\epsilon` is set to be :math:`10^{-7}`.

Appendix A.2 Solving the Optimization Problem
---------------------------------------------

Appendix A.2.1 Maximization
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution process for :math:`i_k` is given as follows, of which the same
logic can apply to other actions :math:`i_j, \mathcal{E}` easily.

First order condition for :math:`i_k` writes

.. math::


   \delta\left(\frac{\alpha-i_k-i_j-\alpha \phi_0\left[1-\frac{\mathcal{E}}{\beta_t \alpha \exp(k)}\right]^{\phi_1}}{\exp (\Phi)} \exp(k)\right)^{-\rho} \frac{\exp (k)}{\exp (\Phi)} = \frac{d \Phi}{dk}\left(1-\kappa i_k\right)

which is a highly non-linear equation of :math:`i_k` and doesn’t admit a
quasi-analytial solution.

Cobweb algorithm states that given current value function and
probability distortion, we can update current actions
:math:`i_k^{n}, i_j^{n}, \mathcal{E}^{n}` according to

.. math::


   mu^{n} = \frac{d \Phi^n}{dk}\left(1-\kappa {i_k^{n+1}}'\right)

where we define

.. math::


   mu^{n} \doteq \delta\left(\frac{\alpha-i_k^{n}-i_j^{n}-\alpha \phi_0\left[1-\frac{\mathcal{E}^{n}}{\beta_t \alpha \exp(k)}\right]^{\phi_1}}{\exp (\Phi^n)} \exp(k)\right)^{-\rho} \frac{\exp (k)}{\exp (\Phi^n)}

And :math:`i_k^{n+1}` is computed with relaxation paramter :math:`\chi`
as

.. math::


   i_k^{n+1} = \chi i_k^{n} + (1-\chi) {i_k^{n+1}}'

Appendix A.2.2 Minimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution process to probability distortions is simpler and we take that
of :math:`h_k` as an example, of which the same logic can apply to other
probability distortions :math:`h_y, h_j, g, f_\ell`.

First order condition for :math:`h_k` is written as

.. math::


   \frac{\partial \Phi}{\partial k} \sigma_k = -\xi_k h_k

With given value function :math:`\Phi^n`, we can update
:math:`h_k^{n+1}` according to

.. math::


   h_k^{n+1} = - \frac{1}{\xi_k} \frac{\partial \Phi^n}{\partial k} \sigma_k 

Appendix A.3 Solving the Algebraic System
-----------------------------------------

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

Let’s consider a generalized time-independent three-dimensional HJB
equation:

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

Appendix A.3.1 False Transient Algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To mitigate the inherent instability of the non-linear HJB, we add a
false transcient (time) dimension and solve it until convergence. And
the new HJB equation is as

.. math::

   \begin{aligned}
   0= & \max_{\alpha} -\delta v(x,y,z, t) + u(x,y,z,\alpha) + \partial_t v(x,y,z,t)\\
       & + \mu^x(x,y,z,\alpha) \partial_x v(x,y,z, t) + \frac{{\sigma^x}(x,y,z,\alpha)^2}{2}\partial_{xx} v(x,y,z, t) \\
       &+ \mu^y(x,y,z,\alpha) \partial_y v(x,y,z, t) + \frac{{\sigma^y}(x,y,z,\alpha)^2}{2}\partial_{yy} v(x,y,z, t) \\
       & + \mu^z(x,y,z,\alpha) \partial_z v(x,y,z, t) + \frac{{\sigma^z}(x,y,z,\alpha)^2}{2}\partial_{zz} v(x,y,z, t)
   \end{aligned}

Appendix A.3.2 Finite-Difference Scheme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Appendix A.3.2.1 Upwind Scheme
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Accordingly, we construct equispaced grids for these three state
variable :math:`x,y,z` as

.. math::

   \begin{aligned}
   X &= \{x_1=\underline{X},\ldots,x_N=\bar{X}\} \\
   Y &= \{y_1=\underline{Y},\ldots,y_N=\bar{Y}\} \\
   Z &= \{z_1=\underline{Z},\ldots,z_N=\bar{Z}\}
   \end{aligned}

where the distance between two grid points are
:math:`\Delta x, \Delta y, \Delta z`

We now approximate value function on grid points and use short-hand
notation :math:`v(x_i,y_j,z_k) \doteq v_{i,j,k}` and so on.

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

which is an average of forward and backward difference approximation.

Then, we approximate the second-order partial derivatives
:math:`\partial_{xx} v(x,y,z)` with a central difference approximation

.. math::

   \begin{aligned}
   \partial_{xx} v_{i,j,k} &=  \frac{v_{i+1,j,k} + v_{i-1,j,k}- 2v_{i,j,k}}{\Delta x^2} 
   \end{aligned}

We can employ the first-order-condition to express our control
:math:`\alpha` on a grid point :math:`x_i, y_j, z_k` as a nonlinear
function of value function approximations
:math:`\partial_{x,C} v_{i,j,k}` and :math:`\partial_{xx} v_{i,j,k}`. Therefore, we use short-hand notations for our control,
drift and diffusion term as

.. math::

   \begin{aligned}
   \alpha(x_i,y_j,z_k) &= \alpha_{i,j,k} \\
   u(x_i,y_j,z_k,\alpha(x_i,y_j,z_k)) &= u_{i,j,k} \\
   \mu^w(x_i,y_j,z_k,\alpha(x_i,y_j,z_k)) &= \mu^w_{i,j,k}, \quad w=x,y,z\\
   \sigma^w(x_i,y_j,z_k,\alpha(x_i,y_j,z_k)) &= \sigma^w_{i,j,k}, \quad w=x,y,z\\
   \end{aligned}

We use upwind scheme and construct backward approximation with negative
drift and forward approximation with positive drift.

To sum up, starting with current value function :math:`v^{n}`, we update
:math:`v^{n+1}` according to

.. math::

   \begin{aligned}
   \frac{v^{n+1}_{i,j,k} - v^{n}_{i,j,k}}{\Delta t} = &  -\delta v^{n+1}_{i,j,k} + u_{i,j,k}^{n}\\
       & + {\mu^{x,n}_{i,j,k}}^{+} \partial_x v^{n+1,F}_{i,j,k} + {\mu^{x,n}_{i,j,k}}^{-}  \partial_x v^{n+1,B}_{i,j,k}+ \frac{{\sigma^{x,n}_{i,j,k}}^2}{2}\partial_{xx} v_{i,j,k}^{n+1}\\
       & + {\mu^{y,n}_{i,j,k}}^{+} \partial_y v^{n+1,F}_{i,j,k} + {\mu^{y,n}_{i,j,k}}^{-}  \partial_y v^{n+1,B}_{i,j,k}+ \frac{{\sigma^{y,n}_{i,j,k}}^2}{2}\partial_{yy} v_{i,j,k}^{n+1}\\
       & + {\mu^{z,n}_{i,j,k}}^{+} \partial_x v^{n+1,F}_{i,j,k} + {\mu^{z,n}_{i,j,k}}^{-}  \partial_z v^{n+1,B}_{i,j,k}+ \frac{{\sigma^{z,n}_{i,j,k}}^2}{2}\partial_{zz} v_{i,j,k}^{n+1}\\
   \end{aligned}

A.3.2.2 Natural Boundary Condition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We approximate second order derivative at boundaries with natural
boundary condition. More specifically, suppose state variable :math:`x`
is at its upper boundary, we set second order derivative of value
function to be the same as that of closet inner point.

.. math::

   \begin{aligned}
   \partial_{xx} v^{n+1}_{N,j,k} &=  \partial_{xx} v^{n+1}_{N-1,j,k} = \frac{v^{n+1}_{N,j,k} + v^{n+1}_{N-2,j,k}- 2v^{n+1}_{N-1,j,k}}{\Delta x^2} 
   \end{aligned}

Now the matrix notation of HJB equation can be written as

.. math::

   \begin{aligned}
   \frac{1}{\Delta t} (v^{n+1}-v^{n}) + \delta v^{n+1} = u^{n} + A^{n} v^{n+1}
   \end{aligned}

A.3.2.3 Implicit Euler
^^^^^^^^^^^^^^^^^^^^^^

Appendix A.4 List of Parameters Chosen in Algorithm
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

.. raw:: html

   <!-- ## Appendix A.2 Cobweb Relaxation

   ### Appendix A.2.1 A Deep Look into First Order Condition

   There are HJB equations with simple control dynamics. For example, this HJB equation, describing heterogenous agents model in Aiyagari-Bewley-Huggett Economy, 

   $$
   \rho v(a, z)=\max _c u(c)+\partial_a v(a, z)(z+r a-c)+\mu(z) \partial_z v(a, z)+\frac{\sigma^2(z)}{2} \partial_{z z} v(a, z)
   $$

   has a very straight-forward optimal consumption choice as

   $$
   c^* = u^{\prime-1}\left(\partial_a v(a, z)\right)
   $$

   However, our HJB equations doesn't contain such simple dynamics. To solve a very complex system, we resort to a special algorithm called Cobweb algorithm. As it will show, the key idea is to reduce the non-linearity of the first order condition by progressively solving it in multiple steps.

   ### Appendix A.2.1 Progressive Algorithm against Strong Non-linearity

   We take the HJB equation for post technology jump as an example.

   \begin{aligned}
   0= & \max_{i_k}\min_{h_k} \left(\frac{\delta}{1-\rho}\right)\left[\left(\frac{\alpha-i_k}{\exp (v)} \exp(k)\right)^{1-\rho}-1\right] \\
   & +\frac{d v}{dk}\left[\mu_k+i_k-\frac{\kappa}{2} i_k^2-\frac{\left|\sigma_k\right|^2}{2}+\sigma_k h_k\right]+\frac{d^2 v}{d k^2} \frac{\left|\sigma_k\right|^2}{2} \\
   & +\xi_k \frac{\left|h_k\right|^2}{2}
   \end{aligned}

   First order condition for $i_k$ writes

   $$
   \delta\left(\frac{\alpha-i_k}{\exp (v)} \exp (k)\right)^{-\rho} \frac{\exp (k)}{\exp (v)} = \frac{d v}{dk}\left(1-\kappa i_k\right)
   $$

   which is a highly nonlinear equation of $i_k$ and doesn't lead to a quasi-analytical solution.

   To get around the nonlinearity, the Cobweb algorithm states that we define a new term $mu$ as

   $$
   m u=\frac{d v}{dk}\left(1-\kappa i_k\right)
   $$

   Then we solve the equation in multiple steps. Starting with a initial guess of $i_k$ as $i_k^0$, we update $i_k^n$, $n=1,2,\ldots,N$ according to 

   $$
   mu^{n}= \frac{d v}{dk}\left(1-\kappa i_k^{n+1}\right)
   $$

   where 

   $$
   mu^{n} = \delta\left(\frac{\alpha-i_k^n}{\exp (v)} \exp (k)\right)^{-\rho} \frac{\exp (k)}{\exp (v)}
   $$


   Now, to decide when to stop, we hope to see the difference between two subsequent iterations very tiny, meaning we have obtained a convergent solution to the equation. In other words, we wish to see

   $$
   |i_k^n-i_k^{n-1}| < \epsilon
   $$

   where $\epsilon$ is set to be $10^{-7}$.


   ### Appendix A.2.3 Further Improvement

   While the Cobweb algorithm can alleviate our computational burden of dealing with complex first order conditions a lot, there is still much room for further improvement on efficiency of our algorithm. For example, as we notice that the main purpose is to deliver a convergent solution to the value function in the HJB equation, we can alternate the Cobweb algorithm in a way that it's iterating not over control, such as $i_k$, but directly over value function.

   In other words, we start with initial guess of $v$, $i_k$ as $v^0$, $i_k^0$ and complete a inner iteration over $i_k$ and an outer iteration over $v$. 

   In the inner iteration, we take value function $v^n$ as given and attempt to update $i_k^n$ according to 

   $$
   mu^{n}= \frac{d v^{n}}{dk}\left(1-\kappa {i_k^{n+1}}'\right)
   $$


   where 

   $$
   mu^{n}= \delta\left(\frac{\alpha-i_k^{n}}{\exp (v^{n})} \exp (k)\right)^{-\rho} \frac{\exp (k)}{\exp (v^{n})}
   $$

   Here we progressively update $i_k^n$ to $i_k^{n+1}$ by a convex combination of $i_k^n$ and ${i_k^{n+1}}'$ with a relaxation parameter $\chi$ as

   $$
   i_k^{n+1}= \chi i_k^n + (1-\chi) {i_k^{n+1}}'.
   $$



   Once we have updated $i_k^{n+1}$, we can turn to outer iteration that updating $v^{n+1}$ according to 


   \begin{aligned}
   0= &  \left(\frac{\delta}{1-\rho}\right)\left[\left(\frac{\alpha-i_k^{n+1}}{\exp (v^{n})} \exp(k)\right)^{1-\rho}-1\right] \\
   & +\frac{d v^{n+1}}{dk}\left[\mu_k+{i_k^{n+1}}-\frac{\kappa}{2} {i_k^{n+1}}^2-\frac{\left|\sigma_k\right|^2}{2}+\sigma_k {h_k^{n+1}}\right]+\frac{d^2 v^{n+1}}{d k^2} \frac{\left|\sigma_k\right|^2}{2} \\
   & +\xi_k \frac{\left|{h_k^{n+1}}\right|^2}{2}
   \end{aligned}

   To sum up, this alternated Cobweb algorithm aims at achieving a very tiny difference between two subsequent iterations over value function $v$ more directly, 

   $$
   |v^{n+1}-v^{n}| < \epsilon
   $$

   which improved the efficiency and stability gallantly.
    -->


