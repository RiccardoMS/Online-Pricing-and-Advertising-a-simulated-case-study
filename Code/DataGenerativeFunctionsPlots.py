import matplotlib.pyplot as plt

from DataGenerativeFunctions import *
from DataParameters import *
from MC_Estimation_Stochastic_Aggregate_Distributions import *

import matplotlib.pyplot as plt

from DataGenerativeFunctions import *
from DataParameters import *
from MC_Estimation_Stochastic_Aggregate_Distributions import *

# Marginal Revnue: Fixed Cost, Fixed Percentage, Scaling Margin
plt.figure(0)
plt.xlim([14.5, 25.5])
plt.plot(prices, margin, 'o', color='#0f9b8e')
plt.plot(prices, margin1, 'o', color='#7bc8f6')
plt.plot(prices, margin2, 'o', color='#005249')
plt.legend(['Candidate: Fixed cost percentage', 'Candidate: Fixed cost', 'Chosen margin: Scaling margin'])
plt.plot(np.linspace(15, 25, num=1000), [x - 5 - 0.3 * x for x in np.linspace(15, 25, num=1000)], '-', color='#0f9b8e')
plt.plot(np.linspace(15, 25, num=1000), [x - 5 - 5 for x in np.linspace(15, 25, num=1000)], '-', color='#7bc8f6')
plt.plot(np.linspace(15, 25, num=1000), [x - 5 - (1.5 * x / 100) * x for x in np.linspace(15, 25, num=1000)], '-', color='#005249')
plt.xlabel('Price')
plt.ylabel('Marginal Revenue')
plt.show()

# Conversion Rates
# Linear interpolation
plt.figure(1)
plt.plot(prices, C1['conversion rate'], 'o-', color='#fb7d07')
plt.plot(prices, C2['conversion rate'], 'o-', color='#5ca904')
plt.plot(prices, C3['conversion rate'], 'o-', color='#069af3')
plt.plot(prices, aggregate['conversion rate'], 'o-', color='#ca0147')
plt.legend(['C1 : Low Needs', 'C2 : High Needs', 'C3 : Very High Needs', 'Aggregate'])
plt.xlabel('Price')
plt.ylabel('Conversion Rate')
plt.ylim([0, 1])
plt.show()

# Smoothed Functions
fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(x, y1, 'o', color='#fb7d07')
ax[0, 0].plot(xx, Cr_1(xx), '-', color='#fb7d07')
ax[0, 0].legend(['Class 1'])
ax[0, 0].set_xlim([15, 25])
ax[0, 0].set_ylim([0, 1])
# ax[0, 0].set_xlabel('Price')
ax[0, 0].set_ylabel('Conversion Rate')
ax[0, 1].plot(x, y2, 'o', color='#5ca904')
ax[0, 1].plot(xx, Cr_2(xx), '-', color='#5ca904')
ax[0, 1].legend(['Class 2'])
ax[0, 1].set_xlim([15, 25])
ax[0, 1].set_ylim([0, 1])
# ax[0, 1].set_xlabel('Price')
# ax[0, 1].set_ylabel('Conversion Rate')
ax[1, 0].plot(x, y3, 'o', color='#069af3')
ax[1, 0].plot(xx, Cr_3(xx), '-', color='#069af3')
ax[1, 0].legend(['Class 3'])
ax[1, 0].set_xlim([15, 25])
ax[1, 0].set_ylim([0, 1])
ax[1, 0].set_xlabel('Price')
ax[1, 0].set_ylabel('Conversion Rate')
ax[1, 1].plot(x, ya, 'o', color='#ca0147')
ax[1, 1].plot(xx, Cr_a(xx), '-', color='#ca0147')
ax[1, 1].plot(xx, Cr_1(xx), '-', color='#fb7d07', alpha=0.3)
ax[1, 1].plot(xx, Cr_2(xx), '-', color='#5ca904', alpha=0.3)
ax[1, 1].plot(xx, Cr_3(xx), '-', color='#069af3', alpha=0.3)
ax[1, 1].legend(['Aggregate'])
ax[1, 1].set_xlim([15, 25])
ax[1, 1].set_ylim([0, 1])
ax[1, 1].set_xlabel('Price')
# ax[1, 1].set_ylabel('Conversion Rate')
plt.suptitle('Conversion Rate Functions ')
plt.show()

