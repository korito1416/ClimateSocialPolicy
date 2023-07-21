import plotly.io as pio
import plotly.offline as pyo
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os
import sys
import pickle
sys.path.append(os.path.dirname(os.getcwd()))
pyo.init_notebook_mode()
pio.templates.default = "none"

theta_list = pd.read_csv('data/model144.csv', header=None).to_numpy()[:, 0] / 1000.
gamma_3_list = np.linspace(0, 1./3, 20)
xi_list_fullaversion_low = [0.025, 0.050, 10000.]
xi_list_fullaversion_high = [0.075, 0.150, 10000.]
xi_list_uncertainty_low = [0.050]
xi_list_uncertainty_high = [0.150]




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
        fig.data[2*2 + i]["visible"] = True
        fig.data[2*2 + i+12]["visible"] = True
        
        fig.data[2*2 + i]["showlegend"] = True
        fig.data[2*2 + 12]["showlegend"] = True


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
                active=2,
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
        fig.data[2*2 + i]["visible"] = True
        fig.data[2*2 + i+12]["visible"] = True
        
        fig.data[2*2 + i]["showlegend"] = True
        fig.data[2*2 + 12]["showlegend"] = True


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
                active=2,
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
        fig.data[3*2 + i]["visible"] = True
        # fig.data[3*2 + i+12]["visible"] = True
        
        fig.data[3*2 + i]["showlegend"] = True
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
                active=2,
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
                if before15 == False:
                    fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"],
                                             y=model_tech1_pre_damage[graph_type],
                                             name=label,
                                             showlegend=False,
                                             visible=False,
                                             line=dict(color=color[xi_num]),
                                             #  visible=False
                                             ))
                elif before15 == True:
                    fig.add_trace(go.Scatter(x=model_tech1_pre_damage["years"][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                             y=model_tech1_pre_damage[graph_type][model_tech1_pre_damage["states"][:, 1] < 1.5],
                                             name=label,
                                             showlegend=False,
                                             visible=False,
                                             line=dict(color=color[xi_num]),

                                             #  visible=False
                                             ))

    for i in range(4):
        fig.data[4*2 + i]["visible"] = True
        # fig.data[3*2 + i+12]["visible"] = True
        
        fig.data[4*2 + i]["showlegend"] = True
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
                active=2,
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
