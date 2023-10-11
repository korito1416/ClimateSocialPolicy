6 Complete Model and HJB
========================

We specify here that the four subvectors of Brownian motion are mutually
independent. Hence, we make further definition of distortion as

.. math::


   h = \begin{bmatrix} {h^k} \cr {h^r} \cr {h^y} \cr \end{bmatrix}

For our analysis here, rather than a constant value of :math:`\xi` for
all uncertainty channels, we use a set of values
:math:`\{\xi^k, \xi^c, \xi^r, \xi^d, \xi^g\}`, one for each uncertainty
channel, one for each uncertainty channel so that we can carry out our uncertainty decompositions.

We define realizations of controls and states as following:

Controls:

-  :math:`i^k` is a potential value for :math:`I_t^k`
-  :math:`i^r` is a potential value for :math:`I_t^r`
-  :math:`e` is a potential value for :math:`\mathcal{E}_t`
-  :math:`{h^k}` is the distortion to capital accumulation.
-  :math:`{h^y}` is the distortion to temperature anomaly accumulation.
-  :math:`{h^r}` is the distortion to R&D accumulation.
-  :math:`g` is the misspecification to technology jump.
-  :math:`f` is the misspecification to damage jump.

State:

-  :math:`k` is a realization of :math:`K_t`.
-  :math:`y` is a realization of :math:`Y_t`.
-  :math:`r` is a realization of :math:`R_t`.
-  :math:`n` is a realization of :math:`N_t`.

6.1 Post Technology Jump
------------------------

6.1.1 Post Technology and Post Damage Jump
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have HJB for post technology and post damage jump as follows

.. math::

   \begin{aligned}
   0= & \max_{i^k}\min_{{h^k}} \left(\frac{\delta}{1-\rho}\right)\left[\left(\frac{\alpha k -i^k}{\exp (\tilde{v}(\tilde{x}(\tilde{z}), \tilde{z}))} \right)^{1-\rho}-1\right] \\
   & +\frac{d \tilde{v}(\tilde{x}(\tilde{z}), \tilde{z})}{d \log k}\left[\mu_k+\frac{i^k}{k}-\frac{\kappa}{2} \left(\frac{i^k}{k}\right)^2-\frac{\left|\sigma_k\right|^2}{2}+\sigma_k {h^k}\right]+\frac{d^2 \tilde{v}(\tilde{x}(\tilde{z}), \tilde{z})}{d \log k^2} \frac{\left|\sigma_k\right|^2}{2} \\
   & +\xi^k \frac{\left|{h^k}\right|^2}{2}
   \end{aligned}

where :math:`\tilde{z} \in \{(1,1), (1,2), \ldots, (1,L_n)\}`

6.1.2 Post Technology and Pre Damage Jump
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have HJB for post technology and post damage jump as follows

.. math::

   \begin{aligned}
   0= & \max_{i^k}\min_{{h^k}} \left(\frac{\delta}{1-\rho}\right)\left[\left(\frac{\alpha k -i^k}{\exp (\tilde{v}(\tilde{x}(\tilde{z}), \tilde{z}))} \right)^{1-\rho}-1\right] \\
   & +\frac{d \tilde{v}(\tilde{x}(\tilde{z}), \tilde{z})}{d \log k}\left[\mu_k+\frac{i^k}{k}-\frac{\kappa}{2} \left(\frac{i^k}{k}\right)^2-\frac{\left|\sigma_k\right|^2}{2}+\sigma_k {h^k}\right]+\frac{d^2 \tilde{v}(\tilde{x}(\tilde{z}), \tilde{z})}{d \log k^2} \frac{\left|\sigma_k\right|^2}{2} \\
   & +\xi^k \frac{\left|{h^k}\right|^2}{2}
   \end{aligned}

where :math:`\tilde{z} \in \{(1,0)\}`

6.2 Pre technology Jump
-----------------------

6.2.1 Pre Technology and Post Damage Jump
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The solution has a quasi-analytical simplification of the form

.. math::


   \tilde{V}\left(X_t, Z_t\right)=\tilde{v}\left(X_t^1, Z_t\right)-\log N

After plugging this simplification into our HJB equation and removing
common terms, we are left with the following simplified HJB to solve:

