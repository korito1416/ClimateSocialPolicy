6 Complete Model and HJB
========================

6.1 Post Technology Jump
------------------------

Controls:

-  :math:`i_k` is a potential value for :math:`\frac{I_t^k}{K_t}`
-  :math:`h_k` is the distortion to capital accumulation.

State: 

- :math:`k` is a realization of :math:`\log K`.

We have HJB for post technology jump as follows

.. math::

   \begin{aligned}
   0= & \max_{i_k}\min_{h_k} \left(\frac{\delta}{1-\rho}\right)\left[\left(\frac{\alpha-i_k}{\exp (v)} \exp(k)\right)^{1-\rho}-1\right] \\
   & +\frac{d v}{dk}\left[\mu_k+i_k-\frac{\kappa}{2} i_k^2-\frac{\left|\sigma_k\right|^2}{2}+\sigma_k h_k\right]+\frac{d^2 v}{d k^2} \frac{\left|\sigma_k\right|^2}{2} \\
   & +\xi_k \frac{\left|h_k\right|^2}{2}
   \end{aligned}

In case of post damage jump, we call obtained solution as
:math:`v \doteq \Phi^{\ell,II}`. And in case of pre damage jump, we call
obtained solution as :math:`v \doteq\Phi^{II}`.

First order condition
~~~~~~~~~~~~~~~~~~~~~

Let

.. math::


   m u \doteq \delta\left(\frac{\alpha-i_k}{\exp (v)} \exp (k)\right)^{-\rho} \frac{\exp (k)}{\exp (\Phi^{m,II})}

Then first order condition for :math:`i_k` is

.. math::


   m u=\frac{d \Phi^{\ell,II}}{dk}\left(1-\kappa i_k\right)

while first order condition for :math:`h_k` is

.. math::


   \frac{d \Phi^{m,II}}{dk} \sigma_k=-\xi_k h_k

6.2 Pre technology Jump
-----------------------

6.2.1 Pre Technology and Post Damage Jump
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Controls:

-  :math:`i_k` is a potential value for :math:`\frac{I_t^k}{K_t}`
-  :math:`i_j` is a potential value for :math:`\frac{I_t^j}{K_t}`
-  :math:`\mathcal{E}` is a potential value for :math:`\mathcal{E}_t`
-  :math:`h_k` is the distortion to capital accumulation.
-  :math:`h_y` is the distortion to temperature anomaly accumulation.
-  :math:`h_j` is the distortion to R&D accumulation.

State:

-  :math:`k` is a realization of :math:`\log K`.
-  :math:`y` is a realization of :math:`Y`.
-  :math:`j` is a realization of :math:`\log J`.
-  :math:`n` is a realization of :math:`\log N`.

We attempt to solve a value function of the form

.. math::


   V^\ell(k,y,j,n) =  \frac{\partial V^\ell}{\partial n} n + \Phi^\ell(k, y, j)

.. math::

   \begin{aligned}
   & 0=\max_{i_k, i_j, \mathcal{E}} \min_{h_k, h_y, h_j} \left(\frac{\delta}{1-\rho}\right)\left[\left(\frac{\alpha-i_k-i_j-\alpha \phi_0\left[1-\frac{\mathcal{E}}{\beta_t \alpha K}\right]^{\phi_1}}{\exp (\Phi^\ell)} K\right)^{1-\rho}-1\right] \\
   & +\frac{\partial \Phi^\ell}{\partial k}\left[\mu_k+i_k-\frac{\kappa}{2} i_k^2-\frac{\left|\sigma_k\right|^2}{2}+\sigma_k h_k\right]+\frac{\partial^2 \Phi^\ell}{\partial k^2} \frac{\left|\sigma_k\right|^2}{2} \\
   & +\frac{\partial \Phi^\ell}{\partial y}\left(\frac{1}{M} \sum_m^M q(x \mid m) \theta(m)+\varsigma h_y\right) \mathcal{E}+\frac{\partial^2 \Phi^\ell}{\partial y^2} \frac{|\varsigma|^2}{2} \mathcal{E}^2 \\
   & -\left(\left[\lambda_1+\lambda_2 y+\lambda_3(y-\bar{y})\right]\left(\frac{1}{M} \sum_m^M q(x \mid m) \theta(m)+\varsigma h_y\right) \mathcal{E}+\left(\lambda_2+\lambda_3\right) \frac{|\varsigma|^2}{2} \mathcal{E}^2\right) \\
   & +\frac{\partial \Phi^\ell}{\partial j}\left(-\zeta+\psi_0\left(i_j\right)^{\psi_1} \exp \left(\psi_1 k-\psi_1 j\right)-\frac{\left|\sigma_j\right|^2}{2}+\sigma_j h_j\right)+\frac{\partial^2 \Phi^\ell}{\partial j^2}\frac{\left|\sigma_j\right|^2}{2} \\
   & +\xi_g I_g(J)(1-g+g \log g)+I_g(J) g\left(\Phi^{\ell,II}-\Phi^\ell\right) \\
   & +\xi_k \frac{\left|h_k\right|^2}{2}+\xi_c \frac{\left|h_y\right|^2}{2}+\xi_j \frac{\left|h_j\right|^2}{2}+\xi_a \frac{1}{M} \sum_m^M q(x \mid m) \log q(x \mid m) \\
   &
   \end{aligned}

