4 Value Decomposition
=====================

There are two steps to do value decomposition:

1. `Simulate <https://github.com/korito1416/two-capital-climate-change/blob/main/python/FeymannKacs_simulate.py>`__
   state variable processes and first variation processes.

2. Calculated four terms of discounted social cash flow.

4.1 Simulate First Variational Process and State Variables
----------------------------------------------------------

`FeymannKacs_simulate.py <https://github.com/korito1416/two-capital-climate-change/blob/306b1c5ee51eb6ad24e6267fe0d2b82ad5286e98/python/FeymannKacs_simulate.py#L193>`__
simulates the first variational process and state variables of
pre-tech-pre-damage case.

| The first variational process and distorted state variable process are
| 

  .. math::

      
     M_t=
      \begin{bmatrix} 
      M_t^{ \log \tilde{ {K}}} \cr  
      M_t^{\tilde{Y}} \cr  
      M_t^{\log\tilde{{R}}} \cr  
      M_t^{\log\tilde{{N}}}  
     \end{bmatrix},\quad
     \tilde{X}_t=
      \begin{bmatrix} 
      \log \tilde{ {K}}_t \cr  
      \tilde{Y}_t \cr  
      \log\tilde{{R}}_t \cr  
      \log\tilde{{N}}_t  
     \end{bmatrix}

  For notation clarification, we using $:raw-latex:`\log{K}` $ instead
  of $:raw-latex:`\hat{K}` $ in this section.

To simulate the first variational process with respect to technology, we
set the initial value of :math:`M_t` to be :math:`[0,0,1,0]'`, and
:math:`\tilde{X}_t` to be
:math:`[log(\frac{85}{0.115}), 1.1, log(11.2),1.1 \gamma_1  + 0.5\times 1.1^2\gamma_2 ]'`.
Initial values are set in code line
`905 <https://github.com/korito1416/two-capital-climate-change/blob/306b1c5ee51eb6ad24e6267fe0d2b82ad5286e98/python/FeymannKacs_simulate.py#L905>`__.

We use :math:`M^{\log \tilde{ {K}}_t}` as an example and others are the
same. The implied evolution of the process
:math:`M^{\log \tilde{ {K}}_t}` is given by

.. math:: dM_{t}^{\log \tilde{ {K}}_t} = \left(M_t\right)'\frac{\partial \mu_{\log \tilde{ {K}}_t}}{\partial \tilde{x}}(\tilde{X}_t) dt + \left({M_t}\right)'\frac{\partial \sigma_{\log \tilde{ {K}}_t}}{\partial \tilde{x}}(\tilde{X}_t) dW_t

, where :math:`\tilde{X}_t` are distorted state variables.

Recall that the distorted Capital evoluation is

.. math:: d \log \tilde{ K}_t =   \left( - \mu_k    + \frac {I_{t}^k}{\tilde{K}_t}  -{\frac { \kappa} 2} \left( {\frac {I_{t} ^k} {\tilde{K}_t}} \right)^2  + h_{\tilde{K}} + \frac{\sigma_k^2}{2} \right) dt +  \sigma_k  dW_t

where :math:`\sigma_{\log \tilde{ {K}}_t} = \sigma_k` and
:math:`\mu_{\log \tilde{ {K}}_t}`

.. math:: \mu_{\log \tilde{ {K}}_t} = - \mu_k    + \frac {I_{t}^k}{\tilde{K}_t}  -{\frac { \kappa} 2} \left( {\frac {I_{t} ^k} {\tilde{K}_t}} \right)^2  + h_{\tilde{K}} + \frac{\sigma_k^2}{2}

.. math::

    \frac{\partial \mu_{\log \tilde{ {K}}_t}}{\partial \tilde{x}} =
    \begin{bmatrix} 
    \frac{\partial \mu_{\log \tilde{ {K}}_t}}{\partial \log \tilde{ {K}}_t}\cr  
    \frac{\partial \mu_{\log \tilde{ {K}}_t}}{\partial \tilde{Y}_t } \cr  
   \frac{\partial \mu_{\log \tilde{ {K}}_t}}{\partial \log\tilde{{R}}_t} \cr  
   \frac{\partial \mu_{\log \tilde{ {K}}_t}}{\partial \log\tilde{{N}}_t} 
   \end{bmatrix}, \quad
   \frac{\partial \sigma_{\log \tilde{ {K}}_t}}{\partial \tilde{x}} = 0
     

Here we use `finite difference
method <https://github.com/korito1416/two-capital-climate-change/blob/306b1c5ee51eb6ad24e6267fe0d2b82ad5286e98/python/FeymannKacs_simulate.py#L354>`__
to calculate the derivatives with respect to state variables and the
`interpolate <https://github.com/korito1416/two-capital-climate-change/blob/306b1c5ee51eb6ad24e6267fe0d2b82ad5286e98/python/FeymannKacs_simulate.py#L397>`__
to get partial derivatives at every point.



The derivative we need to calculate is

.. math::  \frac{\partial \mu_i}{\partial x}(x) ,    \frac{\partial \sigma_i}{\partial x}(x) , \frac{\partial V}{\partial x}(x)  ,V^\ell_x(X_t) , U_x(X_t) , {\mathcal J}^{\ell}_x(X_t)  

.. math::


   Dis_t = \exp\left( - \int_0^t \left[\delta +  \sum_{\ell=1}^{L}  {\mathcal J}^{\ell}(X_u)   \right]du \right)

Then we start the for
`loop <https://github.com/korito1416/two-capital-climate-change/blob/306b1c5ee51eb6ad24e6267fe0d2b82ad5286e98/python/FeymannKacs_simulate.py#L727>`__
from time 0 to recursively get four discounted term.

