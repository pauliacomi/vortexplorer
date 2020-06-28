import copy
from datetime import datetime
import pandas as pd

from src.palette import palette, graph_custom


def generate_overview_year(data, column="AVG"):

    dff = pd.DataFrame({key: data[key] for key in [column, "Released"]})
    try:
        dff.index = pd.to_datetime(dff["Released"], format="%Y")
        dff = dff.resample('A').agg({'Released': 'count', column: 'mean'})
    except:
        dff.index = pd.to_datetime(dff["Released"], format="%b-%d-%Y")
        dff = dff.resample('M', label='left').agg({
            'Released': 'count',
            column: 'mean'
        })

    data = [
        dict(
            type="bar",
            x=dff.index,
            y=dff["Released"],
            name="All years",
            hovertemplate=
            "<b> %{x}: </b> <br> Albums: %{y} <br> Average: %{marker.color:.2f}<extra></extra>",
            marker={
                'color': dff[column],
                'showscale': True,
                'colorbar': {
                    'title': {
                        'text': 'Average'
                    }
                },
            },
            colorscale='inferno'
        ),
    ]
    layout = copy.deepcopy(graph_custom)
    layout.update(
        dict(
            title="Albums throughout time",
            yaxis={
                'title': 'Number of albums',
                'gridcolor': palette['white'],
                'gridwidth': 1,
                'showgrid': True,
            },
            xaxis={
                'title': 'Time',
            },
            dragmode='select',
            selectdirection='h',
        )
    )
    return {'data': data, 'layout': layout}


def generate_overview_year_tbl(data, sel_year, sel_stats, column="AVG"):

    dff = pd.DataFrame({
        key: data[col]
        for key, col in zip(
            ["Released", "Artist", "Album", "AVG", "Votes"],
            ["Released", "Artist", "Album", column, "Votes"],
        )
    })

    year_fmt = "%Y"

    try:
        dff["Released"] = pd.to_datetime(dff["Released"], format="%Y")
    except:
        year_fmt = '%b-%m'
        dff["Released"] = pd.to_datetime(dff["Released"], format="%b-%d-%Y")

    if sel_year is not None:
        start = datetime.strptime(sel_year["range"]['x'][1][:10], "%Y-%m-%d")
        end = datetime.strptime(sel_year["range"]['x'][0][:10], "%Y-%m-%d")
        dff = dff[dff['Released'].between(start, end)]

    if sel_stats is not None:
        start = sel_stats["range"]['x'][0]
        end = sel_stats["range"]['x'][1]
        dff = dff[dff[column].between(start, end)]

    dff['Released'] = dff['Released'].apply(lambda x: x.strftime(year_fmt))
    return dff.to_dict('records')