# Return probs distribution
times = np.array([0, 1, 2, 3])
fig, ax = plt.subplots(2, 2)
ax[0, 0].bar(times, r_1.pmf(times), color='#fb7d07')
ax[0, 0].set_ylim(0, 1)
ax[0, 0].legend(['Class 1'])
# ax[0, 0].set_xlabel('Times')
ax[0, 0].set_ylabel('Probability')
ax[0, 1].bar(times, r_2.pmf(times), color='#5ca904')
ax[0, 1].set_ylim(0, 1)
ax[0, 1].legend(['Class 2'])
# ax[0, 1].set_xlabel('Times')
# ax[0, 1].set_ylabel('Probability')
ax[1, 0].bar(times, r_3.pmf(times), color='#069af3')
ax[1, 0].set_ylim(0, 1)
ax[1, 0].legend(['Class 3'])
ax[1, 0].set_xlabel('Times')
ax[1, 0].set_ylabel('Probability')
ax[1, 1].bar(times, r_a.pmf(times), color='#ca0147')
ax[1, 1].set_ylim(0, 1)
ax[1, 1].legend(['Aggregate'])
ax[1, 1].set_xlabel('Times')
# ax[1, 1].set_ylabel('Probability')
fig.suptitle("Customer Loyalty")
plt.show()

# Cost Per click Functions
y_cpc_a = np.zeros(len(bb_cpc))
std_cpc_a = np.zeros(len(bb_cpc))
for i in range(len(bb_cpc)):
    y_cpc_a[i] = cpc_a_MC(bb_cpc[i])
    std_cpc_a[i] = cpc_a_std_MC(bb_cpc[i])
fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(bb_cpc, cpc_1(bb_cpc), color='#fb7d07')
ax[0, 0].set_ylim(-0.02, 3)
ax[0, 0].legend(['Class 1'])
ax[0, 0].fill_between(bb_cpc, cpc_1(bb_cpc) - C1['CPC'][2] - C1['CPC'][2],
                      cpc_1(bb_cpc) + C1['CPC'][2] + C1['CPC'][2], color='#fb7d07', alpha=0.2)
ax[0, 0].fill_between(bb_cpc, np.repeat([-0.01], len(bb_cpc)), np.repeat([-0.02], len(bb_cpc)), color='w', alpha=1)
ax[0, 0].plot(b_cpc, Cpc_1(b_cpc), 'o', color='#fb7d07')
# ax[0, 0].set_xlabel('Bid')
ax[0, 0].set_ylabel('Cost per Click')
ax[0, 1].plot(bb_cpc, cpc_2(bb_cpc), color='#5ca904')
ax[0, 1].set_ylim(-0.02, 3)
ax[0, 1].legend(['Class 2'])
ax[0, 1].fill_between(bb_cpc, cpc_2(bb_cpc) - C2['CPC'][2] - C2['CPC'][2],
                      cpc_2(bb_cpc) + C2['CPC'][2] + C2['CPC'][2], color='#5ca904', alpha=0.2)
ax[0, 1].fill_between(bb_cpc, np.repeat([-0.01], len(bb_cpc)), np.repeat([-0.02], len(bb_cpc)), color='w', alpha=1)
ax[0, 1].plot(b_cpc, Cpc_2(b_cpc), 'o', color='#5ca904')
# ax[0, 1].set_xlabel('Bid')
ax[0, 1].set_ylabel('Cost per Click')
ax[1, 0].plot(bb_cpc, cpc_3(bb_cpc), color='#069af3')
ax[1, 0].set_ylim(-0.02, 3)
ax[1, 0].legend(['Class 3'])
ax[1, 0].fill_between(bb_cpc, cpc_3(bb_cpc) - C3['CPC'][2] - C3['CPC'][2],
                      cpc_3(bb_cpc) + C3['CPC'][2] + C3['CPC'][2], color='#069af3', alpha=0.2)
