import plotly.io as pio
import plotly.offline as pyo
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go 
import os
import sys
import pickle
import plotly.express as px
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.getcwd()))
pyo.init_notebook_mode()
pio.templates.default = "none"

theta_list = pd.read_csv('data/model144.csv', header=None).to_numpy()[:, 0] / 1000.
gamma_3_list = np.linspace(0, 1./3, 20)
xi_list_fullaversion_low = [0.025, 0.050, 10000.]
xi_list_fullaversion_high = [0.075, 0.150, 10000.]
xi_list_uncertainty_low = [0.050]
xi_list_uncertainty_high = [0.150]

alpha=0.115

def plot_hist(graph_title):
    fig = go.Figure()
    theta_list = pd.read_csv('./data/model144.csv',
                         header=None).to_numpy()[:, 0] / 1000.
    trace_base = go.Histogram(
        x=theta_list * 1000,
        histnorm='probability density',
        marker=dict(color="red", line=dict(color='grey', width=1)),
        showlegend=False,
        xbins=dict(size=0.15),
        name='baseline',
        legendgroup=1,
        opacity=0.5,
    )

    fig.add_trace(trace_base)
    # fig.add_trace(trace_worstcase, 1, 1)

    fig.update_layout(
        width=600,
        height=500,
        plot_bgcolor='white',
        title=graph_title
    )

    fig.update_yaxes(
        showline=True,
        showgrid=False,
        linewidth=1,
        linecolor="black",
        title="Density",
        range=[0, 1.5],
    )

    fig.update_xaxes(
        showline=True,
        showgrid=False,
        linewidth=1,
        linecolor='black',
        range=[0.8, 3],
        title=go.layout.xaxis.Title(text="Climate Sensitivity",
                                    font=dict(size=13)),
    )
    return fig


def plot_damage(graph_title):
    fig = go.Figure()
    Y = np.linspace(0., 3., 1000)
    y_underline = 1.5
    y_overline = 2 

    gamma_1 = 0.00017675
    gamma_2 = 2 * 0.0022    
    gamma_3_list = np.linspace(0, 1. / 3, 20)

    y_limits = np.arange(y_underline, y_overline + 0.05, 0.1)
    
    def y_data(y_limit):
        LHS_ylimit = np.zeros((1000,20))
        
    
        i=0
        for gamma_3 in gamma_3_list:
            
            LHS_ylimitlower = gamma_1 * Y + gamma_2/2 * Y**2 # y<y_limit
            LHS_ylimitupper = gamma_1 * Y + gamma_2*y_overline * \
                (Y-y_limit) + (gamma_2+gamma_3)/2 * \
                (Y-y_limit)**2 + gamma_2/2 * y_limit**2
        
            LHS_ylimit[:,i] =LHS_ylimitlower*(Y<y_limit) + LHS_ylimitupper*(Y>y_limit)
            i = i+1
        return LHS_ylimit

    for y_limit in y_limits:
        damages = y_data(y_limit)
        damage_upper = np.max(np.exp(-damages), axis=1)
        damage_lower = np.min(np.exp(-damages), axis=1)
        mean_damage = np.mean(np.exp(-damages), axis=1)

        fig.add_trace(
            go.Scatter(
                x=Y,
                y=damage_lower,
                visible=False,
                showlegend=False,
                line=dict(color="rgba(214,39,40, 0.5)"),
            ))
        fig.add_trace(
            go.Scatter(x=Y,
                       y=damage_upper,
                       fill='tonexty',
                       fillcolor="rgba(214,39,40, 0.3)",
                       visible=False,
                       showlegend=False,
                       line=dict(color="rgba(214,39,40, 0.5)")))
        fig.add_trace(
            go.Scatter(
                x=Y,
                y=mean_damage,
                visible=False,
                showlegend=False,
                line=dict(color='black'),
            ))
        fig.add_trace(
            go.Scatter(
                x=y_limit * np.ones(100),
                y=np.linspace(0.65, 1.01, 100),
                line=dict(color='black', dash="dash"),
                visible=False,
                showlegend=False,
            ))

    for i in range(4):
        fig.data[i].visible = True

    fig.update_layout(
        height=500,
        width=1000,
    )

    steps = []
    for i in range(len(y_limits)):
        # Hide all traces
        label = r'ỹ='+"{:.2f}".format(y_limits[i])
        step = dict(method='update',
                    args=[
                        {
                            'visible': [False] * len(fig.data)
                        },
                    ],
                    label=label)
        # Enable the two traces we want to see
        for j in range(4):
            step['args'][0]["visible"][4 * i + j] = True
        # Add step to step list
        steps.append(step)

    sliders = [
        dict(
            active=0,
            currentvalue={"prefix": 'Jump threshold ', "offset": 20},
            steps=steps,
            pad={"t": 70},
        )
    ]

    fig.update_layout(sliders=sliders, 
                      font=dict(size=13),
                      plot_bgcolor="white",
                      title=graph_title)
    fig.update_xaxes(linecolor='black',
                     range=[0, 3],
                     title_text="Temperature Anomaly",
                     title_font={"size": 13})
    fig.update_yaxes(range=[0.65, 1 + 0.01],
                     showline=True,
                     linecolor="black",
                     title_text="Proportional reduction in economic output",
                     title_font={"size": 13})
    # fig.write_html('fig1.html')
    return fig


def plot_damage2(graph_title):
    fig = go.Figure()
    Y = np.linspace(0., 3., 1000)
    y_underline = 1.5
    y_overline = 2

    gamma_1 = 0.00017675
    gamma_2 = 2 * 0.0022
    gamma_3_list = np.linspace(0, 1. / 3, 20)

    y_limits = np.arange(y_underline, y_overline + 0.05, 0.1)

    def y_data(y_limit):
        LHS_ylimit = np.zeros((1000, 20))

        i = 0
        for gamma_3 in gamma_3_list:

            LHS_ylimitlower = gamma_1 * Y + gamma_2/2 * Y**2  # y<y_limit
            LHS_ylimitupper = gamma_1 * Y + gamma_2*y_underline * \
                (Y-y_limit) + (gamma_2+gamma_3)/2 * \
                (Y-y_limit)**2 + gamma_2/2 * y_limit**2

            LHS_ylimit[:, i] = LHS_ylimitlower * \
                (Y < y_limit) + LHS_ylimitupper*(Y > y_limit)
            i = i+1
        return LHS_ylimit

    for y_limit in y_limits:
        damages = y_data(y_limit)
        damage_upper = np.max(damages, axis=1)
        damage_lower = np.min(damages, axis=1)
        mean_damage = np.mean(damages, axis=1)

        fig.add_trace(
            go.Scatter(
                x=Y,
                y=damage_lower,
                visible=False,
                showlegend=False,
                line=dict(color="rgba(214,39,40, 0.5)"),
            ))
        fig.add_trace(
            go.Scatter(x=Y,
                       y=damage_upper,
                       fill='tonexty',
                       fillcolor="rgba(214,39,40, 0.3)",
                       visible=False,
                       showlegend=False,
                       line=dict(color="rgba(214,39,40, 0.5)")))
        fig.add_trace(
            go.Scatter(
                x=Y,
                y=mean_damage,
                visible=False,
                showlegend=False,
                line=dict(color='black'),
            ))
        fig.add_trace(
            go.Scatter(
                x=y_limit * np.ones(100),
                y=np.linspace(0.65, 1.01, 100),
                line=dict(color='black', dash="dash"),
                visible=False,
                showlegend=False,
            ))

    for i in range(4):
        fig.data[i].visible = True

    fig.update_layout(
        height=500,
        width=1000,
    )

    steps = []
    for i in range(len(y_limits)):
        # Hide all traces
        label = r'ỹ='+"{:.2f}".format(y_limits[i])
        step = dict(method='update',
                    args=[
                        {
                            'visible': [False] * len(fig.data)
                        },
                    ],
                    label=label)
        # Enable the two traces we want to see
        for j in range(4):
            step['args'][0]["visible"][4 * i + j] = True
        # Add step to step list
        steps.append(step)

    sliders = [
        dict(
            active=0,
            currentvalue={"prefix": 'Jump threshold ', "offset": 20},
            steps=steps,
            pad={"t": 70},
        )
    ]

    fig.update_layout(sliders=sliders,
                      font=dict(size=13),
                      plot_bgcolor="white",
                      title=graph_title)
    fig.update_xaxes(linecolor='black',
                     range=[0, 3],
                     title_text="Temperature Anomaly",
                     title_font={"size": 13})
    fig.update_yaxes(range=[0.65, 1 + 0.01],
                     showline=True,
                     linecolor="black",
                     title_text="Proportional reduction in economic output",
                     title_font={"size": 13})
    # fig.write_html('fig1.html')
    return fig





def plot_intensity(graph_title):
    def J(Y, y_underline=1.5):
        r1 = 1.5
        r2 = 2.5
        return r1*(np.exp(r2/2*(Y - y_underline)**2) - 1) * (Y >= y_underline)

    fig = go.Figure(layout=dict(width=800, height=500, plot_bgcolor="white"))
    Y = np.linspace(0., 3., 1000)
    fig.add_trace(go.Scatter(x=Y, y=J(Y), line=dict(color="darkblue")))
    fig.update_layout(title=graph_title)
    fig.update_xaxes(linecolor='black',
                     range=[1, 2.],
                     title_text="Temperature anomaly (ᵒC)",
                     title_font={"size": 13}
                     )
    fig.update_yaxes(
        showline=True,
        linecolor="black",
        range=[-0.01, 1],
        # title_text=r"$\mathcal{J}(y)$",
        title_text=r"J(y)",
        title_font={"size": 13}
    )

    return fig



def plot_climatehist(graph_title):

    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta=0.01
    
    fig = make_subplots(rows=1, cols=2)
    hovertemplate = "%{y:.2f}"


    colors = ["#1f77b4", "navy"]

    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            folder = "./data_simul2/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
                abatement_cost)
            
            if abatement_cost ==0.1:
                
                xi_list = [0.025, 0.050]
                cost_label="φ₀=0.1"
            if abatement_cost ==0.5:
                
                xi_list = [0.075, 0.150]
                cost_label="φ₀=0.5"
            xi_label_list = ["More Aversion", "Less Aversion"]

            for xi_num in range(len(xi_list)):
                    
                xi_label = xi_label_list[xi_num]
                xi = xi_list[xi_num]
                filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(xi_base, xi, xi, xi, xi,xi, psi_0, psi_1, varrho, rho, delta)
                
                with open(folder + filename + "model_tech1_pre_damage_UD_simul_40direct_direct", "rb") as f:
                    model_tech1_pre_damage = pickle.load(f)


                trace = go.Histogram(
                    # histfunc="sum",
                    x=model_tech1_pre_damage["theta_ell_new"][:,-1]*1000,
                    histnorm='probability density',
                    marker=dict(color=colors[xi_num], line=dict(color='grey', width=1)),
                    showlegend=False,
                    visible=False,
                    xbins=dict(size=0.15),
                    name=xi_label_list[xi_num],
                    # legendgroup=xi_num+1,
                    opacity=0.5,
                    hovertemplate=hovertemplate
                )

                fig.add_trace(trace, 1, xi_num+1)

    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            folder = "./data_simul2/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
                abatement_cost)
            
            if abatement_cost ==0.1:
                
                xi_list = [0.025, 0.050]
                cost_label="φ₀=0.1"
            if abatement_cost ==0.5:
                
                xi_list = [0.075, 0.150]
                cost_label="φ₀=0.5"
            xi_label_list = ["More Aversion", "Less Aversion"]

            for xi_num in range(len(xi_list)):
                    
                xi_label = xi_label_list[xi_num]
                xi = xi_list[xi_num]
                filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(xi_base, xi, xi, xi, xi,xi, psi_0, psi_1, varrho, rho, delta)
                
                trace_base = go.Histogram(
                    x=theta_list* 1000,
                    histnorm='probability density',
                    marker=dict(color="#d62728", line=dict(color='grey', width=1)),
                    showlegend=False,
                    visible=False,
                    xbins=dict(size=0.15),
                    name='Baseline',
                    # legendgroup=xi_num+1,
                    opacity=0.5,
                    hovertemplate=hovertemplate
                )   
                fig.add_trace(trace_base, 1, xi_num+1)


    for i in range(2):
        fig.data[2*4 + i]["visible"] = True
        fig.data[2*4 + i+12]["visible"] = True
        
        fig.data[2*4 + i]["showlegend"] = True
        fig.data[2*4 + 12]["showlegend"] = True


    buttons = []
    i=0

    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost ==0.1:
                
                xi_list = [0.025, 0.050]
                cost_label="φ₀=0.1"
            if abatement_cost ==0.5:
                
                xi_list = [0.075, 0.150]
                cost_label="φ₀=0.5"

            # Hide all traces
            label = cost_label+r', ρ' +'= {:.2f}'.format(rho)


            button = dict(method='update',
                        args=[
                            {
                                'visible': [False] * (2 * 3 * 2 *2),
                                'showlegend': [False] * (2 * 3 * 2* 2),
                            },
                        ],
                        label=label)
            # Enable the two traces we want to see
            # print(button['args'][0]["visible"])

            button['args'][0]["visible"][2*i + 0] = True
            button['args'][0]["visible"][2*i + 1] = True
            button['args'][0]["visible"][2*i + 0 +12] = True
            button['args'][0]["visible"][2*i + 1 +12] = True

            button['args'][0]["showlegend"][2*i + 0] = True
            button['args'][0]["showlegend"][2*i + 1] = True
            button['args'][0]["showlegend"][2*i + 0 +12] = True
            # button['args'][0]["showlegend"][2*i + 1 +12] = True
            # print(button['args'][0]["visible"])

            i = i+1
            # Add step to step list
            buttons.append(button)


    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                buttons=buttons,
                # direction="right",
                active=4,
                x=1.25,
                y=0.7,
                # xanchor="left",
                # yanchor="top",
                pad={"r": 10,
                     "t": 10, "b": 10},
                showactive=True
            )
        ])

    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=900,
        height=500,
        margin=dict(l=30, r=0),
        # legend=dict(
        #     orientation="h",
        #     yanchor="top",
        #     y=0.99,
        #     xanchor="left",
        #     x=0.01),
        # legend_tracegroupgap = 1,
        # legend_orientation="h"
         )
    
    fig.update_yaxes(range=[0., 1.5],
                    showline=True,
                    showgrid=False,
                    linecolor="black",
                    linewidth=1,
                    )
    fig.update_xaxes(
        range=[1.0, 3.0],
        showline=True,
        showgrid=False,
        linecolor="black",
        linewidth=1,
        title=go.layout.xaxis.Title(text=r"Climate Sensitivity", font=dict(size=13)),
    )


    return fig