We primarily use above code to get the value decomposition results. In
each iteraton step, we store calculate every term used in value
decomposition. Alternative way is to get the entire simulated state
variable and first variational path and then calculate remaining terms.
We can use our generalized code for state varibable and impulse response
simulation.

**The output variables are** In each simulated path, we can get state
variabls and controls with first variational process

.. math::

   \begin{align*}
      \{ \hat{k}_t, y_t, \hat{r}_t , \hat{n}_t\},  \{i^k,i^r,\mathcal{E}_t\},\{M_t\},
   \end{align*}

and other variables that we use to do value decomposition.

.. math::

   \begin{align*}
     \{g^{\ell } ,f^{L } \},\{    \mathcal{J}^{\ell}  ,\mathcal{J}^{L}  ,
       {\mathcal J}^{L}_{\hat{r} }\}
   \end{align*}

4.2 Value Decomposition
-----------------------

We interpret the partial derivative of the value function with respect
to the R&D knowledge state as an asset price. As such, it has four
payoff contributions as we have derived previously:

1. :math:`\delta m \cdot \frac{\partial U}{\partial x}`;
2. :math:`m \cdot \sum_{\ell=1}^L \frac{\partial {\mathcal J}^\ell}{\partial x} g^{\ell*} (V^\ell - V)`;
3. :math:`m \cdot \sum_{\ell=1}^L {\mathcal J}^\ell g^{\ell*} \frac{\partial V^\ell}{\partial x}`;
4. :math:`\xi m \cdot \sum_{\ell=1}^L \frac{\partial {\mathcal J}^\ell}{\partial x} (1 - g^{\ell*} + g^{\ell*} \log g^{\ell*})`.

We also consider four different configurations of uncertainty aversion
as a way to assess the different economic forces in play:

-  

   a. pre-jump neutrality - post-jump neutrality;

-  

   b. pre-jump neutrality - post-jump aversion;

-  

   c. pre-jump aversion - post-jump neutrality;

-  

   d. pre-jump aversion - post-jump aversion.

We include cases b) and c) because they provide revealing intermediate
cases that help understand the overall uncertainty implications. For
instance, there are two forces in play. First, uncertainty about when
the new technology will be realized would seem to make investment in R&D
less attractive. Second, the positive implications for a technological
success can be stronger when there is more aversion to this uncertainty.
Intermediate case c) allows us to feature more the first force, while
intermediate case b) shifts attention to the second force. With these
intermediate cases, we can better assess the quantitative magnitude of
these offsetting forces.

4.3 Expected Marginal Social Payoffs for Alternative Horizons
-------------------------------------------------------------

As we demonstrated, the derivative of the value function has the
interpretation as a stochastically discounted social cash flow, with the
four contributions given at the outset of Section 3.3. The “stochastic
discount factor” includes the vector of stochastic impulse responses,
the process :math:`M`, along with the subjective rate of discount,
:math:`\delta`. The following figure shows the period-by-period
contribution for each of the four components.

Horizon decomposition of social cash flow contributions to the R&D stock
valuation. The four panels correspond to different uncertainty aversion
configurations: Panel A is the pre neutrality-post aversion
configuration; Panel B is the pre aversion-post neutrality
configuration; Panel C is the pre aversion-post aversion configuration;
and Panel D is the pre neutrality-post neutrality configuration. The
blue lines correspond to the payoff contribution

i)   :math:`\delta m \cdot \frac{\partial U}{\partial r}`. The green
     lines correspond to the payoff contribution

ii)  :math:`m \cdot \sum_\ell g^{\ell*}\frac{\partial {\mathcal J}^\ell}{\partial r} (V^\ell - V)`.
     The red lines correspond to the payoff contribution

iii) :math:`m\cdot \sum_\ell g^{\ell*}\mathcal J^\ell \frac{\partial V^\ell}{\partial r}`
     . The light blue lines correspond to the payoff contribution

iv)  :math:`\xi m \cdot \sum_\ell \frac{\partial {\mathcal J}^\ell }{\partial r} (1-g^{\ell*} + g^{\ell*} \log g^{\ell*} )`.

.. code:: ipython3

    from pdf2image import convert_from_path
    import matplotlib.pyplot as plt
    
    # List of PDF paths
    pdf_files = [
        'additional/Aversion IntensityPre Neutrality Post Less AversionTechnology0.083_Discount_Term1234_dt2.pdf',
        'additional/Aversion IntensityPre Less Aversion Post NeutralityTechnology0.083_Discount_Term1234_dt2.pdf',
        'additional/Aversion IntensityPre Less Aversion Post Less AversionTechnology0.083_Discount_Term1234_dt2.pdf',
        'additional/Aversion IntensityPre Neutrality Post NeutralityTechnology0.083_Discount_Term1234_dt2.pdf'
    ]
    
    # Convert each PDF to image
    images = [convert_from_path(pdf, first_page=0, last_page=1)[0] for pdf in pdf_files]
    
    # Plot the images in a 2x2 grid using matplotlib
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    
    # Display each image in the grid
    captions = [
        'pre neutrality-post aversion', 
        'pre aversion-post neutrality', 
        'pre aversion-post aversion', 
        'pre neutrality-post neutrality'
    ]
    
    for i, ax in enumerate(axs.flatten()):
        ax.imshow(images[i])
        ax.axis('off')  # Turn off axis
        ax.set_title(captions[i])
    
    # Adjust layout for spacing between images and titles
    plt.tight_layout()
    plt.show()




.. image:: sec4_value_decomposition_files/sec4_value_decomposition_20_0.png