.. math::

   \begin{aligned}
   & 0=\max_{i^k, i^r, e} \min_{{h^k}, {h^y}, {h^r}, g} \left(\frac{\delta}{1-\rho}\right)\left[\left(\frac{\alpha k -i^k-i^r-\alpha k \phi_0(z)\left[1-\frac{e}{\beta_t \alpha k }\right]^{\phi_1}}{\exp (\tilde{v})} \right)^{1-\rho}-1\right] \\
   & +\frac{\partial \tilde{v}}{\partial \log k}\left[\mu_k+i^k-\frac{\kappa}{2} \left(i^k\right)^2-\frac{\left|\sigma_k\right|^2}{2}+\sigma_k {h^k}\right]+\frac{\partial^2 \tilde{v}(\tilde{x}(\tilde{z}), \tilde{z})}{\partial \log k^2} \frac{\left|\sigma_k\right|^2}{2} \\
   & +\frac{\partial \tilde{v}}{\partial y}\left(\frac{1}{L_y} \sum_{\ell=1}^{L_y} q(\ell \mid x,z) \theta(\ell)+\varsigma {h^y}\right) e+\frac{\partial^2 \tilde{v}}{\partial y^2} \frac{|\varsigma|^2}{2} e^2 \\
   & -\left(\left[\lambda_1+\lambda_2 y+\lambda_3(y-\bar{y})\right]\left(\frac{1}{L_y} \sum_\ell^{L_y} q(\ell \mid x,z) \theta(\ell)+\varsigma {h^y}\right) e+\left(\lambda_2+\lambda_3\right) \frac{|\varsigma|^2}{2} e^2\right) \\
   & +\frac{\partial \tilde{v}}{\partial \log r}\left(-\zeta+\psi_0\left(i^r\right)^{\psi_1} \exp \left(-\psi_1 \log r\right)-\frac{\left|\sigma_r\right|^2}{2}+\sigma_r {h^r}\right)+\frac{\partial^2 \tilde{v}}{\partial \log r^2}\frac{\left|\sigma_r\right|^2}{2} \\
   & +\xi^g \mathcal{J}_g(r)(1-g(\tilde{z} \mid x, z)+g(\tilde{z} \mid x, z) \log g(\tilde{z} \mid x, z))+\mathcal{J}_g(r) g(\tilde{z} \mid x, z)\left(\tilde{v}(\tilde{x}(\hat{z}), \hat{z})-\tilde{v}\right) \\
   & +\xi^k \frac{\left|{h^k}\right|^2}{2}+\xi^c \frac{\left|{h^y}\right|^2}{2}+\xi^r \frac{\left|{h^r}\right|^2}{2}+\chi \frac{1}{L_y} \sum_\ell^{L_y}  q(\ell \mid x,z) \log  q(\ell \mid x,z) \\
   &
   \end{aligned}

where the first component for :math:`\hat{z}` is 1.

6.2.1 Pre Technology and Pre Damage Jump
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We attempt to solve a value function of the form

.. math::


   \hat{V}\left(X_t, Z_t\right)=v\left(X_t^1, Z_t\right)-\log N

.. math::

   \begin{aligned}
   0 & = \max_{i^k, i^r, e} \min_{{h^k}, {h^y}, {h^r}, g, f}\left(\frac{\delta}{1-\rho}\right)\left[\left(\frac{\alpha k-i^k-i^r-\alpha k \phi_0(z)\left[1-\frac{e}{\beta_t \alpha k}\right]^{\phi_1}}{\exp (v)} \right)^{1-\rho}-1\right] \\
   & +\frac{\partial v}{\partial \log k}\left[\mu_k+i^k-\frac{\kappa}{2} \left(i^k\right)^2-\frac{\left|\sigma_k\right|^2}{2}+\sigma_k {h^k}\right]+\frac{\partial^2 v}{\partial \log k^2} \frac{\left|\sigma_k\right|^2}{2} \\
   & +\frac{\partial v}{\partial y}\left(\frac{1}{L_y} \sum_{\ell=1}^{L_y} q(\ell \mid x,z) \theta(\ell)+\varsigma {h^y}\right) e+\frac{\partial^2 v}{\partial y^2} \frac{|\varsigma|^2}{2} e^2 \\
   & -\left(\left[\lambda_1+\lambda_2 y\right]\left(\frac{1}{L_y} \sum_{\ell=1}^{L_y} q(\ell \mid x,z) \theta(\ell)+\varsigma {h^y}\right) e+\lambda_2 \frac{|\varsigma|^2}{2} e^2\right) \\
   & +\frac{\partial v}{\partial \log r}\left(-\zeta+\psi_0\left(i^r\right)^{\psi_1} \exp \left(-\psi_1 \log r\right)-\frac{\left|\sigma_r\right|^2}{2}+\sigma_r {h^r}\right)+\frac{\partial^2 v}{\partial \log r^2} \frac{\left|\sigma_r\right|^2}{2} \\
   & +\xi^g \mathcal{J}_g(r)(1-g(\tilde{z} \mid x, z)+g(\tilde{z} \mid x, z) \log g(\tilde{z} \mid x, z))+\mathcal{J}_g(r) g(\tilde{z} \mid x, z)\left(\tilde{v}(\tilde{x}(\tilde{z}), \tilde{z})-v\right) \\
   & +\xi^d \mathcal{J}_n(y) \sum_{\tilde{z} \in \mathcal{Z}} \pi(\tilde{z} \mid x, z)(1-f(\tilde{z} \mid x, z)+f(\tilde{z} \mid x, z) \log f(\tilde{z} \mid x, z)) \\
   & +\mathcal{J}_n(y) \sum_{\tilde{z} \in \mathcal{Z}} \pi(\tilde{z} \mid x, z) f(\tilde{z} \mid x, z)\left(\tilde{v}(\tilde{x}(\tilde{z}), \tilde{z})-v\right) \\
   & +\xi^k \frac{\left|{h^k}\right|^2}{2}+\xi^c \frac{\left|{h^y}\right|^2}{2}+\xi^r \frac{\left|{h^r}\right|^2}{2}+\chi \frac{1}{L_y} \sum_{\ell=1}^{L_y} q(\ell \mid x,z) \log q(\ell \mid x,z)
   \end{aligned}