def plot_climatehist_notech(graph_title):

    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01

    # fig = make_subplots(rows=1, cols=2)
    fig = go.Figure()
    hovertemplate = "%{y:.2f}"

    colors = ["#1f77b4", "navy"]

    # for abatement_cost in [0.1, 0.5]:
    #     for rho in [0.66, 1.0, 1.5]:
    abatement_cost = 0.5
    rho  = 1.0

    folder = "./data_simul6/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
        abatement_cost)


    if abatement_cost == 0.5:

        xi_list = [0.075, 0.150]
        cost_label = "φ₀=0.5"
    xi_label_list = ["More Aversion", "Less Aversion"]

    # for xi_num in range(len(xi_list)):

    # xi_label = xi_label_list[xi_num]
    # xi = xi_list[xi_num]
    xi = 0.025
    filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
        xi_base, xi, xi, xi_base, xi, xi_base, psi_0, psi_1, varrho, rho, delta)

    with open(folder + filename + "model_tech1_pre_damage_UD_simul_40direct_direct", "rb") as f:
        model_tech1_pre_damage = pickle.load(f)

    trace = go.Histogram(
        # histfunc="sum",
        x=model_tech1_pre_damage["theta_ell_new"][:, -1]*1000,
        histnorm='probability density',
        # marker=dict(color=colors[xi_num],
        #             line=dict(color='grey', width=1)),
        showlegend=True,
        visible=True,
        xbins=dict(size=0.15),
        name="No Technology Uncentainty",
        # legendgroup=xi_num+1,
        opacity=0.5,
        hovertemplate=hovertemplate
    )

    fig.add_trace(trace)

    trace_base = go.Histogram(
        x=theta_list * 1000,
        histnorm='probability density',
        marker=dict(color="#d62728", line=dict(
            color='grey', width=1)),
        showlegend=True,
        visible=True,
        xbins=dict(size=0.15),
        name='Baseline',
        # legendgroup=xi_num+1,
        opacity=0.5,
        hovertemplate=hovertemplate
    )
    fig.add_trace(trace_base)

    # for abatement_cost in [0.1, 0.5]:
    # for rho in [0.66, 1.0, 1.5]:

    #     folder = "./data_simul2/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
    #         abatement_cost)

    #     if abatement_cost == 0.1:

    #         xi_list = [0.025, 0.050]
    #         cost_label = "φ₀=0.1"
    #     if abatement_cost == 0.5:

    #         xi_list = [0.075, 0.150]
    #         cost_label = "φ₀=0.5"
    #     xi_label_list = ["More Aversion", "Less Aversion"]

    #     for xi_num in range(len(xi_list)):

    #         xi_label = xi_label_list[xi_num]
    #         xi = xi_list[xi_num]
    #         filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
    #             xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

    #         trace_base = go.Histogram(
    #             x=theta_list * 1000,
    #             histnorm='probability density',
    #             marker=dict(color="#d62728", line=dict(
    #                 color='grey', width=1)),
    #             showlegend=False,
    #             visible=False,
    #             xbins=dict(size=0.15),
    #             name='Baseline',
    #             # legendgroup=xi_num+1,
    #             opacity=0.5,
    #             hovertemplate=hovertemplate
    #         )
    #         fig.add_trace(trace_base, 1, xi_num+1)

    # for i in range(2):
    #     fig.data[2*4 + i]["visible"] = True
    #     fig.data[2*4 + i+12]["visible"] = True

    #     fig.data[2*4 + i]["showlegend"] = True
    #     fig.data[2*4 + 12]["showlegend"] = True

    # buttons = []
    # i = 0

    # for abatement_cost in [0.1, 0.5]:
    #     for rho in [0.66, 1.0, 1.5]:

    #         if abatement_cost == 0.1:

    #             xi_list = [0.025, 0.050]
    #             cost_label = "φ₀=0.1"
    #         if abatement_cost == 0.5:

    #             xi_list = [0.075, 0.150]
    #             cost_label = "φ₀=0.5"

    #         # Hide all traces
    #         label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

    #         button = dict(method='update',
    #                       args=[
    #                           {
    #                               'visible': [False] * (2 * 3 * 2 * 2),
    #                               'showlegend': [False] * (2 * 3 * 2 * 2),
    #                           },
    #                       ],
    #                       label=label)
    #         # Enable the two traces we want to see
    #         # print(button['args'][0]["visible"])

    #         button['args'][0]["visible"][2*i + 0] = True
    #         button['args'][0]["visible"][2*i + 1] = True
    #         button['args'][0]["visible"][2*i + 0 + 12] = True
    #         button['args'][0]["visible"][2*i + 1 + 12] = True

    #         button['args'][0]["showlegend"][2*i + 0] = True
    #         button['args'][0]["showlegend"][2*i + 1] = True
    #         button['args'][0]["showlegend"][2*i + 0 + 12] = True
    #         # button['args'][0]["showlegend"][2*i + 1 +12] = True
    #         # print(button['args'][0]["visible"])

    #         i = i+1
    #         # Add step to step list
    #         buttons.append(button)

    # fig.update_layout(
    #     updatemenus=[
    #         dict(
    #             type="buttons",
    #             buttons=buttons,
    #             # direction="right",
    #             active=4,
    #             x=1.25,
    #             y=0.7,
    #             # xanchor="left",
    #             # yanchor="top",
    #             pad={"r": 10,
    #                  "t": 10, "b": 10},
    #             showactive=True
    #         )
    #     ])

    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=700,
        height=500,
        margin=dict(l=30, r=0),
        # legend=dict(
        #     orientation="h",
        #     yanchor="top",
        #     y=0.99,
        #     xanchor="left",
        #     x=0.01),
        # legend_tracegroupgap = 1,
        # legend_orientation="h"
    )

    fig.update_yaxes(range=[0., 1.5],
                     showline=True,
                     showgrid=False,
                     linecolor="black",
                     linewidth=1,
                     )
    fig.update_xaxes(
        range=[1.0, 3.0],
        showline=True,
        showgrid=False,
        linecolor="black",
        linewidth=1,
        title=go.layout.xaxis.Title(
            text=r"Climate Sensitivity", font=dict(size=13)),
    )

    return fig




def plot_gammahist(graph_title):

    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01

    fig = make_subplots(rows=1, cols=2)
    hovertemplate = "%{y:.2f}"

    colors = ["#1f77b4", "navy"]

    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            folder = "./data_simul2/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
                abatement_cost)

            if abatement_cost == 0.1:

                xi_list = [0.025, 0.050]
                cost_label = "φ₀=0.1"
            if abatement_cost == 0.5:

                xi_list = [0.075, 0.150]
                cost_label = "φ₀=0.5"
            xi_label_list = ["More Aversion", "Less Aversion"]

            for xi_num in range(len(xi_list)):

                xi_label = xi_label_list[xi_num]
                xi = xi_list[xi_num]
                filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
                    xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

                with open(folder + filename + "model_tech1_pre_damage_UD_simul_40direct_direct", "rb") as f:
                    model_tech1_pre_damage = pickle.load(f)
                # print(model_tech1_pre_damage["gt_dmg"][:, -1])
                trace = go.Histogram(
                histfunc="sum",
                x=gamma_3_list,                    
                y=model_tech1_pre_damage["gt_dmg"][:, -1],
                    histnorm='probability',
                    marker=dict(color=colors[xi_num],
                                line=dict(color='grey', width=1)),
                    showlegend=False,
                    visible=False,
                    xbins=dict(start=0, end=1. / 3, size=1 / 20 / 3),
                    name=xi_label_list[xi_num],
                    # legendgroup=xi_num+1,
                    opacity=0.5,
                    hovertemplate=hovertemplate
                )

                fig.add_trace(trace, 1, xi_num+1)

    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            folder = "./data_simul2/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
                abatement_cost)

            if abatement_cost == 0.1:

                xi_list = [0.025, 0.050]
                cost_label = "φ₀=0.1"
            if abatement_cost == 0.5:

                xi_list = [0.075, 0.150]
                cost_label = "φ₀=0.5"
            xi_label_list = ["More Aversion", "Less Aversion"]

            for xi_num in range(len(xi_list)):

                xi_label = xi_label_list[xi_num]
                xi = xi_list[xi_num]
                filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
                    xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

                trace_base = go.Histogram(
                    x=gamma_3_list,
                    histnorm='probability',
                    marker=dict(color="#d62728", line=dict(
                        color='grey', width=1)),
                    showlegend=False,
                    visible=False,
                    xbins=dict(start=0, end=1. / 3, size=1 / 20 / 3),
                    name='Baseline',
                    legendgroup=1,
                    opacity=0.5,
                    hovertemplate=hovertemplate
                )
                fig.add_trace(trace_base, 1, xi_num+1)


    for i in range(2):
        fig.data[2*4 + i]["visible"] = True
        fig.data[2*4 + i+12]["visible"] = True
        
        fig.data[2*4 + i]["showlegend"] = True
        fig.data[2*4 + 12]["showlegend"] = True


    buttons = []
    i = 0

    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                xi_list = [0.025, 0.050]
                cost_label = "φ₀=0.1"
            if abatement_cost == 0.5:

                xi_list = [0.075, 0.150]
                cost_label = "φ₀=0.5"

            # Hide all traces
            label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

            button = dict(method='update',
                          args=[
                              {
                                  'visible': [False] * (2 * 3 * 2 * 2),
                                  'showlegend': [False] * (2 * 3 * 2 * 2),
                              },
                          ],
                          label=label)
            # Enable the two traces we want to see
            # print(button['args'][0]["visible"])

            button['args'][0]["visible"][2*i + 0] = True
            button['args'][0]["visible"][2*i + 1] = True
            button['args'][0]["visible"][2*i + 0 + 12] = True
            button['args'][0]["visible"][2*i + 1 + 12] = True

            button['args'][0]["showlegend"][2*i + 0] = True
            button['args'][0]["showlegend"][2*i + 1] = True
            button['args'][0]["showlegend"][2*i + 0 + 12] = True
            # button['args'][0]["showlegend"][2*i + 1 +12] = True
            # print(button['args'][0]["visible"])

            i = i+1
            # Add step to step list
            buttons.append(button)

    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                buttons=buttons,
                # direction="right",
                active=4,
                x=1.25,
                y=0.7,
                # xanchor="left",
                # yanchor="top",
                pad={"r": 10,
                     "t": 10, "b": 10},
                showactive=True
            )
        ])

    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=900,
        height=500,
        margin=dict(l=30, r=0),
        # legend=dict(
        #     orientation="h",
        #     yanchor="top",
        #     y=0.99,
        #     xanchor="left",
        #     x=0.01),
        # legend_tracegroupgap = 1,
        # legend_orientation="h"
    )

    fig.update_yaxes(range=[0., 0.15],
    # fig.update_yaxes(
                     showline=True,
                     showgrid=False,
                     linecolor="black",
                     linewidth=1,
                     )
    fig.update_xaxes(
        range=[0,1/3],
        showline=True,
        showgrid=False,
        linecolor="black",
        linewidth=1,
        title=go.layout.xaxis.Title(
            text=r" γ₃", font=dict(size=13)),
    )

    return fig


def plot_gammahist_notech(graph_title):

    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01

    # fig = make_subplots(rows=1, cols=2)
    fig = go.Figure()
    hovertemplate = "%{y:.2f}"

    colors = ["#1f77b4", "navy"]

    # for abatement_cost in [0.1, 0.5]:
    #     for rho in [0.66, 1.0, 1.5]:
    abatement_cost = 0.5
    rho = 1.0
    
    folder = "./data_simul6/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
        abatement_cost)

            # if abatement_cost == 0.1:

            #     xi_list = [0.025, 0.050]
            #     cost_label = "φ₀=0.1"
    if abatement_cost == 0.5:

        xi_list = [0.075, 0.150]
        cost_label = "φ₀=0.5"
    xi_label_list = ["More Aversion", "Less Aversion"]

            # for xi_num in range(len(xi_list)):

    # xi_label = xi_label_list[xi_num]
    xi =0.025
    filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
        xi_base, xi, xi, xi_base, xi, xi_base, psi_0, psi_1, varrho, rho, delta)

    with open(folder + filename + "model_tech1_pre_damage_UD_simul_40direct_direct", "rb") as f:
        model_tech1_pre_damage = pickle.load(f)
    # print(model_tech1_pre_damage["gt_dmg"][:, -1])
    trace = go.Histogram(
        histfunc="sum",
        x=gamma_3_list,
        y=model_tech1_pre_damage["gt_dmg"][:, -1],
        histnorm='probability',
        # marker=dict(color=colors[xi_num],
        #             line=dict(color='grey', width=1)),
        showlegend=True,
        visible=True,
        xbins=dict(start=0, end=1. / 3, size=1 / 20 / 3),
        name="No technology Uncertainty",
        # legendgroup=xi_num+1,
        opacity=0.5,
        hovertemplate=hovertemplate
    )

    fig.add_trace(trace)

    # for abatement_cost in [0.1, 0.5]:
    #     for rho in [0.66, 1.0, 1.5]:

    #         folder = "./data_simul2/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
    #             abatement_cost)

    #         if abatement_cost == 0.1:

    #             xi_list = [0.025, 0.050]
    #             cost_label = "φ₀=0.1"
    #         if abatement_cost == 0.5:

    #             xi_list = [0.075, 0.150]
    #             cost_label = "φ₀=0.5"
    #         xi_label_list = ["More Aversion", "Less Aversion"]

    #         for xi_num in range(len(xi_list)):

    #             xi_label = xi_label_list[xi_num]
    #             xi = xi_list[xi_num]
    #             filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
    #                 xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

    trace_base = go.Histogram(
        x=gamma_3_list,
        histnorm='probability',
        marker=dict(color="#d62728", line=dict(
            color='grey', width=1)),
        showlegend=True,
        visible=True,
        xbins=dict(start=0, end=1. / 3, size=1 / 20 / 3),
        name='Baseline',
        legendgroup=1,
        opacity=0.5,
        hovertemplate=hovertemplate
    )
    fig.add_trace(trace_base)

    # for i in range(2):
    #     fig.data[2*4 + i]["visible"] = True
    #     fig.data[2*4 + i+12]["visible"] = True

    #     fig.data[2*4 + i]["showlegend"] = True
    #     fig.data[2*4 + 12]["showlegend"] = True

    # buttons = []
    # i = 0

    # for abatement_cost in [0.1, 0.5]:
    #     for rho in [0.66, 1.0, 1.5]:

    #         if abatement_cost == 0.1:

    #             xi_list = [0.025, 0.050]
    #             cost_label = "φ₀=0.1"
    #         if abatement_cost == 0.5:

    #             xi_list = [0.075, 0.150]
    #             cost_label = "φ₀=0.5"

    #         # Hide all traces
    #         label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

    #         button = dict(method='update',
    #                       args=[
    #                           {
    #                               'visible': [False] * (2 * 3 * 2 * 2),
    #                               'showlegend': [False] * (2 * 3 * 2 * 2),
    #                           },
    #                       ],
    #                       label=label)
    #         # Enable the two traces we want to see
    #         # print(button['args'][0]["visible"])

    #         button['args'][0]["visible"][2*i + 0] = True
    #         button['args'][0]["visible"][2*i + 1] = True
    #         button['args'][0]["visible"][2*i + 0 + 12] = True
    #         button['args'][0]["visible"][2*i + 1 + 12] = True

    #         button['args'][0]["showlegend"][2*i + 0] = True
    #         button['args'][0]["showlegend"][2*i + 1] = True
    #         button['args'][0]["showlegend"][2*i + 0 + 12] = True
    #         # button['args'][0]["showlegend"][2*i + 1 +12] = True
    #         # print(button['args'][0]["visible"])

    #         i = i+1
    #         # Add step to step list
    #         buttons.append(button)

    # fig.update_layout(
    #     updatemenus=[
    #         dict(
    #             type="buttons",
    #             buttons=buttons,
    #             # direction="right",
    #             active=4,
    #             x=1.25,
    #             y=0.7,
    #             # xanchor="left",
    #             # yanchor="top",
    #             pad={"r": 10,
    #                  "t": 10, "b": 10},
    #             showactive=True
    #         )
    #     ])

    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=900,
        height=500,
        margin=dict(l=30, r=0),
        # legend=dict(
        #     orientation="h",
        #     yanchor="top",
        #     y=0.99,
        #     xanchor="left",
        #     x=0.01),
        # legend_tracegroupgap = 1,
        # legend_orientation="h"
    )

    fig.update_yaxes(range=[0., 0.15],
                     # fig.update_yaxes(
                     showline=True,
                     showgrid=False,
                     linecolor="black",
                     linewidth=1,
                     )
    fig.update_xaxes(
        range=[0, 1/3],
        showline=True,
        showgrid=False,
        linecolor="black",
        linewidth=1,
        title=go.layout.xaxis.Title(
            text=r" γ₃", font=dict(size=13)),
    )

    return fig

