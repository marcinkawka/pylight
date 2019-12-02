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
        id='moj_wykres',
        figure={
            'data': [{'x': df_pogoda.index, 'y': df_pogoda['temp_min'], 'type': 'line', 'name': 'temperatura minimalna'},
                {'x': df_pogoda.index, 'y': df_pogoda['temp_max'], 'type': 'line', 'name': 'temperatura maksymalna'}
            ],
            'layout': {
                'title': 'Temperatura'
            }
        }
    )
#Możemy dodać statyczną listę rozwijaną
prosta_lista_rozwijana = dcc.Dropdown(
    id='statyczna_lista',
    options=[
        {'label': 'Opcja Pierwsza', 'value': 'v3'},
        {'label': 'Opcja Lepsza', 'value': 'v2'},
        {'label': 'Fatalna Opcja', 'value': 'v1'}
    ],
    multi=True,
    value='v1'
)  
#ale możemy też listę wygenerować automatycznie na podstawie naszego DataFrame
automatyczna_lista_rozwijana = dcc.Dropdown(
    id='automatyczna_lista',
    options=[{'label':kolumna,'value':kolumna} for kolumna in df.columns],
    value='temp_min'
)  

app.layout = html.Div(children=[
    html.H1(children='Hello PyLight'),
    html.Div(children=''' Wybierz element z listy rozwijanej '''),
    #prosta_lista_rozwijana,
    automatyczna_lista_rozwijana,
    html.H3('Dzięki callbeckowi wykres dostosuje się do wybranego elementu'),
    jakis_wykres
])

#Dekorator dla funkcji poniżej
@app.callback(
    dash.dependencies.Output('moj_wykres', 'figure'),   #w ramach reakcji podmień figure w elemencie moj_wykres
    [dash.dependencies.Input('automatyczna_lista', 'value')]) #przekaż do funkcji update wybraną z listy wartość

def uaktualnij_wykres(value):
    return {
            'data': [{'x': df.index, 'y': df['temp_min'], 'type': 'line', 'name': 'temperatura minimalna'},
                {'x': df.index, 'y': df[value], 'type': 'line', 'name': value}
            ],
            'layout': {
                'title': 'Temperatura'
            }
        }

#uruchamiamy aplikację
app.run_server(debug=True)