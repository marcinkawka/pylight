import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd 

#przygotowanie danych
df =pd.read_csv('dane_zsumowane_z_pogoda.csv')
df['dzien']=pd.to_datetime(df['Data'])
df.set_index(['dzien'],inplace=True)

#dane pogodowe w DataFramie
df_pogoda = df[['temp_min','temp_max','temp_avg','deszcz','snieg']]

#Można to zrobić ładnie
#elegancki_arkusz_stylow = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
ladne_kolory={
    'background': '#111111',
    'text': '#7FDBFF'
}
#app = dash.Dash(__name__, external_stylesheets=elegancki_arkusz_stylow)

#Można to zrobić na szybko
app = dash.Dash("Mój pierwszy daszbord")


jakis_wykres = dcc.Graph(
        id='example-graph',
        figure={
            'data': [{'x': df_pogoda.index, 'y': df_pogoda['temp_min'], 'type': 'line', 'name': 'temperatura minimalna'},
                {'x': df_pogoda.index, 'y': df_pogoda['temp_max'], 'type': 'line', 'name': 'temperatura maksymalna'}
            ],
            'layout': {
                'title': 'Temperatura'
            }
        }
    )



app.layout = html.Div(children=[
    html.H1(children='Hello PyLight'),
    html.Div(children=''' Paragragraf1 '''),
    jakis_wykres,
    html.H2(children='Moje ulubione strony'),
    html.A('Zapraszam na witrynę Pylight',href='http://www.pylight.org')
])

#uruchamiamy aplikację
app.run_server(debug=True)