def Distorted_total_prob():
    # Define the relative paths to the CSV files
    file_path_1 = './data/figure6_phi00.1_rho1.0.csv'
    file_path_2 = './data/figure6_phi00.5_rho1.0.csv'
    file_path_3 = './data/figure6_phi00.1_rho1.5.csv'
    file_path_4 = './data/figure6_phi00.5_rho1.5.csv'
    file_path_5 = './data/figure6_phi00.1_rho0.66.csv'

    # Read the CSV files
    data_1 = pd.read_csv(file_path_1)
    data_2 = pd.read_csv(file_path_2)
    data_3 = pd.read_csv(file_path_3)
    data_4 = pd.read_csv(file_path_4)
    data_5 = pd.read_csv(file_path_5)

    # Create a figure to hold both datasets
    fig = go.Figure()

    # Add traces for the first dataset (Abatement Cost φ₀ = 0.1) with wider lines
    fig.add_trace(go.Scatter(x=data_1['time'], y=data_1['more aversion'], mode='lines', name='More Aversion', 
                            line=dict(width=4)))
    fig.add_trace(go.Scatter(x=data_1['time'], y=data_1['less aversion'], mode='lines', name='Less Aversion', 
                            line=dict(width=4)))
    fig.add_trace(go.Scatter(x=data_1['time'], y=data_1['neutrality'], mode='lines', name='Neutrality', 
                            line=dict(width=4)))

    # Add traces for the second dataset (Abatement Cost φ₀ = 0.5) with wider lines, initially hidden
    fig.add_trace(go.Scatter(x=data_2['time'], y=data_2['more aversion'], mode='lines', name='More Aversion', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_2['time'], y=data_2['less aversion'], mode='lines', name='Less Aversion', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_2['time'], y=data_2['neutrality'], mode='lines', name='Neutrality', 
                            line=dict(width=4), visible=False))
    
    # Add traces for the first dataset (Abatement Cost φ₀ = 0.1) with wider lines
    fig.add_trace(go.Scatter(x=data_3['time'], y=data_3['more aversion'], mode='lines', name='More Aversion', 
                            line=dict(width=4)))
    fig.add_trace(go.Scatter(x=data_3['time'], y=data_3['less aversion'], mode='lines', name='Less Aversion', 
                            line=dict(width=4)))
    fig.add_trace(go.Scatter(x=data_3['time'], y=data_3['neutrality'], mode='lines', name='Neutrality', 
                            line=dict(width=4)))

    # Add traces for the second dataset (Abatement Cost φ₀ = 0.5) with wider lines, initially hidden
    fig.add_trace(go.Scatter(x=data_4['time'], y=data_4['more aversion'], mode='lines', name='More Aversion', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_4['time'], y=data_4['less aversion'], mode='lines', name='Less Aversion', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_4['time'], y=data_4['neutrality'], mode='lines', name='Neutrality', 
                            line=dict(width=4), visible=False)) 
    
    fig.add_trace(go.Scatter(x=data_5['time'], y=data_5['more aversion'], mode='lines', name='More Aversion', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_5['time'], y=data_5['less aversion'], mode='lines', name='Less Aversion', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_5['time'], y=data_5['neutrality'], mode='lines', name='Neutrality', 
                            line=dict(width=4), visible=False))
    # Create buttons to toggle between the datasets
    
    buttons = [
        dict(label="φ₀ = 0.1,  ρ=1",
            method="update",
            args=[{"visible": [True, True, True, False, False, False, False, False, False, False, False, False, False, False, False]},  # Show traces from dataset 1
                {"title": "Distorted Jump Probability"}]),
        dict(label="φ₀ = 0.5,  ρ=1",
            method="update",
            args=[{"visible": [False, False, False, True, True, True, False, False, False, False, False, False, False, False, False]},  # Show traces from dataset 2
                {"title": "Distorted Jump Probability"}]),
        dict(label="φ₀ = 0.1,  ρ=1.5",
            method="update",
            args=[{"visible": [False, False, False, False, False, False, True, True, True, False, False, False, False, False, False]},  # Show traces from dataset 2
                {"title": "Distorted Jump Probability"}]),
        dict(label="φ₀ = 0.5,  ρ=1.5",
            method="update",
            args=[{"visible": [False, False, False, False, False, False, False, False, False, True, True, True, False, False, False]},  # Show traces from dataset 2
                {"title": "Distorted Jump Probability"}]),
        dict(label="φ₀ = 0.1,  ρ=0.6",
            method="update",
            args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, True, True, True]},  # Show traces from dataset 2
                {"title": "Distorted Jump Probability"}])
    ]

    # Add buttons to the layout (positioned to the right) and adjust axis and line width
    fig.update_layout(
        updatemenus=[dict(type="buttons", buttons=buttons, direction="down", x=1.15, y=0.5)],  # Buttons on the right side
        title="Distorted Jump Probability",
        xaxis_title="Time",
        xaxis=dict(showline=True, linewidth=3, showgrid=True, zeroline=False, range=[0, 60]),  # Thicker x-axis line
        yaxis=dict(showline=True, linewidth=3, showgrid=True, zeroline=False),  # Thicker y-axis line
        plot_bgcolor="white"
    )

    # Show the figure
    fig.show()


def Distorted_tech_jump_prob():
    # Define the relative paths to the CSV files
    file_path_1 = './data/figure7b_phi00.1_rho1.0.csv'
    file_path_2 = './data/figure7b_phi00.5_rho1.0.csv'
    file_path_3 = './data/figure7b_phi00.1_rho1.5.csv'
    file_path_4 = './data/figure7b_phi00.5_rho1.5.csv'
    file_path_5 = './data/figure7b_phi00.1_rho0.66.csv'
    # Read the CSV files
    data_1 = pd.read_csv(file_path_1)
    data_2 = pd.read_csv(file_path_2)
    data_3 = pd.read_csv(file_path_3)
    data_4 = pd.read_csv(file_path_4)
    data_5 = pd.read_csv(file_path_5)
 


    # Create a figure to hold both datasets
    fig = go.Figure()

    # Add traces for the first dataset (Abatement Cost φ₀ = 0.1) with wider lines
    fig.add_trace(go.Scatter(x=data_1['time'], y=data_1['more aversion'], mode='lines', name='More Aversion', 
                            line=dict(width=4)))
    fig.add_trace(go.Scatter(x=data_1['time'], y=data_1['less aversion'], mode='lines', name='Less Aversion', 
                            line=dict(width=4)))
    fig.add_trace(go.Scatter(x=data_1['time'], y=data_1['neutrality'], mode='lines', name='Neutrality', 
                            line=dict(width=4)))

    # Add traces for the second dataset (Abatement Cost φ₀ = 0.5) with wider lines, initially hidden
    fig.add_trace(go.Scatter(x=data_2['time'], y=data_2['more aversion'], mode='lines', name='More Aversion', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_2['time'], y=data_2['less aversion'], mode='lines', name='Less Aversion', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_2['time'], y=data_2['neutrality'], mode='lines', name='Neutrality', 
                            line=dict(width=4), visible=False))
    # Add traces for the second dataset (Abatement Cost φ₀ = 0.5) with wider lines, initially hidden
    fig.add_trace(go.Scatter(x=data_3['time'], y=data_3['more aversion'], mode='lines', name='More Aversion', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_3['time'], y=data_3['less aversion'], mode='lines', name='Less Aversion', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_3['time'], y=data_3['neutrality'], mode='lines', name='Neutrality', 
                            line=dict(width=4), visible=False))    
    # Add traces for the second dataset (Abatement Cost φ₀ = 0.5) with wider lines, initially hidden
    fig.add_trace(go.Scatter(x=data_4['time'], y=data_4['more aversion'], mode='lines', name='More Aversion', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_4['time'], y=data_4['less aversion'], mode='lines', name='Less Aversion', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_4['time'], y=data_4['neutrality'], mode='lines', name='Neutrality', 
                            line=dict(width=4), visible=False))
    # Add traces for the second dataset (Abatement Cost φ₀ = 0.5) with wider lines, initially hidden
    fig.add_trace(go.Scatter(x=data_5['time'], y=data_5['more aversion'], mode='lines', name='More Aversion', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_5['time'], y=data_5['less aversion'], mode='lines', name='Less Aversion', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_5['time'], y=data_5['neutrality'], mode='lines', name='Neutrality', 
                            line=dict(width=4), visible=False))
    # Create buttons to toggle between the datasets
    buttons = [
        dict(label="φ₀ = 0.1,  ρ=1",
            method="update",
            args=[{"visible": [True, True, True, False, False, False, False, False, False, False, False, False, False, False, False]},  # Show traces from dataset 1
                {"title": "Distorted Technology Jump Probability"}]),
        dict(label="φ₀ = 0.5,  ρ=1",
            method="update",
            args=[{"visible": [False, False, False, True, True, True, False, False, False, False, False, False, False, False, False]},  # Show traces from dataset 2
                {"title": "Distorted Technology Jump Probability"}]),
        dict(label="φ₀ = 0.1,  ρ=1.5",
            method="update",
            args=[{"visible": [False, False, False, False, False, False, True, True, True, False, False, False, False, False, False]},  # Show traces from dataset 2
                {"title": "Distorted Technology Jump Probability"}]),
        dict(label="φ₀ = 0.5,  ρ=1.5",
            method="update",
            args=[{"visible": [False, False, False, False, False, False, False, False, False, True, True, True, False, False, False]},  # Show traces from dataset 2
                {"title": "Distorted Technology Jump Probability"}]),
        dict(label="φ₀ = 0.1,  ρ=0.6",
            method="update",
            args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, True, True, True]},  # Show traces from dataset 2
                {"title": "Distorted Technology Jump Probability"}])
    ]

    # Add buttons to the layout (positioned to the right) and adjust axis and line width
    fig.update_layout(
        updatemenus=[dict(type="buttons", buttons=buttons, direction="down", x=1.15, y=0.5)],  # Buttons on the right side
        title="Distorted Technology Jump Probability",
        xaxis_title="Time",
        xaxis=dict(showline=True, linewidth=3, showgrid=True, zeroline=False, range=[0, 60]),  # Thicker x-axis line
        yaxis=dict(showline=True, linewidth=3, showgrid=True, zeroline=False),  # Thicker y-axis line
        plot_bgcolor="white"
    )

    # Show the figure
    fig.show()



def Distorted_damage_jump_prob():
    # Define the relative paths to the CSV files
    file_path_1 = './data/figure7a_phi00.1_rho1.0.csv'
    file_path_2 = './data/figure7a_phi00.5_rho1.0.csv'
    file_path_3 = './data/figure7a_phi00.1_rho1.5.csv'
    file_path_4 = './data/figure7a_phi00.5_rho1.5.csv'
    file_path_5 = './data/figure7a_phi00.1_rho0.66.csv'
    # Read the CSV files
    data_1 = pd.read_csv(file_path_1)
    data_2 = pd.read_csv(file_path_2)
    data_3 = pd.read_csv(file_path_3)
    data_4 = pd.read_csv(file_path_4)
    data_5 = pd.read_csv(file_path_5)

    # Create a figure to hold both datasets
    fig = go.Figure()

    # Add traces for the first dataset (Abatement Cost φ₀ = 0.1) with wider lines
    fig.add_trace(go.Scatter(x=data_1['time'], y=data_1['more aversion'], mode='lines', name='More Aversion', 
                            line=dict(width=4)))
    fig.add_trace(go.Scatter(x=data_1['time'], y=data_1['less aversion'], mode='lines', name='Less Aversion', 
                            line=dict(width=4)))
    fig.add_trace(go.Scatter(x=data_1['time'], y=data_1['neutrality'], mode='lines', name='Neutrality', 
                            line=dict(width=4)))

    # Add traces for the second dataset (Abatement Cost φ₀ = 0.5) with wider lines, initially hidden
    fig.add_trace(go.Scatter(x=data_2['time'], y=data_2['more aversion'], mode='lines', name='More Aversion ', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_2['time'], y=data_2['less aversion'], mode='lines', name='Less Aversion ', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_2['time'], y=data_2['neutrality'], mode='lines', name='Neutrality ', 
                            line=dict(width=4), visible=False))
    # Add traces for the first dataset (Abatement Cost φ₀ = 0.1) with wider lines
    fig.add_trace(go.Scatter(x=data_3['time'], y=data_3['more aversion'], mode='lines', name='More Aversion', 
                            line=dict(width=4)))
    fig.add_trace(go.Scatter(x=data_3['time'], y=data_3['less aversion'], mode='lines', name='Less Aversion', 
                            line=dict(width=4)))
    fig.add_trace(go.Scatter(x=data_3['time'], y=data_3['neutrality'], mode='lines', name='Neutrality', 
                            line=dict(width=4)))

    # Add traces for the second dataset (Abatement Cost φ₀ = 0.5) with wider lines, initially hidden
    fig.add_trace(go.Scatter(x=data_4['time'], y=data_4['more aversion'], mode='lines', name='More Aversion ', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_4['time'], y=data_4['less aversion'], mode='lines', name='Less Aversion ', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_4['time'], y=data_4['neutrality'], mode='lines', name='Neutrality ', 
                            line=dict(width=4), visible=False))
    
    fig.add_trace(go.Scatter(x=data_5['time'], y=data_5['more aversion'], mode='lines', name='More Aversion ', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_5['time'], y=data_5['less aversion'], mode='lines', name='Less Aversion ', 
                            line=dict(width=4), visible=False))
    fig.add_trace(go.Scatter(x=data_5['time'], y=data_5['neutrality'], mode='lines', name='Neutrality ', 
                            line=dict(width=4), visible=False))
    # Create buttons to toggle between the datasets
    buttons = [
        dict(label="φ₀ = 0.1,  ρ=1",
            method="update",
            args=[{"visible": [True, True, True, False, False, False, False, False, False, False, False, False, False, False, False]},  # Show traces from dataset 1
                {"title": "Distorted Damage Jump Probability"}]),
        dict(label="φ₀ = 0.5,  ρ=1",
            method="update",
            args=[{"visible": [False, False, False, True, True, True, False, False, False, False, False, False, False, False, False]},  # Show traces from dataset 2
                {"title": "Distorted Damage Jump Probability"}]),
        dict(label="φ₀ = 0.1,  ρ=1.5",
            method="update",
            args=[{"visible": [ False, False, False, False, False, False,True, True, True, False, False, False, False, False, False]},  # Show traces from dataset 1
                {"title": "Distorted Damage Jump Probability"}]),        
        dict(label="φ₀ = 0.5,  ρ=1.5",
            method="update",
            args=[{"visible": [False, False, False,False, False, False,False, False, False,True, True, True, False, False, False ]},  # Show traces from dataset 1
                {"title": "Distorted Damage Jump Probability"}]),
        dict(label="φ₀ = 0.1,  ρ=0.6",
            method="update",
            args=[{"visible": [False, False, False,False, False, False,False, False, False, False, False, False,True, True, True, ]},  # Show traces from dataset 1
                {"title": "Distorted Damage Jump Probability"}]),
    ]

    # Add buttons to the layout (positioned to the right) and adjust axis and line width
    fig.update_layout(
        updatemenus=[dict(type="buttons", buttons=buttons, direction="down", x=1.15, y=0.5)],  # Buttons on the right side
        title="Distorted Damage Jump Probability",
        xaxis_title="Time",
        xaxis=dict(showline=True, linewidth=3, showgrid=True, zeroline=False, range=[0, 60]),  # Thicker x-axis line
        yaxis=dict(showline=True, linewidth=3, showgrid=True, zeroline=False),  # Thicker y-axis line
        plot_bgcolor="white"
    )

    # Show the figure
    fig.show()