6.2.1 Pre Technology and Pre Damage Jump
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Controls:

-  :math:`i_k` is a potential value for :math:`\frac{I_t^k}{K_t}`
-  :math:`i_j` is a potential value for :math:`\frac{I_t^j}{K_t}`
-  :math:`\mathcal{E}` is a potential value for :math:`\mathcal{E}_t`
-  :math:`h_k` is the distortion to capital accumulation.
-  :math:`h_y` is the distortion to temperature anomaly accumulation.
-  :math:`h_j` is the distortion to R&D accumulation.

State:

-  :math:`k` is a realization of :math:`\log K`.
-  :math:`y` is a realization of :math:`Y`.
-  :math:`j` is a realization of :math:`\log J`.
-  :math:`n` is a realization of :math:`\log N`.

We attempt to solve a value function of the form

.. math::


   V(k,y,j,n) =  \frac{\partial V}{\partial n} n + \Phi(k, y, j)

.. math::

   \begin{aligned}
   0 & = \max_{i_k, i_j, \mathcal{E}} \min_{h_k, h_y, h_j}\left(\frac{\delta}{1-\rho}\right)\left[\left(\frac{\alpha-i_k-i_j-\alpha \phi_0\left[1-\frac{\mathcal{E}}{\beta_t \alpha K}\right]^{\phi_1}}{\exp (\Phi)} K\right)^{1-\rho}-1\right] \\
   & +\frac{\partial \Phi}{\partial k}\left[\mu_k+i_k-\frac{\kappa}{2} i_k^2-\frac{\left|\sigma_k\right|^2}{2}+\sigma_k h_k\right]+\frac{\partial^2 \Phi}{\partial k^2} \frac{\left|\sigma_k\right|^2}{2} \\
   & +\frac{\partial \Phi}{\partial y}\left(\frac{1}{M} \sum_m^M q(x \mid m) \theta(m)+\varsigma h_y\right) \mathcal{E}+\frac{\partial^2 \Phi}{\partial y^2} \frac{|\varsigma|^2}{2} \mathcal{E}^2 \\
   & -\left(\left[\lambda_1+\lambda_2 y\right]\left(\frac{1}{M} \sum_m^M q(x \mid m) \theta(m)+\varsigma h_y\right) \mathcal{E}+\lambda_2 \frac{|\varsigma|^2}{2} \mathcal{E}^2\right) \\
   & +\frac{\partial \Phi}{\partial j}\left(-\zeta+\psi_0\left(i_j\right)^{\psi_1} \exp \left(\psi_1 \log K-\psi_1 \log J\right)-\frac{\left|\sigma_j\right|^2}{2}+\sigma_j h_j\right)+\frac{\partial^2 \Phi}{\partial j^2} \frac{\left|\sigma_j\right|^2}{2} \\
   & +\xi_g I_g(J)(1-g+g \log g)+I_g(J) g\left(\Phi^{II}-\Phi\right) \\
   & +\xi_d I_n(y) \sum_{\ell=1}^L \pi_d^{\ell}\left(1-f_{\ell}+f_{\ell} \log f_{\ell}\right)+I_n(y) \sum_{\ell=1}^L \pi_d^{\ell} f_{\ell}\left(\Phi^{\ell}-\Phi\right) \\
   & +\xi_k \frac{\left|h_k\right|^2}{2}+\xi_c \frac{\left|h_y\right|^2}{2}+\xi_j \frac{\left|h_j\right|^2}{2}+\xi_a \frac{1}{M} \sum_m^M q(x \mid m) \log q(x \mid m)
   \end{aligned}
