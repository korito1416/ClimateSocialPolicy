16.1 Value Decomposition
------------------------

We interpret the partial derivative of the value function with respect
to the R&D knowledge state as an asset price. As such, it has four
payoff contributions as we have derived previously:

1. :math:`\delta m \cdot \frac{\partial U}{\partial x}`;
2. :math:`m \cdot \sum_{\ell=1}^L \frac{\partial {\mathcal J}^\ell}{\partial x} g^{\ell*} (V^\ell - V)`;
3. :math:`m \cdot \sum_{\ell=1}^L {\mathcal J}^\ell g^{\ell*} \frac{\partial V^\ell}{\partial x}`;
4. :math:`\xi m \cdot \sum_{\ell=1}^L \frac{\partial {\mathcal J}^\ell}{\partial x} (1 - g^{\ell*} + g^{\ell*} \log g^{\ell*})`.

Terms ii) and iv) simplify further because
:math:`\frac{\partial {\mathcal J}^\ell}{\partial r} = 0` except for
:math:`\ell = L`, which is the technology jump. Term iii) has a
**direct** contribution coming from

.. math::


   \sum_{\ell=1}^{L-1} {\mathcal J}^\ell g^{\ell*} \frac{\partial V^\ell}{\partial {\hat r}}.

Note that the continuation value function :math:`V^L` does not depend on
the R&D stock because it conditions on the R&D success.

Term iii) also has indirect contributions because a marginal change in
the initial stock of R&D induces marginal changes in the other state
variables. While the continuation values :math:`V^{\ell}` for
:math:`\ell = 1,2,\dots, L-1` do not depend on the pre-jump temperature,
term iii) includes contributions from the damage jumps as these will
depend on the knowledge stock along with the other state variables.

Term iv) reflects the reduction in the uncertainty challenges associated
with a technology jump. These four contributions to the marginal values
add up to the total. In the computations that follow, we measure them
separately. In addition, we will split the contribution to iii) coming
from the damage curve realization jumps (:math:`\ell = 1,\dots,L-1`) and
the technology discovery jump (:math:`\ell = L`).

We also consider four different configurations of uncertainty aversion
as a way to assess the different economic forces in play:

1. pre-jump neutrality - post-jump neutrality;
2. pre-jump neutrality - post-jump aversion;
3. pre-jump aversion - post-jump neutrality;
4. pre-jump aversion - post-jump aversion.

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

The results are reported in Table below.

+-------------------------+----+----+-------+-------+-----+-------+
| Case                    | i  | ii | ii    | ii    | iv  | sum   |
|                         |    |    | i(dc) | i(td) |     |       |
+=========================+====+====+=======+=======+=====+=======+
| pre neutrality          |    |    |       |       |     |       |
+-------------------------+----+----+-------+-------+-----+-------+
| a) post neutrality      | 0  | 0  | 0.    | 0.    | 0   | 0.    |
|                         | .0 | .0 | 01356 | 00173 | .00 | 03003 |
|                         | 01 | 12 |       |       | 000 |       |
|                         | 86 | 87 |       |       |     |       |
+-------------------------+----+----+-------+-------+-----+-------+
| b) post aversion        | 0  | 0  | 0.    | 0.    | 0   | 0.    |
|                         | .0 | .0 | 01570 | 00264 | .00 | 03705 |
|                         | 02 | 16 |       |       | 000 |       |
|                         | 61 | 10 |       |       |     |       |
+-------------------------+----+----+-------+-------+-----+-------+
| pre aversion            |    |    |       |       |     |       |
+-------------------------+----+----+-------+-------+-----+-------+
| c) post neutrality      | 0  | 0  | 0.    | 0.    | 0   | 0.    |
|                         | .0 | .0 | 01598 | 00124 | .00 | 03113 |
|                         | 01 | 09 |       |       | 241 |       |
|                         | 90 | 60 |       |       |     |       |
+-------------------------+----+----+-------+-------+-----+-------+
| d) post aversion        | 0  | 0  | 0.    | 0.    | 0   | 0.    |
|                         | .0 | .0 | 01999 | 00177 | .00 | 03962 |
|                         | 02 | 11 |       |       | 387 |       |
|                         | 72 | 04 |       |       |     |       |
+-------------------------+----+----+-------+-------+-----+-------+

