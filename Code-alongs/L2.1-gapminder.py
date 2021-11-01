import plotly_express as px

gapminder = px.data.gapminder()

africa = gapminder[gapminder["continent"]=="Africa"]
asia = gapminder[gapminder["continent"]=="Asia"]
europe = gapminder[gapminder["continent"]=="Europe"]
americas = gapminder[gapminder["continent"]=="Americas"]


fig = px.scatter(americas, x="gdpPercap", 
    y="lifeExp", 
    size = "pop", 
    color = "country",
    size_max= 70, 
    log_x=True, 
    animation_frame="year",
    title = "Americas",
    range_x = [100,100000],
    range_y = [25,90])

fig.show()