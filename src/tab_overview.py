import dash_table as dt
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from src.palette import palette, graph_custom


def tab_overview():
    return [
        # Explanation and details
        dbc.Row(
            dbc.Col(
                children=[
                    html.Div(
                        id="description-card",
                        children=[
                            html.H3("General overview of the spreadsheet"),
                            dbc.Card(
                                """Drag to select on the top graphs, the table will update based on this selection. """
                                """Clicking on the table headers will sort, while typing in the first row will search. """
                                """Searching for numbers and dates takes ranges: ">3" means above average of 3. """,
                                body=True,
                                id="intro"
                            ),
                        ],
                    ),
                ]
            ),
            className="mb-4 mt-4",
        ),
        # Dataset details
        dbc.Row(
            dbc.Col(
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardBody([
                                html.H4(
                                    "Card title",
                                    id="card-album-number",
                                    className="card-title"
                                ),
                                html.P(
                                    "Number of albums", className="card-text"
                                ),
                            ]),
                        ]),
                    ),
                    dbc.Col(
                        dbc.Card([
                            dbc.CardBody([
                                html.H4(
                                    "Card title",
                                    id="card-artist-number",
                                    className="card-title"
                                ),
                                html.P(
                                    "Number of artists", className="card-text"
                                ),
                            ]),
                        ]),
                    ),
                    dbc.Col(
                        dbc.Card([
                            dbc.CardBody([
                                html.H4(
                                    "Card title",
                                    id="card-overall-avg",
                                    className="card-title"
                                ),
                                html.P(
                                    children=[
                                        "Vote average  ",
                                        dbc.Checklist(
                                            options=[
                                                {
                                                    "label": "Use wAVG?",
                                                    "value": False
                                                },
                                            ],
                                            id="average-select",
                                            switch=True,
                                            inline=True,
                                            style={"display": "inline"}
                                        ),
                                    ],
                                    className="card-text"
                                ),
                            ]),
                        ]),
                    ),
                ]),
            ),
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id="overview_year", figure={'layout': graph_custom}
                    ),
                    md=6,
                ),
                dbc.Col(
                    dcc.Graph(
                        id="overview_stats", figure={'layout': graph_custom}
                    ),
                    md=6,
                ),
            ],
            className="mb-4 mt-4",
        ),
        dbc.Row(
            [
                dbc.Col(
                    dt.DataTable(
                        id='overview_year_tbl',
                        columns=[
                            {
                                'id': "Released",
                                'name': 'Released'
                            },
                            {
                                'id': "Artist",
                                'name': 'Artist'
                            },
                            {
                                'id': "Album",
                                'name': 'Album'
                            },
                            {
                                'id': "AVG",
                                'name': 'Average'
                            },
                            {
                                'id': "Votes",
                                'name': '#Votes'
                            },
                        ],
                        style_header={'backgroundColor': palette['black']},
                        style_cell={
                            'backgroundColor': 'rgb(50, 50, 50)',
                            'color': palette['white'],
                            'border': '1px solid black'
                        },
                        style_filter={
                            'backgroundColor': palette['lblue'],
                            'color': palette['white']
                        },
                        page_size=12,
                        sort_action='native',
                        filter_action='native',
                        style_as_list_view=True,
                    ),
                ),
            ],
            className="mb-4 mt-4",
        )
    ]
