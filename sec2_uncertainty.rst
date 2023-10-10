2 Confronting Uncertainty
=========================

2.1: Brownian Motion
--------------------

Under a baseline probability specification,
:math:`W \doteq \{ W_t : t \ge 0\}` is a multivariate standard Brownian
motion.

We partition the vector of Brownian motion into four subvectors as
follows:

.. math::


   dW_t = \begin{bmatrix} dW_t^k \cr dW_t^r \cr dW_t^y \cr dW_t^n \cr \end{bmatrix}

where the first component consists of the technology shocks, the second
component consists of the R&D shocks and the third component contains
the climate change shocks.

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


   \mathcal{J}(x, z) \sum_{\tilde{z} \in \mathcal{Z}}[\tilde{V}[\tilde{x}(\tilde{z}), \tilde{z}]-\hat{V}(x, z)] \pi(\tilde{z} \mid x, z)

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
