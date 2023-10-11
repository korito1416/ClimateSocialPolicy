2 Confronting Uncertainty
=========================

2.1: Brownian Motion Misspecification
-------------------------------------

Under a baseline probability specification,
:math:`W := \{ W_t : t \ge 0\}` is a multivariate standard Brownian
motion, and :math:`{\mathfrak F} := \{ {\mathfrak F}_t : t \ge 0\}` is
the corresponding information filtration with :math:`\mathfrak{F}_t`
generated information that is realized between dates zero and t. This
information includes the Brownian increments that have been realized up
to date :math:`t`. Initially, we let :math:`{\mathfrak F}` be the
Brownian filtration, but we subsequently will augment this filtration to
include realizations of jumps that will influence technology and damages
induced by climate change.

As is familiar from derivative claims pricing, positive martingales with
expectations equal to one parameterize changes in probability measures.
From Girsanov theory, such martingales can be characterized by their
implied drift distortions. In particular, under the martingale change in
the probability measure, process :math:`W := \{ W_t : t \ge 0\}` instead
has a drift :math:`H := \{ H_t : t \ge 0\}`.

Suppose that the state vector process :math:`X` has a local mean
increment :math:`\mu_x(X_t,A_t)dt` and stochastic increment
:math:`\sigma_x(X_t, A_t) dW_t`, where :math:`A_t` is a decision or
action taken at time :math:`t`. Throughout the essay we let lower-case
variables capture potential realizations of random vectors. The
realizations of the state vector :math:`X_t` reside in a state space
:math:`{\mathcal X}.` For a value function, :math:`{\widehat V},` the
drift or local mean of :math:`{\widehat V} (X)` is given by