def plot_simulatedpath_full2(graph_type, graph_title, yaxis_label, graph_range, before15):

    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01
    # fig = make_subplots(1, 2)
    color = ["#d62728", "darkgreen", "navy", "darkorange"]

    fig = go.Figure()
    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                xi_list_fullaversion = [0.025, 0.050, 100000.]
                xi_list_uncertaintydecomp = [0.050]

            if abatement_cost == 0.5:

                xi_list_fullaversion = [0.075, 0.150, 100000.]
                xi_list_uncertaintydecomp = [0.150]

            folder = "./data_simul2/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
                abatement_cost)
            i = 0
            for xi in xi_list_fullaversion:
                filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
                    xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

                with open(folder + filename + "model_tech1_pre_damage_UD_simul_40direct_direct", "rb") as f:
                    model_tech1_pre_damage = pickle.load(f)
                # print(model_tech1_pre_damage.keys())
                # print(filename)
                # label = r'ξᵣ = {:.1f}'.format(xi_list_fullaversion[i])
                if xi == 100000.:
                    label = "Baseline"
                if xi == 0.050 or xi == 0.150:
                    label = "Less Aversion"
                if xi == 0.025 or xi == 0.075:
                    label = "More Aversion"
                # print(model_tech1_pre_damage[graph_type])
                if graph_type=="hkt" or graph_type=="hjt":
                    if before15 == False:
                        fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"],
                                                y=-model_tech1_pre_damage[graph_type],
                                                name=label,
                                                showlegend=False,
                                                visible=False,                                     line=dict(color=color[i]),
                                                #  visible=False
                                                ))
                    elif before15 == True:
                        fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                                y=-model_tech1_pre_damage[graph_type][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                                name=label,
                                                showlegend=False,
                                                visible=False,                                     line=dict(color=color[i]),
                                                #  visible=False
                                                ))
                elif graph_type=="CapIOutputRatio":
                    Y_Plot = model_tech1_pre_damage["i"]/(alpha * np.exp(model_tech1_pre_damage["states"][:, 0]))*100
                    if before15 == False:
                        fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"],
                                                y=Y_Plot,
                                                name=label,
                                                showlegend=False,
                                                visible=False,                                     line=dict(color=color[i]),
                                                #  visible=False
                                                ))
                    elif before15 == True:
                        fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                                y=Y_Plot,
                                                name=label,
                                                showlegend=False,
                                                visible=False,                                     line=dict(color=color[i]),
                                                #  visible=False
                                                ))
                else:
                    if before15 == False:
                        fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"],
                                                 y=model_tech1_pre_damage[graph_type],
                                                 name=label,
                                                 showlegend=False,
                                                 visible=False,                                     line=dict(color=color[i]),
                                                 #  visible=False
                                                 ))
                    elif before15 == True:
                        fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                                 y=model_tech1_pre_damage[graph_type][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                                 name=label,
                                                 showlegend=False,
                                                 visible=False,                                     line=dict(color=color[i]),
                                                 #  visible=False
                                                 ))
                i = i+1

    for i in range(3):
        fig.data[3*4 + i]["visible"] = True
        # fig.data[3*2 + i+12]["visible"] = True
        
        fig.data[3*4 + i]["showlegend"] = True
        # fig.data[3*2 + 12]["showlegend"] = True




    buttons = []
    i = 0

    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                xi_list = [0.025, 0.050]
                cost_label = "φ₀=0.1"
            if abatement_cost == 0.5:

                xi_list = [0.075, 0.150]
                cost_label = "φ₀=0.5"

            # Hide all traces
            label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

            button = dict(method='update',
                          args=[
                              {
                                  'visible': [False] * (2 * 3 * 4 * 2),
                                  'showlegend': [False] * (2 * 3 * 4 * 2),
                              },
                          ],
                          label=label)
            # Enable the two traces we want to see
            # print(button['args'][0]["visible"])

            button['args'][0]["visible"][3*i + 0] = True
            button['args'][0]["visible"][3*i + 1] = True
            button['args'][0]["visible"][3*i + 2] = True

            button['args'][0]["showlegend"][3*i + 0] = True
            button['args'][0]["showlegend"][3*i + 1] = True
            button['args'][0]["showlegend"][3*i + 2] = True

            i = i+1
            # Add step to step list
            buttons.append(button)

    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                buttons=buttons,
                # direction="right",
                active=4,
                x=1.3,
                y=0.7,
                # xanchor="left",
                # yanchor="top",
                pad={"r": 10,
                     "t": 10, "b": 10},
                showactive=True
            )
        ])

    fig.update_xaxes(showgrid=False, showline=True,
                     title="Years", range=[0, 40])
    fig.update_yaxes(showgrid=False,
                     showline=True,
                     range=graph_range,
                     title_text=yaxis_label,
                     tickformat=".2f")

    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=800,
        height=500,
        margin=dict(l=50, r=0))

    return fig


def plot_simulatedpath_full2_post(graph_type, graph_title, yaxis_label, graph_range, before15):

    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01
    # fig = make_subplots(1, 2)
    color = ["#d62728", "darkgreen", "navy", "darkorange"]

    fig = go.Figure()
    # for abatement_cost in [0.1, 0.5]:
    #     for rho in [0.66, 1.0, 1.5]:
    abatement_cost = 0.5
    rho = 1.0

    if abatement_cost == 0.1:

        xi_list_fullaversion = [0.025, 0.050, 100000.]
        xi_list_uncertaintydecomp = [0.050]

    if abatement_cost == 0.5:

        xi_list_fullaversion = [0.075, 0.150, 100000.]
        xi_list_uncertaintydecomp = [0.150]

    folder = "./data_simul6/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
        abatement_cost)
    i = 0
    # for xi in xi_list_fullaversion:
    xi = 0.150
    filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
        xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

    for TAjump in [1.5, 2.0]:
        for gamma_3_i in gamma_3_list:
            
            with open(folder + filename + "model_tech1_pre_damage_to_post_damage_{:.4f}" .format(gamma_3_i)+"_UD_simul_fulltransit_50_{}".format(TAjump) + "direct_direct", "rb") as f:
                model_tech1_pre_damage = pickle.load(f)
            # print(model_tech1_pre_damage.keys())
            # print(filename)
            # label = r'ξᵣ = {:.1f}'.format(xi_list_fullaversion[i])
            # if xi == 100000.:
            #     label = "Baseline"
            # if xi == 0.050 or xi == 0.150:
            #     label = "Less Aversion"
            # if xi == 0.025 or xi == 0.075:
            #     label = "More Aversion"
            # print(model_tech1_pre_damage[graph_type])

            label ="λ₃={:.4f}".format(gamma_3_i)

            # if before15 == False:
            # for k in [1.5, 2.0]:
            #     for j in [1.5, 2.0]:
                    
            #         if k==1.5 and j ==1.5:
                        
            #             graph_type = graph_type + "hist"
            
            fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"],
                                        y=model_tech1_pre_damage[graph_type],
                                        name=label,
                                        showlegend=False,
                                        visible=False,                                     
                                        # line=dict(color=color[i]),
                                        #  visible=False
                                        ))
            # elif before15 == True:
            #     fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"][model_tech1_pre_damage["states"][:, 1] < 1.5],
            #                                 y=model_tech1_pre_damage[graph_type][model_tech1_pre_damage["states"][:, 1] < 1.5],
            #                                 name=label,
            #                                 showlegend=False,
            #                                 visible=False,                                     line=dict(color=color[i]),
            #                                 #  visible=False
            #                                 ))
            
    # i = i+1

    for i in range(20):
        fig.data[0*20 + i]["visible"] = True
        # fig.data[3*2 + i+12]["visible"] = True
        
        fig.data[0*20 + i]["showlegend"] = True
        # fig.data[3*2 + 12]["showlegend"] = True




    buttons = []
    i = 0

    # for abatement_cost in [0.1, 0.5]:
    #     for rho in [0.66, 1.0, 1.5]:

    abatement_cost = 0.5
    rho = 1.0
    
    for TAjump in [1.5, 2.0]:
        

        cost_label = "Jump at {:.1f} degree".format(TAjump)


        # Hide all traces
        # label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

        button = dict(method='update',
                        args=[
                            {
                                'visible': [False] * (2 * 20),
                                'showlegend': [False] * (2 * 20),
                            },
                        ],
                      label=cost_label)
        # Enable the two traces we want to see
        # print(button['args'][0]["visible"])

        for j in range(20):
            button['args'][0]["visible"][20*i + j] = True
            button['args'][0]["showlegend"][20*i + j] = True




        i = i+1
        # Add step to step list
        buttons.append(button)

    fig.update_layout(
        updatemenus=[
            dict(
                type="dropdown",
                direction="down",
                buttons=buttons,
                # direction="right",
                active=0,
                x=0.7,
                y=1.0,
                # xanchor="left",
                # yanchor="top",
                pad={"r": 10,
                     "t": 10, "b": 10},
                showactive=True
            )
        ])

    fig.update_xaxes(showgrid=False, showline=True,
                     title="Years", range=[0, 50])
    fig.update_yaxes(showgrid=False,
                     showline=True,
                     range=graph_range,
                     title_text=yaxis_label,
                     tickformat=".2f")
    # fig.update_yaxes(showgrid=False, showline=True,
    #                  range=[1., 2.1], col=2, row=1)
    # fig.update_yaxes(tickvals=[1, 1.2, 1.4, 1.5, 1.6, 1.8, 2.0],
    #                  tickformat=".1f",
    #                  col=2,
    #                  row=1)
    # fig.update_layout(height=400, width=1280)
    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=1000,
        height=700,
        margin=dict(l=50, r=0))

    return fig



def plot_simulatedpath_full2_lambda_post(graph_type, graph_title, yaxis_label, graph_range, before15):
    colors = ["#d62728", "darkorange", "darkgreen", "navy"]

    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01
    # fig = make_subplots(1, 2)
    color = ["#d62728", "darkgreen", "navy", "darkorange"]

    fig = go.Figure()
    # for abatement_cost in [0.1, 0.5]:
    #     for rho in [0.66, 1.0, 1.5]:
    abatement_cost = 0.5
    rho = 1.0

    if abatement_cost == 0.1:

        xi_list_fullaversion = [0.025, 0.050, 100000.]
        xi_list_uncertaintydecomp = [0.050]

    if abatement_cost == 0.5:

        xi_list_fullaversion = [0.075, 0.150, 100000.]
        xi_list_uncertaintydecomp = [0.150]

    folder = "./data_simul6/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
        abatement_cost)
    i = 0
    # for xi in xi_list_fullaversion:
    xi = 0.150
    filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
        xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

    # for TAjump in [1.5, 2.0]:
        # for gamma_3_i in gamma_3_list:
            
    with open(folder + filename + "model_tech1_pre_damage"+"_UD_simul_50" + "direct_direct", "rb") as f:
        model_tech1_pre_damage = pickle.load(f)
    # print(model_tech1_pre_damage.keys())
    # print(filename)
    # label = r'ξᵣ = {:.1f}'.format(xi_list_fullaversion[i])
    # if xi == 100000.:
    #     label = "Baseline"
    # if xi == 0.050 or xi == 0.150:
    #     label = "Less Aversion"
    # if xi == 0.025 or xi == 0.075:
    #     label = "More Aversion"
    # print(model_tech1_pre_damage[graph_type])

    # label ="λ₃={:.4f}".format(gamma_3_i)

    # if before15 == False:
    for k in [1.5, 2.0]:
        for j in [1.5, 2.0]:
            
            if k==1.5 and j ==1.5:
                
                graph_type1 = graph_type + "hist_k15_j15"
            
            if k==1.5 and j ==2:
                
                graph_type1 = graph_type + "hist_k15_j2"
                        
            if k==2 and j ==1.5:
                
                graph_type1 = graph_type + "hist_k2_j15"
                        
            if k==2 and j ==2:
                
                graph_type1 = graph_type + "hist_k2_j2"
                
            if k == 1.5:

                cost_label1 = "Low Capital, "

            else:
                cost_label1 = "High Capital, "

            if j == 1.5:

                cost_label2 = "Low R&D Stock"

            else:
                cost_label2 = "High R&D Stock"

            cost_label = cost_label1 + cost_label2

            if graph_type=="x":

                line15 = 3.55
                line2 = 5.82
            
            if graph_type=="e":
                line15 = 12.08
                line2 = 18.37


            grid = model_tech1_pre_damage["gamma_3_list"]
            # grid = (model_tech1_pre_damage["gamma_3_list"],)
            # grid = np.expand_dims(grid,axis=-1)
            value = model_tech1_pre_damage[graph_type1][:,0]
            # value = np.expand_dims(model_tech1_pre_damage[graph_type1][:,0],axis=-1)
            # print(grid.shape,value.shape)

            # graph_func = RegularGridInterpolator(grid, value)
            graph_func = interp1d(grid, value,kind="cubic")


            def point_return(line):

                err = 1

                x_lower = 0
                x_upper = 1/3

                x_lower = np.expand_dims(x_lower,axis=-1)
                x_upper = np.expand_dims(x_upper,axis=-1)

                while err > 10**(-9):

                    x_mid = (x_lower+x_upper)/2

                    if (graph_func(x_lower)-line)*(graph_func(x_mid)-line) < 0:
                        x_upper = x_mid

                    if (graph_func(x_upper)-line)*(graph_func(x_mid)-line) < 0:
                        x_lower = x_mid     
                    
                    err = max(abs(x_mid - x_upper),abs(x_mid - x_lower))

                return x_mid[0]
            


                
            # fig.update_traces(marker=dict(size=12),
            #     selector=dict(mode='markers'))
            color_cur=colors[i]
            # print(model_tech1_pre_damage["gamma_3_list"].shape)
            # print(model_tech1_pre_damage[graph_type1].shape)
            trace = go.Scatter(x=model_tech1_pre_damage["gamma_3_list"],
                                        y=model_tech1_pre_damage[graph_type1][:,0],
                                        name=cost_label,
                                        # showlegend=False,
                                        # visible=False,                                     
                                        line=dict(color=color_cur),
                                        mode="lines",
                                         visible=True
                                        )
            fig.add_trace(trace)
            # print(fig.layout.template.layout.colorway)


            # print(fig.data)
            
            if k == 1.5:

                fig.add_trace(go.Scatter(
                        x=np.array((point_return(line15))),
                        y=np.array((line15)),
                        hovertemplate='x: %{x} <br>y: %{y}',
                        name="Jump at 1.5 Degree",
                        mode="markers",
                        showlegend=False,
                        marker=dict(size=12,color=color_cur)
                    ))
                # print(point_return(line15))

            if k == 2:
                
                fig.add_trace(go.Scatter(
                        x=np.array((point_return(line2))),
                        y=np.array((line2)),
                        hovertemplate='x: %{x} <br>y: %{y}',
                        name="Jump at 2 Degree",
                        mode="markers",
                        showlegend=False,
                        marker=dict(size=12,color=color_cur)
                    ))

                # print(point_return(line2))

            i = i+1

    buttons = []
    i = 0



    fig.update_xaxes(showgrid=False, showline=True,
                     title="λ₃", range=[0, 1/3])
    fig.update_yaxes(showgrid=False,
                     showline=True,
                     range=graph_range,
                     title_text=yaxis_label,
                     tickformat=".2f")
    # fig.update_yaxes(showgrid=False, showline=True,
    #                  range=[1., 2.1], col=2, row=1)
    # fig.update_yaxes(tickvals=[1, 1.2, 1.4, 1.5, 1.6, 1.8, 2.0],
    #                  tickformat=".1f",
    #                  col=2,
    #                  row=1)
    # fig.update_layout(height=400, width=1280)
    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=1000,
        height=700,
        margin=dict(l=50, r=0))

    return fig
