import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime

st.set_page_config(layout="centered")

hide_streamlit_style = """
<style>
.css-hi6a2p {padding-top: 0rem;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

pt = datetime.today().strftime('%Y-%m-%d')

df = pd.DataFrame([
    dict(Task="athenahealth", Start='2018-02-14', Finish='2019-10-14', Resource=1),
    dict(Task="Lincoln Financial Group", Start='2019-10-15', Finish='2021-06-29', Resource=1),
    dict(Task="Lincoln Financial Group", Start='2021-06-29', Finish=pt, Resource=1)

    # dict(Resource="p"),
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Start",
hover_name = "Task",  
                  color_discrete_sequence=px.colors.diverging.delta
                  , opacity=.7
                  , title="<b>Interactive Resume: Work History</b>"
                    ,hover_data={"Start": False,
                              "Finish": False,
                              "Task": False,
                              "Resource": False}

                  )

fig.update_layout(

        showlegend=False
        ,yaxis_visible=False
        ,yaxis_showticklabels=False
        ,paper_bgcolor="#FFFFFF"
        ,yaxis_range=['2006-02-28','2020-04-15']
        ,plot_bgcolor = "#FFFFFF"
       , xaxis_range=[df.Start.min(), df.Finish.max()]
        ,xaxis = dict(
        showgrid=False
        ,rangeslider_visible=False
        ,side ="bottom"
        ,tickmode = 'array'
        ,ticks="outside"
        ,zeroline=True
        ,showline=True
        ,ticklen=20
        ,tickfont=dict(
            family='Serif',size=22,color="#100700")),
        hoverlabel = dict(
            bgcolor="white",
            font_size=16,
            font_family="Rockwell")

)

fig.update_traces(width=9, line_color='black', selector=dict(fill='toself'),
                  hovertemplate = "Country:%{label}: <br>Population: %{value} </br> iso num:%{customdata}")
fig.update_xaxes(range=['2016-02-28', pt])
fig.add_annotation(ax=0, ay=-200,
                   x = pd.Timestamp('2021-06-20') + (pd.Timestamp(pt) - pd.Timestamp('2021-06-20'))/2, y = 1.4,
            text="Senior Data Scientist",
            arrowhead=6,
           arrowsize=2,
           arrowwidth=1

                   )

fig.add_annotation(ax=0, ay=-100,
                   x = pd.Timestamp('2019-10-15') + (pd.Timestamp('2021-06-29') - pd.Timestamp('2019-10-15'))/2, y = 1.4,
            text="Data Scientist",
            arrowhead=6,
           arrowsize=2,
           arrowwidth=1

                   )

fig.add_annotation(ax=0, ay=-150,
                   x = pd.Timestamp('2018-02-14') + (pd.Timestamp('2019-10-14') - pd.Timestamp('2018-02-14'))/2, y = 1.4,
            text="Senior UX Researcher",
            arrowhead=6,
           arrowsize=2,
           arrowwidth=1

                   )

fig.add_annotation(ax=0, ay=-75,
                   x = pd.Timestamp('2016-12-01') + (pd.Timestamp('2017-01-31') - pd.Timestamp('2016-12-01'))/2, y = 1.4,
            text="UX/Data Analyst Intern",
            arrowhead=6,
           arrowsize=2,
           arrowwidth=1

                   )
st.plotly_chart(fig, user_container_width = True)

pf = pd.DataFrame([
    dict(Task="Rowan University", Start='2007-09-01', Finish='2011-05-15', Resource=1),
    dict(Task="Rutgers University", Start='2011-09-01', Finish='2013-05-15', Resource=1),
    dict(Task="Stony Brook University", Start='2014-09-01', Finish='2016-05-15', Resource=1),
    dict(Task="Stony Brook University", Start='2016-05-16', Finish= '2019-05-15', Resource=1)

    # dict(Resource="p"),
])

dig = px.timeline(pf, x_start="Start", x_end="Finish", y="Resource", color="Start",
hover_name = "Task", 
                  color_discrete_sequence=px.colors.diverging.Fall
                  , opacity=.7
                  , title="<b>Interactive Resume: Academic History</b>"
                    ,hover_data={"Start": False,
                              "Finish": False,
                              "Task": False,
                              "Resource": False}

                  )
dig.update_layout(

        showlegend=False
        ,yaxis_visible=False
        ,yaxis_showticklabels=False
        ,paper_bgcolor="#FFFFFF"
        ,yaxis_range=['2006-02-28','2020-04-15']
        ,plot_bgcolor = "#FFFFFF"
       , xaxis_range=[df.Start.min(), df.Finish.max()]
        ,xaxis = dict(
        showgrid=False
        ,rangeslider_visible=False
        ,side ="bottom"
        ,tickmode = 'array'
        ,ticks="outside"
        ,zeroline=True
        ,showline=True
        ,ticklen=20
        ,tickfont=dict(
            family='Serif',size=22,color="#100700")),
        hoverlabel = dict(
            bgcolor="white",
            font_size=16,
            font_family="Rockwell")

)

dig.update_traces(width=9, line_color='black', selector=dict(fill='toself'),
                  hovertemplate = "Country:%{label}: <br>Population: %{value} </br> iso num:%{customdata}")
dig.update_xaxes(range=['2007-01-01', '2020-01-01'])
dig.add_annotation(ax=0, ay=-200,
                   x = pd.Timestamp('2007-09-01') + (pd.Timestamp('2011-05-15') - pd.Timestamp('2007-09-01'))/2, y = 1.4,
            text="BA Psychology/BA Political Science",
            arrowhead=6,
           arrowsize=2,
           arrowwidth=1

                   )

dig.add_annotation(ax=0, ay=-100,
                   x = pd.Timestamp('2011-09-01') + (pd.Timestamp('2013-05-15') - pd.Timestamp('2011-09-01'))/2, y = 1.4,
            text="MA Psychology",
            arrowhead=6,
           arrowsize=2,
           arrowwidth=1

                   )

dig.add_annotation(ax=0, ay=-150,
                   x = pd.Timestamp('2014-09-01') + (pd.Timestamp('2016-05-15') - pd.Timestamp('2014-09-01'))/2, y = 1.4,
            text="MA Cognitive Science",
            arrowhead=6,
           arrowsize=2,
           arrowwidth=1

                   )

dig.add_annotation(ax=0, ay=-75,
                   x = pd.Timestamp('2016-05-16') + (pd.Timestamp('2019-05-15') - pd.Timestamp('2016-05-16'))/2, y = 1.4,
            text="PhD Cognitive Science",
            arrowhead=6,
           arrowsize=2,
           arrowwidth=1

                   ) 
st.plotly_chart(dig, use_container_width=True)
