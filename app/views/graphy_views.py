from math import pi
from django.contrib.auth.decorators import login_required
from bokeh.embed import components
from bokeh.layouts import grid
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
from django.shortcuts import render
from ..services import tarefa_service
import pandas as pd
from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap
from bokeh.transform import cumsum

@login_required()
def plot_multi(request):

    qs = tarefa_service.grafico_autor(request.user)
    data = pd.DataFrame(qs)
    source = ColumnDataSource(data)
    p = figure(plot_width=600, plot_height=200, toolbar_location="above", tools="pan,save,box_zoom,reset")
    p.circle(x='custo_unidade', y='preco_venda', source=source, size=10, color='black')
    p.title.text = 'Elementos'
    p.xaxis.axis_label = 'Custo'
    p.yaxis.axis_label = 'Preço de Venda'
    hover = HoverTool()
    hover.tooltips = [
        ("", "@unidade / @produto/ @custo_unidade/ @preco_venda")
    ]
    hover.mode = 'vline'
    p.add_tools(hover)
    return (p)

@login_required()
def plot_pie(request):
    qs = tarefa_service.grafico_autor(request.user)
    data = pd.DataFrame(qs)
    data['lucro'] = data['preco_venda'] - data['custo_unidade']
    data['unidade'] = data['unidade'].str.upper()
    group_autor = data.groupby('unidade').sum()
    source = ColumnDataSource(group_autor)
    unid = source.data['unidade'].tolist()
    data['angle'] = data['lucro'] / data['lucro'].sum() * 2 * pi
    p = figure(plot_height=400, plot_width=500, title="Lucro em Unidades", toolbar_location="above",
               tools="pan,save,box_zoom,reset", tooltips="@unidade: @lucro R$", x_range=(-0.45, 1.25))
    color_map = factor_cmap(field_name='unidade', palette=Spectral5, factors=unid)
    p.wedge(x=0, y=0.8, radius=0.14,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", color=color_map, legend='unidade', source=data)
    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None
    return [p]

@login_required()
def plot_histo(request):
    qs = tarefa_service.grafico_autor(request.user)
    data = pd.DataFrame(qs)
    data['estoque'] = data['quant_compra'] - data['quant_venda']
    data['unidade'] = data['unidade'].str.upper()
    group_autor = data.groupby('unidade').sum()
    source = ColumnDataSource(group_autor)
    unid=source.data['unidade'].tolist()
    p = figure(x_range=unid, plot_width=800, plot_height=200, toolbar_location="above", tools="pan,save,box_zoom,reset")
    color_map = factor_cmap(field_name='unidade', palette=Spectral5, factors=unid)
    p.vbar(x='unidade', top='estoque', source=source, width=0.60, color=color_map)
    p.title.text = 'Estoque'
    p.xaxis.axis_label = 'Unidade'
    p.yaxis.axis_label = 'Estoque'
    hover = HoverTool()
    hover.tooltips = [
        ("", "@unidade / @estoque unidades")
    ]
    hover.mode = 'vline'
    p.add_tools(hover)
    return [p]

@login_required()
def plot_histdif(request):
    qs = tarefa_service.grafico_autor(request.user)
    data = pd.DataFrame(qs)
    data['lucro']=data['preco_venda']-data['custo_unidade']
    group_autor = data.groupby('unidade').sum()
    source = ColumnDataSource(group_autor)
    unid = source.data['unidade'].tolist()
    p = figure(y_range=unid, plot_width=800, plot_height=200, toolbar_location="above", tools="pan,save,box_zoom,reset")
    p.hbar_stack(['custo_unidade','preco_venda', 'lucro'],
                 y='unidade', height=0.80, color=("grey", "lightgrey" , "black"), source=source, )
    p.title.text = 'Análise por Unidade'
    p.xaxis.axis_label = 'Custo|Preço|Lucro'
    p.xgrid.grid_line_color = None  # remove the x grid lines
    p.yaxis.axis_label = 'Unidade'
    hover = HoverTool()
    hover.tooltips = [
        ("", "@unidade Custo @custo_unidade/ Preco @preco_venda / Lucro @lucro ")
    ]
    hover.mode = 'vline'
    p.add_tools(hover)
    return [p]

@login_required()
def plot_pere(request):
    qs = tarefa_service.grafico_autor(request.user)
    data = pd.DataFrame(qs)
    data['lucro']=data['preco_venda']-data['custo_unidade']
    data['estoque'] = data['quant_compra'] - data['quant_venda']
    group_autor = data.groupby('perecibilidade').sum()
    source = ColumnDataSource(group_autor)
    unid = source.data['perecibilidade'].tolist()
    p = figure(y_range=unid, plot_width=800, plot_height=200, toolbar_location="above", tools="pan,save,box_zoom,reset")
    p.hbar_stack(['quant_venda','estoque'],
                 y='perecibilidade', height=0.80, color=("blue", "lightblue"), source=source, )
    p.title.text = 'Análise Perecibilidade'
    p.xaxis.axis_label = 'Quantidade vendida|Estoque'
    p.xgrid.grid_line_color = None  # remove the x grid lines
    p.yaxis.axis_label = 'Perecibilidade'
    hover = HoverTool()
    hover.tooltips = [
        ("", "@perecibilidade/ @estoque unidades/ Lucro @lucro R$")
    ]
    hover.mode = 'vline'
    p.add_tools(hover)
    return [p]

# tuple list grid
@login_required()
def grid_plot(request):
    l = grid([
        plot_pie(request),
        plot_multi(request),
        plot_histo(request),
        plot_histdif(request),
        plot_pere(request)
    ], sizing_mode='stretch_both')
    script, div = components(l)
    return render(request, 'tarefas/graphy_tarefa.html', {'script': script, 'div': div})