.. math::
   
   \begin{equation} 
   \frac{\partial {\widehat V} }{\partial x'}(X_t)\mu_x(X_t,A_t) + \frac 1 2 {\rm trace}\left[\sigma_x(X_t,A_t)' \frac{\partial^2 {\widehat V} }{\partial x \partial x'}(X_t)\sigma_x(X_t,A_t)\right] .
   \end{equation}

In this equation, we omit time dependence and think of
:math:`\widehat{V}` as the value function for an infinite
horizon discounted problem.


Formula (1) captures the time increment to risk confronted by the
decision-maker.

The decision-maker entertains possible misspecification uncertainty by
replacing formula (1) with the solution

.. math::

   \begin{align*} 
   \min_{h} \frac{\partial {\widehat V} }{\partial x'}(x) \left[\mu_x(x,a) + \sigma_x(x,a) h \right] + \frac 1 2 {\rm trace}\left[\sigma_x(x,a)' \frac{\partial^2 {\widehat V} }{\partial x \partial x'}(x)\sigma_x(x,a)\right] + \frac{\xi}{2} h'h 
   \end{align*}

for a penalty parameter :math:`\xi`.

The minimization captures a form of uncertainty aversion, analogous to
risk aversion, since the minimizing objective will be less than or equal
to (1). The penalty parameter :math:`\xi` restrains the concern for
robustness to model misspecification. The quadratic penalty in :math:`h`
is a local measure of \``relative entropy’’ or Kulback–Leibler
divergence. A limiting choice of :math:`\xi \approx \infty` implies a
minimizing choice of :math:`h=0` with an implied contribution given by
(1). Since the minimization problem is quadratic in :math:`h`, the
minimizer is

.. math::

   \begin{equation} 
   h^* = - \frac 1 {\xi} \sigma_x(x,a)'\frac{\partial {\widehat V} }{\partial x}(x)
   \end{equation}

with a minimized objective:

.. math::

   \begin{align*} 
   \frac{\partial {\widehat V} }{\partial x'}(x) \mu_x(x,a) + \frac 1 2 {\rm trace}\left[\sigma_x(x,a)' \frac{\partial^2 {\widehat V} }{\partial x \partial x'}(x)\sigma_x(x,a)\right] 
   - \frac 1 {2 \xi} \frac{\partial {\widehat V} }{\partial x'}(x)\sigma_x(x,a)\sigma_x(x,a)'\frac{\partial {\widehat V} }{\partial x}(x) .
   \end{align*}

Notice that the minimizing drift, :math:`h^*,` is potentially state
dependent. When :math:`\sigma` depends on the action :math:`a`, the
drift of interest for valuation and interpretation depends on the
maximizing action :math:`a` expressed as a function of the state. The
drift vector, :math:`h^*,` has larger entries where the value function
is more adversely exposed to the Brownian increments. Smaller values of
:math:`\xi` result in drift adjustments with larger
magnitudes.

   While we motivated the adjustment to an HJB equation in terms of
   robustness, it may also be viewed as a risk adjustment in conjunction
   with recursive utility. Consider the local counterpart or small
   :math:`\epsilon` counterpart to the risk adjustment:

   .. math::

      \begin{align} 
      & \frac 1 {\epsilon } \left( \frac 1 {1 -\gamma}  \log {\mathbb E} \left[ \exp \left( (1- \gamma) {\widehat V}(X_{t+\epsilon})  \right) \mid {\mathfrak F}_t \right] - {\widehat V}(X_t)\right) \cr &  =  \frac 1 {\epsilon (1 -\gamma) }\log {\mathbb E} \left[ \exp \left( (1 - \gamma) \left({\widehat V}(X_{t+\epsilon}) - {\widehat V}(X_t) \right) \right) \mid {\mathfrak F}_t \right] .
      \end{align}

   This exponential risk adjustment of the continuationv value induces a local log-normal type of adjustment given by
   
   .. math::

      \begin{align*} 
      (1- \gamma)  \frac {\partial {\widehat V}(x)}  {\partial x'}\sigma(x,a) \sigma(x,a)' \frac {\partial {\widehat V}(x)}{\partial x} ,
      \end{align*}
   where the term multiplying :math:`1-\gamma` is the  local variance of the continuation value process
   :math:`{\widehat V}(X)`. Setting $ :math:`\gamma - 1 = \frac{1}{\xi}` gives a mathematical
   equivalence between robustness and risk considerations, although the
   rationale for the two adjustments is very different. We will
   eventually show how to embed this into a full recursive utility
   specification preferences. The resulting equivalence is a direct
   extension of a well-known result from risk-sensitive control theory.

..

   As :cite:t:`AndersonHansenSargent:2003` emphasize, the
   negative implied drift distortions from a planner’s problem are also
   the local shadow prices for concerns about misspecification. While
   they featured the case in which these shadow prices are also
   pertinent for competitive financial markets, the same insight carries
   over to social valuation in the presence of externalities that induce
   a wedge between market prices and social counterparts.

2.2: Jump misspecification
--------------------------

We suppose there is a discrete set of jump states :math:`\mathcal{Z}`.
Let :math:`z` denote a realized value in the set :math:`\mathcal{Z}`.
Let :math:`\mathcal{J}` denote a state-dependent jump intensity, and let
:math:`\pi(\tilde{z} \mid x, z), z \in \mathcal{Z}` give the jump
distribution conditioned on a jump when :math:`X_t=x` in discrete state
:math:`Z_t=z`. Recall that the jump intensity, :math:`\mathcal{J}`,
implies an approximate jump probability, :math:`\epsilon \mathcal{J}`,
over a small time increment, :math:`\epsilon`. Following a jump,
:math:`x` changes as does the value function. For each choice of
:math:`\tilde{z}`, :math:`x` jumps to the :math:`\tilde{x}(\tilde{z})`,
where :math:`\tilde{z}` is uncertain prior to the jump. The baseline
probabilities are :math:`\pi(\tilde{z} \mid x, z)` for
:math:`z \in \mathcal{Z}`, where

.. math::


   \sum_{\mathcal{Z}} \pi(\tilde{z} \mid x, z)=1 .

With these jumps, a value function shifts from :math:`\hat{V}(x, z)` to
:math:`\tilde{V}[\tilde{x}(\tilde{z}), \tilde{z}]`. The jump process
contributes the following term to the drift of :math:`\widehat{V}(X, Z)`
:

.. math::

   \begin{equation}
   \mathcal{J}(x, z) \sum_{\tilde{z} \in \mathcal{Z}}[\tilde{V}[\tilde{x}(\tilde{z}), \tilde{z}]-\hat{V}(x, z)] \pi(\tilde{z} \mid x, z)
   \end{equation}

capturing the jump risk contribution to the decision problem.

To capture potential misspecification, we introduce a non-negative
function :math:`f` where the altered jump distribution is

.. math::


   \frac{f(\tilde{z} \mid x, z) \pi(\tilde{z} \mid x, z)}{\tilde{f}(x, z)}

and intensity :math:`\mathcal{J}(x, z) \bar{f}(x, z)` where

.. math::


   \bar{f}(x, z)=\sum_{\bar{z} \in \mathcal{Z}} f(\tilde{z} \mid x, z) \pi(\tilde{z} \mid x, z) .

To restrain the exploration of potential misspecification, we introduce
a convex cost:

.. math::


   \xi \mathcal{J}(x, z) \sum_{\tilde{z} \in \mathcal{Z}}[1-f(\tilde{z} \mid x, z)+f(\tilde{z} \mid x, z) \log f(\tilde{z} \mid x, z)] \pi(\tilde{z} \mid x, z)

The term multiplying :math:`\xi` is a local (in time) measure of
relative entropy or Kullback–Leibler divergence applicable to jump
processes

To confront misspecification, we solve:

.. math::

   \begin{align*} 
   \min _{f \geqslant 0} & \mathcal{J}(x, z) \sum_{\tilde{z} \in \mathcal{Z}}[\tilde{V}[\tilde{x}(\tilde{z}), \tilde{z}]-\hat{V}(x, z)] f(\tilde{z} \mid x, z) \pi(\tilde{z} \mid x, z) \\
   & +\xi \mathcal{J}(x, z) \sum_{\tilde{z} \in \mathcal{Z}}[1-f(\tilde{z} \mid x, z)+f(\tilde{z} \mid x, z) \log f(\tilde{z} \mid x, z)] \pi(\tilde{z} \mid x, z) .
   \end{align*}

The above minimization problem has a quasi-analytical solution:

.. math::

   \begin{align}
   f^*( {\tilde z}  \mid x, z )  = \exp \left( - {\frac{1}{\xi}} \left( {\widetilde  V} [{\tilde x}({\tilde z}), {\tilde z} ] - {\widehat V} (x, z) \right) \right), 
   \end{align}

with a minimized objective: 

.. math::

   \begin{equation}
   \xi {\mathcal J}(x, z) \left[ 1 -  \sum_{{\tilde z } \in {\mathcal Z}}   \exp \left( - {\frac{1}{\xi}} \left( {\widetilde  V} [{\tilde x}({\tilde z}), {\tilde z} ] - {\widehat V} (x, z) \right) \right) \right] \pi({\tilde z} \mid x, z)  ,
   \end{equation}

which we use in place of (1).

2.3 Incorporating ambiguity aversion
------------------------------------

Imagine there are alternative models of different components of the
dynamics. We follow :cite:t:`HansenMiao:2018` by supposing
that the drift :math:`\mu(x, z, a \mid \theta)` depends on an unknown
parameter :math:`\theta` residing in a set :math:`\Theta.` The
parameter, :math:`\theta,` could index one of a discrete set of
alternative models or depict a unknown parameter vector. The
decision-maker has a baseline probability :math:`d P_t(\theta)` for each
time instant, :math:`t`, and makes an adjustment for ambiguity by
solving 

.. math::

   \begin{align*}
   \min_{q,\, \int_\Theta q(\theta) dP_t(\theta)  = 1} \hspace{.3cm} &\frac{\partial {\widehat V} }{\partial x'}(x, z) \int_\Theta \mu_x(x, z, a \mid \theta) q(\theta)  d P_t(\theta)  \cr & + \chi \int_\Theta  q(\theta) \log q(\theta) d P_t(\theta) ,
   \end{align*}

where :math:`\chi` is a penalty parameter.

This problem is known to have a solution that entails exponential
tilting as a function of the drift of the value function for alternative
values of :math:`\theta`:

.. math::
   \begin{equation*}
   q^*_t({\tilde \theta}) = \frac {\exp\left( - \frac 1 {\chi} \frac{\partial {\widehat V} }{\partial x'}(x, z)  \mu_x (x, z, a \mid {\tilde \theta}) \right)}{ \int_\Theta \exp\left( - \frac 1 {\chi} \frac{\partial {\widehat V} }{\partial x'}(x, z)  \mu_x\left(x, z, a \mid \theta\right)\right) d P_t(\theta) } .
   \end{equation*}

The minimized objective is 

.. math::
   \begin{equation*}
   \chi \log \int_\Theta  \exp\left( - \frac 1 {\chi} \frac{\partial {\widehat V} }{\partial x'}(x, z)  \mu_x(x, z, a \mid \theta)\right) d P_t(\theta) .
   \end{equation*}

Notice that this formulation implies an exponential adjustment for model ambiguity concerns.

We allow the baseline probability to be time dependent to allow for
recursive learning, although we will abstract from this learning in our
application.

Problem 3 and Problem 2 show a notable similarity. The smooth ambiguity
model applies to Brownian uncertainty, and the objective of interest is
the local evolution of the value function. In the case of jump
uncertainty, this is replaced by the intensity times the difference
between the post-jump and pre-jump value functions. The counterpart to
:math:`\chi` for the smooth ambiguity adjustment is the intensity times
:math:`\xi.`

The relative density :math:`q` in Problem 3 plays a role analogous to  :math:`f/\bar{f}` in Problem 2 when deducing the worst-case
distribution. With this mapping, the two robustness adjustments are
mathematically equivalent. As we noted, however, the required
specification of the intensity introduces an additional source of
potential misspecification for the case of jump uncertainty.


