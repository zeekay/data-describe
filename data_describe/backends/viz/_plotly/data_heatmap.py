from typing import List

import numpy as np
from plotly.offline import init_notebook_mode, iplot
from IPython import get_ipython
import plotly.graph_objs as go

from data_describe.config._config import get_option


def viz_data_heatmap(data, colnames: List[str], missing: bool = False, **kwargs):
    """Plots the data heatmap.

    Args:
        data: The dataframe
        colnames: The column names, used for tick labels
        missing: If True, plots missing values instead
        kwargs: Keyword arguments passed to seaborn.heatmap
    """
    data_fig = go.Heatmap(
        z=np.flip(data.values, axis=0),
        x=list(range(data.shape[0])),
        y=list(colnames[::-1]),
        ygap=1,
        zmin=-3,
        zmax=3,
        colorscale="Viridis" if not missing else "gray",
        colorbar={"title": "z-score (bounded)"},
    )

    figure = go.Figure(
        data=[data_fig],
        layout=go.Layout(
            autosize=False,
            title={
                "text": "Data Heatmap",
                "font": {"size": get_option("display.plotly.title_size")},
            },
            width=get_option("display.plotly.fig_width"),
            height=get_option("display.plotly.fig_height"),
            xaxis=go.layout.XAxis(ticks="", title="Record #", showgrid=False),
            yaxis=go.layout.YAxis(
                ticks="", title="Variable", automargin=True, showgrid=False
            ),
            plot_bgcolor="rgb(0,0,0,0)",
            paper_bgcolor="rgb(0,0,0,0)",
        ),
    )

    if get_ipython() is not None:
        init_notebook_mode(connected=True)
        return iplot(figure, config={"displayModeBar": False})
    else:
        return figure
