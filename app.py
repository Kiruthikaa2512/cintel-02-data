import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins #This package provides the palmer penguins dataset

#Loading Palmerpenguins Dataset
penguins_df=palmerpenguins.load_penguins()

ui.page_opts(title="Penguin Explorer – Dashboard by Kiruthikaa", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