def plot_simulatedpath_full2_dist_post(graph_type, graph_title, xlabel, yaxis_label, graph_range, before15):

    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01
    # fig = make_subplots(1, 2)
    color = ["#d62728", "darkgreen", "navy", "darkorange"]

    fig = go.Figure()
    # for abatement_cost in [0.1, 0.5]:
    #     for rho in [0.66, 1.0, 1.5]:
    abatement_cost = 0.5
    rho = 1.0

    if abatement_cost == 0.1:

        xi_list_fullaversion = [0.025, 0.050, 100000.]
        xi_list_uncertaintydecomp = [0.050]

    if abatement_cost == 0.5:

        xi_list_fullaversion = [0.075, 0.150, 100000.]
        xi_list_uncertaintydecomp = [0.150]

    folder = "./data_simul6/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
        abatement_cost)
    i = 0
    # for xi in xi_list_fullaversion:
    xi = 0.150
    filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
        xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

    # for TAjump in [1.5, 2.0]:
        # for gamma_3_i in gamma_3_list:
            
    with open(folder + filename + "model_tech1_pre_damage"+"_UD_simul_50" + "direct_direct", "rb") as f:
        model_tech1_pre_damage = pickle.load(f)
    # print(model_tech1_pre_damage.keys())
    # print(filename)
    # label = r'ξᵣ = {:.1f}'.format(xi_list_fullaversion[i])
    # if xi == 100000.:
    #     label = "Baseline"
    # if xi == 0.050 or xi == 0.150:
    #     label = "Less Aversion"
    # if xi == 0.025 or xi == 0.075:
    #     label = "More Aversion"
    # print(model_tech1_pre_damage[graph_type])

    # label ="λ₃={:.4f}".format(gamma_3_i)

    # if before15 == False:
    for k in [1.5, 2.0]:
        for j in [1.5, 2.0]:
            
            if k==1.5 and j ==1.5:
                
                graph_type1 = graph_type + "hist_k15_j15"
            
            if k==1.5 and j ==2:
                
                graph_type1 = graph_type + "hist_k15_j2"
                        
            if k==2 and j ==1.5:
                
                graph_type1 = graph_type + "hist_k2_j15"
                        
            if k==2 and j ==2:
                
                graph_type1 = graph_type + "hist_k2_j2"
                        
            if k == 1.5:

                cost_label1 = "Low Capital, "

            else:
                cost_label1 = "High Capital, "

            if j == 1.5:

                cost_label2 = "Low R&D Stock"

            else:
                cost_label2 = "High R&D Stock"

            cost_label = cost_label1 + cost_label2



            fig.add_trace(go.Histogram(
                x=model_tech1_pre_damage[graph_type1][:,0],
                histnorm='probability density',
                # marker=dict(color="red", line=dict(color='grey', width=1)),
                showlegend=False,
                xbins=dict(size=0.5),
                name=cost_label,
                # legendgroup=1,
                opacity=0.5,
            ))
            # elif before15 == True:
            #     fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"][model_tech1_pre_damage["states"][:, 1] < 1.5],
            #                                 y=model_tech1_pre_damage[graph_type][model_tech1_pre_damage["states"][:, 1] < 1.5],
            #                                 name=label,
            #                                 showlegend=False,
            #                                 visible=False,                                     line=dict(color=color[i]),
            #                                 #  visible=False
            #                                 ))

    # i = i+1

    for i in range(4):
        fig.data[0*4 + i]["visible"] = True
        # fig.data[3*2 + i+12]["visible"] = True
        
        fig.data[0*4 + i]["showlegend"] = True
        # fig.data[3*2 + 12]["showlegend"] = True




    buttons = []
    i = 0


    abatement_cost = 0.5
    rho = 1.0
    
    for k in [1.5, 2.0]:
        for j in [1.5, 2.0]:
            
            if k==1.5:
                
                cost_label1 = "Low Capital, "
            
            else:
                cost_label1 = "High Capital, "
                
            if j==1.5:
                
                cost_label2 = "Low R&D Stock"
            
            else:
                cost_label2 = "High R&D Stock"


            cost_label = cost_label1 + cost_label2


            # Hide all traces
            # label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

            button = dict(method='update',
                            args=[
                                {
                                    'visible': [False] * (4),
                                    'showlegend': [False] * (4),
                                },
                            ],
                        label=cost_label)
            # Enable the two traces we want to see
            # print(button['args'][0]["visible"])

            # for j in range(4):
            button['args'][0]["visible"][4*0 + i] = True
            button['args'][0]["showlegend"][4*0 + i] = True


            i = i+1
            # Add step to step list
            buttons.append(button)

    # fig.update_layout(
    #     updatemenus=[
    #         dict(
    #             type="dropdown",
    #             direction="down",
    #             buttons=buttons,
    #             # direction="right",
    #             active=0,
    #             x=0.7,
    #             y=1.0,
    #             # xanchor="left",
    #             # yanchor="top",
    #             pad={"r": 10,
    #                  "t": 10, "b": 10},
    #             showactive=True
    #         )
    #     ])


    fig.update_xaxes(showgrid=False, showline=True,
                     title=xlabel, range=graph_range)
    fig.update_yaxes(showgrid=False,
                     showline=True,
                    #  range=graph_range,
                     title_text=yaxis_label,
                     tickformat=".2f")
    # fig.update_yaxes(showgrid=False, showline=True,
    #                  range=[1., 2.1], col=2, row=1)
    # fig.update_yaxes(tickvals=[1, 1.2, 1.4, 1.5, 1.6, 1.8, 2.0],
    #                  tickformat=".1f",
    #                  col=2,
    #                  row=1)
    # fig.update_layout(height=400, width=1280)
    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=1000,
        height=700,
        margin=dict(l=50, r=0))

    return fig




def plot_simulatedpath_flow_full2(graph_type, graph_title, yaxis_label, graph_range, before15):

    xi_base = 100000.
    psi_01 = 0.052915
    psi_02 = 0.052915
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01
    # fig = make_subplots(1, 2)
    color = ["#d62728", "darkgreen", "navy", "darkorange"]

    fig = go.Figure()
    for abatement_cost in [0.1, 0.5]:
        for rho in [1.0]:

            if abatement_cost == 0.1:

                xi_list_fullaversion = [0.025, 0.050, 100000.]
                xi_list_uncertaintydecomp = [0.050]

            if abatement_cost == 0.5:

                xi_list_fullaversion = [0.075, 0.150, 100000.]
                xi_list_uncertaintydecomp = [0.150]

            folder = "./data_simul2/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_flow_phi0_{}/".format(
                abatement_cost)
            i = 0
            for xi in xi_list_fullaversion:
                filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_01_{}_psi_02_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
                    xi_base, xi, xi, xi, xi, xi, psi_01, psi_02, psi_1, varrho, rho, delta)

                with open(folder + filename + "model_tech1_pre_damage_UD_simul_40direct_direct", "rb") as f:
                    model_tech1_pre_damage = pickle.load(f)
                # print(model_tech1_pre_damage.keys())
                # print(filename)
                # label = r'ξᵣ = {:.1f}'.format(xi_list_fullaversion[i])
                if xi == 100000.:
                    label = "Baseline"
                if xi == 0.050 or xi == 0.150:
                    label = "Less Aversion"
                if xi == 0.025 or xi == 0.075:
                    label = "More Aversion"
                # print(model_tech1_pre_damage[graph_type])
                if before15 == False:
                    fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"],
                                             y=model_tech1_pre_damage[graph_type],
                                             name=label,
                                             showlegend=False,
                                             visible=False,                                     line=dict(color=color[i]),
                                             #  visible=False
                                             ))
                elif before15 == True:
                    fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                             y=model_tech1_pre_damage[graph_type][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                             name=label,
                                             showlegend=False,
                                             visible=False,                                     line=dict(color=color[i]),
                                             #  visible=False
                                             ))
                i = i+1

    for i in range(3):
        fig.data[1*3 + i]["visible"] = True
        # fig.data[3*2 + i+12]["visible"] = True
        
        fig.data[1*3 + i]["showlegend"] = True
        # fig.data[3*2 + 12]["showlegend"] = True




    buttons = []
    i = 0

    for abatement_cost in [0.1, 0.5]:
        for rho in [1.0]:

            if abatement_cost == 0.1:

                xi_list = [0.025, 0.050]
                cost_label = "φ₀=0.1"
            if abatement_cost == 0.5:

                xi_list = [0.075, 0.150]
                cost_label = "φ₀=0.5"

            # Hide all traces
            label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

            button = dict(method='update',
                          args=[
                              {
                                  'visible': [False] * (2 * 1 * 3),
                                  'showlegend': [False] * (2 * 1 * 3),
                              },
                          ],
                          label=label)
            # Enable the two traces we want to see
            # print(button['args'][0]["visible"])

            button['args'][0]["visible"][3*i + 0] = True
            button['args'][0]["visible"][3*i + 1] = True
            button['args'][0]["visible"][3*i + 2] = True

            button['args'][0]["showlegend"][3*i + 0] = True
            button['args'][0]["showlegend"][3*i + 1] = True
            button['args'][0]["showlegend"][3*i + 2] = True

            i = i+1
            # Add step to step list
            buttons.append(button)

    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                buttons=buttons,
                # direction="right",
                active=4,
                x=1.3,
                y=0.7,
                # xanchor="left",
                # yanchor="top",
                pad={"r": 10,
                     "t": 10, "b": 10},
                showactive=True
            )
        ])

    fig.update_xaxes(showgrid=False, showline=True,
                     title="Years", range=[0, 40])
    fig.update_yaxes(showgrid=False,
                     showline=True,
                     range=graph_range,
                     title_text=yaxis_label,
                     tickformat=".2f")
    # fig.update_yaxes(showgrid=False, showline=True,
    #                  range=[1., 2.1], col=2, row=1)
    # fig.update_yaxes(tickvals=[1, 1.2, 1.4, 1.5, 1.6, 1.8, 2.0],
    #                  tickformat=".1f",
    #                  col=2,
    #                  row=1)
    # fig.update_layout(height=400, width=1280)
    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=800,
        height=500,
        margin=dict(l=50, r=0))

    return fig

def plot_simulatedpath_uncer_decomp2(graph_type, graph_title, yaxis_label, graph_range, before15):

    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01
    # fig = make_subplots(1, 2)
    fig = go.Figure()

    color = ["#d62728", "darkgreen", "darkorange", "navy"]
    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            folder = "./data_simul2/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
                abatement_cost)

            for xi_num in range(4):

                xi_list_uncertaintydecomp = 100000.0 * np.ones((5))

                if abatement_cost == 0.1:

                    xi_list_uncertaintydecomp[xi_num] = 0.050

                    if xi_num == 2:
                        xi_list_uncertaintydecomp[4] = 0.050
                if abatement_cost == 0.5:

                    xi_list_uncertaintydecomp[xi_num] = 0.150
                    if xi_num == 2:
                        xi_list_uncertaintydecomp[4] = 0.150
                # print(xi_list_uncertaintydecomp)
                # filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
                #     xi_base, xi_list_uncertaintydecomp[0], xi_list_uncertaintydecomp[1], xi_list_uncertaintydecomp[2], xi_list_uncertaintydecomp[3],xi_list_uncertaintydecomp[4], psi_0, psi_1, varrho, rho, delta)
                filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
                    xi_base, xi_list_uncertaintydecomp[3], xi_list_uncertaintydecomp[0], xi_list_uncertaintydecomp[2], xi_list_uncertaintydecomp[1], xi_list_uncertaintydecomp[4], psi_0, psi_1, varrho, rho, delta)

                with open(folder + filename + "model_tech1_pre_damage_UD_simul_40direct_direct", "rb") as f:
                    model_tech1_pre_damage = pickle.load(f)
                # print(model_tech1_pre_damage.keys())
                # print(filename)
                # label = r'ξᵣ = {:.1f}'.format(xi_list_fullaversion[i])
                if xi_num == 0:
                    label = "Climate Uncertainty"
                if xi_num == 1:
                    label = "Damage Uncertainty"
                if xi_num == 2:
                    label = "Technology Uncertainty"
                if xi_num == 3:
                    label = "Producticity Uncertainty"
                # print(model_tech1_pre_damage[graph_type])
                if graph_type == "hkt" or graph_type == "hjt":
                    if before15 == False:
                        fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"],
                                                 y=-model_tech1_pre_damage[graph_type],
                                                 name=label,
                                                 showlegend=False,
                                                 visible=False,                                     line=dict(color=color[xi_num]),
                                                 #  visible=False
                                                 ))
                    elif before15 == True:
                        fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                                 y=-model_tech1_pre_damage[graph_type][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                                 name=label,
                                                 showlegend=False,
                                                 visible=False,                                     line=dict(color=color[xi_num]),
                                                 #  visible=False
                                                 ))
                elif graph_type=="CapIOutputRatio":
                    Y_Plot = model_tech1_pre_damage["i"]/(alpha * np.exp(model_tech1_pre_damage["states"][:, 0]))*100
                    if before15 == False:
                        fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"],
                                                y=Y_Plot,
                                                name=label,
                                                showlegend=False,
                                                visible=False,                                     line=dict(color=color[xi_num]),
                                                #  visible=False
                                                ))
                    elif before15 == True:
                        fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                                y=Y_Plot,
                                                name=label,
                                                showlegend=False,
                                                visible=False,                                     line=dict(color=color[xi_num]),
                                                #  visible=False
                                                ))
                else:
                    if before15 == False:
                        fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"],
                                                 y=model_tech1_pre_damage[graph_type],
                                                 name=label,
                                                 showlegend=False,
                                                 visible=False,                                     line=dict(color=color[xi_num]),
                                                 #  visible=False
                                                 ))
                    elif before15 == True:
                        fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                                 y=model_tech1_pre_damage[graph_type][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                                 name=label,
                                                 showlegend=False,
                                                 visible=False,                                     line=dict(color=color[xi_num]),
                                                 #  visible=False
                                                 ))

    for i in range(4):
        fig.data[4*4 + i]["visible"] = True
        # fig.data[3*2 + i+12]["visible"] = True
        
        fig.data[4*4 + i]["showlegend"] = True
        # fig.data[3*2 + 12]["showlegend"] = True

    buttons = []
    i = 0

    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                xi_list = [0.025, 0.050]
                cost_label = "φ₀=0.1"
            if abatement_cost == 0.5:

                xi_list = [0.075, 0.150]
                cost_label = "φ₀=0.5"

            # Hide all traces
            label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

            button = dict(method='update',
                          args=[
                              {
                                  'visible': [False] * (2 * 3 * 4 * 2),
                                  'showlegend': [False] * (2 * 3 * 4 * 2),
                              },
                          ],
                          label=label)
            # Enable the two traces we want to see
            # print(button['args'][0]["visible"])

            button['args'][0]["visible"][4*i + 0] = True
            button['args'][0]["visible"][4*i + 1] = True
            button['args'][0]["visible"][4*i + 2] = True
            button['args'][0]["visible"][4*i + 3] = True

            button['args'][0]["showlegend"][4*i + 0] = True
            button['args'][0]["showlegend"][4*i + 1] = True
            button['args'][0]["showlegend"][4*i + 2] = True
            button['args'][0]["showlegend"][4*i + 3] = True

            i = i+1
            # Add step to step list
            buttons.append(button)

    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                buttons=buttons,
                # direction="right",
                active=4,
                x=1.3,
                y=0.7,
                # xanchor="left",
                # yanchor="top",
                pad={"r": 10,
                     "t": 10, "b": 10},
                showactive=True
            )
        ])

    fig.update_xaxes(showgrid=False, showline=True,
                     title="Years", range=[0, 40])
    fig.update_yaxes(showgrid=False,
                     showline=True,
                     range=graph_range,
                     title_text=yaxis_label,
                     tickformat=".2f")
    # fig.update_yaxes(showgrid=False, showline=True,
    #                  range=[1., 2.1], col=2, row=1)
    # fig.update_yaxes(tickvals=[1, 1.2, 1.4, 1.5, 1.6, 1.8, 2.0],
    #                  tickformat=".1f",
    #                  col=2,
    #                  row=1)
    # fig.update_layout(height=400, width=1280)
    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=800,
        height=500,
        margin=dict(l=50, r=0))

    return fig


