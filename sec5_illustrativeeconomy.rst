5 Economic Framework
====================

We start by considering a simple production-based model with an AK
production technology subject to adjustment costs. By design, this
formulation has close ties to much of the long-run risk with consumption
exogenously specified consumption endowments. Prior to introducing
climate change, we include two modifications. First, we include an
energy input in way that is mathematically similar to what is used in so
called \``DICE’’ models; and second, we allow for R&D that could
eventually remove the need for energy input. In regards to the second
modification, some suggest that an economically viable version of
nuclear fusion might achieve this aim.

5.1 Production and Innovation
-----------------------------

| The economic component to our model has two endogenous state
  variables: the stock of productive capital and the stock of research
  and development capital.
| The stock of productive capital, :math:`K_t,` evolves as

.. math::


   dK_t = K_t \left[ - \mu_k    + \left({\frac {I_{t}^k}{K_t}} \right)  -
   {\frac { \kappa} 2} \left( {\frac {I_{t}^k} {K_t}} \right)^2 \right] dt 
   + K_t \sigma_k dW_t

where :math:`\sigma_k` is a row vector with the same dimension as the
underlying Brownian motion. Capital is broadly conceived to include
human capital and intangible capital. Investment :math:`I_t^k`
contributes new capital subject to an adjustment cost captured by the
curvature parameter :math:`\kappa`.

A process :math:`R` captures the stock of knowledge induced by research
and development as measured by :math:`R_t`:

.. math::


   d R_t = - \zeta R_t dt + \psi_0 \left(I_t^r\right)^{\psi_1} \left(R_t\right)^{1 - \psi_1} dt + R_t \sigma_r dW_t 

where :math:`0 < \psi_1 < 1` and :math:`I_t^j` is an investment in
research and development (R & D).

While we will solve a social planner’s problem, we will subsequently
entertain the possibility that this evolution equation includes an
externality associated with R&D. For pedagogical simplicity, we consider
the case of a single technology jump to a fully productive green
technology. The parameter, :math:`\zeta,` captures depreciation in the
stock of knowledge pertinent for future technological progress.

5.1.1 Output
~~~~~~~~~~~~

Output is split between consumption, productive and R&D capital
investments, and emissions abatement expenditure.

.. math::


   C_t + I_t^k +  I_t^r = \alpha K_t  \left[1 - \phi_{0}(Z_t)\left(A^b_t\right)^{\phi_1} \right] 

for :math:`\phi_1 \ge 2` and :math:`0<\phi_{0}(Z_t) \le 1,` where

.. math::


   A^b_t  =   \left(1 - \frac {{\mathcal E}_t}{\beta \alpha K_t}  \right){\mathbf 1}_{\{{\mathcal E}_t  < \beta \alpha K_t\}}

and where :math:`{\mathbf 1}` is an indicator function that assigns one
to the event in the parentheses. When emissions fall short of the
threshold :math:`\beta_t \alpha K_t,` there is a corresponding convex
adjustment in the output given by the right-hand side of output
constraint.

This technology is, by design, homogeneous of degree one. For a fixed
:math:`K_t,` the implied production function is flat when emissions
exceed the threshold of :math:`\beta \alpha K_t,` and has a zero left
derivative at this point. The function equals :math:`1-\phi_{0}(Z_t)`
when :math:`{\mathcal E}_t=0` and increases up the threshold as a
concave function with curvature dictated by the parameter
:math:`\phi_1.` We feature the case in which :math:`\phi_1 = 3.`

5.2 Social Valuation
--------------------

In our computations we use the following state variables:


.. math::

   \begin{align*}
    X_t :=\begin{bmatrix} X_t^1 \cr {\widehat N}_t  \end{bmatrix}  \hspace{.3cm} \textrm{ where } \hspace{.3cm} 
   X_t^1  := \begin{bmatrix}
   {\widehat K_t} \cr {\widehat R}_t  \cr {\widehat Y}_t \end{bmatrix},
   \end{align*}

where

.. math::
   
   \begin{align*}
   {\widehat K}_t & := \log K_t \cr
   {\widehat R}_t  & := \log R_t \cr
   {\widehat N}_t & := \log N_t .
   \end{align*}

We treat the damage jump and technology jump realizations
as implying continuation values for the post-jump outcomes. These become
inputs into HJB equations prior to the jump. We compute a representation
for the continuation values as

.. math::
   
   \begin{align*}
   {\widehat V}(X_t, Z_t) = {\widehat V}^1(X_t^1, Z_t)  - {\widehat N}_t \,,
   \end{align*}

| where it is straightforward to verify the additive separability in the
  logarithm of damages. This separability simplifies our numerical
  solutions.
| We have three controls:

:math:`\frac {I_t^k}{K_t}, \frac {I_t^r}{K_t},` and
:math:`{\mathcal E}_t.`

Consumption is then determined by the output constraint. We solve the
model using an iterative scheme whereby we iterate between maximization
and minimization controls and a finite difference solution for the
social value function.

5.2.1 Investment Alternatives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The social planner has two investment opportunities in our model:
investment in new capital and investment in R&D. We investigate the
first-order conditions prior to the realization of either technology or
damage jump. In both cases we see the role of the shadow value of the
corresponding asset stock.

The first-order conditions for investment in new capital are

