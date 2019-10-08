import dash
import dash_html_components as html
import plotly.graph_objs as go

import psycopg2 #postgres connection lib


app = dash.Dash(__name__,)

# Plotly mapbox public token
mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNqdnBvNDMyaTAxYzkzeW5ubWdpZ2VjbmMifQ.TXcBE-xg9BFdV2ocecc_7g"

# dictionary items for dropdown
list_of_countries = {
    "Angola": "angola_analysis.html",
    "Botswana": "angola_analysis.html",
    "Burundi": "angola_analysis.html",
    "DRC": "angola_analysis.html",
    "Djibouti": "angola_analysis.html",
    "Egypt": "angola_analysis.html",
    "Ethiopia": "angola_analysis.html",
    "India": "angola_analysis.html",
    "Kenya": "angola_analysis.html",
    "Lesotho": "angola_analysis.html",
    "Libya": "angola_analysis.html",
    "Malawi": "angola_analysis.html",
    "Mozambique": "angola_analysis.html",
    "Namibia": "angola_analysis.html",
    "Rwanda": "angola_analysis.html",
    "South Africa": "angola_analysis.html",
    "Sudan": "angola_analysis.html",
    "Swaziland": "angola_analysis.html", 
    "Tanzania": "angola_analysis.html", 
    "Uganda": "angola_analysis.html", 
    "Zambia": "angola_analysis.html", 
    "Zimbabwe": "angola_analysis.html",
}

list_of_energies = {
	"CSP", "PV", "Wind",
}

try:
	#connect to server
	conn = psycopg2.connect(host="localhost", port="5432", database="mapre", user="Anaavu", password="")
	#create cursor to execute SQL commands
	cur = conn.cursor()
	#the SQL query to execute
	cur.execute('SELECT version()')
	#retrieve query result
	db_version = cur.fetchone()
	print(db_version)

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)




app.layout = html.Div([
    html.H2("Analysis",
            style={'textAlign': 'center', 'color': '#7FDBFF'}),

    html.Iframe(id='anal', srcDoc=open("angola_analysis.html", "r").read(),
    	style={'display': 'inline-block', 'width': '100%', 'height': '800px'}),
],
)

if __name__ == '__main__':
    app.run_server(port=8080, debug=True)