def plot_simulatedpath_uncer_decomp2_notech(graph_type, graph_title, yaxis_label, graph_range, before15):

    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01
    # fig = make_subplots(1, 2)
    fig = go.Figure()

    color = ["#d62728", "darkgreen", "darkorange", "navy"]
    # for abatement_cost in [0.1, 0.5]:
    #     for rho in [0.66, 1.0, 1.5]:
    abatement_cost = 0.5
    rho = 1.0
    
    folder = "./data_simul6/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
        abatement_cost)

    for xi_num in range(4):

        xi_list_uncertaintydecomp = 100000.0 * np.ones((5))


        if abatement_cost == 0.5:

            xi_list_uncertaintydecomp[xi_num] = 0.025
            
            if xi_num == 2:
                xi_list_uncertaintydecomp[0] = 0.025
                xi_list_uncertaintydecomp[1] = 0.025
                xi_list_uncertaintydecomp[2] = 100000.0
                xi_list_uncertaintydecomp[3] = 0.025
                
        # print(xi_list_uncertaintydecomp)
        # filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
        #     xi_base, xi_list_uncertaintydecomp[0], xi_list_uncertaintydecomp[1], xi_list_uncertaintydecomp[2], xi_list_uncertaintydecomp[3],xi_list_uncertaintydecomp[4], psi_0, psi_1, varrho, rho, delta)
        filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
            xi_base, xi_list_uncertaintydecomp[3], xi_list_uncertaintydecomp[0], xi_list_uncertaintydecomp[2], xi_list_uncertaintydecomp[1], xi_list_uncertaintydecomp[4], psi_0, psi_1, varrho, rho, delta)

        with open(folder + filename + "model_tech1_pre_damage_UD_simul_40direct_direct", "rb") as f:
            model_tech1_pre_damage = pickle.load(f)
        # print(model_tech1_pre_damage.keys())
        # print(filename)
        # label = r'ξᵣ = {:.1f}'.format(xi_list_fullaversion[i])
        if xi_num == 0:
            label = "Climate Uncertainty"
        if xi_num == 1:
            label = "Damage Uncertainty"
        if xi_num == 2:
            label = "No Technology Uncertainty"
        if xi_num == 3:
            label = "Producticity Uncertainty"
        # print(model_tech1_pre_damage[graph_type])
        if graph_type == "hkt" or graph_type == "hjt":
            if before15 == False:
                fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"],
                                            y=-model_tech1_pre_damage[graph_type],
                                            name=label,
                                            showlegend=False,
                                            visible=False,                                     line=dict(color=color[xi_num]),
                                            #  visible=False
                                            ))
            elif before15 == True:
                fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                            y=-model_tech1_pre_damage[graph_type][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                            name=label,
                                            showlegend=False,
                                            visible=False,                                     line=dict(color=color[xi_num]),
                                            #  visible=False
                                            ))
        else:
            if before15 == False:
                fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"],
                                            y=model_tech1_pre_damage[graph_type],
                                            name=label,
                                            showlegend=False,
                                            visible=False,                                     line=dict(color=color[xi_num]),
                                            #  visible=False
                                            ))
            elif before15 == True:
                fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                            y=model_tech1_pre_damage[graph_type][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                            name=label,
                                            showlegend=False,
                                            visible=False,                                     line=dict(color=color[xi_num]),
                                            #  visible=False
                                            ))

    for i in range(4):
        fig.data[0*4 + i]["visible"] = True
        # fig.data[3*2 + i+12]["visible"] = True

        fig.data[0*4 + i]["showlegend"] = True
        # fig.data[3*2 + 12]["showlegend"] = True

    # buttons = []
    # i = 0

    # for abatement_cost in [0.1, 0.5]:
    #     for rho in [0.66, 1.0, 1.5]:

    #         if abatement_cost == 0.1:

    #             xi_list = [0.025, 0.050]
    #             cost_label = "φ₀=0.1"
    #         if abatement_cost == 0.5:

    #             xi_list = [0.075, 0.150]
    #             cost_label = "φ₀=0.5"

    #         # Hide all traces
    #         label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

    #         button = dict(method='update',
    #                       args=[
    #                           {
    #                               'visible': [False] * (2 * 3 * 4 * 2),
    #                               'showlegend': [False] * (2 * 3 * 4 * 2),
    #                           },
    #                       ],
    #                       label=label)
    #         # Enable the two traces we want to see
    #         # print(button['args'][0]["visible"])

    #         button['args'][0]["visible"][4*i + 0] = True
    #         button['args'][0]["visible"][4*i + 1] = True
    #         button['args'][0]["visible"][4*i + 2] = True
    #         button['args'][0]["visible"][4*i + 3] = True

    #         button['args'][0]["showlegend"][4*i + 0] = True
    #         button['args'][0]["showlegend"][4*i + 1] = True
    #         button['args'][0]["showlegend"][4*i + 2] = True
    #         button['args'][0]["showlegend"][4*i + 3] = True

    #         i = i+1
    #         # Add step to step list
    #         buttons.append(button)

    # fig.update_layout(
    #     updatemenus=[
    #         dict(
    #             type="buttons",
    #             buttons=buttons,
    #             # direction="right",
    #             active=4,
    #             x=1.3,
    #             y=0.7,
    #             # xanchor="left",
    #             # yanchor="top",
    #             pad={"r": 10,
    #                  "t": 10, "b": 10},
    #             showactive=True
    #         )
    #     ])

    fig.update_xaxes(showgrid=False, showline=True,
                     title="Years", range=[0, 40])
    fig.update_yaxes(showgrid=False,
                     showline=True,
                     range=graph_range,
                     title_text=yaxis_label,
                     tickformat=".2f")
    # fig.update_yaxes(showgrid=False, showline=True,
    #                  range=[1., 2.1], col=2, row=1)
    # fig.update_yaxes(tickvals=[1, 1.2, 1.4, 1.5, 1.6, 1.8, 2.0],
    #                  tickformat=".1f",
    #                  col=2,
    #                  row=1)
    # fig.update_layout(height=400, width=1280)
    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=800,
        height=500,
        margin=dict(l=50, r=0))

    return fig



def plot_simulated_stoc_path_full2(graph_type, graph_title, yaxis_label, graph_range):


    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01
    # fig = make_subplots(1, 2)
    color = ["#d62728", "darkgreen", "navy", "darkorange"]

    fig = go.Figure()
    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                xi_list_fullaversion = [0.050]

            if abatement_cost == 0.5:

                xi_list_fullaversion = [0.150]

            folder = "./data_simul2/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
                abatement_cost)
            i = 0
            
            for xi in xi_list_fullaversion:
                filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
                    xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

                with open(folder + filename + "model_tech1_pre_damage_UD_simulstoccompile_40direct_direct", "rb") as f:
                    model_tech1_pre_damage = pickle.load(f)
                
                PathLength = model_tech1_pre_damage["years"].shape[1]
                Years = model_tech1_pre_damage["years"][:,0]
                
                Mat = model_tech1_pre_damage[graph_type]
                
                df = pd.DataFrame(Mat)

                df.index = Years
                
                df.columns.names=['Path']
                pxobj = px.line(df, x=df.index, y=df.columns)
                

                fig.add_traces(
                    list(pxobj.select_traces())
                )
                fig.update_traces(visible=False)

                i = i+1

    for i in range(PathLength):
        fig.data[4*PathLength + i]["visible"] = True
        # fig.data[3*2 + i+12]["visible"] = True

        fig.data[4*PathLength + i]["showlegend"] = True
        # fig.data[3*2 + 12]["showlegend"] = True
    
    buttons = []
    i = 0

    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                cost_label = "φ₀=0.1"
            if abatement_cost == 0.5:

                cost_label = "φ₀=0.5"

            # Hide all traces
            label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

            button = dict(method='update',
                          args=[
                              {
                                  'visible': [False] * (2 * 3 * PathLength ),
                                  'showlegend': [False] * (2 * 3 * PathLength ),
                              },
                          ],
                          label=label)
            # Enable the two traces we want to see
            # print(button['args'][0]["visible"])

            for j in range(PathLength):
                
                button['args'][0]["visible"][PathLength*i + j] = True

                button['args'][0]["showlegend"][PathLength*i + j] = True

            i = i+1
            # Add step to step list
            buttons.append(button)



    fig.update_layout(
        updatemenus=[
            dict(
                type="dropdown",
                direction="down",
                buttons=buttons,
                active=4,
                x=0.6,
                y=1.05,
                pad={'r': 10, 't': 10})
        ],
    )
    
    fig.update_xaxes(showgrid=False, showline=True,
                    title="Years", range=[0, 40])
    fig.update_yaxes(showgrid=False,
                    showline=True,
                    range=graph_range,
                    title_text=yaxis_label,
                    tickformat=".2f")

    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=1000,
        height=700,
        margin=dict(l=50, r=0))


    return fig




def plot_simulated_stoc_path_full2_selected(graph_type, graph_title, yaxis_label, graph_range):


    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01
    # fig = make_subplots(1, 2)
    color = ["#d62728", "darkgreen", "navy", "darkorange"]
    j_dict = {"phi=0.1,rho=0.66":  [1, 25, 6, 10, 24], 
            "phi=0.1,rho=1.0":  [4, 7, 9, 2, 15],
            "phi=0.1,rho=1.5":  [5, 1, 24, 7, 12],
            "phi=0.5,rho=0.66":  [19, 4, 18, 10, 12],
            "phi=0.5,rho=1.0":  [4, 24, 20, 5, 12],
            "phi=0.5,rho=1.5":  [2, 7, 3, 24, 21]
            }
    fig = go.Figure()
    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                xi_list_fullaversion = [0.050]

            if abatement_cost == 0.5:

                xi_list_fullaversion = [0.150]
                

            folder = "./data_simul5/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
            # folder = "./data_simul3/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
                abatement_cost)
            i = 0
            label = "phi={},rho={}".format(abatement_cost,rho)
            j_list = j_dict[label]
            # j_list = [16, 0, 2, 13, 14]

            PathLength_selected = 5
            for xi in xi_list_fullaversion:
                filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
                    xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

                with open(folder + filename + "model_tech1_pre_damage_UD_simulstoccompile2_40direct_direct", "rb") as f:
                # with open(folder + filename + "model_tech1_pre_damage_UD_simulstoccompile_40direct_direct", "rb") as f:
                    model_tech1_pre_damage = pickle.load(f)
                
                PathLength = model_tech1_pre_damage["years"].shape[1]
                Years = model_tech1_pre_damage["years"][:,0]
                
                Mat = model_tech1_pre_damage[graph_type][:,0:]

                for j in range(PathLength_selected):
                    
                    legend_name = "Path {}".format(j+1)
                    j_used = j_list[j]-1
                    # j_used = j_list[j]

                    if abatement_cost ==0.5 and rho==1.0:
                        fig.add_trace(go.Scatter(x=Years,
                                                    y=Mat[:, j_used],
                                                    name=legend_name,
                                                    showlegend=True,
                                                    visible=True,
                                                    # line=dict(width=8),
                                                    #  visible=False
                                                    ))
                    else:
                        fig.add_trace(go.Scatter(x=Years,
                                                 y=Mat[:, j_used],
                                                 name=legend_name,
                                                 showlegend=False,
                                                 visible=False,
                                                 # line=dict(width=8),
                                                 #  visible=False
                                                 ))

                # fig.update_traces(visible=False, line=dict(width=8))
                # fig.update_traces(visible=False)
                

                i = i+1

    # for i in range(PathLength_selected):
    #     fig.data[4*PathLength_selected + i]["visible"] = True
    #     # fig.data[3*2 + i+12]["visible"] = True

    #     fig.data[4*PathLength_selected + i]["showlegend"] = True
    #     # fig.data[3*2 + 12]["showlegend"] = True
    
    buttons = []
    i = 0

    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                cost_label = "φ₀=0.1"
            if abatement_cost == 0.5:

                cost_label = "φ₀=0.5"

            # Hide all traces
            label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

            button = dict(method='update',
                          args=[
                              {
                                  'visible': [False] * (2 * 3 * PathLength_selected ),
                                  'showlegend': [False] * (2 * 3 * PathLength_selected ),
                              },
                          ],
                          label=label)
            # Enable the two traces we want to see
            # print(button['args'][0]["visible"])

            for j in range(PathLength_selected):
                
                button['args'][0]["visible"][PathLength_selected*i + j] = True

                button['args'][0]["showlegend"][PathLength_selected*i + j] = True

            i = i+1
            # Add step to step list
            buttons.append(button)



    fig.update_layout(
        updatemenus=[
            dict(
                type="dropdown",
                direction="down",
                buttons=buttons,
                active=4,
                x=0.6,
                y=1.05,
                pad={'r': 10, 't': 10})
        ],
    )
    
    fig.update_xaxes(showgrid=False, showline=True,
                    title="Years", range=[0, 40])
    fig.update_yaxes(showgrid=False,
                    showline=True,
                    range=graph_range,
                    title_text=yaxis_label,
                    tickformat=".2f")

    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=1000,
        height=800,
        margin=dict(l=50, r=0))


    return fig