.. math::


   \frac {\partial {\widehat V}}{ \partial {\hat k} } (X_t, Z_t) \left(1 - \kappa \, \frac {I_t^k}{K_t} \right)
    - \delta \, \left(C_t\right)^{-\rho}  \left(N_t\right)^{\rho-1}  K_t
    \, \exp \left( (\rho - 1) {\widehat V}(X_t, Z_t)\right)  = 0. 

where we replace :math:`C_t` with $.. math::\frac {C_t}` {N_t} $ in
the preference specification. Thus we obtain the formula for investment:

.. math::


   \frac {I_t^k}{K_t} = \frac 1 \kappa \left[ 1 - \frac{   
     \delta \, \left(C_t\right)^{-\rho}  \left(N_t\right)^{\rho} 
    \, \exp \left((\rho - 1) {\widehat V}(X_t, Z_t)\right) }{N_t\left(K_t\right)^{-1}\frac {\partial {\widehat V}}{ \partial {\hat k} } (X_t, Z_t)}\right] , 

where the term

.. math::


    \frac {N_t\left(K_t\right)^{-1}\frac {\partial {\widehat V}}{ \partial {\hat k}(X_t, Z_t) }}
   {\delta \, \left(C_t\right)^{-\rho}  \left(N_t\right)^{\rho} 
    \, \exp \left((\rho - 1) {\widehat V}(X_t, Z_t)\right) }

is the :math:`Q` from the theory of investment adjusted for damages. In our
analysis this is a social valuation, which may be distinct from a
marginal valuation.

The first-order conditions for the socially efficient R&D investment are

.. math::


   \frac {\partial {\widehat V}}{ \partial {\hat r} } (X_t, Z_t) \psi_0 \psi_1 \left( \frac {I_t^r}{R_t}  \right)^{\psi_1-1} 
    - \delta \, \left(C_t\right)^{-\rho}  \left(N_t\right)^{\rho-1}  
    \exp \left((\rho - 1) {\widehat V}(X_t, Z_t)\right) = 0 , 

Thus

.. math::

    
   \left( \frac {I_t^r}{R_t}  \right)^{1 - \psi_1} = \psi_0 \psi_1 R_t   \left[  \frac { N_t\left(R_t\right)^{-1} \frac { \partial { \widehat V}}{ \partial {\hat r} } (X_t, Z_t)  }{
   \delta \, \left(C_t\right)^{-\rho}  \left(N_t\right)^{\rho }  \,
    \exp \left( (\rho - 1) {\widehat V}(X_t, Z_t)\right) }\right] .

The term in square brackets is the social value of the knowledge stock
of R&D expressed in units of (damaged) consumption.

5.2.2 Emission
~~~~~~~~~~~~~~

Prior to both jump realizations, the first-order conditions for
emissions are

.. math::

   \begin{align*}
   & \left[ \frac {\partial {\widehat V}} {\partial y} (X_t, Z_t)  - \lambda_1 - \lambda_2 Y_t    \right] \left[{\frac 1 L_y} \sum_{\ell = 1}^{L_y} q(\ell \mid X_t, Z_t) \theta(\ell) + \varsigma H_t  \right] 
   + {\mathcal E}_t \left[ \frac {\partial^2 {\widehat V}(X_t, Z_t)}{\partial y^2 } - \lambda_2 \right]|\varsigma|^2 \cr
   & + \delta \left( C_t \right)^{-\rho}\left( N_t \right)^{\rho - 1} 
   \exp \left( (\rho - 1) {\widehat V}(X_t, Z_t) \right)
   \frac {\phi_0 \phi_1} {\beta } \left(\frac {A_t^b}  { \beta \alpha K_t }\right)^{\phi_1 - 1}{\bf 1}_{\{{\mathcal E}_t < \beta \alpha K_t\} } =0 .
   \end{align*}

The implied social cost of carbon is

.. math::


    \frac {\left[ -\frac {\partial {\widehat V}} {\partial y} (X_t, Z_t)  + \lambda_1 + \lambda_2 Y_t    \right] \left[{\frac 1 L_y} \sum_{\ell  = 1}^{L_y} q(\ell \mid X_t, Z_t) \theta(\ell) + \varsigma H_t \right]
   - {\mathcal E}_t \left[ \frac {\partial^2 {\widehat V}(X_t, Z_t)}{\partial y^2 } - \lambda_2 \right]|\varsigma|^2}{\delta \left( C_t \right)^{-\rho}\left( N_t \right)^{\rho } \exp \left( (\rho - 1) {\widehat V}(X_t, Z_t) \right) } , 

and the social benefit is

.. math::


   { \frac{1}{N_t}} \frac {\phi_0 \phi_1} {\beta} \left(\frac {A_t^b}  { \beta \alpha K_t }\right)^{\phi_1 - 1}{\bf 1}_{\{{\mathcal E}_t < \beta \alpha K_t\} },

where the formulas are evaluated at the socially efficient emissions and
the minimizing :math:`q(\cdot \mid X_t, Z_t)` and :math:`H_t,` inclusive
of the misspecification adjustment.

Again we see a central role for the social valuation of an endogenous
state; in this case it is the social cost of global warming given by

.. math::


   \frac {-\frac {\partial {\widehat V}} {\partial y} (X_t, Z_t)}{\delta \left( C_t \right)^{-\rho}\left( N_t \right)^{\rho } \exp \left( (\rho - 1) {\widehat V}(X_t, Z_t) \right) } .

Notice also that social cost of carbon .. math::\eqref{SCC}` includes
an explicit volatility adjustment because emissions in our model alter
the local exposure to Brownian motion risk.