Table: Components to the partial derivative of the value function with respect to the R&D state variable. The column iii(dc) includes only the contributions from the damage curve realization jumps to iii, and iii(td) includes the remaining contribution from the technology discovery jump to iii.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The partial derivative decomposition in the table reveals the following:

-  The totals for pre aversion-post aversion (0.040) are very close to
   pre neutrality-post aversion (0.037).
-  The continuation value contributions ii) and iii) are larger for pre
   neutrality-post aversion than for pre neutrality-post neutrality, as
   might be expected.
-  The continuation value contribution iii) is primarily due to the
   damage jumps and not to the technology jump.
-  The total for pre aversion-post neutrality (0.031) is only slightly
   larger than for pre neutrality-post neutrality (0.030). The
   difference is more than offset by the relative entropy contribution
   to the pre neutrality-post aversion total.

In terms of the fourth observation, when we net out the entropy
contribution, the pre-jump uncertainty contribution reduces the marginal
valuation because of the more pessimistic view of the success of R&D.
This reduction turns out to be quite small, however. Perhaps this small
magnitude should be anticipated because of our very low subjective
discount rate. For instance, by driving the discount rate to zero, we
make the timing of the success less relevant in decision-making.

16.2 Expected Marginal Social Payoffs for Alternative Horizons
--------------------------------------------------------------

As we demonstrated, the derivative of the value function has the
interpretation as a stochastically discounted social cash flow, with the
four contributions given at the outset of Section 3.3. The “stochastic
discount factor” includes the vector of stochastic impulse responses,
the process :math:`M`, along with the subjective rate of discount,
:math:`\delta`. The following figure shows the period-by-period
contribution for each of the four components.

Both of the continuation value contributions to the social cash flow,
terms ii) and iii), are important contributors to the marginal value of
R&D, but there are substantial differences in their horizon dependence.
Term ii) has an important initial contribution that then gradually
vanishes so that by a thirty-year horizon it is between one fourth and a
third of its initial impact, depending on the uncertainty configuration.
In contrast, term iii) is initially very small but has a substantial
peak effect by year thirty. Both contributions are enhanced by post-jump
uncertainty aversion. Its impact on marginal valuation remains important
well past a horizon of forty years, reflecting the long-term nature of
the valuation. The direct marginal utility contribution, term i), is
small across all horizons, although it does increase up to twenty years.
The entropy contribution, term iv), is also relatively minor across all
horizons and uncertainty aversion configurations, though the initial
magnitude is augmented by pre-jump uncertainty aversion, and this effect
persists out to thirty years.

In summary, the more skeptical assessment of R&D prospects prior to a
jump induces only a quantitatively minor adverse impact on the incentive
for R&D investment. A possible R&D success, however, gives a
quantitatively important incentive for more R&D investment. While these
quantitative results are special and tied to our model calibration,
these competing forces are likely to be in play in more general
circumstances.

Remark
~~~~~~

Recall that this is “big project” R&D analogous perhaps to the Manhattan
Project or the Apollo program, with uncertainty in the R&D investment
only about the timing of a successful outcome or social payoff. For the
reasons we have discussed, more R&D leads to an increased likelihood
that the new, clean technology will be discovered sooner, even though
the uncertainty in the technology may be greater. This increase in a
more uncertain investment stands in contrast to a standard portfolio
allocation problem with riskless and uncertain investment alternatives.
In this latter problem, an enhanced concern about uncertainty leads to a
reduction in the portfolio weight associated with the uncertain
investment.