def plot_simulated_stoc_path_full2_split_var3(graph_type, graph_title, yaxis_label, graph_range):

    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01
    # fig = make_subplots(1, 2)
    color = ["#d62728", "darkgreen", "navy", "darkorange"]

    fig = go.Figure()
    
    group_total = {}
    
    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            group_list = {"No Jump": [], "Damage Jump": [],  "Techonology Jump": []}

            if abatement_cost == 0.1:

                xi_list_fullaversion = [0.050]

            if abatement_cost == 0.5:

                xi_list_fullaversion = [0.150]

            folder = "./data_simul3/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
                abatement_cost)

            label = "φ₀={:.1f}".format(
                abatement_cost)+r', ρ' + '= {:.2f}'.format(rho)

            
            i = 0

            for xi in xi_list_fullaversion:
                filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
                    xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

                with open(folder + filename + "model_tech1_pre_damage_UD_simulstoccompile_40direct_direct", "rb") as f:
                    model_tech1_pre_damage = pickle.load(f)

                PathLength = model_tech1_pre_damage["years"].shape[1]
                Years = model_tech1_pre_damage["years"][:, 0]

                Mat = model_tech1_pre_damage[graph_type]

                for j in range(PathLength):

                    tech = model_tech1_pre_damage["tech_activate"][:, j]
                    damage = model_tech1_pre_damage["damage_activate"][:, j]

                    if np.max(tech) == 0 and np.max(damage) == 0:

                        group_name = "No Jump"
                        
                    if np.max(tech) == 0 and np.max(damage) == 1:

                        group_name = "Damage Jump"

                    if np.max(tech) == 1:
                        group_name = "Techonology Jump"

                    group_list[group_name].append(j)

                i = i+1
                
            group_total[label] = group_list


    # print(group_total)
    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                xi_list_fullaversion = [0.050]

            if abatement_cost == 0.5:

                xi_list_fullaversion = [0.150]

            folder = "./data_simul3/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
                abatement_cost)

            label = "φ₀={:.1f}".format(
                abatement_cost)+r', ρ' + '= {:.2f}'.format(rho)

            i = 0

            for xi in xi_list_fullaversion:
                filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
                    xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

                with open(folder + filename + "model_tech1_pre_damage_UD_simulstoccompile_40direct_direct", "rb") as f:
                    model_tech1_pre_damage = pickle.load(f)

                PathLength = model_tech1_pre_damage["years"].shape[1]
                Years = model_tech1_pre_damage["years"][:, 0]

                Mat = model_tech1_pre_damage[graph_type]

                for k in group_total[label].keys():
                    
                    group = group_total[label][k]
                    
                    for j in group:

                        tech = model_tech1_pre_damage["tech_activate"][:, j]
                        damage = model_tech1_pre_damage["damage_activate"][:, j]

                        if np.max(tech) == 0 and np.max(damage) == 0:

                            group_name = "No Jump"

                        if np.max(tech) == 0 and np.max(damage) == 1:

                            group_name = "Damage Jump"

                        if np.max(tech) == 1:
                            group_name = "Techonology Jump"

                        legend_name = "Path {}".format(j)
                        
                        if abatement_cost==0.5 and rho==0.66:
                            fig.add_trace(go.Scatter(x=Years,
                                                    y=Mat[:, j],
                                                    name=legend_name,
                                                    showlegend=True,
                                                    visible=True,
                                                    legendgroup=group_name,
                                                    legendgrouptitle_text=group_name,
                                                    # line=dict(color=color[i]),
                                                    #  visible=False
                                                    ))
                        else:
                            fig.add_trace(go.Scatter(x=Years,
                                                    y=Mat[:, j],
                                                    name=legend_name,
                                                    showlegend=False,
                                                    visible=False,
                                                    legendgroup=group_name,
                                                    legendgrouptitle_text=group_name,
                                                    # line=dict(color=color[i]),
                                                    #  visible=False
                                                    ))
                i = i+1
                
    # for i in range(PathLength):
    #     fig.data[3*PathLength + i]["visible"] = True
    #     # fig.data[3*2 + i+12]["visible"] = True

    #     fig.data[3*PathLength + i]["showlegend"] = True
    #     # fig.data[3*2 + 12]["showlegend"] = True

    buttons = []
    i = 0

    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                cost_label = "φ₀=0.1"
            if abatement_cost == 0.5:

                cost_label = "φ₀=0.5"

            # Hide all traces
            label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

            button = dict(method='update',
                          args=[
                              {
                                  'visible': [False] * (2 * 3 * PathLength),
                                  'showlegend': [False] * (2 * 3 * PathLength),
                              },
                          ],
                          label=label)
            # Enable the two traces we want to see
            # print(button['args'][0]["visible"])

            for j in range(PathLength):

                button['args'][0]["visible"][PathLength*i + j] = True

                button['args'][0]["showlegend"][PathLength*i + j] = True

            i = i+1
            # Add step to step list
            buttons.append(button)

    fig.update_layout(
        updatemenus=[
            dict(
                type="dropdown",
                direction="down",
                buttons=buttons,
                active=3,
                x=0.6,
                y=1.05,
                pad={'r': 10, 't': 10}
            ),
        ],
    )

    fig.update_xaxes(showgrid=False, showline=True,
                     title="Years", range=[0, 40])
    fig.update_yaxes(showgrid=False,
                     showline=True,
                     range=graph_range,
                     title_text=yaxis_label,
                     tickformat=".2f")

    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=1000,
        height=700,
        margin=dict(l=50, r=0))

    return fig


def plot_simulated_stoc_path_full2_split(graph_type, graph_title, yaxis_label, graph_range):

    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01
    # fig = make_subplots(1, 2)
    color = ["#d62728", "darkgreen", "navy", "darkorange"]

    fig = go.Figure()

    # print(group_total)
    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                xi_list_fullaversion = [0.050]

            if abatement_cost == 0.5:

                xi_list_fullaversion = [0.150]

            folder = "./data_simul3/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
                abatement_cost)

            label = "φ₀={:.1f}".format(
                abatement_cost)+r', ρ' + '= {:.2f}'.format(rho)

            i = 0

            for xi in xi_list_fullaversion:
                filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
                    xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

                with open(folder + filename + "model_tech1_pre_damage_UD_simulstoccompile_40direct_direct", "rb") as f:
                    model_tech1_pre_damage = pickle.load(f)

                PathLength = model_tech1_pre_damage["years"].shape[1]
                Years = model_tech1_pre_damage["years"][:, 0]

                Mat = model_tech1_pre_damage[graph_type]


                for j in range(PathLength):

                    tech = model_tech1_pre_damage["tech_activate"][:, j]
                    damage = model_tech1_pre_damage["damage_activate"][:, j]

                    if np.max(tech) == 0 and np.max(damage) == 0:

                        group_name = "No Jump"
                        legend_rank = 1

                    if np.max(tech) == 0 and np.max(damage) == 1:

                        group_name = "Damage Jump"
                        legend_rank = 2

                    if np.max(tech) == 1:
                        group_name = "Techonology Jump"
                        legend_rank = 3

                    legend_name = "Path {}".format(j)

                    if abatement_cost == 0.5 and rho == 1.0:
                        fig.add_trace(go.Scatter(x=Years,
                                                    y=Mat[:, j],
                                                    name=legend_name,
                                                    showlegend=True,
                                                    visible=True,
                                                    legendgroup=group_name,
                                                    legendgrouptitle_text=group_name,
                                                    legendrank=legend_rank
                                                    # line=dict(color=color[i]),
                                                    #  visible=False
                                                    ))
                    else:
                        fig.add_trace(go.Scatter(x=Years,
                                                    y=Mat[:, j],
                                                    name=legend_name,
                                                    showlegend=False,
                                                    visible=False,
                                                    legendgroup=group_name,
                                                    legendgrouptitle_text=group_name,
                                                    legendrank=legend_rank
                                                    # line=dict(color=color[i]),
                                                    #  visible=False
                                                    ))
                i = i+1

    # for i in range(PathLength):
    #     fig.data[3*PathLength + i]["visible"] = True
    #     # fig.data[3*2 + i+12]["visible"] = True

    #     fig.data[3*PathLength + i]["showlegend"] = True
    #     # fig.data[3*2 + 12]["showlegend"] = True

    buttons = []
    i = 0

    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                cost_label = "φ₀=0.1"
            if abatement_cost == 0.5:

                cost_label = "φ₀=0.5"

            # Hide all traces
            label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

            button = dict(method='update',
                          args=[
                              {
                                  'visible': [False] * (2 * 3 * PathLength),
                                  'showlegend': [False] * (2 * 3 * PathLength),
                              },
                          ],
                          label=label)
            # Enable the two traces we want to see
            # print(button['args'][0]["visible"])

            for j in range(PathLength):

                button['args'][0]["visible"][PathLength*i + j] = True

                button['args'][0]["showlegend"][PathLength*i + j] = True

            i = i+1
            # Add step to step list
            buttons.append(button)

    fig.update_layout(
        updatemenus=[
            dict(
                type="dropdown",
                direction="down",
                buttons=buttons,
                active=4,
                x=0.6,
                y=1.05,
                pad={'r': 10, 't': 10}
            ),
        ],
    )

    fig.update_xaxes(showgrid=False, showline=True,
                     title="Years", range=[0, 40])
    fig.update_yaxes(showgrid=False,
                     showline=True,
                     range=graph_range,
                     title_text=yaxis_label,
                     tickformat=".2f")

    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=1000,
        height=700,
        margin=dict(l=50, r=0))

    return fig



def plot_simulated_stoc_path_full2_split2(graph_type, graph_title, yaxis_label, graph_range):

    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01
    # fig = make_subplots(1, 2)
    color = ["#d62728", "darkgreen", "navy", "darkorange"]

    fig = go.Figure()

    # print(group_total)
    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                xi_list_fullaversion = [0.050]

            if abatement_cost == 0.5:

                xi_list_fullaversion = [0.150]

            folder = "./data_simul5/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
                abatement_cost)

            label = "φ₀={:.1f}".format(
                abatement_cost)+r', ρ' + '= {:.2f}'.format(rho)

            i = 0

            for xi in xi_list_fullaversion:
                filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
                    xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

                with open(folder + filename + "model_tech1_pre_damage_UD_simulstoccompile2_40direct_direct", "rb") as f:
                    model_tech1_pre_damage = pickle.load(f)

                PathLength = model_tech1_pre_damage["years"].shape[1]
                Years = model_tech1_pre_damage["years"][:, 0]

                Mat = model_tech1_pre_damage[graph_type]


                for j in range(PathLength):

                    tech = model_tech1_pre_damage["tech_activate"][:, j]
                    damage = model_tech1_pre_damage["damage_activate"][:, j]

                    if np.max(tech) == 0 and np.max(damage) == 0:

                        group_name = "No Jump"
                        legend_rank = 1

                    if np.max(tech) == 0 and np.max(damage) == 1:

                        group_name = "Damage Jump"
                        legend_rank = 2

                    if np.max(tech) == 1:
                        group_name = "Techonology Jump"
                        legend_rank = 3

                    legend_name = "Path {}".format(j+1)

                    if abatement_cost == 0.5 and rho == 1.0:
                        fig.add_trace(go.Scatter(x=Years,
                                                    y=Mat[:, j],
                                                    name=legend_name,
                                                    showlegend=True,
                                                    visible=True,
                                                    legendgroup=group_name,
                                                    legendgrouptitle_text=group_name,
                                                    legendrank=legend_rank
                                                    # line=dict(color=color[i]),
                                                    #  visible=False
                                                    ))
                    else:
                        fig.add_trace(go.Scatter(x=Years,
                                                    y=Mat[:, j],
                                                    name=legend_name,
                                                    showlegend=False,
                                                    visible=False,
                                                    legendgroup=group_name,
                                                    legendgrouptitle_text=group_name,
                                                    legendrank=legend_rank
                                                    # line=dict(color=color[i]),
                                                    #  visible=False
                                                    ))
                i = i+1

    # for i in range(PathLength):
    #     fig.data[3*PathLength + i]["visible"] = True
    #     # fig.data[3*2 + i+12]["visible"] = True

    #     fig.data[3*PathLength + i]["showlegend"] = True
    #     # fig.data[3*2 + 12]["showlegend"] = True

    buttons = []
    i = 0

    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                cost_label = "φ₀=0.1"
            if abatement_cost == 0.5:

                cost_label = "φ₀=0.5"

            # Hide all traces
            label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

            button = dict(method='update',
                          args=[
                              {
                                  'visible': [False] * (2 * 3 * PathLength),
                                  'showlegend': [False] * (2 * 3 * PathLength),
                              },
                          ],
                          label=label)
            # Enable the two traces we want to see
            # print(button['args'][0]["visible"])

            for j in range(PathLength):

                button['args'][0]["visible"][PathLength*i + j] = True

                button['args'][0]["showlegend"][PathLength*i + j] = True

            i = i+1
            # Add step to step list
            buttons.append(button)

    fig.update_layout(
        updatemenus=[
            dict(
                type="dropdown",
                direction="down",
                buttons=buttons,
                active=4,
                x=0.6,
                y=1.05,
                pad={'r': 10, 't': 10}
            ),
        ],
    )

    fig.update_xaxes(showgrid=False, showline=True,
                     title="Years", range=[0, 40])
    fig.update_yaxes(showgrid=False,
                     showline=True,
                     range=graph_range,
                     title_text=yaxis_label,
                     tickformat=".2f")

    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=1000,
        height=800,
        margin=dict(l=50, r=0))

    return fig



def plot_simulated_stoc_path_full2_singapore(graph_type, graph_title, yaxis_label, graph_range):


    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01
    # fig = make_subplots(1, 2)
    color = ["#d62728", "darkgreen", "navy", "darkorange"]

    fig = go.Figure()
    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                xi_list_fullaversion = [0.050]

            if abatement_cost == 0.5:

                xi_list_fullaversion = [0.150]

            folder = "./data_simul2/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
                abatement_cost)
            i = 0
            
            for xi in xi_list_fullaversion:
                filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
                    xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

                with open(folder + filename + "model_tech1_pre_damage_UD_simulstoccompile_40direct_direct", "rb") as f:
                    model_tech1_pre_damage = pickle.load(f)
                
                PathLength = 10
                Years = model_tech1_pre_damage["years"][:,0]
                
                Mat = model_tech1_pre_damage[graph_type][:, 0:PathLength]

                for j in range(5):
                    
                    legend_name = "Path {}".format(j+1)
                    if j==4:
                        j=9
                    fig.add_trace(go.Scatter(x=Years,
                                                y=Mat[:, j],
                                                name=legend_name,
                                                showlegend=True,
                                                visible=True,
                                                line=dict(width=8),
                                                #  visible=False
                                                ))

                fig.update_traces(visible=False, line=dict(width=8))

                i = i+1
    PathLength=5

    for i in range(PathLength):
        fig.data[3*PathLength + i]["visible"] = True
        # fig.data[3*2 + i+12]["visible"] = True

        fig.data[3*PathLength + i]["showlegend"] = True
        # fig.data[3*2 + 12]["showlegend"] = True
    
    buttons = []
    i = 0

    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                cost_label = "φ₀=0.1"
            if abatement_cost == 0.5:

                cost_label = "φ₀=0.5"

            # Hide all traces
            label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

            button = dict(method='update',
                          args=[
                              {
                                  'visible': [False] * (2 * 3 * PathLength ),
                                  'showlegend': [False] * (2 * 3 * PathLength ),
                              },
                          ],
                          label=label)
            # Enable the two traces we want to see
            # print(button['args'][0]["visible"])

            for j in range(PathLength):
                
                button['args'][0]["visible"][PathLength*i + j] = True

                button['args'][0]["showlegend"][PathLength*i + j] = True

            i = i+1
            # Add step to step list
            buttons.append(button)



    fig.update_layout(
        updatemenus=[
            dict(
                type="dropdown",
                direction="down",
                buttons=buttons,
                active=3,
                x=0.6,
                y=1.05,
                pad={'r': 10, 't': 10})
        ],
    )
    
    fig.update_xaxes(showgrid=False, showline=True,
                    title="Years", range=[0, 40], linewidth=8)
    fig.update_yaxes(showgrid=False,
                    showline=True,
                    range=graph_range,
                     title_text=yaxis_label, linewidth=8
                    # tickformat=".2f"
                    )

    fig.update_layout(
        # title=graph_title,
        # barmode="overlay",
        plot_bgcolor="white",
        width=1100,
        height=700,
        font=dict(size=24),
        margin=dict(l=100, r=0,t=0))


    return fig


