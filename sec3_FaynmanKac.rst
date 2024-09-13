3. Value Decomposition
======================

3.1: Pre-jump stochastic dynamics
---------------------------------

As a part of a more general derivation, we begin with state dynamics
modeled as a Markov diffusion:

.. math::


   dX_t = \mu(X_t) dt + \sigma(X_t) dW_t

Consider the evaluation of discounted utility where the instantaneous
contribution is :math:`U(x)`, where :math:`x` is the realization of a
state vector :math:`X_t`. The function :math:`V` is known to satisfy a
Feynman-Kac (FK) equation:

:raw-latex:`\begin{align}  
0 \hspace{.2cm} = \hspace{.2cm} & \delta U(x) - \delta V(x) + 
\mu(x) \cdot \frac{\partial V}{\partial x}(x)
+ {\frac{1}{2}} {\rm trace}\left[\sigma(x)' \frac{\partial^2 V}{\partial x \partial x'}(x) \sigma(x) \right] \cr
& + \sum_{\ell = 1}^L {\mathcal J}^\ell(x)  \left[ {V}^\ell(x)   - V (x) \right]
\end{align}`

for a given collection of “terminal” value functions, :math:`V^{\ell}`
for :math:`\ell = 1,2,...,L`. These are post-jump value functions that
are computed in advance of solving for :math:`V`. Then :math:`V`
satisfies the forward-looking equation:

:raw-latex:`\begin{equation}  
V(X_0) = \mathbb{E} \left[ \int_0^\infty Dis_t \left[\delta U(X_t) + \sum_{\ell = 1}^L {\mathcal J}^\ell(x) V^\ell(x) \right] \mid X_0 \right]
\end{equation}`

where :math:`Dis` contributes a state-dependent discount rate:

:raw-latex:`\begin{equation} 
Dis_t = \exp\left( - \int_0^t \left[\delta +  \sum_{\ell=1}^{L}  {\mathcal J}^{\ell}(X_u) \right] du \right)
\end{equation}`

The process :math:`Dis` includes both an adjustment for the probability
that a jump has not occurred, given by:

.. math::


   \exp\left( - \int_0^t \left[ \sum_{\ell=1}^{L}  {\mathcal J}^{\ell}(X_u) \right] du \right)

along with the usual exponential contribution :math:`\exp(-\delta t)`.
The flow term being discounted in the formula includes both a direct
utility contribution and a continuation-value contribution should a jump
take place.

We want to represent:

.. math::


   V_{x_i}(x) \equiv \frac{\partial V}{\partial x_i}(x)

as an expected discounted value of a marginal impulse response of future
:math:`X_t` to a marginal change in the :math:`i^{th}` coordinate of
:math:`x`.

3.2 Variational process
-----------------------

We form the first variational process, :math:`M`, that gives the
marginal impact on future :math:`X` of a marginal change in one of the
initial states. This process has the same dimension as the number of
components of :math:`X`. By initializing the process at one of the
alternative coordinate vectors, we determine the initial state of
interest.

The drift for the :math:`i^{th}` component of :math:`M` is given by:

.. math::


   m' \frac{\partial \mu_i}{\partial x}(x)

and the coefficient on the Brownian increment is given by:

.. math::


   m' \frac{\partial \sigma_i}{\partial x}(x)

for :math:`m` as a hypothetical realization of :math:`M_t` and :math:`x`
as a hypothetical realization of :math:`X_t`, where :math:`'` denotes
vector or matrix transposition. The implied evolution of the process
:math:`M^i` is given by:

.. math::


   dM_{t}^i = \left(M_t\right)'\frac{\partial \mu_i}{\partial x}(X_t) dt + \left({M_t}\right)'\frac{\partial \sigma_i}{\partial x}(X_t) dW_t

The drift for the composite process :math:`(X,M)` is given by:

:raw-latex:`\begin{equation} 
\hat{\mu} (x,m) = \begin{bmatrix} 
\mu(x) \\ 
m' \frac{\partial \mu_1}{\partial x}(x) \\ 
\vdots \\ 
m' \frac{\partial \mu_n}{\partial x}(x) 
\end{bmatrix}
\end{equation}`

and the composite matrix coefficient on :math:`dW_t` is given by:

:raw-latex:`\begin{equation}  
\hat{\sigma}(x,m) = \begin{bmatrix} 
\sigma(x) \\ 
m' \frac{\partial \sigma_1}{\partial x}(x) \\ 
\vdots \\ 
m' \frac{\partial \sigma_n}{\partial x}(x) 
\end{bmatrix}
\end{equation}`

With these constructions, we now write the composite dynamics as:

.. math::

    
   \begin{bmatrix} d X_t \\ d M_t \end{bmatrix} = \hat{\mu}(X_t, M_t) dt + \hat{\sigma}(X_t, M_t) d W_t

By initializing :math:`M_0` at a coordinate vector in
:math:`\mathbb{R}^n` with a one in position :math:`i`, we obtain the
vector :math:`M_t` of stochastic responses to a marginal change in the
:math:`i^{th}` component of the state vector :math:`X_0`. In our
application, we simulate the :math:`M` process using these stochastic
dynamics.

3.3 Marginal valuation
----------------------