ax[1, 0].fill_between(bb_cpc, np.repeat([-0.01], len(bb_cpc)), np.repeat([-0.02], len(bb_cpc)), color='w', alpha=1)
ax[1, 0].plot(b_cpc, Cpc_3(b_cpc), 'o', color='#069af3')
ax[1, 0].set_xlabel('Bid')
ax[1, 0].set_ylabel('Cost per Click')
ax[1, 1].plot(bb_cpc, y_cpc_a, color='#ca0147')
ax[1, 1].set_ylim(-0.02, 3)
ax[1, 1].legend(['Aggregate'])
ax[1, 1].plot(b_cpc, Cpc_a(b_cpc), 'o', color='#ca0147')
ax[1, 1].set_xlabel('Bid')
ax[1, 1].set_ylabel('Cost per Click')
ax[1, 1].fill_between(bb_cpc, y_cpc_a - 2 * std_cpc_a,
                      y_cpc_a + 2 * std_cpc_a, color='#ca0147', alpha=0.2)
ax[1, 1].fill_between(bb_cpc, np.repeat([-0.01], len(bb_cpc)), np.repeat([-0.02], len(bb_cpc)), color='w', alpha=1)
fig.suptitle('Cost per Click Stochastic Functions')
plt.show()

# Number of Daily Clicks Functions
y_ndc_a = np.zeros(len(bb_ndc))
std_ndc_a = np.zeros(len(bb_ndc))
for i in range(len(bb_ndc)):
    y_ndc_a[i] = ndc_a_MC(bb_ndc[i])
    std_ndc_a[i] = ndc_a_std_MC(bb_ndc[i])
fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(bb_ndc, ndc_1(bb_ndc), color='#fb7d07')
ax[0, 0].set_ylim(-0.1, 200)
ax[0, 0].legend(['Class 1'])
ax[0, 0].fill_between(bb_ndc, ndc_1(bb_ndc) - C1['NNC'][2] - C1['NNC'][2],
                      ndc_1(bb_ndc) + C1['NNC'][2] + C1['NNC'][2], color='#fb7d07', alpha=0.2)
ax[0, 0].plot(b_ndc, Ndc_1(b_ndc), 'o', color='#fb7d07')
# ax[0, 0].set_xlabel('Bid')
ax[0, 0].set_ylabel('Daily Clicks of New Users')
ax[0, 1].plot(bb_ndc, ndc_2(bb_ndc), color='#5ca904')
ax[0, 1].set_ylim(-0.1, 200)
ax[0, 1].legend(['Class 2'])
ax[0, 1].fill_between(bb_ndc, ndc_2(bb_ndc) - C2['NNC'][2] - C2['NNC'][2],
                      ndc_2(bb_ndc) + C2['NNC'][2] + C2['NNC'][2], color='#5ca904', alpha=0.2)
ax[0, 1].plot(b_ndc, Ndc_2(b_ndc), 'o', color='#5ca904')
# ax[0, 1].set_xlabel('Bid')
# ax[0, 1].set_ylabel('Daily Clicks of New Users')
ax[1, 0].plot(bb_ndc, ndc_3(bb_ndc), color='#069af3')
ax[1, 0].set_ylim(-0.1, 200)
ax[1, 0].legend(['Class 3'])
ax[1, 0].fill_between(bb_ndc, ndc_3(bb_ndc) - C3['NNC'][2] - C3['NNC'][2],
                      ndc_3(bb_ndc) + C3['NNC'][2] + C3['NNC'][2], color='#069af3', alpha=0.2)
ax[1, 0].plot(b_ndc, Ndc_3(b_ndc), 'o', color='#069af3')
ax[1, 0].set_xlabel('Bid')
ax[1, 0].set_ylabel('Daily Clicks of New Users')
ax[1, 1].plot(bb_ndc, y_ndc_a, color='#ca0147')
ax[1, 1].set_ylim(-0.1, 200)
ax[1, 1].legend(['Aggregate'])
ax[1, 1].plot(b_ndc, Ndc_a(b_ndc), 'o', color='#ca0147')
ax[1, 1].fill_between(bb_ndc, y_ndc_a - 2 * std_ndc_a,
                      y_ndc_a + 2 * std_ndc_a, color='#ca0147', alpha=0.2)
ax[1, 1].set_xlabel('Bid')
# ax[1, 1].set_ylabel('Daily Clicks of New Users')
fig.suptitle('Daily Clicks of New Users Stochastic Functions')
plt.show()