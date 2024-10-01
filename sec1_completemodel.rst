1 Economic Model and HJB
========================

**State**

-  The stock of productive capital :math:`K_t` :

   .. math:: dK_t = K_t \left( - \mu_k    + \frac {I_{t}^k}{K_t}  -{\frac { \kappa} 2} \left( {\frac {I_{t} ^k} {K_t}} \right)^2 \right) dt + K_t \sigma_k dW_t
-  Temperature anomaly :math:`Y_t`:

   .. math:: dY_t = {\mathcal E}_t [{\bar \theta} dt + \varsigma dW_t]
-  the stock of R&D-induced knowledge capital :math:`R_t`:

   .. math:: d R_t = - \zeta R_t dt + \psi_0 \left(I_t^r\right)^{\psi_1} \left(R_t\right)^{1 - \psi_1} dt + R_t \sigma_r dW_t 
-  The damage evolution :math:`N_t`.

.. math::

   \begin{align*} 
    d \log N_t = 
       \begin{cases}
       \left( \lambda_1 + \lambda_2 Y_t \right) \mathcal{E}_t \left[ \bar{\theta}\, dt + \varsigma\, dW_t \right] + \dfrac{ \lambda_2 |\varsigma|^2 \left( \mathcal{E}_t \right)^2 }{2}\, dt, & \text{if } t \leq \tau \\[2ex]
       \left[ \lambda_1 + \lambda_2 \widehat{Y}_t + \lambda_3(\ell)\left( \widehat{Y}_t - \bar{y} \right) \right] \mathcal{E}_t \left[ \bar{\theta}\, dt + \varsigma\, dW_t \right] \\
       \quad + \dfrac{ \left[ \lambda_2 + \lambda_3(\ell) \right] |\varsigma|^2 \left( \mathcal{E}_t \right)^2 }{2}\, dt, & \text{if } t > \tau
       \end{cases}
   \end{align*}

:math:`k_t` is a potential realization of :math:`K_t`, and
:math:`\hat{k_t}` is :math:`\log k_t`. Similarly, :math:`n_t` is a
potential realization of :math:`N_t`, and :math:`\hat{n_t}` is
:math:`\log n_t`; :math:`r_t` is a potential realization of :math:`R_t`,
and :math:`\hat{r_t}` is :math:`\log r_t`.

**Controls**

-  :math:`i^k` is a potential value for :math:`I_t^k`
-  :math:`i^r` is a potential value for :math:`I_t^r`
-  :math:`e` is a potential value for :math:`\mathcal{E}_t`

**Distortion**

-  :math:`h^k` is the distortion to capital accumulation.
-  :math:`h^y` is the distortion to temperature anomaly accumulation.
-  :math:`h^r` is the distortion to R&D accumulation.
-  :math:`g` is the misspecification to technology jump.
-  :math:`f` is the misspecification to damage jump.

For our analysis here, rather than a constant value of :math:`\xi` for
all uncertainty channels, we use a set of values
:math:`\{\xi^k, \xi^c, \xi^r, \xi^d, \xi^g\}`, one for each uncertainty
channel so that we can carry out our uncertainty decomposition.

1.1 HJB equations
-----------------

1.1.1 Post-tech-post-damage HJB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After technology jump occurs, temperature and damage remains constant.
Then the optimal choice of emission is 0. In this case, the state space,
control space and distortion space become

.. math::

   \begin{align*}
       X &= \{ \hat{k} \}\\
       \Phi &= \{  i^k \}\\
       \Gamma &= \{h^k\}
   \end{align*}

Compute :math:`V^{\ell,L}(x)` for :math:`\ell = 1, ..., L-1` conditioned
on both a technology jump and a damage jump occurring,by solving HJB
equation

