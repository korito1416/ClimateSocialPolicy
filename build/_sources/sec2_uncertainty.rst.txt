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


   dW_t = \begin{bmatrix} dW_t^k \cr dW_t^j \cr dW_t^y \cr dW_t^n \cr \end{bmatrix}

where the first component consists of the technology shocks, the second
component consists of the R&D shocks and the third component contains
the climate change shocks.

2.2: Jump misspecification
--------------------------

Let :math:`{\mathfrak I}` denote a state dependent jump intensity and
let :math:`\pi(\ell \mid x )`,
:math:`\ell =1,2,…,L`` give the jump distribution conditioned on
a jump when :math:`X_t = x`. While our application will have multiple
jumps, for pedagogical simplicity, we suppose that there is a single
jump that shifts a value function from :math:`{\widehat V}(x)` to
:math:`{\widetilde V}[\tilde x(\ell), \ell ]` with baseline
probability :math:`\pi(\ell \mid x)` for :math:`\ell=0,1,...L` where

.. math::

    \begin{equation}
    \sum_{\ell = 0}^L \pi(\ell \mid  x) = 1.
    \end{equation}


Following a jump, :math:`x` changes as does the value function. For
each choice of :math:`\ell`, :math:`x` jumps to the
:math:`{\tilde x}(\ell)` where :math:`\ell` is uncertain prior to the
jump.
| The jump process contributes the following term to the drift of
:math:`{\widehat V} (X)`:

.. math::
    
    \begin{equation}
    {\mathfrak I}(x) \sum_{\ell=0}^L  \left[ {\widetilde  V} [\tilde x(\ell),\ell] - {\widehat V} (x) \right] \pi(\ell \mid x)  .
    \end{equation}

To capture potential misspecification, we introduce a nonnegative
function :math:`f` where the altered jump distribution is:

.. math::


   \frac {f( \ell  \mid x) \pi(\ell, x) }{ {\bar f}( x) },

and intensity :math:`\mathfrak I(x) {\bar f}( x )` where

.. math::


   {\bar f}( x ) = \sum_{{m} = 0}^M  f ( \ell  \mid x ) \pi({\ell} \mid x)

To restrain the exploration of potential misspecification, we introduce
a convex cost:

.. math::


   \xi_r {\mathfrak I}(x) \sum_{\ell = 0}^L \left[ 1 - f( \ell \mid x )  + f( \ell  \mid x )  \log f( \ell  \mid x )\right]   \pi(\ell \mid x).  

The term multiplying :math:`\xi_r` is a local (in time) measure of
relative entropy applicable to jump
processes[#]_.


To confront misspecification, we solve: 

.. math::
    \begin{align*} 
    \min_{f \ge 0} \hspace{.3cm}  & {\mathfrak I}(x)  \sum_{\ell = 0}^L   \left[ {\widetilde  V} [\tilde x(\ell),\ell] - {\widehat V} (x) \right] f( \ell  \mid x) \pi( \ell \mid x)\cr
    & +  \xi_r {\mathfrak I}(x) \sum_{\ell=0}^L \left[ 1 - f( \ell \mid x )  + f( \ell \mid x )  \log f( \ell \mid x )\right]   \pi(\ell \mid x)  
    \end{align*}

.. [#] See, for instance,  :cite:t:`AndersonHansenSargent:2003`.