def plot_simulated_stoc_path_full2_singapore2(graph_type, graph_title, yaxis_label, graph_range):


    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01
    # fig = make_subplots(1, 2)
    color = ["#d62728", "darkgreen", "navy", "darkorange"]
    j_list = [16, 0, 6, 13, 14]
    
    fig = go.Figure()
    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                xi_list_fullaversion = [0.050]

            if abatement_cost == 0.5:

                xi_list_fullaversion = [0.150]

            folder = "./data_simul3/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
                abatement_cost)
            i = 0
            
            for xi in xi_list_fullaversion:
                filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
                    xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

                with open(folder + filename + "model_tech1_pre_damage_UD_simulstoccompile_40direct_direct", "rb") as f:
                    model_tech1_pre_damage = pickle.load(f)
                
                PathLength = 20
                Years = model_tech1_pre_damage["years"][:,0]
                
                Mat = model_tech1_pre_damage[graph_type][:, 0:PathLength]

                for j in range(5):
                    
                    legend_name = "Path {}".format(j+1)
                    j_used = j_list[j]

                    fig.add_trace(go.Scatter(x=Years,
                                                y=Mat[:, j_used],
                                                name=legend_name,
                                                showlegend=True,
                                                visible=True,
                                                line=dict(width=8),
                                                #  visible=False
                                                ))

                fig.update_traces(visible=False, line=dict(width=8))

                i = i+1
    PathLength=5

    for i in range(PathLength):
        fig.data[3*PathLength + i]["visible"] = True
        # fig.data[3*2 + i+12]["visible"] = True

        fig.data[3*PathLength + i]["showlegend"] = True
        # fig.data[3*2 + 12]["showlegend"] = True
    
    buttons = []
    i = 0

    for abatement_cost in [0.1, 0.5]:
        for rho in [0.66, 1.0, 1.5]:

            if abatement_cost == 0.1:

                cost_label = "φ₀=0.1"
            if abatement_cost == 0.5:

                cost_label = "φ₀=0.5"

            # Hide all traces
            label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

            button = dict(method='update',
                          args=[
                              {
                                  'visible': [False] * (2 * 3 * PathLength ),
                                  'showlegend': [False] * (2 * 3 * PathLength ),
                              },
                          ],
                          label=label)
            # Enable the two traces we want to see
            # print(button['args'][0]["visible"])

            for j in range(PathLength):
                
                button['args'][0]["visible"][PathLength*i + j] = True

                button['args'][0]["showlegend"][PathLength*i + j] = True

            i = i+1
            # Add step to step list
            buttons.append(button)



    fig.update_layout(
        updatemenus=[
            dict(
                type="dropdown",
                direction="down",
                buttons=buttons,
                active=3,
                x=0.6,
                y=1.05,
                pad={'r': 10, 't': 10})
        ],
    )
    
    fig.update_xaxes(showgrid=False, showline=True,
                    title="Years", range=[0, 40], linewidth=8)
    fig.update_yaxes(showgrid=False,
                    showline=True,
                    range=graph_range,
                     title_text=yaxis_label, linewidth=8
                    # tickformat=".2f"
                    )

    fig.update_layout(
        # title=graph_title,
        # barmode="overlay",
        plot_bgcolor="white",
        width=1100,
        height=700,
        font=dict(size=24),
        margin=dict(l=100, r=0,t=0))


    return fig





def plot_simulated_stoc_path_full2_selected_mat(graph_type, graph_title, yaxis_label, graph_range):


    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01
    # fig = make_subplots(1, 2)
    color = ["#d62728", "darkgreen", "navy", "darkorange"]
    colors = ['blue','red', 'green', 'cyan', 'purple']

    j_dict = {"phi=0.1,rho=0.66":  [1, 25, 6, 10, 24], 
            "phi=0.1,rho=1.0":  [4, 7, 9, 2, 15],
            "phi=0.1,rho=1.5":  [5, 1, 24, 7, 12],
            "phi=0.5,rho=0.66":  [19, 4, 18, 10, 12],
            # "phi=0.5,rho=1.0":  [4, 24, 20, 5, 12],
            "phi=0.5,rho=1.0":  [16, 0, 2, 13, 14],
            "phi=0.5,rho=1.5":  [2, 7, 3, 24, 21]
            }
    fig = go.Figure()
    # for abatement_cost in [0.1, 0.5]:
    #     for rho in [0.66, 1.0, 1.5]:

    plt.style.use('classic')
    plt.rcParams["savefig.bbox"] = "tight"
    plt.rcParams["figure.figsize"] = (10,8)
    plt.rcParams["figure.dpi"] = 500
    plt.rcParams["font.size"] = 12
    plt.rcParams["legend.frameon"] = False
    plt.rcParams["lines.linewidth"] = 5
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=colors) 
    plt.rcParams['figure.facecolor'] = 'w'
    rho = 1.0
    abatement_cost = 0.5

    if abatement_cost == 0.1:

        xi_list_fullaversion = [0.050]

    if abatement_cost == 0.5:

        xi_list_fullaversion = [0.150]
        

    folder = "./data_simul3/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.2,0.1,0.1_LR_0.0025_FK_phi0_{}/".format(
        abatement_cost)
    i = 0
    label = "phi={},rho={}".format(abatement_cost,rho)
    j_list = j_dict[label]
    PathLength_selected = 5
    for xi in xi_list_fullaversion:
        filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
            xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

        with open(folder + filename + "model_tech1_pre_damage_UD_simulstoccompile_40direct_direct", "rb") as f:
            model_tech1_pre_damage = pickle.load(f)
        
        PathLength = model_tech1_pre_damage["years"].shape[1]
        Years = model_tech1_pre_damage["years"][:,0]
        
        Mat = model_tech1_pre_damage[graph_type][:,0:]

        for j in range(PathLength_selected):
            
            legend_name = "Path {}".format(j+1)
            j_used = j_list[j]

            # if abatement_cost ==0.5 and rho==1.0:
            #     fig.add_trace(go.Scatter(x=Years,
            #                                 y=Mat[:, j_used],
            #                                 name=legend_name,
            #                                 showlegend=True,
            #                                 visible=True,
            #                                 # line=dict(width=8),
            #                                 #  visible=False
            #                                 ))
            # else:
            #     fig.add_trace(go.Scatter(x=Years,
            #                                 y=Mat[:, j_used],
            #                                 name=legend_name,
            #                                 showlegend=False,
            #                                 visible=False,
            #                                 # line=dict(width=8),
            #                                 #  visible=False
            #                                 ))


            plt.plot(Years, Mat[:, j_used],label=legend_name,linewidth=5.0)
        # fig.update_traces(visible=False, line=dict(width=8))
        # fig.update_traces(visible=False)
        

        i = i+1
    plt.legend(loc="upper left")
    plt.xlim(0,40)
    plt.xlabel("Years")
    plt.ylim(graph_range)
    if graph_type =="RD_Plot":
        plt.ylabel("% of GDP")
    # for i in range(PathLength_selected):
    #     fig.data[4*PathLength_selected + i]["visible"] = True
    #     # fig.data[3*2 + i+12]["visible"] = True

    #     fig.data[4*PathLength_selected + i]["showlegend"] = True
    #     # fig.data[3*2 + 12]["showlegend"] = True
    
    buttons = []
    i = 0

    # for abatement_cost in [0.1, 0.5]:
    #     for rho in [0.66, 1.0, 1.5]:

    #         if abatement_cost == 0.1:

    #             cost_label = "φ₀=0.1"
    #         if abatement_cost == 0.5:

    #             cost_label = "φ₀=0.5"

    #         # Hide all traces
    #         label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

    #         button = dict(method='update',
    #                       args=[
    #                           {
    #                               'visible': [False] * (2 * 3 * PathLength_selected ),
    #                               'showlegend': [False] * (2 * 3 * PathLength_selected ),
    #                           },
    #                       ],
    #                       label=label)
    #         # Enable the two traces we want to see
    #         # print(button['args'][0]["visible"])

    #         for j in range(PathLength_selected):
                
    #             button['args'][0]["visible"][PathLength_selected*i + j] = True

    #             button['args'][0]["showlegend"][PathLength_selected*i + j] = True

    #         i = i+1
    #         # Add step to step list
    #         buttons.append(button)



    # fig.update_layout(
    #     updatemenus=[
    #         dict(
    #             type="dropdown",
    #             direction="down",
    #             buttons=buttons,
    #             active=4,
    #             x=0.6,
    #             y=1.05,
    #             pad={'r': 10, 't': 10})
    #     ],
    # )
    
    # fig.update_xaxes(showgrid=False, showline=True,
    #                 title="Years", range=[0, 40])
    # fig.update_yaxes(showgrid=False,
    #                 showline=True,
    #                 range=graph_range,
    #                 title_text=yaxis_label,
    #                 tickformat=".2f")

    # fig.update_layout(
    #     title=graph_title,
    #     barmode="overlay",
    #     plot_bgcolor="white",
    #     width=1000,
    #     height=800,
    #     margin=dict(l=50, r=0))


    return 0





def plot_simulatedpath_full2_delta(graph_type, graph_title, yaxis_label, graph_range, before15):

    xi_base = 100000.
    psi_0 = 0.10583
    psi_1 = 0.5
    varrho = 1120.0
    delta = 0.01
    # fig = make_subplots(1, 2)
    color = ["#d62728", "darkgreen", "navy", "darkorange"]

    fig = go.Figure()
    # for abatement_cost in [0.1, 0.5]:
    #     for rho in [0.66, 1.0, 1.5]:
    abatement_cost = 0.5
    rho = 1.0

    if abatement_cost == 0.1:

        xi_list_fullaversion = [0.025, 0.050, 100000.]
        xi_list_uncertaintydecomp = [0.050]

    if abatement_cost == 0.5:

        xi_list_fullaversion = [0.075, 0.150, 100000.]

        xi_list_uncertaintydecomp = [0.150]

    delta_list = [0.010, 0.015, 0.020]

    folder = "./data_simul7/2jump_step_4.00,9.00_0.0,4.0_1.0,6.0_0.0,3.0_SS_0.1,0.1,0.1_LR_0.025_FK2_phi0_{}/".format(
        abatement_cost)
    i = 0

    for delta in delta_list:
        xi = 0.150
        filename = "xi_a_{}_xi_k_{}_xi_c_{}_xi_j_{}_xi_d_{}_xi_g_{}_psi_0_{}_psi_1_{}_varrho_{}_rho_{}_delta_{}_" .format(
            xi_base, xi, xi, xi, xi, xi, psi_0, psi_1, varrho, rho, delta)

        with open(folder + filename + "model_tech1_pre_damage_UD_simul_40direct_direct", "rb") as f:
            model_tech1_pre_damage = pickle.load(f)
        # print(model_tech1_pre_damage.keys())
        # print(filename)
        # label = r'ξᵣ = {:.1f}'.format(xi_list_fullaversion[i])
        # if xi == 100000.:
        #     label = "Baseline"
        # if xi == 0.050 or xi == 0.150:
        #     label = "Less Aversion"
        # if xi == 0.025 or xi == 0.075:
        #     label = "More Aversion"

        label = "δ={:.3f}".format(delta)
        # print(model_tech1_pre_damage[graph_type])
        if graph_type=="hkt" or graph_type=="hjt":
            if before15 == False:
                fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"],
                                        y=-model_tech1_pre_damage[graph_type],
                                        name=label,
                                        showlegend=False,
                                        visible=False,                                     line=dict(color=color[i]),
                                        #  visible=False
                                        ))
            elif before15 == True:
                fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                        y=-model_tech1_pre_damage[graph_type][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                        name=label,
                                        showlegend=False,
                                        visible=False,                                     line=dict(color=color[i]),
                                        #  visible=False
                                        ))
        elif graph_type=="CapIOutputRatio":
            Y_Plot = model_tech1_pre_damage["i"]/(alpha * np.exp(model_tech1_pre_damage["states"][:, 0]))*100
            if before15 == False:
                fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"],
                                        y=Y_Plot,
                                        name=label,
                                        showlegend=False,
                                        visible=False,                                     line=dict(color=color[i]),
                                        #  visible=False
                                        ))
            elif before15 == True:
                fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                        y=Y_Plot,
                                        name=label,
                                        showlegend=False,
                                        visible=False,                                     line=dict(color=color[i]),
                                        #  visible=False
                                        ))
        else:
            if before15 == False:
                fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"],
                                            y=model_tech1_pre_damage[graph_type],
                                            name=label,
                                            showlegend=True,
                                            visible=True,                                     line=dict(color=color[i]),
                                            #  visible=False
                                            ))
            elif before15 == True:
                fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                            y=model_tech1_pre_damage[graph_type][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                            name=label,
                                            showlegend=True,
                                            visible=True,                                     line=dict(color=color[i]),
                                            #  visible=False
                                            ))
        i = i+1

    # for i in range(3):
    #     fig.data[3*4 + i]["visible"] = True
    #     # fig.data[3*2 + i+12]["visible"] = True
        
    #     fig.data[3*4 + i]["showlegend"] = True
    #     # fig.data[3*2 + 12]["showlegend"] = True




    # buttons = []
    # i = 0

    # for abatement_cost in [0.1, 0.5]:
    #     for rho in [0.66, 1.0, 1.5]:

    #         if abatement_cost == 0.1:

    #             xi_list = [0.025, 0.050]
    #             cost_label = "φ₀=0.1"
    #         if abatement_cost == 0.5:

    #             xi_list = [0.075, 0.150]
    #             cost_label = "φ₀=0.5"

    #         # Hide all traces
    #         label = cost_label+r', ρ' + '= {:.2f}'.format(rho)

    #         button = dict(method='update',
    #                       args=[
    #                           {
    #                               'visible': [False] * (2 * 3 * 4 * 2),
    #                               'showlegend': [False] * (2 * 3 * 4 * 2),
    #                           },
    #                       ],
    #                       label=label)
    #         # Enable the two traces we want to see
    #         # print(button['args'][0]["visible"])

    #         button['args'][0]["visible"][3*i + 0] = True
    #         button['args'][0]["visible"][3*i + 1] = True
    #         button['args'][0]["visible"][3*i + 2] = True

    #         button['args'][0]["showlegend"][3*i + 0] = True
    #         button['args'][0]["showlegend"][3*i + 1] = True
    #         button['args'][0]["showlegend"][3*i + 2] = True

    #         i = i+1
    #         # Add step to step list
    #         buttons.append(button)

    # fig.update_layout(
    #     updatemenus=[
    #         dict(
    #             type="buttons",
    #             buttons=buttons,
    #             # direction="right",
    #             active=4,
    #             x=1.3,
    #             y=0.7,
    #             # xanchor="left",
    #             # yanchor="top",
    #             pad={"r": 10,
    #                  "t": 10, "b": 10},
    #             showactive=True
    #         )
    #     ])

    fig.update_xaxes(showgrid=False, showline=True,
                     title="Years", range=[0, 40])
    fig.update_yaxes(showgrid=False,
                     showline=True,
                     range=graph_range,
                     title_text=yaxis_label,
                     tickformat=".2f")
    # fig.update_yaxes(showgrid=False, showline=True,
    #                  range=[1., 2.1], col=2, row=1)
    # fig.update_yaxes(tickvals=[1, 1.2, 1.4, 1.5, 1.6, 1.8, 2.0],
    #                  tickformat=".1f",
    #                  col=2,
    #                  row=1)
    # fig.update_layout(height=400, width=1280)
    fig.update_layout(
        title=graph_title,
        barmode="overlay",
        plot_bgcolor="white",
        width=800,
        height=500,
        margin=dict(l=50, r=0))

    return fig