.. math::


   \begin{align*}
   0= & \max_{i^k}\min_{{h^k}} \left(\frac{\delta}{1-\rho}\right)\left[\left(\frac{\alpha k -i^k}{\exp (\hat{V}^{\ell,L})} \right)^{1-\rho}-1\right] \\
   & +\frac{\partial \hat{V}^{\ell,L}}{\partial \hat{k}}\left[\mu_k+\frac{i^k}{k}-\frac{\kappa}{2} \left(\frac{i^k}{k}\right)^2-\frac{\left|\sigma_k\right|^2}{2}+\sigma_k {h^k}\right]+\frac{\partial^2 \hat{V}^{\ell,L}}{\partial \hat{k} \, \partial \hat{k}'}\frac{\left|\sigma_k\right|^2}{2} \\
   & +\xi^k \frac{\left|{h^k}\right|^2}{2}
   \end{align*}

If :math:`\rho =1`, the first term of the HJB becomes

.. math:: \delta \log ( \alpha k  -i^k )  -   \delta \hat{V}^{\ell,L}

1.1.2 Post Technology and Pre Damage HJB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compute the value function :math:`V^L(x)` assuming that only a
technology jump has been realized. This value function incorporates the
possibility of jumping to one of :math:`L-1` possible damage states,
however, because the temperature anomaly remains constant at the point
where any incremental curvature has no impact on the damages this damage
curve realization is inconsequential. Therefore, we can ignore the
damage curve intensities and the associated continuation values for this
computation.

In this case, the state space, control space and distortion space become

.. math::

   \begin{align*}
       X &= \{ \hat{k} \}\\
       \Phi &= \{  i^k \}\\
       \Gamma &= \{h^k\}
   \end{align*}

We have HJB for post technology and post damage jump as follows

.. math::


   \begin{align*}
   0= & \max_{i^k}\min_{{h^k}} \left(\frac{\delta}{1-\rho}\right)\left[\left(\frac{\alpha k -i^k}{\exp (\hat{V}^L)} \right)^{1-\rho}-1\right] \\
   & +\frac{\partial \hat{V}^{L}}{\partial \hat{k}}\left[\mu_k+\frac{i^k}{k}-\frac{\kappa}{2} \left(\frac{i^k}{k}\right)^2-\frac{\left|\sigma_k\right|^2}{2}+\sigma_k {h^k}\right]+\frac{\partial^2 \hat{V}^{ L}}{\partial \hat{k} \, \partial \hat{k}'} \frac{\left|\sigma_k\right|^2}{2} \\
   & +\xi^k \frac{\left|{h^k}\right|^2}{2}
   \end{align*}

1.1.3 Pre Technology and Post Damage HJB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compute the values functions :math:`V^{\ell}(x)` assuming that only a
damage jump has been realized for :math:`\ell = 1,..., L-1.` These
values functions depend on the entire state vector :math:`X` and have
one possible jump state which is the technology discovery with intensity
:math:`{\mathcal J}^L.` The continuation value for the jump is
:math:`V^{\ell,L}(x)` viewed as a function of :math:`x` for
:math:`\ell=1,...,L-1.`

.. math::


   \begin{align*}
       X &= \{ \hat{k}, y, \hat{r}, \hat{n} \}\\
       \Phi &= \{  i^k, i^r, e \}\\
       \Gamma &= \{{h^k}, {h^y}, {h^r}, g\}
   \end{align*}

After plugging this simplification into our HJB equation and removing
common terms, we are left with the following simplified HJB to solve:

.. math::


   \begin{align*}
   & 0=\max_{i^k, i^r, e} \min_{{h^k}, {h^y}, {h^r}, g} \left(\frac{\delta}{1-\rho}\right)\left[\left(\frac{\alpha k -i^k-i^r-\alpha k \phi_0(z)\left[1-\frac{e}{\beta_t \alpha k }\right]^{\phi_1}}{\exp (\hat{V}^\ell)} \right)^{1-\rho}-1\right] \\
   & +\frac{\partial \hat{V}^\ell}{\partial \hat{k}}\left[\mu_k+\frac{i^k}{k}-\frac{\kappa}{2} \left(\frac{i^k}{k}\right)^2-\frac{\left|\sigma_k\right|^2}{2}+\sigma_k {h^k}\right]+\frac{\partial^2 \hat{V}^\ell }{\partial  \hat{k} \partial  \hat{k}'} \frac{\left|\sigma_k\right|^2}{2} \\
   & +\frac{\partial \hat{V}^\ell}{\partial \hat{y}}\left(  \bar{\theta}+\varsigma {h^y}\right) e+\frac{\partial^2 \hat{V}^\ell}{\partial y \partial y'} \frac{|\varsigma|^2}{2} e^2 \\
   & -\left(\left[\lambda_1+\lambda_2 y+\lambda_3(y-\bar{y})\right]\left( \bar{\theta}+\varsigma {h^y}\right) e+\left(\lambda_2+\lambda_3\right) \frac{|\varsigma|^2}{2} e^2\right) \\
   & +\frac{\partial \hat{V}^\ell}{\partial \hat{r} }\left(-\zeta+\psi_0\left(i^r\right)^{\psi_1} \exp \left(-\psi_1 \log r\right)-\frac{\left|\sigma_r\right|^2}{2}+\sigma_r {h^r}\right)+\frac{\partial^2 \hat{V}^\ell}{\partial \hat{r} \partial \hat{r}'}\frac{\left|\sigma_r\right|^2}{2} \\
   & +\xi^g \mathcal{J}_g (1-g +g  \log g )+\mathcal{J}_g  g \left(\hat{V}^{\ell,L}-\hat{V}^\ell \right) \\
   & +\xi^k \frac{\left|{h^k}\right|^2}{2}+\xi^c \frac{\left|{h^y}\right|^2}{2}+\xi^r \frac{\left|{h^r}\right|^2}{2}  \\
   &
   \end{align*}

If :math:`\rho =1`, the first term of the HJB becomes

.. math:: \delta \log ( \alpha k -i^k-i^r-\alpha k \phi_0(z)\left[1-\frac{e}{\beta_t \alpha k }\right]^{\phi_1} )  -   \delta \hat{V}^\ell

1.1.4 Pre-tech-pre-damage HJB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compute :math:`V(x)` prior to any jumps occurring. This value function
has two possible types of jumps, either a technology jump or a damage
curvature jump. The continuation value for the technology jump is
:math:`V^L(x)`, and the potential continuation values for the damage
curvature jump are the set of :math:`V^{\ell}(x)` for
:math:`\ell = 1,..., L-1.`

.. math::

   \begin{align*}
       X &= \{ k, y,r,n \}\\
       \Phi &= \{  i^k, i^r, e \}\\
       \Gamma &= \{{h^k}, {h^y}, {h^r}, g, f\}
   \end{align*}

After plugging this simplification into our HJB equation and removing
common terms,

.. math::

   \begin{align*}
   0  = & \max_{i^k, i^r, e} \, \min_{h, g^{\ell}} \, \frac{\delta}{1-\rho} \left(\left(\frac{\alpha k-i^{k}-i^{r}-\alpha k \phi_0 \left(1-\frac{e}{\beta \alpha k}\right)^{\phi_1}}{\exp(\hat{V})} \right)^{1-\rho}-1 \right) \\
   & + \frac{\partial \hat{V}}{\partial \hat{k}} \left( -\mu_{k}+ \frac{i^{k}}{k}-\frac{\kappa}{2}\left(\frac{I^{k}}{k}\right)^{2}-\frac{|\sigma_{k}|^{2}}{2} + \sigma_k h^k \right) +  \frac{\partial^2 \hat{V}}{\partial \hat{k} \, \partial \hat{k}'}\frac{|\sigma_{k}|^{2}}{2} \\
   & + \frac{\partial \hat{V}}{\partial y} e \left( \bar{\theta}+\varsigma h^y \right) + \frac{\partial^2 \hat{V}}{\partial y \, \partial y'}\frac{|\varsigma|^{2}}{2}e^{2}  - \left( (\lambda_{1}+\lambda_{2}y) e \left( \bar{\theta}+\varsigma h^y \right) +\lambda_{2}\frac{|\varsigma|^{2}}{2}e^{2} \right) \\
   & + \frac{\partial \hat{V}}{\partial \hat{r}} \left( -\zeta + \psi_{0}(i^{r})^{\psi_{1}}\exp( -\psi_{1} \hat{r})-\frac{|\sigma_{r}|^{2}}{2}+\sigma_{r} h^r \right) +\frac{\partial^2 \hat{V}}{\partial \hat{r} \, \partial \hat{r}'}\frac{|\sigma_{r}|^{2}}{2} \\
   & +\xi^g \mathcal{J}_g (1-g +g  \log g )+\mathcal{J}_g  \cdot g  \cdot \left(\hat{V}^L -\hat{V}\right) \\
   &+\xi^d \mathcal{J}_n  \sum_{\ell} \pi^\ell  (1-f^\ell +f^\ell  \log f^\ell ) \\
   &+\mathcal{J}_n \sum_{\ell  } \pi^\ell  f^\ell \cdot \left(\hat{V}^\ell-\hat{V}\right) \\
   &+\xi^k \frac{\left|{h^k}\right|^2}{2}+\xi^c \frac{\left|{h^y}\right|^2}{2}+\xi^r \frac{\left|{h^r}\right|^2}{2}
   \end{align*}

To solve HJB equations, we first run below code in
`two-capital-climate-change/master
/master_zero_shock.sh <https://github.com/korito1416/two-capital-climate-change/blob/main/master/master_zero_shock.sh>`__.
Make sure you give right command-line arguments.

We solve four types of HJB equations sequentially.

1. First, solve one post-tech-post-damage HJB. As after technology jump
   occurs, the curvature of damage function does not appear in HJB
   equations.

2. Second we solve one post-tech-pre-damage and twenty
   pre-tech-post-damage HJB conditional on post-tech-post-damage value
   function.

3. Finally, we solve pre-tech-pre-damage HJB given post-tech-pre-damage
   and pre-tech-post-damage value functions.

In
`Postdamage.sh <https://github.com/korito1416/two-capital-climate-change/blob/641046304faed6e6c5bace7bc0f9af45c8196fd9/python/Postdamage.py>`__,
we solve post_damage_post_tech and post-damage-pre-tech value functions
and controls.
`Post_damage_post_tech <https://github.com/korito1416/two-capital-climate-change/blob/641046304faed6e6c5bace7bc0f9af45c8196fd9/python/Postdamage.py#L310>`__
section solves post-damage-post-tech HJB.
`Post-damage-pre-tech <https://github.com/korito1416/two-capital-climate-change/blob/641046304faed6e6c5bace7bc0f9af45c8196fd9/python/Postdamage.py#L412>`__
section solves Post-damage-pre-tech HJB. In order to make sure our
results are stable, we first randomly pick initial values and then use
the first result to resolve the HJB.

`Postdamage_sub.sh <https://github.com/korito1416/two-capital-climate-change/blob/641046304faed6e6c5bace7bc0f9af45c8196fd9/conduction/Postdamage_sub.sh>`__
is aimed at further improving computational efficiency. The solutions
obtained from post_damage.py serve as baseline solutions for
Postdamage_sub.py to resolve the HJB equations.

In
`Predamage.sh <https://github.com/korito1416/two-capital-climate-change/blob/641046304faed6e6c5bace7bc0f9af45c8196fd9/python/Predamage.py>`__,
we solve pre_damage_post_tech and pre-damage-pre-tech value functions
and controls.
`Pre_damage_post_tech <https://github.com/korito1416/two-capital-climate-change/blob/641046304faed6e6c5bace7bc0f9af45c8196fd9/python/Predamage.py#L249>`__
section solves pre-damage-post-tech HJB.
`Pre-damage-pre-tech <https://github.com/korito1416/two-capital-climate-change/blob/641046304faed6e6c5bace7bc0f9af45c8196fd9/python/Predamage.py#L312>`__
section solves Pre-damage-pre-tech HJB.

1.2 Computation method
----------------------

In this section, we explain how did we solve HJB equation.

1.2.1 Policy Iteration
~~~~~~~~~~~~~~~~~~~~~~

For simplicity, I denote the control set and distortion set:

.. math::

   \begin{align*}
      \Phi^n &= \{ i_k^{n}, i_j^{n}, \mathcal{E}^{n} \} \\
      \Gamma^n &=\{ h_k^{n}, h_y^{n}, h_j^{n}, g^{n}, f_\ell^{n} \} 
   \end{align*}

Algorithm: Solving the HJB Equation via Policy Iteration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::


   \begin{align*}
   \textbf{Input:} &\ \text{Initial guess for value function } V^0, \epsilon = 10^{-7} \\ 
   &\text{Initialize } n = 0, V^n = V^0 \\
   \textbf{while} &\ |V^{n+1} - V^n| \geq \epsilon \text{ do:} \\
   &\ \quad \text{Step 1: Solve for optimal actions} \Phi^{n+1} \text{ by maximization} \\
   &\ \quad \quad \text{Cobweb algorithm   is applied here:} \\
   &\ \quad \quad \Phi^{n+1} = \Phi(V^n, \Phi^{n}, \Gamma^{n}) \\
   &\ \quad \text{Step 2: Solve for optimal probability distortions } \Gamma^{n+1} \text{ by minization}\\
   &\ \quad \quad \Gamma^{n+1} = \Gamma(V^n, \Phi^{n+1}, \Gamma^{n}) \\
   &\ \quad \text{Step 3: Update value function } V^{n+1} \text{ by minimization}\\
   &\ \quad \quad V^{n+1} = V(V^n, \Phi^{n+1}, \Gamma^{n+1}) \\
   &\ \quad \text{Step 4: Check for convergence} \\
   &\ \quad \quad\text{If } |V^{n+1} - V^n| < \epsilon \text{ then stop, otherwise continue.} \\
   \textbf{Return:} &\ V^* \\
   \end{align*}

1.2.2 Updating Rules :math:`\Phi^{n+1} = \Phi(V^n,\Phi^{n},\Gamma^{n})`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In solving HJB equations, we often encounter complex, highly non-linear
equations that do not admit analytical solutions. To address this
challenge, iterative numerical methods like the
`Cobweb <https://github.com/korito1416/two-capital-climate-change/blob/306b1c5ee51eb6ad24e6267fe0d2b82ad5286e98/python/src/PreSolver_CRS2_new.py#L85>`__
algorithm are employed to approximate the optimal control variables.

The Cobweb algorithm works by:

-  Starting with an initial guess for the control variable.
-  Computing the corresponding values in the equations.
-  Updating the control variable based on the discrepancies observed.
-  Repeating the process until the control variable converges to a
   stable value.

For example, we update for :math:`i_k` for pre damage pre technology
HJB, using the first-order condition:

.. math:: \delta \left( \frac{\alpha k - i_k - i_j - \alpha k \phi_0(z) \left[1 - \frac{\mathcal{E}}{\beta_t \alpha k}\right]^{\phi_1}}{\exp(v)} \right)^{-\rho} \frac{1}{\exp(v)} = \frac{\partial v}{\partial \log k} \left(1 - \kappa i_k\right)

Since this equation is highly non-linear and does not admit an
analytical solution, we use the
`Cobweb <https://github.com/korito1416/two-capital-climate-change/blob/306b1c5ee51eb6ad24e6267fe0d2b82ad5286e98/python/src/PreSolver_CRS2_new.py#L246>`__
algorithm to iteratively update the actions. For each iteration
:math:`n`, the update is:

.. math::

   \begin{align}  
   \hat{i}_k^{n+1} = \frac{1}{\kappa}-\frac{1}{\kappa}\delta \left( \frac{\alpha k - i_k^n - i_j - \alpha k \phi_0(z) \left[1 - \frac{\mathcal{E}}{\beta_t \alpha k}\right]^{\phi_1}}{\exp(v)} \right)^{-\rho} \frac{1}{\exp(v)} \frac{1}{\frac{\partial v}{\partial \log k}}  \end{align}

The updated
`action <https://github.com/korito1416/two-capital-climate-change/blob/306b1c5ee51eb6ad24e6267fe0d2b82ad5286e98/python/src/PreSolver_CRS2_new.py#L250>`__
:math:`i_k^{n+1}` is computed using a relaxation parameter
:math:`\zeta`:

.. math:: i_k^{n+1} = \zeta i_k^n + (1 - \zeta) \hat{i}_k^{n+1}

1.2.3 Updating Rules :math:`\Gamma^{n+1} = \Gamma(V^n,\Phi^{n+1},\Gamma^{n} )`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every distortion has analytical solution. For example, we solve for
:math:`h_k`, and the same logic applies to :math:`h_y, h_j, g, f_l`. The
first-order condition for :math:`h_k` is:

.. math:: \frac{\partial v}{\partial \log k} \sigma_k = - \xi_k h_k

Given the value function :math:`v^n`, we
`update <https://github.com/korito1416/two-capital-climate-change/blob/306b1c5ee51eb6ad24e6267fe0d2b82ad5286e98/python/src/PreSolver_CRS2_new.py#L282>`__
the distortion :math:`h_k^{n+1}` as follows:

.. math:: h_k^{n+1} = - \frac{1}{\xi_k} \frac{\partial v^n}{\partial \log k} \sigma_k

1.2.4 Solve Linear PDE Equation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Updating value functions, given the state variables and controls, is
solving a linear PDE system. To mitigate the potential instability of
the non-linear HJB, we add a false transcient (time) dimension and solve
it until convergence. Here we use `Petsc <https://petsc.org/release/>`__
to solve the PDE system, so we show how to rewrite the PDE and call
Petsc package.

For example, in pre-tech-pre-damage case with :math:`\rho\neq 1`, we can
write the HJB into the form:

.. math::

   A \hat{V} 
   +B_{\hat{k}}  \frac{\partial \hat{V}}{\partial \hat{k}}
   +B_{y}\frac{\partial \hat{V}}{\partial y}
   +B_{\hat{r}} \frac{\partial \hat{V}}{\partial \hat{r}} 
   +C_{\hat{k}} \frac{\partial^2 \hat{V}}{\partial \hat{k} \, \partial \hat{k}'}
   +C_{y} \frac{\partial^2 \hat{V}}{\partial y \, \partial y'}
   +C_{\hat{r}} \frac{\partial^2 \hat{V}}{\partial \hat{r} \, \partial \hat{r}'} 
   +D =0

First and Second order partial derivatives

.. math:: \{\frac{\partial \hat{V}}{\partial \hat{k}},\frac{\partial \hat{V}}{\partial y}, \frac{\partial \hat{V}}{\partial \hat{r}}\}, \quad, \{ \frac{\partial^2 \hat{V}}{\partial \hat{k} \, \partial \hat{k}'}, \frac{\partial^2 \hat{V}}{\partial y \, \partial y'}, \frac{\partial^2 \hat{V}}{\partial \hat{r} \, \partial \hat{r}'} \}

The coefficient before Value function:

.. math:: A = - \mathcal{J}_g \cdot g-\mathcal{J}_n \sum_{\ell  } \pi^\ell  f^\ell 

Coefficient of first order partial derivatives:

.. math:: B_{\hat{k}} = -\mu_{k}+ \frac{i^{k}}{k}-\frac{\kappa}{2}\left(\frac{I^{k}}{k}\right)^{2}-\frac{|\sigma_{k}|^{2}}{2} + \sigma_k h^k 

.. math:: B_{y} =e \left( \bar{\theta}+\varsigma h^y \right) 

.. math:: B_{\hat{r}} = -\zeta + \psi_{0}(i^{r})^{\psi_{1}}\exp( -\psi_{1} \hat{r})-\frac{|\sigma_{r}|^{2}}{2}+\sigma_{r} h^r  

Coefficient of second order partial derivatives:

.. math:: C_{\hat{k}} =  \frac{|\sigma_{k}|^{2}}{2},\quad C_{y} = \frac{|\varsigma|^{2}}{2}e^{2},\quad C_{\hat{r}} = \frac{|\sigma_{r}|^{2}}{2}

.. math::

   \begin{align*}
   D = &  \frac{\delta}{1-\rho} \left(\left(\frac{\alpha k-i^{k}-i^{r}-\alpha k \phi_0 \left(1-\frac{e}{\beta \alpha k}\right)^{\phi_1}}{\exp(\hat{V})} \right)^{1-\rho}-1 \right)  \\
   &   - \left( (\lambda_{1}+\lambda_{2}y) e \left( \bar{\theta}+\varsigma h^y \right) +\lambda_{2}\frac{|\varsigma|^{2}}{2}e^{2} \right) \\
   & +\xi^g \mathcal{J}_g (1-g +g  \log g )+\mathcal{J}_g  \cdot g  \cdot \hat{V}^L  \\
   &+\xi^d \mathcal{J}_n  \sum_{\ell} \pi^\ell  (1-f^\ell +f^\ell  \log f^\ell ) \\
   &+\mathcal{J}_n \sum_{\ell  } \pi^\ell  f^\ell \cdot \hat{V}^\ell \\
   &+\xi^k \frac{\left|{h^k}\right|^2}{2}+\xi^c \frac{\left|{h^y}\right|^2}{2}+\xi^r \frac{\left|{h^r}\right|^2}{2}
   \end{align*}

1.2.5 Finite Difference Schemes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Central Difference (Interior Points):

.. math::

   \begin{align*}
           (\frac{\partial f}{\partial x})_i    = \frac{f_{i+1} - f_{i-1}}{2 \Delta x} \\
           (\frac{\partial^2 f}{\partial x^2})_i =\frac{f_{i+1} + f_{i-1} - 2f_i}{\Delta x^2}
       \end{align*}

-  Forward Difference (First Boundary Point):

.. math::

   \begin{align*}
           (\frac{\partial f}{\partial x})_0 =\frac{f_{1} - f_{0}}{\Delta x} \\
           (\frac{\partial^2 f}{\partial x^2})_0 =\frac{f_{2} + f_{0} - 2f_{1}}{\Delta x^2}
       \end{align*}

-  Backward Difference (Last Boundary Point):

.. math::

   \begin{align*}
      (\frac{\partial f}{\partial x})_{N-1}  =\frac{f_{N-1} - f_{N-2}}{\Delta x} \\
      (\frac{\partial^2 f}{\partial x^2})_{N-1}=\frac{f_{N-1} + f_{N-3} - 2f_{N-2}}{\Delta x^2}
   \end{align*}

Below two functions are two finite difference functions we used in
solving HJB equations.

-  `finiteDiff_3D <https://github.com/korito1416/two-capital-climate-change/blob/641046304faed6e6c5bace7bc0f9af45c8196fd9/python/src/Utility.py#L211>`__
   function in two-capital-climate-change/python/src/Utility.py

-  `finiteDiff <https://github.com/korito1416/two-capital-climate-change/blob/641046304faed6e6c5bace7bc0f9af45c8196fd9/python/src/supportfunctions.py#L12>`__
   in two-capital-climate-change/python/src/supportfunctions.py