By differentiating the Feynman-Kac equation with respect to each
coordinate, we obtain a vector of equations, one for each state
variable. We then form the dot product of this vector system with
respect to :math:`m` to obtain a scalar equation system that is of
particular interest. The resulting equation turns out to also be an FK
equation for the function:

.. math::


   m \cdot \frac{\partial V}{\partial x}(x)

Given that the equation to be solved involves both :math:`m` and
:math:`x`, this equation uses the diffusion dynamics for the joint
process :math:`(X,M)`.

The solution to this derived Feynman-Kac equation is of the form of a
discounted expected value:

:raw-latex:`\begin{equation}  
\frac{\partial V}{\partial x}(X_0) \cdot M_0 = \mathbb{E} \left[ \int_0^\infty Dis_t \left(M_t \cdot Scf_t \right) \mid X_0, M_0 \right]
\end{equation}`

where :math:`Dis` is given by the discount equation, and :math:`Scf` is
a social cash flow vector given as:

:raw-latex:`\begin{align}
Scf_t = \delta U_x(X_t) 
 + \sum_{\ell=1}^{L} {\mathcal J}^{\ell}_x(X_t) \left[V^\ell(X_t) - V(X_t)\right]  
+  \sum_{\ell=1}^{L} {\mathcal J}^{\ell}(X_t) V^\ell_x(X_t)
\end{align}`

By initializing the state vector :math:`M_0` to be a coordinate vector
of zeros in all entries but entry :math:`i`, we obtain the formula of
interest.

The social cash flow process :math:`Scf` has three terms to be
discounted, two of which come from the possibilities of jumps to new
continuation values. The marginal response process :math:`M` acts as an
additional stochastic adjustment to valuation. In effect, there is a
composite stochastic discount vector process :math:`Dis M` applied
component-by-component to the state vector. Notice that the cash-flow
process can be decomposed additively into a direct utility contribution
and contributions for each of the potential jumps.

In our application, we report contributions for each time horizon and
for each jump component along with the direct utility contribution:

:raw-latex:`\begin{align*}
\delta &  \mathbb{E}\left[ Dis_t M_t \cdot U_x(X_t) \mid X_0, M_0 \right]  \cr
& + \mathbb{E}\left[Dis_t M_t \cdot  {\mathcal J}^{\ell}_x(X_t)  \left[V^\ell(X_t)  - V(X_t)  \right] \mid X_0, M_0 \right] \cr  
& + \mathbb{E} \left[  Dis_t M_t \cdot   V^\ell_x(X_t) {\mathcal J}^{\ell}(X_t) \mid X_0, M_0 \right]
\end{align*}`

for :math:`t \geq 0` and :math:`\ell = 1,\dots,L`. These provide
valuation counterparts to impulse responses commonly reported in
economic dynamics. The initialization of :math:`M_0` dictates the
marginal change under consideration.

3.4 Incorporating robustness
----------------------------

To incorporate robustness, we use the expectation associated with the
stochastic dynamics induced by the minimizing :math:`h` and
:math:`g^\ell`\ ’s. We let :math:`g^{\ell *}` denote the latter
minimizer for :math:`\ell = 1, 2, ... L`. We obtain a formula analogous
to the marginal value function:

.. math::


    \frac{\partial V}{\partial x}(X_0) \cdot M_0  =   \widetilde{\mathbb E} \left[ \int_0^\infty  Dis_t \left(M_t \cdot Scf_t \right)  \mid X_0, M_0 \right]

where the expectation :math:`\widetilde{\mathbb E}` uses the diffusion
dynamics incorporating the minimizing drift distortions, :math:`h^*`,
implied by robustness. In addition, we modify the discount factor term
to be:

.. math::


   Dis_t = \exp\left( - \int_0^t \left[\delta +  \sum_{\ell=1}^{L}  {\mathcal J}^{\ell}(X_\tau) g^{\ell*}(X_\tau) \right] d\tau  \right)

and the flow term:

:raw-latex:`\begin{align} 
Scf_t  = \delta U_x(X_t) 
 & + \sum_{\ell=1}^{L} {\mathcal J}^{\ell}_x(X_t) g^{\ell*}(X_t) \left[V^\ell(X_t)  - V(X_t)  \right] \\
 & +  \sum_{\ell=1}^{L}  {\mathcal J}^{\ell}(X_t) g^{\ell*}(X_t)   V^\ell_x(X_t) \\
 & + \xi \sum_{\ell = 1}^L {\mathcal J}^\ell_x(X_t)  \left[ 1 - g^{\ell*}(X_t) + g^{\ell*}(X_t) \log g^{\ell*} (X_t) \right].
\end{align}`

Notice that we have scaled each intensity or its partial derivative by
the corresponding :math:`g^{\ell*}` with the exception of the fourth
contribution to the flow term. This fourth term is included because
marginal changes in the state vector alter the exposure to uncertainty
and thus impact valuation. While partial derivatives with respect to the
intensities :math:`{\mathcal J}^\ell` contribute to the second term in
:math:`Scf`, there is no counterpart from the jump distortion,
:math:`g^{\ell*}`. We may treat this robust probability adjustment as
exogenous to the decision maker and hence not impacted by endogenous
state vector components. As verified in the appendix, this treatment is
a ramification of the minimization (via application of the Envelope
Theorem).
