import pandas as pd
import streamlit as st

st.sidebar.title("Welcome to our app!")

radio = st.sidebar.radio('Navigation Menu: ',
                         ["🏡 Home", "📕 Documentation", "🧙 Magic Bar Graph", "📅 Implementation Plan",
                          "👍 Success or Failure?", "🗃 Work Cited", "💻 View Source Code Here"])

if radio == "🏡 Home":
    st.image('\Kochlogo\Kochlogo.png', caption=None,
             width=None, use_column_width=None, clamp=False, channels='RGB',
             output_format='auto')


    st.title("Use Case Team 23")
    st.header("")
    st.subheader("")
    st.write("We developed a web app to present our idea leveraging Streamlit!")
    st.markdown("___")
    st.image('/Users/nolens1\Downloads\pp1.png', caption=None,
             width=None, use_column_width=None, clamp=False, channels='RGB',
             output_format='auto')
    st.markdown("___")
    st.image('/Users/nolens1\Downloads\pp2.png', caption=None,
             width=None, use_column_width=None, clamp=False, channels='RGB',
             output_format='auto')
    st.markdown("___")
    st.image('/Users/nolens1\Downloads\pp3.png', caption=None,
             width=None, use_column_width=None, clamp=False, channels='RGB',
             output_format='auto')
    st.markdown("___")
    st.image('/Users/nolens1\Downloads\pp4.png', caption=None,
             width=None, use_column_width=None, clamp=False, channels='RGB',
             output_format='auto')
    st.markdown("___")
    st.image('/Users/nolens1\Downloads\pp6.png', caption=None,
             width=None, use_column_width=None, clamp=False, channels='RGB',
             output_format='auto')
    st.markdown("___")
    st.image('/Users/nolens1\Downloads\pp7.png', caption=None,
             width=None, use_column_width=None, clamp=False, channels='RGB',
             output_format='auto')
    st.markdown("___")
    st.image('/Users/nolens1\Downloads\pp8.png', caption=None,
             width=None, use_column_width=None, clamp=False, channels='RGB',
             output_format='auto')
    st.markdown("___")
    st.image('/Users/nolens1\Downloads\pp10.png', caption=None,
             width=None, use_column_width=None, clamp=False, channels='RGB',
             output_format='auto')
    st.markdown("___")
    st.image('/Users/nolens1\Downloads\pp11.png', caption=None,
             width=None, use_column_width=None, clamp=False, channels='RGB',
             output_format='auto')
    st.markdown("___")
    st.image('/Users/nolens1\Downloads\pp12.png', caption=None,
             width=None, use_column_width=None, clamp=False, channels='RGB',
             output_format='auto')

if radio == "🧙 Magic Bar Graph":
    st.header("📊 User Input")
    st.write("Use the slider to see what year's net profits you wish to view! (2023 is the recommended year to "
             "view most accurate results)")

    mill_data = {
        "Wisconsin": {
            "Product": "USS",
            "Capacities": {
                "USS": 1500000,
                "UP": 1400000,
            },
            "Material": {
                "USS": 15,
                "UP": 17,
            },
            "Production": {
                "USS": 25,
                "UP": 30,
            },
            "Shipping": {
                "East": 32,
                "West": 44,
                "Midwest": 26,
                "South": 30,
            },
            "Revenue": {
                "USS": 200,
                "UP": 220,
            },
            "Construction": {
                "Switch": 55000000,
                "Days": 50,
            },
            "Expandable": None,
        },
        "Oregon": {
            "Product": "USS",
            "Capacities": {
                "USS": 1100000,
                "UP": 1000000,
            },
            "Material": {
                "USS": 17,
                "UP": 19,
            },
            "Production": {
                "USS": 35,
                "UP": 40,
            },
            "Shipping": {
                "East": 42,
                "West": 22,
                "Midwest": 34,
                "South": 43,
            },
            "Revenue": {
                "USS": 200,
                "UP": 220,
            },
            "Construction": {
                "Switch": 54000000,
                "Days": 40,
            },
            "Expandable": None,
        },
        "Arkansas": {
            "Product": "UP",
            "Capacities": {
                "USS": 900000,
                "UP": 800000,
            },
            "Material": {
                "USS": 16,
                "UP": 18,
            },
            "Production": {
                "USS": 30,
                "UP": 35,
            },
            "Shipping": {
                "East": 30,
                "West": 40,
                "Midwest": 22,
                "South": 20,
            },
            "Revenue": {
                "USS": 200,
                "UP": 220,
            },
            "Construction": {
                "Switch": 51000000,
                "Days": 30,
            },
            "Expandable": None,
        }
    }
    demand_data = {
        "2018": {
            "East": {
                "USS": 750000,
                "UP": 90000,
            },
            "West": {
                "USS": 610000,
                "UP": 220000,
            },
            "Midwest": {
                "USS": 430000,
                "UP": 40000,
            },
            "South": {
                "USS": 510000,
                "UP": 160000,
            },
        },
        "2019": {
            "East": {
                "USS": 880000,
                "UP": 180000,
            },
            "West": {
                "USS": 590000,
                "UP": 320000,
            },
            "Midwest": {
                "USS": 450000,
                "UP": 40000,
            },
            "South": {
                "USS": 620000,
                "UP": 150000,
            },

        },
        "2020": {
            "East": {
                "USS": 925000,
                "UP": 220000,
            },
            "West": {
                "USS": 600000,
                "UP": 400000,
            },
            "Midwest": {
                "USS": 460000,
                "UP": 60000,
            },
            "South": {
                "USS": 715000,
                "UP": 165000,
            },
        }
    }

    st.header('')

    number1 = st.slider('', min_value=2021, max_value=2050)
    gify = st.markdown("![Alt Text](https://media.giphy.com/media/OUwzqE4ZOk5Bm/giphy.gif)")

    n = number1 - 2020
    form = st.form("my_form")

    # Now add a submit button to the form:
    form.form_submit_button("Do some magic")

    growth_Dict = {
        "UP":
            {
                "West":
                    {
                        # get data for up in west from 2018 2019 and 2020
                        #    (((((2019 - 2018) / 2018) + ((2020 - 2019) / 2019)) / 2)+1)
                        # demand_data["2018"]["West"]["UP"],
                        # demand_data["2019"]["West"]["UP"],
                        # demand_data["2020"]["West"]["UP"],
                        ((((demand_data["2019"]["West"]["UP"] - demand_data["2018"]["West"]["UP"]) /
                           demand_data["2018"]["West"]["UP"]) + (
                                  (demand_data["2020"]["West"]["UP"] - demand_data["2019"]["West"]["UP"]) /
                                  demand_data["2019"]["West"]["UP"])) / 2) + 1
                        # growth_Dict["Avg Growth Per Year"]["UP"]["West"]

                    },
                "East":
                    {
                        # get data for up in west from 2018 2019 and 2020
                        #    (((((2019 - 2018) / 2018) + ((2020 - 2019) / 2019)) / 2)+1)
                        # demand_data["2018"]["East"]["UP"],
                        # demand_data["2019"]["East"]["UP"],
                        # demand_data["2020"]["East"]["UP"],
                        ((((demand_data["2019"]["East"]["UP"] - demand_data["2018"]["East"]["UP"]) /
                           demand_data["2018"]["East"]["UP"]) + (
                                  (demand_data["2020"]["East"]["UP"] - demand_data["2019"]["East"]["UP"]) /
                                  demand_data["2019"]["East"]["UP"])) / 2) + 1
                        # growth_Dict["Avg Growth Per Year"]["UP"]["East"]
                    },
                "Midwest":
                    {
                        # get data for up in west from 2018 2019 and 2020
                        #   (((((2019 - 2018) / 2018) + ((2020 - 2019) / 2019)) / 2)+1)
                        # demand_data["2018"]["Midwest"]["UP"],
                        # demand_data["2019"]["Midwest"]["UP"],
                        # demand_data["2020"]["Midwest"]["UP"],
                        ((((demand_data["2019"]["Midwest"]["UP"] - demand_data["2018"]["Midwest"]["UP"]) /
                           demand_data["2018"]["Midwest"]["UP"]) + ((demand_data["2020"]["Midwest"]["UP"] -
                                                                     demand_data["2019"]["Midwest"]["UP"]) /
                                                                    demand_data["2019"]["Midwest"]["UP"])) / 2) + 1
                        # growth_Dict["Avg Growth Per Year"]["UP"]["Midwest"]
                    },
                "South":
                    {
                        # get data for up in west from 2018 2019 and 2020
                        #    (((((2019 - 2018) / 2018) + ((2020 - 2019) / 2019)) / 2)+1)
                        # demand_data["2018"]["South"]["UP"],
                        # demand_data["2019"]["South"]["UP"],
                        # demand_data["2020"]["South"]["UP"],
                        (((((demand_data["2019"]["South"]["UP"] - demand_data["2018"]["South"]["UP"]) /
                            demand_data["2018"]["South"]["UP"]) + (
                                   (demand_data["2020"]["South"]["UP"] - demand_data["2019"]["South"]["UP"]) /
                                   demand_data["2019"]["South"]["UP"])) / 2) + 1)
                        # growth_Dict["Avg Growth Per Year"]["UP"]["South"]
                    }
            },
        "USS":
            {
                "West":
                    {
                        # get data for up in west from 2018 2019 and 2020
                        #    (((((2019 - 2018) / 2018) + ((2020 - 2019) / 2019)) / 2)+1)
                        # demand_data["2018"]["West"]["USS"],
                        # demand_data["2019"]["West"]["USS"],
                        # demand_data["2020"]["West"]["USS"],
                        ((((demand_data["2019"]["West"]["USS"] - demand_data["2018"]["West"]["USS"]) /
                           demand_data["2018"]["West"]["USS"]) + (
                                  (demand_data["2020"]["West"]["USS"] - demand_data["2019"]["West"]["USS"]) /
                                  demand_data["2019"]["West"]["USS"])) / 2)
                        # growth_Dict["Avg Growth Per Year"]["USS"]["West"]
                    },
                "East":
                    {
                        # get data for up in west from 2018 2019 and 2020
                        #    (((((2019 - 2018) / 2018) + ((2020 - 2019) / 2019)) / 2)+1)
                        # demand_data["2018"]["East"]["USS"],
                        # demand_data["2019"]["East"]["USS"],
                        # demand_data["2020"]["East"]["USS"],
                        (((((demand_data["2019"]["East"]["USS"] - demand_data["2018"]["East"]["USS"]) /
                            demand_data["2018"]["East"]["USS"]) + (
                                   (demand_data["2020"]["East"]["USS"] - demand_data["2019"]["East"]["USS"]) /
                                   demand_data["2019"]["East"]["USS"])) / 2) + 1)
                        # growth_Dict["Avg Growth Per Year"]["USS"]["East"]
                    },
                "Midwest":
                    {
                        # get data for up in west from 2018 2019 and 2020
                        #    (((((2019 - 2018) / 2018) + ((2020 - 2019) / 2019)) / 2)+1)
                        # demand_data["2018"]["Midwest"]["USS"],
                        # demand_data["2019"]["Midwest"]["USS"],
                        # demand_data["2020"]["Midwest"]["USS"],
                        (((((demand_data["2019"]["Midwest"]["USS"] - demand_data["2018"]["Midwest"]["USS"]) /
                            demand_data["2018"]["Midwest"]["USS"]) + ((demand_data["2020"]["Midwest"]["USS"] -
                                                                       demand_data["2019"]["Midwest"]["USS"]) /
                                                                      demand_data["2019"]["Midwest"][
                                                                          "USS"])) / 2) + 1)
                        # growth_Dict["Avg Growth Per Year"]["USS"]["Midwest"]
                    },
                "South":
                    {
                        # get data for up in west from 2018 2019 and 2020
                        #    (((((2019 - 2018) / 2018) + ((2020 - 2019) / 2019)) / 2)+1)
                        # demand_data["2018"]["South"]["USS"],
                        # demand_data["2019"]["South"]["USS"],
                        # demand_data["2020"]["South"]["USS"],
                        (((((demand_data["2019"]["South"]["USS"] - demand_data["2018"]["South"]["USS"]) /
                            demand_data["2018"]["South"]["USS"]) + (
                                   (demand_data["2020"]["South"]["USS"] - demand_data["2019"]["South"]["USS"]) /
                                   demand_data["2019"]["South"]["USS"])) / 2) + 1)
                        # growth_Dict["Avg Growth Per Year"]["USS"]["South"]
                    }
            }
    }

    upw = 1.3522727272727273
    ups = 1.01875
    upe = 1.6111111111111112
    upm = 1.25
    ussw = .992081134
    usss = 1.1844560404807085
    usse = 1.1122348484848485
    ussm = 1.0343669250645995

    demand_Dict = {
        "UP":
            {
                "West":
                    {
                        (demand_data["2020"]["West"]["UP"] * (upw ** n))
                    },
                "East":
                    {
                        (demand_data["2020"]["East"]["UP"] * (upe ** n))
                    },
                "Midwest":
                    {
                        (demand_data["2020"]["Midwest"]["UP"] * (upm ** n))
                    },
                "South":
                    {
                        (demand_data["2020"]["South"]["UP"] * (ups ** n))
                    }
            },
        "USS":
            {
                "West":
                    {
                        (demand_data["2020"]["West"]["USS"] * (ussw ** n))
                    },
                "East":
                    {
                        (demand_data["2020"]["East"]["USS"] * (usse ** n))
                    },
                "Midwest":
                    {
                        (demand_data["2020"]["Midwest"]["USS"] * (ussm ** n))
                    },
                "South":
                    {
                        (demand_data["2020"]["South"]["USS"] * (usss ** n))
                    }
            }
    }

    # IF STATEMENTS FOR DEMAND CAPACITY
    # if statement for wisconsin up west demand capacity
    demand_Wisconsin_UP_West = (demand_data["2020"]["West"]["UP"] * (upw ** n))
    if demand_Wisconsin_UP_West > mill_data["Wisconsin"]["Capacities"]["UP"]:
        demand_Wisconsin_UP_West = mill_data["Wisconsin"]["Capacities"]["UP"]

    # if statement for wisconsin up south demand capacity
    demand_Wisconsin_UP_South = (demand_data["2020"]["South"]["UP"] * (ups ** n))
    if demand_Wisconsin_UP_South > mill_data["Wisconsin"]["Capacities"]["UP"]:
        demand_Wisconsin_UP_South = mill_data["Wisconsin"]["Capacities"]["UP"]

    # if statement for wisconsin up east demand capacity
    demand_Wisconsin_UP_East = (demand_data["2020"]["East"]["UP"] * (upe ** n))
    if demand_Wisconsin_UP_East > mill_data["Wisconsin"]["Capacities"]["UP"]:
        demand_Wisconsin_UP_East = mill_data["Wisconsin"]["Capacities"]["UP"]

    # if statement for wisconsin up midwest demand capacity
    demand_Wisconsin_UP_Midwest = (demand_data["2020"]["Midwest"]["UP"] * (upm ** n))
    if demand_Wisconsin_UP_Midwest > mill_data["Wisconsin"]["Capacities"]["UP"]:
        demand_Wisconsin_UP_Midwest = mill_data["Wisconsin"]["Capacities"]["UP"]

    # if statement for wisconsin up west and south demand capacity
    demand_Wisconsin_UP_West_and_South = (demand_data["2020"]["West"]["UP"] * (upw ** n)) + (
            demand_data["2020"]["South"]["UP"] * (ups ** n))
    if demand_Wisconsin_UP_West_and_South > mill_data["Wisconsin"]["Capacities"]["UP"]:
        demand_Wisconsin_UP_West_and_South = (demand_data["2020"]["West"]["UP"] * (upw ** n)) + (mill_data["Wisconsin"]
                                                                                                 ["Capacities"]["UP"] -
                                                                                                 (demand_data["2020"]
                                                                                                  ["West"]["UP"] *
                                                                                                  (upw ** n)))
        if demand_data["2020"]["West"]["UP"] > mill_data["Wisconsin"]["Capacities"]["UP"]:
            demand_Wisconsin_UP_West_and_South = mill_data["Wisconsin"]["Capacities"]["UP"]

    # if statement for wisconsin up west and east demand capacity
    demand_Wisconsin_UP_West_and_East = (demand_data["2020"]["West"]["UP"] * (upw ** n)) + (
            demand_data["2020"]["East"]["UP"] * (upe ** n))
    if demand_Wisconsin_UP_West_and_East > mill_data["Wisconsin"]["Capacities"]["UP"]:
        demand_Wisconsin_UP_West_and_East = (demand_data["2020"]["East"]["UP"] * (upe ** n)) + (mill_data["Wisconsin"]
                                                                                                ["Capacities"]["UP"] -
                                                                                                (demand_data["2020"]
                                                                                                 ["East"]["UP"] *
                                                                                                 (upe ** n)))

    # if statement for wisconsin up west and midwest demand capacity with west as most profitable
    demand_Wisconsin_UP_West_and_Midwest = (demand_data["2020"]["West"]["UP"] * (upw ** n)) + (
            demand_data["2020"]["Midwest"]["UP"] * (upm ** n))
    if demand_Wisconsin_UP_West_and_Midwest > mill_data["Wisconsin"]["Capacities"]["UP"]:
        demand_Wisconsin_UP_West_and_Midwest = (demand_data["2020"]["West"]["UP"] * (upw ** n)) + (
                mill_data["Wisconsin"]
                ["Capacities"]["UP"] -
                (demand_data["2020"]
                 ["West"]["UP"] *
                 (upw ** n)))

    # if statement for wisconsin up south and east demand capacity with east as most profitable
    demand_Wisconsin_UP_South_and_East = (demand_data["2020"]["South"]["UP"] * (ups ** n)) + (
            demand_data["2020"]["East"]["UP"] * (upe ** n))
    if demand_Wisconsin_UP_South_and_East > mill_data["Wisconsin"]["Capacities"]["UP"]:
        demand_Wisconsin_UP_South_and_East = (demand_data["2020"]["East"]["UP"] * (upe ** n)) + (mill_data["Wisconsin"]
                                                                                                 ["Capacities"]["UP"] -
                                                                                                 (demand_data["2020"]
                                                                                                  ["East"]["UP"] *
                                                                                                  (upe ** n)))
    # if statement for wisconsin up south and midwest demand capacity with midwest as most profitable
    demand_Wisconsin_UP_South_and_Midwest = (demand_data["2020"]["South"]["UP"] * (ups ** n)) + (
            demand_data["2020"]["Midwest"]["UP"] * (upm ** n))
    if demand_Wisconsin_UP_South_and_Midwest > mill_data["Wisconsin"]["Capacities"]["UP"]:
        demand_Wisconsin_UP_South_and_Midwest = (demand_data["2020"]["Midwest"]["UP"] * (upm ** n)) + (
                mill_data["Wisconsin"]
                ["Capacities"]["UP"] -
                (demand_data["2020"]
                 ["Midwest"]["UP"] *
                 (upm ** n)))

    # if statement for wisconsin up east and midwest demand capacity with east as most profitable
    demand_Wisconsin_UP_East_and_Midwest = (demand_data["2020"]["East"]["UP"] * (upe ** n)) + (
            demand_data["2020"]["Midwest"]["UP"] * (upm ** n))
    if demand_Wisconsin_UP_East_and_Midwest > mill_data["Wisconsin"]["Capacities"]["UP"]:
        demand_Wisconsin_UP_East_and_Midwest = (demand_data["2020"]["East"]["UP"] * (upe ** n)) + (
                mill_data["Wisconsin"]
                ["Capacities"]["UP"] -
                (demand_data["2020"]
                 ["East"]["UP"] *
                 (upe ** n)))

    # if statement for uss Wisconsin west
    demand_Wisconsin_USS_West = (demand_data["2020"]["West"]["USS"] * (ussw ** n))
    if demand_Wisconsin_USS_West > mill_data["Wisconsin"]["Capacities"]["USS"]:
        demand_Wisconsin_USS_West = mill_data["Wisconsin"]["Capacities"]["USS"]

    # if statement for uss wisconsin south
    demand_Wisconsin_USS_South = (demand_data["2020"]["South"]["USS"] * (usss ** n))
    if demand_Wisconsin_USS_South > mill_data["Wisconsin"]["Capacities"]["USS"]:
        demand_Wisconsin_USS_South = mill_data["Wisconsin"]["Capacities"]["USS"]

    # if statement for wisconsin uss east
    demand_Wisconsin_USS_East = (demand_data["2020"]["East"]["USS"] * (usse ** n))
    if demand_Wisconsin_USS_East > mill_data["Wisconsin"]["Capacities"]["USS"]:
        demand_Wisconsin_USS_East = mill_data["Wisconsin"]["Capacities"]["USS"]

    # if statement for wisconsin uss midwest
    demand_Wisconsin_USS_Midwest = (demand_data["2020"]["Midwest"]["USS"] * (ussm ** n))
    if demand_Wisconsin_USS_Midwest > mill_data["Wisconsin"]["Capacities"]["USS"]:
        demand_Wisconsin_USS_Midwest = mill_data["Wisconsin"]["Capacities"]["USS"]

    # if statement for wisconsin uss west and south as south most profitable
    demand_Wisconsin_USS_West_and_South = (demand_data["2020"]["West"]["USS"] * (ussw ** n)) + (
            demand_data["2020"]["South"]["USS"] * (usss ** n))
    if demand_Wisconsin_USS_West_and_South > mill_data["Wisconsin"]["Capacities"]["USS"]:
        demand_Wisconsin_USS_West_and_South = (demand_data["2020"]["South"]["USS"] * (usss ** n)) + (
                mill_data["Wisconsin"]
                ["Capacities"]["USS"] -
                (demand_data["2020"]
                 ["South"]["USS"] *
                 (usss ** n)))
        if demand_data["2020"]["South"]["USS"] > mill_data["Wisconsin"]["Capacities"]["USS"]:
            demand_Wisconsin_USS_West_and_South = mill_data["Wisconsin"]["Capacities"]["USS"]

    # demand for wisconsin uss west and east with east being most profitable
    demand_Wisconsin_USS_West_and_East = (demand_data["2020"]["West"]["USS"] * (ussw ** n)) + (
            demand_data["2020"]["East"]["USS"] * (usse ** n))
    if demand_Wisconsin_USS_West_and_East > mill_data["Wisconsin"]["Capacities"]["USS"]:
        demand_Wisconsin_USS_West_and_East = (demand_data["2020"]["East"]["USS"] * (usse ** n)) + (
                mill_data["Wisconsin"]
                ["Capacities"]["USS"] -
                (demand_data["2020"]
                 ["East"]["USS"] *
                 (usse ** n)))
        if demand_data["2020"]["East"]["USS"] > mill_data["Wisconsin"]["Capacities"]["USS"]:
            demand_Wisconsin_USS_West_and_East = mill_data["Wisconsin"]["Capacities"]["USS"]

    # demand if statement for wisconsin uss for west and midwest with midwest being most profitable
    demand_Wisconsin_USS_West_and_Midwest = (demand_data["2020"]["West"]["USS"] * (ussw ** n)) + (
            demand_data["2020"]["Midwest"]["USS"] * (ussm ** n))
    if demand_Wisconsin_USS_West_and_Midwest > mill_data["Wisconsin"]["Capacities"]["USS"]:
        demand_Wisconsin_USS_West_and_Midwest = (demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) + (
                mill_data["Wisconsin"]
                ["Capacities"]["USS"] -
                (demand_data["2020"]
                 ["Midwest"]["USS"] *
                 (ussm ** n)))
        if demand_data["2020"]["Midwest"]["USS"] > mill_data["Wisconsin"]["Capacities"]["USS"]:
            demand_Wisconsin_USS_West_and_Midwest = mill_data["Wisconsin"]["Capacities"]["USS"]

    # demand for south and east for wisconsin uss with east being most profitable
    demand_Wisconsin_USS_South_and_East = (demand_data["2020"]["South"]["USS"] * (usss ** n)) + (
            demand_data["2020"]["East"]["USS"] * (usse ** n))
    if demand_Wisconsin_USS_South_and_East > mill_data["Wisconsin"]["Capacities"]["USS"]:
        demand_Wisconsin_USS_South_and_East = (demand_data["2020"]["East"]["USS"] * (usse ** n)) + (
                mill_data["Wisconsin"]
                ["Capacities"]["USS"] -
                (demand_data["2020"]
                 ["East"]["USS"] *
                 (usse ** n)))
        if demand_data["2020"]["East"]["USS"] > mill_data["Wisconsin"]["Capacities"]["USS"]:
            demand_Wisconsin_USS_South_and_East = mill_data["Wisconsin"]["Capacities"]["USS"]

    # demand if statement for wisconsin for south and midwest uss with south being more profitable
    demand_Wisconsin_USS_South_and_Midwest = (demand_data["2020"]["South"]["USS"] * (usss ** n)) + (
            demand_data["2020"]["Midwest"]["USS"] * (ussm ** n))
    if demand_Wisconsin_USS_South_and_Midwest > mill_data["Wisconsin"]["Capacities"]["USS"]:
        demand_Wisconsin_USS_South_and_Midwest = (demand_data["2020"]["South"]["USS"] * (usss ** n)) + (
                mill_data["Wisconsin"]
                ["Capacities"]["USS"] -
                (demand_data["2020"]
                 ["South"]["USS"] *
                 (usss ** n)))
        if demand_data["2020"]["South"]["USS"] > mill_data["Wisconsin"]["Capacities"]["USS"] or \
                demand_data["2020"]["Midwest"]["USS"] > mill_data["Wisconsin"]["Capacities"]["USS"]:
            demand_Wisconsin_USS_South_and_Midwest = mill_data["Wisconsin"]["Capacities"]["USS"]

    # if statement for wisconsin uss east and midwest with east being more profitable
    demand_Wisconsin_USS_East_and_Midwest = (demand_data["2020"]["East"]["USS"] * (usse ** n)) + (
            demand_data["2020"]["Midwest"]["USS"] * (ussm ** n))
    if demand_Wisconsin_USS_East_and_Midwest > mill_data["Wisconsin"]["Capacities"]["USS"]:
        demand_Wisconsin_USS_East_and_Midwest = (demand_data["2020"]["East"]["USS"] * (usse ** n)) + (
                mill_data["Wisconsin"]
                ["Capacities"]["USS"] -
                (demand_data["2020"]
                 ["East"]["USS"] *
                 (usse ** n)))
        if demand_data["2020"]["East"]["USS"] > mill_data["Wisconsin"]["Capacities"]["USS"] or \
                demand_data["2020"]["Midwest"]["USS"] > mill_data["Wisconsin"]["Capacities"]["USS"]:
            demand_Wisconsin_USS_East_and_Midwest = mill_data["Wisconsin"]["Capacities"]["USS"]

    # OREGON

    demand_Oregon_UP_West = (demand_data["2020"]["West"]["UP"] * (upw ** n))
    if demand_Oregon_UP_West > mill_data["Oregon"]["Capacities"]["UP"]:
        demand_Oregon_UP_West = mill_data["Oregon"]["Capacities"]["UP"]

    # if statement for Oregon up south demand capacity
    demand_Oregon_UP_South = (demand_data["2020"]["South"]["UP"] * (ups ** n))
    if demand_Oregon_UP_South > mill_data["Oregon"]["Capacities"]["UP"]:
        demand_Oregon_UP_South = mill_data["Oregon"]["Capacities"]["UP"]

    # if statement for Oregon up east demand capacity
    demand_Oregon_UP_East = (demand_data["2020"]["East"]["UP"] * (upe ** n))
    if demand_Oregon_UP_East > mill_data["Oregon"]["Capacities"]["UP"]:
        demand_Oregon_UP_East = mill_data["Oregon"]["Capacities"]["UP"]

    # if statement for Oregon up midwest demand capacity
    demand_Oregon_UP_Midwest = (demand_data["2020"]["Midwest"]["UP"] * (upm ** n))
    if demand_Oregon_UP_Midwest > mill_data["Oregon"]["Capacities"]["UP"]:
        demand_Oregon_UP_Midwest = mill_data["Oregon"]["Capacities"]["UP"]

    # if statement for Oregon up west and south demand capacity
    demand_Oregon_UP_West_and_South = (demand_data["2020"]["West"]["UP"] * (upw ** n)) + (
            demand_data["2020"]["South"]["UP"] * (ups ** n))
    if demand_Oregon_UP_West_and_South > mill_data["Oregon"]["Capacities"]["UP"]:
        demand_Oregon_UP_West_and_South = (demand_data["2020"]["West"]["UP"] * (upw ** n)) + (mill_data["Oregon"]
                                                                                              ["Capacities"]["UP"] -
                                                                                              (demand_data["2020"]
                                                                                               ["West"]["UP"] *
                                                                                               (upw ** n)))
        if demand_data["2020"]["West"]["UP"] > mill_data["Oregon"]["Capacities"]["UP"]:
            demand_Oregon_UP_West_and_South = mill_data["Oregon"]["Capacities"]["UP"]

    # if statement for Oregon up west and east demand capacity
    demand_Oregon_UP_West_and_East = (demand_data["2020"]["West"]["UP"] * (upw ** n)) + (
            demand_data["2020"]["East"]["UP"] * (upe ** n))
    if demand_Oregon_UP_West_and_East > mill_data["Oregon"]["Capacities"]["UP"]:
        demand_Oregon_UP_West_and_East = (demand_data["2020"]["East"]["UP"] * (upe ** n)) + (mill_data["Oregon"]
                                                                                             ["Capacities"]["UP"] -
                                                                                             (demand_data["2020"]
                                                                                              ["East"]["UP"] *
                                                                                              (upe ** n)))

    # if statement for Oregon up west and midwest demand capacity with west as most profitable
    demand_Oregon_UP_West_and_Midwest = (demand_data["2020"]["West"]["UP"] * (upw ** n)) + (
            demand_data["2020"]["Midwest"]["UP"] * (upm ** n))
    if demand_Oregon_UP_West_and_Midwest > mill_data["Oregon"]["Capacities"]["UP"]:
        demand_Oregon_UP_West_and_Midwest = (demand_data["2020"]["West"]["UP"] * (upw ** n)) + (mill_data["Oregon"]
                                                                                                ["Capacities"]["UP"] -
                                                                                                (demand_data["2020"]
                                                                                                 ["West"]["UP"] *
                                                                                                 (upw ** n)))

    # if statement for Oregon up south and east demand capacity with east as most profitable
    demand_Oregon_UP_South_and_East = (demand_data["2020"]["South"]["UP"] * (ups ** n)) + (
            demand_data["2020"]["East"]["UP"] * (upe ** n))
    if demand_Oregon_UP_South_and_East > mill_data["Oregon"]["Capacities"]["UP"]:
        demand_Oregon_UP_South_and_East = (demand_data["2020"]["East"]["UP"] * (upe ** n)) + (mill_data["Oregon"]
                                                                                              ["Capacities"]["UP"] -
                                                                                              (demand_data["2020"]
                                                                                               ["East"]["UP"] *
                                                                                               (upe ** n)))
    # if statement for Oregon up south and midwest demand capacity with midwest as most profitable
    demand_Oregon_UP_South_and_Midwest = (demand_data["2020"]["South"]["UP"] * (ups ** n)) + (
            demand_data["2020"]["Midwest"]["UP"] * (upm ** n))
    if demand_Oregon_UP_South_and_Midwest > mill_data["Oregon"]["Capacities"]["UP"]:
        demand_Oregon_UP_South_and_Midwest = (demand_data["2020"]["Midwest"]["UP"] * (upm ** n)) + (
                mill_data["Oregon"]
                ["Capacities"]["UP"] -
                (demand_data["2020"]
                 ["Midwest"]["UP"] *
                 (upm ** n)))

    # if statement for Oregon up east and midwest demand capacity with east as most profitable
    demand_Oregon_UP_East_and_Midwest = (demand_data["2020"]["East"]["UP"] * (upe ** n)) + (
            demand_data["2020"]["Midwest"]["UP"] * (upm ** n))
    if demand_Oregon_UP_East_and_Midwest > mill_data["Oregon"]["Capacities"]["UP"]:
        demand_Oregon_UP_East_and_Midwest = (demand_data["2020"]["East"]["UP"] * (upe ** n)) + (
                mill_data["Oregon"]
                ["Capacities"]["UP"] -
                (demand_data["2020"]
                 ["East"]["UP"] *
                 (upe ** n)))

    # if statement for uss Oregon west
    demand_Oregon_USS_West = (demand_data["2020"]["West"]["USS"] * (ussw ** n))
    if demand_Oregon_USS_West > mill_data["Oregon"]["Capacities"]["USS"]:
        demand_Oregon_USS_West = mill_data["Oregon"]["Capacities"]["USS"]

    # if statement for uss Oregon south
    demand_Oregon_USS_South = (demand_data["2020"]["South"]["USS"] * (usss ** n))
    if demand_Oregon_USS_South > mill_data["Oregon"]["Capacities"]["USS"]:
        demand_Oregon_USS_South = mill_data["Oregon"]["Capacities"]["USS"]

    # if statement for Oregon uss east
    demand_Oregon_USS_East = (demand_data["2020"]["East"]["USS"] * (usse ** n))
    if demand_Oregon_USS_East > mill_data["Oregon"]["Capacities"]["USS"]:
        demand_Oregon_USS_East = mill_data["Oregon"]["Capacities"]["USS"]

    # if statement for Oregon uss midwest
    demand_Oregon_USS_Midwest = (demand_data["2020"]["Midwest"]["USS"] * (ussm ** n))
    if demand_Oregon_USS_Midwest > mill_data["Oregon"]["Capacities"]["USS"]:
        demand_Oregon_USS_Midwest = mill_data["Oregon"]["Capacities"]["USS"]

    # if statement for Oregon uss west and south as south most profitable
    demand_Oregon_USS_West_and_South = (demand_data["2020"]["West"]["USS"] * (ussw ** n)) + (
            demand_data["2020"]["South"]["USS"] * (usss ** n))
    if demand_Oregon_USS_West_and_South > mill_data["Oregon"]["Capacities"]["USS"]:
        demand_Oregon_USS_West_and_South = (demand_data["2020"]["South"]["USS"] * (usss ** n)) + (mill_data["Oregon"]
                                                                                                  ["Capacities"][
                                                                                                      "USS"] -
                                                                                                  (demand_data["2020"]
                                                                                                   ["South"]["USS"] *
                                                                                                   (usss ** n)))
        if demand_data["2020"]["South"]["USS"] > mill_data["Oregon"]["Capacities"]["USS"]:
            demand_Oregon_USS_West_and_South = mill_data["Oregon"]["Capacities"]["USS"]

    # demand for Oregon uss west and east with east being most profitable
    demand_Oregon_USS_West_and_East = (demand_data["2020"]["West"]["USS"] * (ussw ** n)) + (
            demand_data["2020"]["East"]["USS"] * (usse ** n))
    if demand_Oregon_USS_West_and_East > mill_data["Oregon"]["Capacities"]["USS"]:
        demand_Oregon_USS_West_and_East = (demand_data["2020"]["East"]["USS"] * (usse ** n)) + (mill_data["Oregon"]
                                                                                                ["Capacities"]["USS"] -
                                                                                                (demand_data["2020"]
                                                                                                 ["East"]["USS"] *
                                                                                                 (usse ** n)))
        if demand_data["2020"]["East"]["USS"] > mill_data["Oregon"]["Capacities"]["USS"]:
            demand_Oregon_USS_West_and_East = mill_data["Oregon"]["Capacities"]["USS"]

    # demand if statement for Oregon uss for west and midwest with midwest being most profitable
    demand_Oregon_USS_West_and_Midwest = (demand_data["2020"]["West"]["USS"] * (ussw ** n)) + (
            demand_data["2020"]["Midwest"]["USS"] * (ussm ** n))
    if demand_Oregon_USS_West_and_Midwest > mill_data["Oregon"]["Capacities"]["USS"]:
        demand_Oregon_USS_West_and_Midwest = (demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) + (
                mill_data["Oregon"]
                ["Capacities"]["USS"] -
                (demand_data["2020"]
                 ["Midwest"]["USS"] *
                 (ussm ** n)))
        if demand_data["2020"]["Midwest"]["USS"] > mill_data["Oregon"]["Capacities"]["USS"]:
            demand_Oregon_USS_West_and_Midwest = mill_data["Oregon"]["Capacities"]["USS"]

    # demand for south and east for Oregon uss with east being most profitable
    demand_Oregon_USS_South_and_East = (demand_data["2020"]["South"]["USS"] * (usss ** n)) + (
            demand_data["2020"]["East"]["USS"] * (usse ** n))
    if demand_Oregon_USS_South_and_East > mill_data["Oregon"]["Capacities"]["USS"]:
        demand_Oregon_USS_South_and_East = (demand_data["2020"]["East"]["USS"] * (usse ** n)) + (
                mill_data["Oregon"]
                ["Capacities"]["USS"] -
                (demand_data["2020"]
                 ["East"]["USS"] *
                 (usse ** n)))
        if demand_data["2020"]["East"]["USS"] > mill_data["Oregon"]["Capacities"]["USS"]:
            demand_Oregon_USS_South_and_East = mill_data["Oregon"]["Capacities"]["USS"]

    # demand if statement for Oregon for south and midwest uss with south being more profitable
    demand_Oregon_USS_South_and_Midwest = (demand_data["2020"]["South"]["USS"] * (usss ** n)) + (
            demand_data["2020"]["Midwest"]["USS"] * (ussm ** n))
    if demand_Oregon_USS_South_and_Midwest > mill_data["Oregon"]["Capacities"]["USS"]:
        demand_Oregon_USS_South_and_Midwest = (demand_data["2020"]["South"]["USS"] * (usss ** n)) + (
                mill_data["Oregon"]
                ["Capacities"]["USS"] -
                (demand_data["2020"]
                 ["South"]["USS"] *
                 (usss ** n)))
        if demand_data["2020"]["South"]["USS"] > mill_data["Oregon"]["Capacities"]["USS"] or \
                demand_data["2020"]["Midwest"]["USS"] > mill_data["Oregon"]["Capacities"]["USS"]:
            demand_Oregon_USS_South_and_Midwest = mill_data["Oregon"]["Capacities"]["USS"]

    # if statement for Oregon uss east and midwest with east being more profitable
    demand_Oregon_USS_East_and_Midwest = (demand_data["2020"]["East"]["USS"] * (usse ** n)) + (
            demand_data["2020"]["Midwest"]["USS"] * (ussm ** n))
    if demand_Oregon_USS_East_and_Midwest > mill_data["Oregon"]["Capacities"]["USS"]:
        demand_Oregon_USS_East_and_Midwest = (demand_data["2020"]["East"]["USS"] * (usse ** n)) + (
                mill_data["Oregon"]
                ["Capacities"]["USS"] -
                (demand_data["2020"]
                 ["East"]["USS"] *
                 (usse ** n)))
        if demand_data["2020"]["East"]["USS"] > mill_data["Oregon"]["Capacities"]["USS"] or \
                demand_data["2020"]["Midwest"]["USS"] > mill_data["Oregon"]["Capacities"]["USS"]:
            demand_Oregon_USS_East_and_Midwest = mill_data["Oregon"]["Capacities"]["USS"]

    # Arkansas demand

    demand_Arkansas_UP_West = (demand_data["2020"]["West"]["UP"] * (upw ** n))
    if demand_Arkansas_UP_West > mill_data["Arkansas"]["Capacities"]["UP"]:
        demand_Arkansas_UP_West = mill_data["Arkansas"]["Capacities"]["UP"]

    # if statement for Arkansas up south demand capacity
    demand_Arkansas_UP_South = (demand_data["2020"]["South"]["UP"] * (ups ** n))
    if demand_Arkansas_UP_South > mill_data["Arkansas"]["Capacities"]["UP"]:
        demand_Arkansas_UP_South = mill_data["Arkansas"]["Capacities"]["UP"]

    # if statement for Arkansas up east demand capacity
    demand_Arkansas_UP_East = (demand_data["2020"]["East"]["UP"] * (upe ** n))
    if demand_Arkansas_UP_East > mill_data["Arkansas"]["Capacities"]["UP"]:
        demand_Arkansas_UP_East = mill_data["Arkansas"]["Capacities"]["UP"]

    # if statement for Arkansas up midwest demand capacity
    demand_Arkansas_UP_Midwest = (demand_data["2020"]["Midwest"]["UP"] * (upm ** n))
    if demand_Arkansas_UP_Midwest > mill_data["Arkansas"]["Capacities"]["UP"]:
        demand_Arkansas_UP_Midwest = mill_data["Arkansas"]["Capacities"]["UP"]

    # if statement for Arkansas up west and south demand capacity
    demand_Arkansas_UP_West_and_South = (demand_data["2020"]["West"]["UP"] * (upw ** n)) + (
            demand_data["2020"]["South"]["UP"] * (ups ** n))
    if demand_Arkansas_UP_West_and_South > mill_data["Arkansas"]["Capacities"]["UP"]:
        demand_Arkansas_UP_West_and_South = (demand_data["2020"]["West"]["UP"] * (upw ** n)) + (mill_data["Arkansas"]
                                                                                                ["Capacities"]["UP"] -
                                                                                                (demand_data["2020"]
                                                                                                 ["West"]["UP"] *
                                                                                                 (upw ** n)))
        if demand_data["2020"]["West"]["UP"] > mill_data["Arkansas"]["Capacities"]["UP"]:
            demand_Arkansas_UP_West_and_South = mill_data["Arkansas"]["Capacities"]["UP"]

    # if statement for Arkansas up west and east demand capacity
    demand_Arkansas_UP_West_and_East = (demand_data["2020"]["West"]["UP"] * (upw ** n)) + (
            demand_data["2020"]["East"]["UP"] * (upe ** n))
    if demand_Arkansas_UP_West_and_East > mill_data["Arkansas"]["Capacities"]["UP"]:
        demand_Arkansas_UP_West_and_East = (demand_data["2020"]["East"]["UP"] * (upe ** n)) + (mill_data["Arkansas"]
                                                                                               ["Capacities"]["UP"] -
                                                                                               (demand_data["2020"]
                                                                                                ["East"]["UP"] *
                                                                                                (upe ** n)))

    # if statement for Arkansas up west and midwest demand capacity with west as most profitable
    demand_Arkansas_UP_West_and_Midwest = (demand_data["2020"]["West"]["UP"] * (upw ** n)) + (
            demand_data["2020"]["Midwest"]["UP"] * (upm ** n))
    if demand_Arkansas_UP_West_and_Midwest > mill_data["Arkansas"]["Capacities"]["UP"]:
        demand_Arkansas_UP_West_and_Midwest = (demand_data["2020"]["West"]["UP"] * (upw ** n)) + (mill_data["Arkansas"]
                                                                                                  ["Capacities"]["UP"] -
                                                                                                  (demand_data["2020"]
                                                                                                   ["West"]["UP"] *
                                                                                                   (upw ** n)))

    # if statement for Arkansas up south and east demand capacity with east as most profitable
    demand_Arkansas_UP_South_and_East = (demand_data["2020"]["South"]["UP"] * (ups ** n)) + (
            demand_data["2020"]["East"]["UP"] * (upe ** n))
    if demand_Arkansas_UP_South_and_East > mill_data["Arkansas"]["Capacities"]["UP"]:
        demand_Arkansas_UP_South_and_East = (demand_data["2020"]["East"]["UP"] * (upe ** n)) + (mill_data["Arkansas"]
                                                                                                ["Capacities"]["UP"] -
                                                                                                (demand_data["2020"]
                                                                                                 ["East"]["UP"] *
                                                                                                 (upe ** n)))
    # if statement for Arkansas up south and midwest demand capacity with midwest as most profitable
    demand_Arkansas_UP_South_and_Midwest = (demand_data["2020"]["South"]["UP"] * (ups ** n)) + (
            demand_data["2020"]["Midwest"]["UP"] * (upm ** n))
    if demand_Arkansas_UP_South_and_Midwest > mill_data["Arkansas"]["Capacities"]["UP"]:
        demand_Arkansas_UP_South_and_Midwest = (demand_data["2020"]["Midwest"]["UP"] * (upm ** n)) + (
                mill_data["Arkansas"]
                ["Capacities"]["UP"] -
                (demand_data["2020"]
                 ["Midwest"]["UP"] *
                 (upm ** n)))

    # if statement for Arkansas up east and midwest demand capacity with east as most profitable
    demand_Arkansas_UP_East_and_Midwest = (demand_data["2020"]["East"]["UP"] * (upe ** n)) + (
            demand_data["2020"]["Midwest"]["UP"] * (upm ** n))
    if demand_Arkansas_UP_East_and_Midwest > mill_data["Arkansas"]["Capacities"]["UP"]:
        demand_Arkansas_UP_East_and_Midwest = (demand_data["2020"]["East"]["UP"] * (upe ** n)) + (
                mill_data["Arkansas"]
                ["Capacities"]["UP"] -
                (demand_data["2020"]
                 ["East"]["UP"] *
                 (upe ** n)))

    # if statement for uss Arkansas west
    demand_Arkansas_USS_West = (demand_data["2020"]["West"]["USS"] * (ussw ** n))
    if demand_Arkansas_USS_West > mill_data["Arkansas"]["Capacities"]["USS"]:
        demand_Arkansas_USS_West = mill_data["Arkansas"]["Capacities"]["USS"]

    # if statement for uss Arkansas south
    demand_Arkansas_USS_South = (demand_data["2020"]["South"]["USS"] * (usss ** n))
    if demand_Arkansas_USS_South > mill_data["Arkansas"]["Capacities"]["USS"]:
        demand_Arkansas_USS_South = mill_data["Arkansas"]["Capacities"]["USS"]

    # if statement for Arkansas uss east
    demand_Arkansas_USS_East = (demand_data["2020"]["East"]["USS"] * (usse ** n))
    if demand_Arkansas_USS_East > mill_data["Arkansas"]["Capacities"]["USS"]:
        demand_Arkansas_USS_East = mill_data["Arkansas"]["Capacities"]["USS"]

    # if statement for Arkansas uss midwest
    demand_Arkansas_USS_Midwest = (demand_data["2020"]["Midwest"]["USS"] * (ussm ** n))
    if demand_Arkansas_USS_Midwest > mill_data["Arkansas"]["Capacities"]["USS"]:
        demand_Arkansas_USS_Midwest = mill_data["Arkansas"]["Capacities"]["USS"]

    # if statement for Arkansas uss west and south as south most profitable
    demand_Arkansas_USS_West_and_South = (demand_data["2020"]["West"]["USS"] * (ussw ** n)) + (
            demand_data["2020"]["South"]["USS"] * (usss ** n))
    if demand_Arkansas_USS_West_and_South > mill_data["Arkansas"]["Capacities"]["USS"]:
        demand_Arkansas_USS_West_and_South = (demand_data["2020"]["South"]["USS"] * (usss ** n)) + (
                mill_data["Arkansas"]
                ["Capacities"]["USS"] -
                (demand_data["2020"]
                 ["South"]["USS"] *
                 (usss ** n)))
        if demand_data["2020"]["South"]["USS"] > mill_data["Arkansas"]["Capacities"]["USS"]:
            demand_Arkansas_USS_West_and_South = mill_data["Arkansas"]["Capacities"]["USS"]

    # demand for Arkansas uss west and east with east being most profitable
    demand_Arkansas_USS_West_and_East = (demand_data["2020"]["West"]["USS"] * (ussw ** n)) + (
            demand_data["2020"]["East"]["USS"] * (usse ** n))
    if demand_Arkansas_USS_West_and_East > mill_data["Arkansas"]["Capacities"]["USS"]:
        demand_Arkansas_USS_West_and_East = (demand_data["2020"]["East"]["USS"] * (usse ** n)) + (mill_data["Arkansas"]
                                                                                                  ["Capacities"][
                                                                                                      "USS"] -
                                                                                                  (demand_data["2020"]
                                                                                                   ["East"]["USS"] *
                                                                                                   (usse ** n)))
        if demand_data["2020"]["East"]["USS"] > mill_data["Arkansas"]["Capacities"]["USS"]:
            demand_Arkansas_USS_West_and_East = mill_data["Arkansas"]["Capacities"]["USS"]

    # demand if statement for Arkansas uss for west and midwest with midwest being most profitable
    demand_Arkansas_USS_West_and_Midwest = (demand_data["2020"]["West"]["USS"] * (ussw ** n)) + (
            demand_data["2020"]["Midwest"]["USS"] * (ussm ** n))
    if demand_Arkansas_USS_West_and_Midwest > mill_data["Arkansas"]["Capacities"]["USS"]:
        demand_Arkansas_USS_West_and_Midwest = (demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) + (
                mill_data["Arkansas"]
                ["Capacities"]["USS"] -
                (demand_data["2020"]
                 ["Midwest"]["USS"] *
                 (ussm ** n)))
        if demand_data["2020"]["Midwest"]["USS"] > mill_data["Arkansas"]["Capacities"]["USS"]:
            demand_Arkansas_USS_West_and_Midwest = mill_data["Arkansas"]["Capacities"]["USS"]

    # demand for south and east for Arkansas uss with east being most profitable
    demand_Arkansas_USS_South_and_East = (demand_data["2020"]["South"]["USS"] * (usss ** n)) + (
            demand_data["2020"]["East"]["USS"] * (usse ** n))
    if demand_Arkansas_USS_South_and_East > mill_data["Arkansas"]["Capacities"]["USS"]:
        demand_Arkansas_USS_South_and_East = (demand_data["2020"]["East"]["USS"] * (usse ** n)) + (
                mill_data["Arkansas"]
                ["Capacities"]["USS"] -
                (demand_data["2020"]
                 ["East"]["USS"] *
                 (usse ** n)))
        if demand_data["2020"]["East"]["USS"] > mill_data["Arkansas"]["Capacities"]["USS"]:
            demand_Arkansas_USS_South_and_East = mill_data["Arkansas"]["Capacities"]["USS"]

    # demand if statement for Arkansas for south and midwest uss with south being more profitable
    demand_Arkansas_USS_South_and_Midwest = (demand_data["2020"]["South"]["USS"] * (usss ** n)) + (
            demand_data["2020"]["Midwest"]["USS"] * (ussm ** n))
    if demand_Arkansas_USS_South_and_Midwest > mill_data["Arkansas"]["Capacities"]["USS"]:
        demand_Arkansas_USS_South_and_Midwest = (demand_data["2020"]["South"]["USS"] * (usss ** n)) + (
                mill_data["Arkansas"]
                ["Capacities"]["USS"] -
                (demand_data["2020"]
                 ["South"]["USS"] *
                 (usss ** n)))
        if demand_data["2020"]["South"]["USS"] > mill_data["Arkansas"]["Capacities"]["USS"] or \
                demand_data["2020"]["Midwest"]["USS"] > mill_data["Arkansas"]["Capacities"]["USS"]:
            demand_Arkansas_USS_South_and_Midwest = mill_data["Arkansas"]["Capacities"]["USS"]

    # if statement for Arkansas uss east and midwest with east being more profitable
    demand_Arkansas_USS_East_and_Midwest = (demand_data["2020"]["East"]["USS"] * (usse ** n)) + (
            demand_data["2020"]["Midwest"]["USS"] * (ussm ** n))
    if demand_Arkansas_USS_East_and_Midwest > mill_data["Arkansas"]["Capacities"]["USS"]:
        demand_Arkansas_USS_East_and_Midwest = (demand_data["2020"]["East"]["USS"] * (usse ** n)) + (
                mill_data["Arkansas"]
                ["Capacities"]["USS"] -
                (demand_data["2020"]
                 ["East"]["USS"] *
                 (usse ** n)))
        if demand_data["2020"]["East"]["USS"] > mill_data["Arkansas"]["Capacities"]["USS"] or \
                demand_data["2020"]["Midwest"]["USS"] > mill_data["Arkansas"]["Capacities"]["USS"]:
            demand_Arkansas_USS_East_and_Midwest = mill_data["Arkansas"]["Capacities"]["USS"]

    # SHIPPING IF STATEMENTS
    # shipping costs for wisconsin up west and south with west being most profitable
    shipping_Wisconsin_UP_West_South = ((demand_data["2020"]["West"]["UP"] * (upw ** n)) *
                                        mill_data["Wisconsin"]["Shipping"]
                                        ["West"]) + ((demand_data["2020"]["South"]["UP"] * (upw ** n)) *
                                                     mill_data["Wisconsin"]["Shipping"]
                                                     ["South"])
    if (demand_data["2020"]["West"]["UP"] * (upw ** n)) > mill_data["Wisconsin"]["Capacities"]["UP"]:
        shipping_Wisconsin_UP_West_South = mill_data["Wisconsin"]["Capacities"]["UP"] * \
                                           mill_data["Wisconsin"]["Shipping"]["West"]

    # shipping cost for wisconsin west and east with east being most profitable of the two regions
    shipping_Wisconsin_UP_West_East = ((demand_data["2020"]["West"]["UP"] * (upw ** n)) *
                                       mill_data["Wisconsin"]["Shipping"]
                                       ["West"]) + ((demand_data["2020"]["East"]["UP"] * (upe ** n)) *
                                                    mill_data["Wisconsin"]["Shipping"]
                                                    ["East"])
    if (demand_data["2020"]["East"]["UP"] * (upe ** n)) > mill_data["Wisconsin"]["Capacities"]["UP"]:
        shipping_Wisconsin_UP_West_East = mill_data["Wisconsin"]["Capacities"]["UP"] * \
                                          mill_data["Wisconsin"]["Shipping"]["East"]

    # shipping cost for wisconsin up west and midwest
    shipping_Wisconsin_UP_West_Midwest = ((demand_data["2020"]["West"]["UP"] * (upw ** n)) *
                                          mill_data["Wisconsin"]["Shipping"]
                                          ["West"]) + ((demand_data["2020"]["Midwest"]["UP"] * (upm ** n)) *
                                                       mill_data["Wisconsin"]["Shipping"]
                                                       ["Midwest"])
    if (demand_data["2020"]["West"]["UP"] * (upw ** n)) > mill_data["Wisconsin"]["Capacities"]["UP"]:
        shipping_Wisconsin_UP_West_Midwest = mill_data["Wisconsin"]["Capacities"]["UP"] * \
                                             mill_data["Wisconsin"]["Shipping"]["West"]

    # shipping cost for wisconsin east and south with east being more profitable
    shipping_Wisconsin_UP_South_East = ((demand_data["2020"]["South"]["UP"] * (ups ** n)) *
                                        mill_data["Wisconsin"]["Shipping"]
                                        ["South"]) + ((demand_data["2020"]["East"]["UP"] * (upe ** n)) *
                                                      mill_data["Wisconsin"]["Shipping"]
                                                      ["East"])
    if (demand_data["2020"]["East"]["UP"] * (upe ** n)) > mill_data["Wisconsin"]["Capacities"]["UP"]:
        shipping_Wisconsin_UP_South_East = mill_data["Wisconsin"]["Capacities"]["UP"] * \
                                           mill_data["Wisconsin"]["Shipping"]["East"]
    # shipping cost for wisconsin in south and midwest with midwest being more profitable
    shipping_Wisconsin_UP_South_Midwest = ((demand_data["2020"]["South"]["UP"] * (ups ** n)) *
                                           mill_data["Wisconsin"]["Shipping"]
                                           ["South"]) + ((demand_data["2020"]["Midwest"]["UP"] * (upm ** n)) *
                                                         mill_data["Wisconsin"]["Shipping"]
                                                         ["Midwest"])
    if (demand_data["2020"]["Midwest"]["UP"] * (upm ** n)) > mill_data["Wisconsin"]["Capacities"]["UP"]:
        shipping_Wisconsin_UP_South_Midwest = mill_data["Wisconsin"]["Capacities"]["UP"] * \
                                              mill_data["Wisconsin"]["Shipping"]["Midwest"]
    # shipping cost for wisconsin up in east and midwest as east as most profitable
    shipping_Wisconsin_UP_East_Midwest = ((demand_data["2020"]["East"]["UP"] * (upe ** n)) *
                                          mill_data["Wisconsin"]["Shipping"]
                                          ["East"]) + ((demand_data["2020"]["Midwest"]["UP"] * (upm ** n)) *
                                                       mill_data["Wisconsin"]["Shipping"]
                                                       ["Midwest"])
    if (demand_data["2020"]["East"]["UP"] * (upe ** n)) > mill_data["Wisconsin"]["Capacities"]["UP"]:
        shipping_Wisconsin_UP_East_Midwest = mill_data["Wisconsin"]["Capacities"]["UP"] * \
                                             mill_data["Wisconsin"]["Shipping"]["East"]

    # shipping cost for wisconsin uss south and west as south being most profitable
    shipping_Wisconsin_USS_West_South = ((demand_data["2020"]["West"]["USS"] * (ussw ** n)) *
                                         mill_data["Wisconsin"]["Shipping"]
                                         ["West"]) + ((demand_data["2020"]["South"]["USS"] * (usss ** n)) *
                                                      mill_data["Wisconsin"]["Shipping"]
                                                      ["South"])
    if (demand_data["2020"]["South"]["USS"] * (usss ** n)) > mill_data["Wisconsin"]["Capacities"]["USS"]:
        shipping_Wisconsin_USS_West_South = mill_data["Wisconsin"]["Capacities"]["USS"] * \
                                            mill_data["Wisconsin"]["Shipping"]["South"]

    # shipping cost for wisconsin west and east with east being most profitable
    shipping_Wisconsin_USS_West_East = ((demand_data["2020"]["West"]["USS"] * (ussw ** n)) *
                                        mill_data["Wisconsin"]["Shipping"]
                                        ["West"]) + ((demand_data["2020"]["East"]["USS"] * (usse ** n)) *
                                                     mill_data["Wisconsin"]["Shipping"]
                                                     ["East"])
    if (demand_data["2020"]["East"]["USS"] * (usse ** n)) > mill_data["Wisconsin"]["Capacities"]["USS"]:
        shipping_Wisconsin_USS_West_East = mill_data["Wisconsin"]["Capacities"]["USS"] * \
                                           mill_data["Wisconsin"]["Shipping"]["East"]

    # shipping cost for wisconsin uss for west and midwest with midwest being more profitable
    shipping_Wisconsin_USS_West_Midwest = ((demand_data["2020"]["West"]["USS"] * (ussw ** n)) *
                                           mill_data["Wisconsin"]["Shipping"]
                                           ["West"]) + ((demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) *
                                                        mill_data["Wisconsin"]["Shipping"]
                                                        ["Midwest"])
    if (demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) > mill_data["Wisconsin"]["Capacities"]["USS"]:
        shipping_Wisconsin_USS_West_Midwest = mill_data["Wisconsin"]["Capacities"]["USS"] * \
                                              mill_data["Wisconsin"]["Shipping"]["Midwest"]

    # shipping cost for wisconsin uss south and east with east being most profitable
    shipping_Wisconsin_USS_South_East = ((demand_data["2020"]["South"]["USS"] * (usss ** n)) *
                                         mill_data["Wisconsin"]["Shipping"]
                                         ["South"]) + ((demand_data["2020"]["East"]["USS"] * (usse ** n)) *
                                                       mill_data["Wisconsin"]["Shipping"]
                                                       ["East"])
    if (demand_data["2020"]["East"]["USS"] * (usse ** n)) > mill_data["Wisconsin"]["Capacities"]["USS"] or \
            (demand_data["2020"]["South"]["USS"] * (usse ** n)) > mill_data["Wisconsin"]["Capacities"]["USS"]:
        shipping_Wisconsin_USS_South_East = mill_data["Wisconsin"]["Capacities"]["USS"] * \
                                            mill_data["Wisconsin"]["Shipping"]["East"]

    # shipping cost for wisconsin uss south and midwest with south being most profitable
    shipping_Wisconsin_USS_South_Midwest = ((demand_data["2020"]["South"]["USS"] * (usss ** n)) *
                                            mill_data["Wisconsin"]["Shipping"]
                                            ["South"]) + ((demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) *
                                                          mill_data["Wisconsin"]["Shipping"]
                                                          ["Midwest"])
    if (demand_data["2020"]["South"]["USS"] * (usss ** n)) > mill_data["Wisconsin"]["Capacities"]["USS"] or \
            (demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) > mill_data["Wisconsin"]["Capacities"]["USS"]:
        shipping_Wisconsin_USS_South_Midwest = mill_data["Wisconsin"]["Capacities"]["USS"] * \
                                               mill_data["Wisconsin"]["Shipping"]["South"]

    # shipping for east and midwest for wisconsin uss with east being most profitable
    shipping_Wisconsin_USS_East_Midwest = ((demand_data["2020"]["East"]["USS"] * (usse ** n)) *
                                           mill_data["Wisconsin"]["Shipping"]
                                           ["East"]) + ((demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) *
                                                        mill_data["Wisconsin"]["Shipping"]
                                                        ["Midwest"])
    if (demand_data["2020"]["East"]["USS"] * (usse ** n)) > mill_data["Wisconsin"]["Capacities"]["USS"] or \
            (demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) > mill_data["Wisconsin"]["Capacities"]["USS"]:
        shipping_Wisconsin_USS_East_Midwest = mill_data["Wisconsin"]["Capacities"]["USS"] * \
                                              mill_data["Wisconsin"]["Shipping"]["East"]

    # Oregon shipping
    # shipping costs for Oregon up west and south with west being most profitable
    shipping_Oregon_UP_West_South = ((demand_data["2020"]["West"]["UP"] * (upw ** n)) *
                                     mill_data["Oregon"]["Shipping"]
                                     ["West"]) + ((demand_data["2020"]["South"]["UP"] * (upw ** n)) *
                                                  mill_data["Oregon"]["Shipping"]
                                                  ["South"])
    if (demand_data["2020"]["West"]["UP"] * (upw ** n)) > mill_data["Oregon"]["Capacities"]["UP"]:
        shipping_Oregon_UP_West_South = mill_data["Oregon"]["Capacities"]["UP"] * \
                                        mill_data["Oregon"]["Shipping"]["West"]

    # shipping cost for Oregon west and east with east being most profitable of the two regions
    shipping_Oregon_UP_West_East = ((demand_data["2020"]["West"]["UP"] * (upw ** n)) *
                                    mill_data["Oregon"]["Shipping"]
                                    ["West"]) + ((demand_data["2020"]["East"]["UP"] * (upe ** n)) *
                                                 mill_data["Oregon"]["Shipping"]
                                                 ["East"])
    if (demand_data["2020"]["East"]["UP"] * (upe ** n)) > mill_data["Oregon"]["Capacities"]["UP"]:
        shipping_Oregon_UP_West_East = mill_data["Oregon"]["Capacities"]["UP"] * \
                                       mill_data["Oregon"]["Shipping"]["East"]

    # shipping cost for Oregon up west and midwest
    shipping_Oregon_UP_West_Midwest = ((demand_data["2020"]["West"]["UP"] * (upw ** n)) *
                                       mill_data["Oregon"]["Shipping"]
                                       ["West"]) + ((demand_data["2020"]["Midwest"]["UP"] * (upm ** n)) *
                                                    mill_data["Oregon"]["Shipping"]["Midwest"])
    if (demand_data["2020"]["West"]["UP"] * (upw ** n)) > mill_data["Oregon"]["Capacities"]["UP"]:
        shipping_Oregon_UP_West_Midwest = mill_data["Oregon"]["Capacities"]["UP"] * \
                                          mill_data["Oregon"]["Shipping"]["West"]

    # shipping cost for Oregon east and south with east being more profitable
    shipping_Oregon_UP_South_East = ((demand_data["2020"]["South"]["UP"] * (ups ** n)) *
                                     mill_data["Oregon"]["Shipping"]
                                     ["South"]) + ((demand_data["2020"]["East"]["UP"] * (upe ** n)) *
                                                   mill_data["Oregon"]["Shipping"]
                                                   ["East"])
    if (demand_data["2020"]["East"]["UP"] * (upe ** n)) > mill_data["Oregon"]["Capacities"]["UP"]:
        shipping_Oregon_UP_South_East = mill_data["Oregon"]["Capacities"]["UP"] * \
                                        mill_data["Oregon"]["Shipping"]["East"]
    # shipping cost for Oregon in south and midwest with midwest being more profitable
    shipping_Oregon_UP_South_Midwest = ((demand_data["2020"]["South"]["UP"] * (ups ** n)) *
                                        mill_data["Oregon"]["Shipping"]
                                        ["South"]) + ((demand_data["2020"]["Midwest"]["UP"] * (upm ** n)) *
                                                      mill_data["Oregon"]["Shipping"]
                                                      ["Midwest"])
    if (demand_data["2020"]["Midwest"]["UP"] * (upm ** n)) > mill_data["Oregon"]["Capacities"]["UP"]:
        shipping_Oregon_UP_South_Midwest = mill_data["Oregon"]["Capacities"]["UP"] * \
                                           mill_data["Oregon"]["Shipping"]["Midwest"]
    # shipping cost for Oregon up in east and midwest as east as most profitable
    shipping_Oregon_UP_East_Midwest = ((demand_data["2020"]["East"]["UP"] * (upe ** n)) *
                                       mill_data["Oregon"]["Shipping"]
                                       ["East"]) + ((demand_data["2020"]["Midwest"]["UP"] * (upm ** n)) *
                                                    mill_data["Oregon"]["Shipping"]
                                                    ["Midwest"])
    if (demand_data["2020"]["East"]["UP"] * (upe ** n)) > mill_data["Oregon"]["Capacities"]["UP"]:
        shipping_Oregon_UP_East_Midwest = mill_data["Oregon"]["Capacities"]["UP"] * \
                                          mill_data["Oregon"]["Shipping"]["East"]

    # shipping cost for Oregon uss south and west as south being most profitable
    shipping_Oregon_USS_West_South = ((demand_data["2020"]["West"]["USS"] * (ussw ** n)) *
                                      mill_data["Oregon"]["Shipping"]
                                      ["West"]) + ((demand_data["2020"]["South"]["USS"] * (usss ** n)) *
                                                   mill_data["Oregon"]["Shipping"]
                                                   ["South"])
    if (demand_data["2020"]["South"]["USS"] * (usss ** n)) > mill_data["Oregon"]["Capacities"]["USS"]:
        shipping_Oregon_USS_West_South = mill_data["Oregon"]["Capacities"]["USS"] * \
                                         mill_data["Oregon"]["Shipping"]["South"]

    # shipping cost for Oregon west and east with east being most profitable
    shipping_Oregon_USS_West_East = ((demand_data["2020"]["West"]["USS"] * (ussw ** n)) *
                                     mill_data["Oregon"]["Shipping"]
                                     ["West"]) + ((demand_data["2020"]["East"]["USS"] * (usse ** n)) *
                                                  mill_data["Oregon"]["Shipping"]
                                                  ["East"])
    if (demand_data["2020"]["East"]["USS"] * (usse ** n)) > mill_data["Oregon"]["Capacities"]["USS"]:
        shipping_Oregon_USS_West_East = mill_data["Oregon"]["Capacities"]["USS"] * \
                                        mill_data["Oregon"]["Shipping"]["East"]

    # shipping cost for Oregon uss for west and midwest with midwest being more profitable
    shipping_Oregon_USS_West_Midwest = ((demand_data["2020"]["West"]["USS"] * (ussw ** n)) *
                                        mill_data["Oregon"]["Shipping"]
                                        ["West"]) + ((demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) *
                                                     mill_data["Oregon"]["Shipping"]
                                                     ["Midwest"])
    if (demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) > mill_data["Oregon"]["Capacities"]["USS"]:
        shipping_Oregon_USS_West_Midwest = mill_data["Oregon"]["Capacities"]["USS"] * \
                                           mill_data["Oregon"]["Shipping"]["Midwest"]

    # shipping cost for Oregon uss south and east with east being most profitable
    shipping_Oregon_USS_South_East = ((demand_data["2020"]["South"]["USS"] * (usss ** n)) *
                                      mill_data["Oregon"]["Shipping"]
                                      ["South"]) + ((demand_data["2020"]["East"]["USS"] * (usse ** n)) *
                                                    mill_data["Oregon"]["Shipping"]
                                                    ["East"])
    if (demand_data["2020"]["East"]["USS"] * (usse ** n)) > mill_data["Oregon"]["Capacities"]["USS"] or \
            (demand_data["2020"]["South"]["USS"] * (usse ** n)) > mill_data["Oregon"]["Capacities"]["USS"]:
        shipping_Oregon_USS_South_East = mill_data["Oregon"]["Capacities"]["USS"] * \
                                         mill_data["Oregon"]["Shipping"]["East"]

    # shipping cost for Oregon uss south and midwest with south being most profitable
    shipping_Oregon_USS_South_Midwest = ((demand_data["2020"]["South"]["USS"] * (usss ** n)) *
                                         mill_data["Oregon"]["Shipping"]
                                         ["South"]) + ((demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) *
                                                       mill_data["Oregon"]["Shipping"]
                                                       ["Midwest"])
    if (demand_data["2020"]["South"]["USS"] * (usss ** n)) > mill_data["Oregon"]["Capacities"]["USS"] or \
            (demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) > mill_data["Oregon"]["Capacities"]["USS"]:
        shipping_Oregon_USS_South_Midwest = mill_data["Oregon"]["Capacities"]["USS"] * \
                                            mill_data["Oregon"]["Shipping"]["South"]

    # shipping for east and midwest for Oregon uss with east being most profitable
    shipping_Oregon_USS_East_Midwest = ((demand_data["2020"]["East"]["USS"] * (usse ** n)) *
                                        mill_data["Oregon"]["Shipping"]
                                        ["East"]) + ((demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) *
                                                     mill_data["Oregon"]["Shipping"]
                                                     ["Midwest"])
    if (demand_data["2020"]["East"]["USS"] * (usse ** n)) > mill_data["Oregon"]["Capacities"]["USS"] or \
            (demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) > mill_data["Oregon"]["Capacities"]["USS"]:
        shipping_Oregon_USS_East_Midwest = mill_data["Oregon"]["Capacities"]["USS"] * \
                                           mill_data["Oregon"]["Shipping"]["East"]

    # Arkansas shipping

    # shipping costs for Arkansas up west and south with west being most profitable
    shipping_Arkansas_UP_West_South = ((demand_data["2020"]["West"]["UP"] * (upw ** n)) *
                                       mill_data["Arkansas"]["Shipping"]
                                       ["West"]) + ((demand_data["2020"]["South"]["UP"] * (upw ** n)) *
                                                    mill_data["Arkansas"]["Shipping"]
                                                    ["South"])
    if (demand_data["2020"]["West"]["UP"] * (upw ** n)) > mill_data["Arkansas"]["Capacities"]["UP"]:
        shipping_Arkansas_UP_West_South = mill_data["Arkansas"]["Capacities"]["UP"] * \
                                          mill_data["Arkansas"]["Shipping"]["West"]

    # shipping cost for Arkansas west and east with east being most profitable of the two regions
    shipping_Arkansas_UP_West_East = ((demand_data["2020"]["West"]["UP"] * (upw ** n)) *
                                      mill_data["Arkansas"]["Shipping"]
                                      ["West"]) + ((demand_data["2020"]["East"]["UP"] * (upe ** n)) *
                                                   mill_data["Arkansas"]["Shipping"]
                                                   ["East"])
    if (demand_data["2020"]["East"]["UP"] * (upe ** n)) > mill_data["Arkansas"]["Capacities"]["UP"]:
        shipping_Arkansas_UP_West_East = mill_data["Arkansas"]["Capacities"]["UP"] * \
                                         mill_data["Arkansas"]["Shipping"]["East"]

    # shipping cost for Arkansas up west and midwest
    shipping_Arkansas_UP_West_Midwest = ((demand_data["2020"]["West"]["UP"] * (upw ** n)) *
                                         mill_data["Arkansas"]["Shipping"]
                                         ["West"]) + ((demand_data["2020"]["Midwest"]["UP"] * (upm ** n)) *
                                                      mill_data["Arkansas"]["Shipping"]
                                                      ["Midwest"])
    if (demand_data["2020"]["West"]["UP"] * (upw ** n)) > mill_data["Arkansas"]["Capacities"]["UP"]:
        shipping_Arkansas_UP_West_Midwest = mill_data["Arkansas"]["Capacities"]["UP"] * \
                                            mill_data["Arkansas"]["Shipping"]["West"]

    # shipping cost for Arkansas east and south with east being more profitable
    shipping_Arkansas_UP_South_East = ((demand_data["2020"]["South"]["UP"] * (ups ** n)) *
                                       mill_data["Arkansas"]["Shipping"]
                                       ["South"]) + ((demand_data["2020"]["East"]["UP"] * (upe ** n)) *
                                                     mill_data["Arkansas"]["Shipping"]
                                                     ["East"])
    if (demand_data["2020"]["East"]["UP"] * (upe ** n)) > mill_data["Arkansas"]["Capacities"]["UP"]:
        shipping_Arkansas_UP_South_East = mill_data["Arkansas"]["Capacities"]["UP"] * \
                                          mill_data["Arkansas"]["Shipping"]["East"]
    # shipping cost for Arkansas in south and midwest with midwest being more profitable
    shipping_Arkansas_UP_South_Midwest = ((demand_data["2020"]["South"]["UP"] * (ups ** n)) *
                                          mill_data["Arkansas"]["Shipping"]
                                          ["South"]) + ((demand_data["2020"]["Midwest"]["UP"] * (upm ** n)) *
                                                        mill_data["Arkansas"]["Shipping"]
                                                        ["Midwest"])
    if (demand_data["2020"]["Midwest"]["UP"] * (upm ** n)) > mill_data["Arkansas"]["Capacities"]["UP"]:
        shipping_Arkansas_UP_South_Midwest = mill_data["Arkansas"]["Capacities"]["UP"] * \
                                             mill_data["Arkansas"]["Shipping"]["Midwest"]
    # shipping cost for Arkansas up in east and midwest as east as most profitable
    shipping_Arkansas_UP_East_Midwest = ((demand_data["2020"]["East"]["UP"] * (upe ** n)) *
                                         mill_data["Arkansas"]["Shipping"]
                                         ["East"]) + ((demand_data["2020"]["Midwest"]["UP"] * (upm ** n)) *
                                                      mill_data["Arkansas"]["Shipping"]
                                                      ["Midwest"])
    if (demand_data["2020"]["East"]["UP"] * (upe ** n)) > mill_data["Arkansas"]["Capacities"]["UP"]:
        shipping_Arkansas_UP_East_Midwest = mill_data["Arkansas"]["Capacities"]["UP"] * \
                                            mill_data["Arkansas"]["Shipping"]["East"]

    # shipping cost for Arkansas uss south and west as south being most profitable
    shipping_Arkansas_USS_West_South = ((demand_data["2020"]["West"]["USS"] * (ussw ** n)) *
                                        mill_data["Arkansas"]["Shipping"]
                                        ["West"]) + ((demand_data["2020"]["South"]["USS"] * (usss ** n)) *
                                                     mill_data["Arkansas"]["Shipping"]
                                                     ["South"])
    if (demand_data["2020"]["South"]["USS"] * (usss ** n)) > mill_data["Arkansas"]["Capacities"]["USS"]:
        shipping_Arkansas_USS_West_South = mill_data["Arkansas"]["Capacities"]["USS"] * \
                                           mill_data["Arkansas"]["Shipping"]["South"]

    # shipping cost for Arkansas west and east with east being most profitable
    shipping_Arkansas_USS_West_East = ((demand_data["2020"]["West"]["USS"] * (ussw ** n)) *
                                       mill_data["Arkansas"]["Shipping"]
                                       ["West"]) + ((demand_data["2020"]["East"]["USS"] * (usse ** n)) *
                                                    mill_data["Arkansas"]["Shipping"]
                                                    ["East"])
    if (demand_data["2020"]["East"]["USS"] * (usse ** n)) > mill_data["Arkansas"]["Capacities"]["USS"]:
        shipping_Arkansas_USS_West_East = mill_data["Arkansas"]["Capacities"]["USS"] * \
                                          mill_data["Arkansas"]["Shipping"]["East"]

    # shipping cost for Arkansas uss for west and midwest with midwest being more profitable
    shipping_Arkansas_USS_West_Midwest = ((demand_data["2020"]["West"]["USS"] * (ussw ** n)) *
                                          mill_data["Arkansas"]["Shipping"]
                                          ["West"]) + ((demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) *
                                                       mill_data["Arkansas"]["Shipping"]
                                                       ["Midwest"])
    if (demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) > mill_data["Arkansas"]["Capacities"]["USS"]:
        shipping_Arkansas_USS_West_Midwest = mill_data["Arkansas"]["Capacities"]["USS"] * \
                                             mill_data["Arkansas"]["Shipping"]["Midwest"]

    # shipping cost for Arkansas uss south and east with east being most profitable
    shipping_Arkansas_USS_South_East = ((demand_data["2020"]["South"]["USS"] * (usss ** n)) *
                                        mill_data["Arkansas"]["Shipping"]
                                        ["South"]) + ((demand_data["2020"]["East"]["USS"] * (usse ** n)) *
                                                      mill_data["Arkansas"]["Shipping"]
                                                      ["East"])
    if (demand_data["2020"]["East"]["USS"] * (usse ** n)) > mill_data["Arkansas"]["Capacities"]["USS"] or \
            (demand_data["2020"]["South"]["USS"] * (usse ** n)) > mill_data["Arkansas"]["Capacities"]["USS"]:
        shipping_Arkansas_USS_South_East = mill_data["Arkansas"]["Capacities"]["USS"] * \
                                           mill_data["Arkansas"]["Shipping"]["East"]

    # shipping cost for Arkansas uss south and midwest with south being most profitable
    shipping_Arkansas_USS_South_Midwest = ((demand_data["2020"]["South"]["USS"] * (usss ** n)) *
                                           mill_data["Arkansas"]["Shipping"]
                                           ["South"]) + ((demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) *
                                                         mill_data["Arkansas"]["Shipping"]
                                                         ["Midwest"])
    if (demand_data["2020"]["South"]["USS"] * (usss ** n)) > mill_data["Arkansas"]["Capacities"]["USS"] or \
            (demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) > mill_data["Arkansas"]["Capacities"]["USS"]:
        shipping_Arkansas_USS_South_Midwest = mill_data["Arkansas"]["Capacities"]["USS"] * \
                                              mill_data["Arkansas"]["Shipping"]["South"]

    # shipping for east and midwest for Arkansas uss with east being most profitable
    shipping_Arkansas_USS_East_Midwest = ((demand_data["2020"]["East"]["USS"] * (usse ** n)) *
                                          mill_data["Arkansas"]["Shipping"]
                                          ["East"]) + ((demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) *
                                                       mill_data["Arkansas"]["Shipping"]
                                                       ["Midwest"])
    if (demand_data["2020"]["East"]["USS"] * (usse ** n)) > mill_data["Arkansas"]["Capacities"]["USS"] or \
            (demand_data["2020"]["Midwest"]["USS"] * (ussm ** n)) > mill_data["Arkansas"]["Capacities"]["USS"]:
        shipping_Arkansas_USS_East_Midwest = mill_data["Arkansas"]["Capacities"]["USS"] * \
                                             mill_data["Arkansas"]["Shipping"]["East"]

    solutions_Data = {
        "Wisconsin": {
            "UP": {
                "West":
                    {

                        demand_Wisconsin_UP_West * mill_data["Wisconsin"]["Revenue"][
                            "UP"] - demand_Wisconsin_UP_West * (
                                mill_data["Wisconsin"]
                                ["Material"]["UP"] + mill_data["Wisconsin"]["Production"]["UP"]) -
                        demand_Wisconsin_UP_West *
                        mill_data
                        ["Wisconsin"]["Shipping"]["West"]

                    },
                "South":
                    {
                        demand_Wisconsin_UP_South * mill_data["Wisconsin"]["Revenue"][
                            "UP"] - demand_Wisconsin_UP_South * (
                                mill_data["Wisconsin"]
                                ["Material"]["UP"] + mill_data["Wisconsin"]["Production"]["UP"]) -
                        demand_Wisconsin_UP_South *
                        mill_data
                        ["Wisconsin"]["Shipping"]["South"]
                    },
                "East":
                    {
                        demand_Wisconsin_UP_East * mill_data["Wisconsin"]["Revenue"][
                            "UP"] - demand_Wisconsin_UP_East * (
                                mill_data["Wisconsin"]
                                ["Material"]["UP"] + mill_data["Wisconsin"]["Production"]["UP"]) -
                        demand_Wisconsin_UP_East *
                        mill_data
                        ["Wisconsin"]["Shipping"]["East"]
                    },
                "Midwest":
                    {
                        demand_Wisconsin_UP_Midwest * mill_data["Wisconsin"]["Revenue"][
                            "UP"] - demand_Wisconsin_UP_Midwest
                        * (
                                mill_data["Wisconsin"]
                                ["Material"]["UP"] + mill_data["Wisconsin"]["Production"]["UP"]) -
                        demand_Wisconsin_UP_Midwest *
                        mill_data
                        ["Wisconsin"]["Shipping"]["Midwest"]
                    },
                "West and South":
                    {

                        (demand_Wisconsin_UP_West_and_South * mill_data["Wisconsin"]["Revenue"]["UP"]) - (
                                demand_Wisconsin_UP_West_and_South
                                * (
                                        mill_data["Wisconsin"]
                                        ["Material"]["UP"] + mill_data["Wisconsin"]["Production"]["UP"])) -
                        shipping_Wisconsin_UP_West_South

                    },
                "West and East":
                    {
                        (demand_Wisconsin_UP_West_and_East * mill_data["Wisconsin"]["Revenue"]["UP"]) - (
                                demand_Wisconsin_UP_West_and_East
                                * (
                                        mill_data["Wisconsin"]
                                        ["Material"]["UP"] + mill_data["Wisconsin"]["Production"]["UP"])) -
                        shipping_Wisconsin_UP_West_East
                    },
                "West and Midwest":
                    {
                        (demand_Wisconsin_UP_West_and_Midwest * mill_data["Wisconsin"]["Revenue"]["UP"]) - (
                                demand_Wisconsin_UP_West_and_Midwest
                                * (
                                        mill_data["Wisconsin"]
                                        ["Material"]["UP"] + mill_data["Wisconsin"]["Production"]["UP"])) -
                        shipping_Wisconsin_UP_West_Midwest
                    },
                "South and East":
                    {
                        (demand_Wisconsin_UP_South_and_East * mill_data["Wisconsin"]["Revenue"]["UP"]) - (
                                demand_Wisconsin_UP_South_and_East
                                * (
                                        mill_data["Wisconsin"]
                                        ["Material"]["UP"] + mill_data["Wisconsin"]["Production"]["UP"])) -
                        shipping_Wisconsin_UP_South_East
                    },
                "South and Midwest":
                    {
                        (demand_Wisconsin_UP_South_and_Midwest * mill_data["Wisconsin"]["Revenue"]["UP"]) - (
                                demand_Wisconsin_UP_South_and_Midwest
                                * (
                                        mill_data["Wisconsin"]
                                        ["Material"]["UP"] + mill_data["Wisconsin"]["Production"]["UP"])) -
                        shipping_Wisconsin_UP_South_Midwest
                    },
                "East and Midwest":
                    {
                        (demand_Wisconsin_UP_East_and_Midwest * mill_data["Wisconsin"]["Revenue"]["UP"]) - (
                                demand_Wisconsin_UP_East_and_Midwest
                                * (
                                        mill_data["Wisconsin"]
                                        ["Material"]["UP"] + mill_data["Wisconsin"]["Production"]["UP"])) -
                        shipping_Wisconsin_UP_East_Midwest
                    },
                "West and South and East":
                    {
                        0
                    },
                "West and East and Midwest":
                    {
                        0
                    },
                "West and South and Midwest":
                    {
                        0
                    },
                "South and East and Midwest":
                    {
                        0
                    },
                "West and South and East and Midwest":
                    {
                        0
                    }
            },

            "USS": {
                "West":
                    {
                        demand_Wisconsin_USS_West * mill_data["Wisconsin"]["Revenue"][
                            "USS"] - demand_Wisconsin_USS_West * (
                                mill_data["Wisconsin"]
                                ["Material"]["USS"] + mill_data["Wisconsin"]["Production"]["USS"]) -
                        demand_Wisconsin_USS_West *
                        mill_data
                        ["Wisconsin"]["Shipping"]["West"]
                    },
                "South":
                    {
                        demand_Wisconsin_USS_South * mill_data["Wisconsin"]["Revenue"][
                            "USS"] - demand_Wisconsin_USS_South * (
                                mill_data["Wisconsin"]
                                ["Material"]["USS"] + mill_data["Wisconsin"]["Production"]["USS"]) -
                        demand_Wisconsin_USS_South *
                        mill_data
                        ["Wisconsin"]["Shipping"]["South"]
                    },
                "East":
                    {
                        demand_Wisconsin_USS_East * mill_data["Wisconsin"]["Revenue"][
                            "USS"] - demand_Wisconsin_USS_East * (
                                mill_data["Wisconsin"]
                                ["Material"]["USS"] + mill_data["Wisconsin"]["Production"]["USS"]) -
                        demand_Wisconsin_USS_East *
                        mill_data
                        ["Wisconsin"]["Shipping"]["East"]
                    },
                "Midwest":
                    {
                        demand_Wisconsin_USS_Midwest * mill_data["Wisconsin"]["Revenue"][
                            "USS"] - demand_Wisconsin_USS_Midwest * (
                                mill_data["Wisconsin"]
                                ["Material"]["USS"] + mill_data["Wisconsin"]["Production"]["USS"]) -
                        demand_Wisconsin_USS_Midwest *
                        mill_data
                        ["Wisconsin"]["Shipping"]["Midwest"]
                    },
                "West and South":
                    {
                        (demand_Wisconsin_USS_West_and_South * mill_data["Wisconsin"]["Revenue"]["USS"]) - (
                                demand_Wisconsin_USS_West_and_South
                                * (
                                        mill_data["Wisconsin"]
                                        ["Material"]["USS"] + mill_data["Wisconsin"]["Production"]["USS"])) -
                        shipping_Wisconsin_USS_West_South
                    },
                "West and East":
                    {
                        (demand_Wisconsin_USS_West_and_East * mill_data["Wisconsin"]["Revenue"]["USS"]) - (
                                demand_Wisconsin_USS_West_and_East
                                * (
                                        mill_data["Wisconsin"]
                                        ["Material"]["USS"] + mill_data["Wisconsin"]["Production"]["USS"])) -
                        shipping_Wisconsin_USS_West_East
                    },
                "West and Midwest":
                    {
                        (demand_Wisconsin_USS_West_and_Midwest * mill_data["Wisconsin"]["Revenue"]["USS"]) - (
                                demand_Wisconsin_USS_West_and_Midwest
                                * (
                                        mill_data["Wisconsin"]
                                        ["Material"]["USS"] + mill_data["Wisconsin"]["Production"]["USS"])) -
                        shipping_Wisconsin_USS_West_Midwest
                    },
                "South and East":
                    {
                        (demand_Wisconsin_USS_South_and_East * mill_data["Wisconsin"]["Revenue"]["USS"]) - (
                                demand_Wisconsin_USS_South_and_East
                                * (
                                        mill_data["Wisconsin"]
                                        ["Material"]["USS"] + mill_data["Wisconsin"]["Production"]["USS"])) -
                        shipping_Wisconsin_USS_South_East
                    },
                "South and Midwest":
                    {
                        (demand_Wisconsin_USS_South_and_Midwest * mill_data["Wisconsin"]["Revenue"]["USS"]) - (
                                demand_Wisconsin_USS_South_and_Midwest
                                * (
                                        mill_data["Wisconsin"]
                                        ["Material"]["USS"] + mill_data["Wisconsin"]["Production"]["USS"])) -
                        shipping_Wisconsin_USS_South_Midwest
                    },
                "East and Midwest":
                    {
                        (demand_Wisconsin_USS_East_and_Midwest * mill_data["Wisconsin"]["Revenue"]["USS"]) - (
                                demand_Wisconsin_USS_East_and_Midwest
                                * (
                                        mill_data["Wisconsin"]
                                        ["Material"]["USS"] + mill_data["Wisconsin"]["Production"]["USS"])) -
                        shipping_Wisconsin_USS_East_Midwest
                    },
                "West and South and East":
                    {
                        0
                    },
                "West and East and Midwest":
                    {
                        0
                    },
                "West and South and Midwest":
                    {
                        0
                    },
                "South and East and Midwest":
                    {
                        0
                    },
                "West and South and East and Midwest":
                    {
                        0
                    }
            },
        },
        "Oregon": {
            "UP": {
                "West":
                    {

                        demand_Oregon_UP_West * mill_data["Oregon"]["Revenue"]["UP"] - demand_Oregon_UP_West * (
                                mill_data["Oregon"]
                                ["Material"]["UP"] + mill_data["Oregon"]["Production"]["UP"]) -
                        demand_Oregon_UP_West *
                        mill_data
                        ["Oregon"]["Shipping"]["West"]

                    },
                "South":
                    {
                        demand_Oregon_UP_South * mill_data["Oregon"]["Revenue"]["UP"] - demand_Oregon_UP_South * (
                                mill_data["Oregon"]
                                ["Material"]["UP"] + mill_data["Oregon"]["Production"]["UP"]) -
                        demand_Oregon_UP_South *
                        mill_data
                        ["Oregon"]["Shipping"]["South"]
                    },
                "East":
                    {
                        demand_Oregon_UP_East * mill_data["Oregon"]["Revenue"]["UP"] - demand_Oregon_UP_East * (
                                mill_data["Oregon"]
                                ["Material"]["UP"] + mill_data["Oregon"]["Production"]["UP"]) -
                        demand_Oregon_UP_East *
                        mill_data
                        ["Oregon"]["Shipping"]["East"]
                    },
                "Midwest":
                    {
                        demand_Oregon_UP_Midwest * mill_data["Oregon"]["Revenue"]["UP"] - demand_Oregon_UP_Midwest
                        * (
                                mill_data["Oregon"]
                                ["Material"]["UP"] + mill_data["Oregon"]["Production"]["UP"]) -
                        demand_Oregon_UP_Midwest *
                        mill_data
                        ["Oregon"]["Shipping"]["Midwest"]
                    },
                "West and South":
                    {

                        (demand_Oregon_UP_West_and_South * mill_data["Oregon"]["Revenue"]["UP"]) - (
                                demand_Oregon_UP_West_and_South
                                * (
                                        mill_data["Oregon"]
                                        ["Material"]["UP"] + mill_data["Oregon"]["Production"]["UP"])) -
                        shipping_Oregon_UP_West_South

                    },
                "West and East":
                    {
                        (demand_Oregon_UP_West_and_East * mill_data["Oregon"]["Revenue"]["UP"]) - (
                                demand_Oregon_UP_West_and_East
                                * (
                                        mill_data["Oregon"]
                                        ["Material"]["UP"] + mill_data["Oregon"]["Production"]["UP"])) -
                        shipping_Oregon_UP_West_East
                    },
                "West and Midwest":
                    {
                        (demand_Oregon_UP_West_and_Midwest * mill_data["Oregon"]["Revenue"]["UP"]) - (
                                demand_Oregon_UP_West_and_Midwest
                                * (
                                        mill_data["Oregon"]
                                        ["Material"]["UP"] + mill_data["Oregon"]["Production"]["UP"])) -
                        shipping_Oregon_UP_West_Midwest
                    },
                "South and East":
                    {
                        (demand_Oregon_UP_South_and_East * mill_data["Oregon"]["Revenue"]["UP"]) - (
                                demand_Oregon_UP_South_and_East
                                * (
                                        mill_data["Oregon"]
                                        ["Material"]["UP"] + mill_data["Oregon"]["Production"]["UP"])) -
                        shipping_Oregon_UP_South_East
                    },
                "South and Midwest":
                    {
                        (demand_Oregon_UP_South_and_Midwest * mill_data["Oregon"]["Revenue"]["UP"]) - (
                                demand_Oregon_UP_South_and_Midwest
                                * (
                                        mill_data["Oregon"]
                                        ["Material"]["UP"] + mill_data["Oregon"]["Production"]["UP"])) -
                        shipping_Oregon_UP_South_Midwest
                    },
                "East and Midwest":
                    {
                        (demand_Oregon_UP_East_and_Midwest * mill_data["Oregon"]["Revenue"]["UP"]) - (
                                demand_Oregon_UP_East_and_Midwest
                                * (
                                        mill_data["Oregon"]
                                        ["Material"]["UP"] + mill_data["Oregon"]["Production"]["UP"])) -
                        shipping_Oregon_UP_East_Midwest
                    },
                "West and South and East":
                    {
                        0
                    },
                "West and East and Midwest":
                    {
                        0
                    },
                "West and South and Midwest":
                    {
                        0
                    },
                "South and East and Midwest":
                    {
                        0
                    },
                "West and South and East and Midwest":
                    {
                        0
                    }
            },

            "USS": {
                "West":
                    {
                        demand_Oregon_USS_West * mill_data["Oregon"]["Revenue"]["USS"] - demand_Oregon_USS_West * (
                                mill_data["Oregon"]
                                ["Material"]["USS"] + mill_data["Oregon"]["Production"]["USS"]) -
                        demand_Oregon_USS_West *
                        mill_data
                        ["Oregon"]["Shipping"]["West"]
                    },
                "South":
                    {
                        demand_Oregon_USS_South * mill_data["Oregon"]["Revenue"][
                            "USS"] - demand_Oregon_USS_South * (
                                mill_data["Oregon"]
                                ["Material"]["USS"] + mill_data["Oregon"]["Production"]["USS"]) -
                        demand_Oregon_USS_South *
                        mill_data
                        ["Oregon"]["Shipping"]["South"]
                    },
                "East":
                    {
                        demand_Oregon_USS_East * mill_data["Oregon"]["Revenue"][
                            "USS"] - demand_Oregon_USS_East * (
                                mill_data["Oregon"]
                                ["Material"]["USS"] + mill_data["Oregon"]["Production"]["USS"]) -
                        demand_Oregon_USS_East *
                        mill_data
                        ["Oregon"]["Shipping"]["East"]
                    },
                "Midwest":
                    {
                        demand_Oregon_USS_Midwest * mill_data["Oregon"]["Revenue"][
                            "USS"] - demand_Oregon_USS_Midwest * (
                                mill_data["Oregon"]
                                ["Material"]["USS"] + mill_data["Oregon"]["Production"]["USS"]) -
                        demand_Oregon_USS_Midwest *
                        mill_data
                        ["Oregon"]["Shipping"]["Midwest"]
                    },
                "West and South":
                    {
                        (demand_Oregon_USS_West_and_South * mill_data["Oregon"]["Revenue"]["USS"]) - (
                                demand_Oregon_USS_West_and_South
                                * (
                                        mill_data["Oregon"]
                                        ["Material"]["USS"] + mill_data["Oregon"]["Production"]["USS"])) -
                        shipping_Oregon_USS_West_South
                    },
                "West and East":
                    {
                        (demand_Oregon_USS_West_and_East * mill_data["Oregon"]["Revenue"]["USS"]) - (
                                demand_Oregon_USS_West_and_East
                                * (
                                        mill_data["Oregon"]
                                        ["Material"]["USS"] + mill_data["Oregon"]["Production"]["USS"])) -
                        shipping_Oregon_USS_West_East
                    },
                "West and Midwest":
                    {
                        (demand_Oregon_USS_West_and_Midwest * mill_data["Oregon"]["Revenue"]["USS"]) - (
                                demand_Oregon_USS_West_and_Midwest
                                * (
                                        mill_data["Oregon"]
                                        ["Material"]["USS"] + mill_data["Oregon"]["Production"]["USS"])) -
                        shipping_Oregon_USS_West_Midwest
                    },
                "South and East":
                    {
                        (demand_Oregon_USS_South_and_East * mill_data["Oregon"]["Revenue"]["USS"]) - (
                                demand_Oregon_USS_South_and_East
                                * (
                                        mill_data["Oregon"]
                                        ["Material"]["USS"] + mill_data["Oregon"]["Production"]["USS"])) -
                        shipping_Oregon_USS_South_East
                    },
                "South and Midwest":
                    {
                        (demand_Oregon_USS_South_and_Midwest * mill_data["Oregon"]["Revenue"]["USS"]) - (
                                demand_Oregon_USS_South_and_Midwest
                                * (
                                        mill_data["Oregon"]
                                        ["Material"]["USS"] + mill_data["Oregon"]["Production"]["USS"])) -
                        shipping_Oregon_USS_South_Midwest
                    },
                "East and Midwest":
                    {
                        (demand_Oregon_USS_East_and_Midwest * mill_data["Oregon"]["Revenue"]["USS"]) - (
                                demand_Oregon_USS_East_and_Midwest
                                * (
                                        mill_data["Oregon"]
                                        ["Material"]["USS"] + mill_data["Oregon"]["Production"]["USS"])) -
                        shipping_Oregon_USS_East_Midwest
                    },
                "West and South and East":
                    {
                        0
                    },
                "West and East and Midwest":
                    {
                        0
                    },
                "West and South and Midwest":
                    {
                        0
                    },
                "South and East and Midwest":
                    {
                        0
                    },
                "West and South and East and Midwest":
                    {
                        0
                    }
            },
        },
        "Arkansas": {
            "UP": {
                "West":
                    {

                        demand_Arkansas_UP_West * mill_data["Arkansas"]["Revenue"]["UP"] - demand_Arkansas_UP_West * (
                                mill_data["Arkansas"]
                                ["Material"]["UP"] + mill_data["Arkansas"]["Production"]["UP"]) -
                        demand_Arkansas_UP_West *
                        mill_data
                        ["Arkansas"]["Shipping"]["West"]

                    },
                "South":
                    {
                        demand_Arkansas_UP_South * mill_data["Arkansas"]["Revenue"]["UP"] - demand_Arkansas_UP_South * (
                                mill_data["Arkansas"]
                                ["Material"]["UP"] + mill_data["Arkansas"]["Production"]["UP"]) -
                        demand_Arkansas_UP_South *
                        mill_data
                        ["Arkansas"]["Shipping"]["South"]
                    },
                "East":
                    {
                        demand_Arkansas_UP_East * mill_data["Arkansas"]["Revenue"]["UP"] - demand_Arkansas_UP_East * (
                                mill_data["Arkansas"]
                                ["Material"]["UP"] + mill_data["Arkansas"]["Production"]["UP"]) -
                        demand_Arkansas_UP_East *
                        mill_data
                        ["Arkansas"]["Shipping"]["East"]
                    },
                "Midwest":
                    {
                        demand_Arkansas_UP_Midwest * mill_data["Arkansas"]["Revenue"]["UP"] - demand_Arkansas_UP_Midwest
                        * (
                                mill_data["Arkansas"]
                                ["Material"]["UP"] + mill_data["Arkansas"]["Production"]["UP"]) -
                        demand_Arkansas_UP_Midwest *
                        mill_data
                        ["Arkansas"]["Shipping"]["Midwest"]
                    },
                "West and South":
                    {

                        (demand_Arkansas_UP_West_and_South * mill_data["Arkansas"]["Revenue"]["UP"]) - (
                                demand_Arkansas_UP_West_and_South
                                * (
                                        mill_data["Arkansas"]
                                        ["Material"]["UP"] + mill_data["Arkansas"]["Production"]["UP"])) -
                        shipping_Arkansas_UP_West_South

                    },
                "West and East":
                    {
                        (demand_Arkansas_UP_West_and_East * mill_data["Arkansas"]["Revenue"]["UP"]) - (
                                demand_Arkansas_UP_West_and_East
                                * (
                                        mill_data["Arkansas"]
                                        ["Material"]["UP"] + mill_data["Arkansas"]["Production"]["UP"])) -
                        shipping_Arkansas_UP_West_East
                    },
                "West and Midwest":
                    {
                        (demand_Arkansas_UP_West_and_Midwest * mill_data["Arkansas"]["Revenue"]["UP"]) - (
                                demand_Arkansas_UP_West_and_Midwest
                                * (
                                        mill_data["Arkansas"]
                                        ["Material"]["UP"] + mill_data["Arkansas"]["Production"]["UP"])) -
                        shipping_Arkansas_UP_West_Midwest
                    },
                "South and East":
                    {
                        (demand_Arkansas_UP_South_and_East * mill_data["Arkansas"]["Revenue"]["UP"]) - (
                                demand_Arkansas_UP_South_and_East
                                * (
                                        mill_data["Arkansas"]
                                        ["Material"]["UP"] + mill_data["Arkansas"]["Production"]["UP"])) -
                        shipping_Arkansas_UP_South_East
                    },
                "South and Midwest":
                    {
                        (demand_Arkansas_UP_South_and_Midwest * mill_data["Arkansas"]["Revenue"]["UP"]) - (
                                demand_Arkansas_UP_South_and_Midwest
                                * (
                                        mill_data["Arkansas"]
                                        ["Material"]["UP"] + mill_data["Arkansas"]["Production"]["UP"])) -
                        shipping_Arkansas_UP_South_Midwest

                    },
                "East and Midwest":
                    {
                        (demand_Arkansas_UP_East_and_Midwest * mill_data["Arkansas"]["Revenue"]["UP"]) - (
                                demand_Arkansas_UP_East_and_Midwest
                                * (
                                        mill_data["Arkansas"]
                                        ["Material"]["UP"] + mill_data["Arkansas"]["Production"]["UP"])) -
                        shipping_Arkansas_UP_East_Midwest
                    },
                "West and South and East":
                    {
                        0
                    },
                "West and East and Midwest":
                    {
                        0
                    },
                "West and South and Midwest":
                    {
                        0
                    },
                "South and East and Midwest":
                    {
                        0
                    },
                "West and South and East and Midwest":
                    {
                        0
                    }
            },

            "USS": {
                "West":
                    {
                        demand_Arkansas_USS_West * mill_data["Arkansas"]["Revenue"][
                            "USS"] - demand_Arkansas_USS_West * (
                                mill_data["Arkansas"]
                                ["Material"]["USS"] + mill_data["Arkansas"]["Production"]["USS"]) -
                        demand_Arkansas_USS_West *
                        mill_data
                        ["Arkansas"]["Shipping"]["West"]
                    },
                "South":
                    {
                        demand_Arkansas_USS_South * mill_data["Arkansas"]["Revenue"][
                            "USS"] - demand_Arkansas_USS_South * (
                                mill_data["Arkansas"]
                                ["Material"]["USS"] + mill_data["Arkansas"]["Production"]["USS"]) -
                        demand_Arkansas_USS_South *
                        mill_data
                        ["Arkansas"]["Shipping"]["South"]
                    },
                "East":
                    {
                        demand_Arkansas_USS_East * mill_data["Arkansas"]["Revenue"][
                            "USS"] - demand_Arkansas_USS_East * (
                                mill_data["Arkansas"]
                                ["Material"]["USS"] + mill_data["Arkansas"]["Production"]["USS"]) -
                        demand_Arkansas_USS_East *
                        mill_data
                        ["Arkansas"]["Shipping"]["East"]
                    },
                "Midwest":
                    {
                        demand_Arkansas_USS_Midwest * mill_data["Arkansas"]["Revenue"][
                            "USS"] - demand_Arkansas_USS_Midwest * (
                                mill_data["Arkansas"]
                                ["Material"]["USS"] + mill_data["Arkansas"]["Production"]["USS"]) -
                        demand_Arkansas_USS_Midwest *
                        mill_data
                        ["Arkansas"]["Shipping"]["Midwest"]
                    },
                "West and South":
                    {
                        (demand_Arkansas_USS_West_and_South * mill_data["Arkansas"]["Revenue"]["USS"]) - (
                                demand_Arkansas_USS_West_and_South
                                * (
                                        mill_data["Arkansas"]
                                        ["Material"]["USS"] + mill_data["Arkansas"]["Production"]["USS"])) -
                        shipping_Arkansas_USS_West_South
                    },
                "West and East":
                    {
                        (demand_Arkansas_USS_West_and_East * mill_data["Arkansas"]["Revenue"]["USS"]) - (
                                demand_Arkansas_USS_West_and_East
                                * (
                                        mill_data["Arkansas"]
                                        ["Material"]["USS"] + mill_data["Arkansas"]["Production"]["USS"])) -
                        shipping_Arkansas_USS_West_East
                    },
                "West and Midwest":
                    {
                        (demand_Arkansas_USS_West_and_Midwest * mill_data["Arkansas"]["Revenue"]["USS"]) - (
                                demand_Arkansas_USS_West_and_Midwest
                                * (
                                        mill_data["Arkansas"]
                                        ["Material"]["USS"] + mill_data["Arkansas"]["Production"]["USS"])) -
                        shipping_Arkansas_USS_West_Midwest
                    },
                "South and East":
                    {
                        (demand_Arkansas_USS_South_and_East * mill_data["Arkansas"]["Revenue"]["USS"]) - (
                                demand_Arkansas_USS_South_and_East
                                * (
                                        mill_data["Arkansas"]
                                        ["Material"]["USS"] + mill_data["Arkansas"]["Production"]["USS"])) -
                        shipping_Arkansas_USS_South_East
                    },
                "South and Midwest":
                    {
                        (demand_Arkansas_USS_South_and_Midwest * mill_data["Arkansas"]["Revenue"]["USS"]) - (
                                demand_Arkansas_USS_South_and_Midwest
                                * (
                                        mill_data["Arkansas"]
                                        ["Material"]["USS"] + mill_data["Arkansas"]["Production"]["USS"])) -
                        shipping_Arkansas_USS_South_Midwest
                    },
                "East and Midwest":
                    {
                        (demand_Arkansas_USS_East_and_Midwest * mill_data["Arkansas"]["Revenue"]["USS"]) - (
                                demand_Arkansas_USS_East_and_Midwest
                                * (
                                        mill_data["Arkansas"]
                                        ["Material"]["USS"] + mill_data["Arkansas"]["Production"]["USS"])) -
                        shipping_Arkansas_USS_East_Midwest
                    },
                "West and South and East":
                    {
                        0
                    },
                "West and East and Midwest":
                    {
                        0
                    },
                "West and South and Midwest":
                    {
                        0
                    },
                "South and East and Midwest":
                    {
                        0
                    },
                "West and South and East and Midwest":
                    {
                        0
                    }
            },
        },
    }
    st.markdown("___")

    for wisconsinupk, wisconsinupv in (solutions_Data["Wisconsin"]["UP"]).items():
        maxwisconsinupvalue = (max(wisconsinupv))
    for wisconsinussk, wisconsinussv in (solutions_Data["Wisconsin"]["USS"]).items():
        print(max(wisconsinussv))
    for oregonupk, oregonupv in (solutions_Data["Oregon"]["UP"]).items():
        print(max(oregonupv))
    for oregonussk, oregonussv in (solutions_Data["Oregon"]["USS"]).items():
        print(max(oregonussv))
    for arkansasupk, arkansasupv in (solutions_Data["Arkansas"]["UP"]).items():
        print(max(arkansasupv))
    for arkansasussk, arkansasussv in (solutions_Data["Arkansas"]["USS"]).items():
        print(max(arkansasussv))

    best_Solutions = {
        "Wisconsin UP": max(solutions_Data["Wisconsin"]["UP"]),
        "Wisconsin USS": max(solutions_Data["Wisconsin"]["USS"]),
        "Oregon UP": max(solutions_Data["Oregon"]["UP"]),
        "Oregon USS": max(solutions_Data["Oregon"]["USS"]),
        "Arkansas UP": max(solutions_Data["Arkansas"]["UP"]),
        "Arkansas USS": max(solutions_Data["Arkansas"]["USS"])
    }
    practice_Solutions = {
        "Wisconsin UP": 180000000,
        "Wisconsin USS": 140000000,
        "Oregon UP": 19000000,
        "Oregon USS": 100000000,
        "Arkansas UP": 50000000,
        "Arkansas USS": 160000000
    }

    wisconsinUPDict = {
        "West": max(solutions_Data["Wisconsin"]["UP"]["West"]),
        "South": max(solutions_Data["Wisconsin"]["UP"]["South"]),
        "Midwest": max(solutions_Data["Wisconsin"]["UP"]["Midwest"]),
        "East": max(solutions_Data["Wisconsin"]["UP"]["East"]),
        "West and South": max(solutions_Data["Wisconsin"]["UP"]["West and South"]),
        "West and East": max(solutions_Data["Wisconsin"]["UP"]["West and East"]),
        "West and Midwest": max(solutions_Data["Wisconsin"]["UP"]["West and Midwest"]),
        "South and East": max(solutions_Data["Wisconsin"]["UP"]["South and East"]),
        "South and Midwest": max(solutions_Data["Wisconsin"]["UP"]["South and Midwest"]),
        "East and Midwest": max(solutions_Data["Wisconsin"]["UP"]["East and Midwest"])
    }
    st.write("Wisconsin Mill producing Ultra Plush")
    wisconsinUPGraph = pd.DataFrame.from_dict(wisconsinUPDict, orient='index')
    st.bar_chart(wisconsinUPGraph)
    st.markdown("___")

    wisconsinUSSDict = {
        "West": max(solutions_Data["Wisconsin"]["USS"]["West"]),
        "South": max(solutions_Data["Wisconsin"]["USS"]["South"]),
        "Midwest": max(solutions_Data["Wisconsin"]["USS"]["Midwest"]),
        "East": max(solutions_Data["Wisconsin"]["USS"]["East"]),
        "West and South": max(solutions_Data["Wisconsin"]["USS"]["West and South"]),
        "West and East": max(solutions_Data["Wisconsin"]["USS"]["West and East"]),
        "West and Midwest": max(solutions_Data["Wisconsin"]["USS"]["West and Midwest"]),
        "South and East": max(solutions_Data["Wisconsin"]["USS"]["South and East"]),
        "South and Midwest": max(solutions_Data["Wisconsin"]["USS"]["South and Midwest"]),
        "East and Midwest": max(solutions_Data["Wisconsin"]["USS"]["East and Midwest"])
    }
    st.write("Wisconsin Mill producing Ultra Soft & Strong")
    wisconsinUSSGraph = pd.DataFrame.from_dict(wisconsinUSSDict, orient='index')
    st.bar_chart(wisconsinUSSGraph)
    st.markdown("___")

    OregonUPDict = {
        "West": max(solutions_Data["Oregon"]["UP"]["West"]),
        "South": max(solutions_Data["Oregon"]["UP"]["South"]),
        "Midwest": max(solutions_Data["Oregon"]["UP"]["Midwest"]),
        "East": max(solutions_Data["Oregon"]["UP"]["East"]),
        "West and South": max(solutions_Data["Oregon"]["UP"]["West and South"]),
        "West and East": max(solutions_Data["Oregon"]["UP"]["West and East"]),
        "West and Midwest": max(solutions_Data["Oregon"]["UP"]["West and Midwest"]),
        "South and East": max(solutions_Data["Oregon"]["UP"]["South and East"]),
        "South and Midwest": max(solutions_Data["Oregon"]["UP"]["South and Midwest"]),
        "East and Midwest": max(solutions_Data["Oregon"]["UP"]["East and Midwest"])
    }
    st.write("Oregon Mill producing Ultra Plush")
    oregonUPGraph = pd.DataFrame.from_dict(OregonUPDict, orient='index')
    st.bar_chart(oregonUPGraph)
    st.markdown("___")

    OregonUSSDict = {
        "West": max(solutions_Data["Oregon"]["USS"]["West"]),
        "South": max(solutions_Data["Oregon"]["USS"]["South"]),
        "Midwest": max(solutions_Data["Oregon"]["USS"]["Midwest"]),
        "OEast": max(solutions_Data["Oregon"]["USS"]["East"]),
        "West and South": max(solutions_Data["Oregon"]["USS"]["West and South"]),
        "West and East": max(solutions_Data["Oregon"]["USS"]["West and East"]),
        "West and Midwest": max(solutions_Data["Oregon"]["USS"]["West and Midwest"]),
        "South and East": max(solutions_Data["Oregon"]["USS"]["South and East"]),
        "South and Midwest": max(solutions_Data["Oregon"]["USS"]["South and Midwest"]),
        "East and Midwest": max(solutions_Data["Oregon"]["USS"]["East and Midwest"])
    }
    st.write("Oregon Mill producing Ultra Soft & Strong")
    oregonUSSGraph = pd.DataFrame.from_dict(OregonUSSDict, orient='index')
    st.bar_chart(oregonUSSGraph)
    st.markdown("___")

    ArkansasUPDict = {
        "West": max(solutions_Data["Arkansas"]["UP"]["West"]),
        "South": max(solutions_Data["Arkansas"]["UP"]["South"]),
        "Midwest": max(solutions_Data["Arkansas"]["UP"]["Midwest"]),
        "East": max(solutions_Data["Arkansas"]["UP"]["East"]),
        "West and South": max(solutions_Data["Arkansas"]["UP"]["West and South"]),
        "West and East": max(solutions_Data["Arkansas"]["UP"]["West and East"]),
        "West and Midwest": max(solutions_Data["Arkansas"]["UP"]["West and Midwest"]),
        "South and East": max(solutions_Data["Arkansas"]["UP"]["South and East"]),
        "South and Midwest": max(solutions_Data["Arkansas"]["UP"]["South and Midwest"]),
        "East and Midwest": max(solutions_Data["Arkansas"]["UP"]["East and Midwest"])
    }
    st.write("Arkansas Mill producing Ultra Plush")
    ArkansasUPGraph = pd.DataFrame.from_dict(ArkansasUPDict, orient='index')
    st.bar_chart(ArkansasUPGraph)
    st.markdown("___")

    ArkansasUSSDict = {
        "West": max(solutions_Data["Arkansas"]["USS"]["West"]),
        "South": max(solutions_Data["Arkansas"]["USS"]["South"]),
        "Midwest": max(solutions_Data["Arkansas"]["USS"]["Midwest"]),
        "East": max(solutions_Data["Arkansas"]["USS"]["East"]),
        "West and South": max(solutions_Data["Arkansas"]["USS"]["West and South"]),
        "West and East": max(solutions_Data["Arkansas"]["USS"]["West and East"]),
        "West and Midwest": max(solutions_Data["Arkansas"]["USS"]["West and Midwest"]),
        "South and East": max(solutions_Data["Arkansas"]["USS"]["South and East"]),
        "South and Midwest": max(solutions_Data["Arkansas"]["USS"]["South and Midwest"]),
        "East and Midwest": max(solutions_Data["Arkansas"]["USS"]["East and Midwest"])
    }
    st.write("Arkansas Mill producing Ultra Soft & Strong")
    arkansasUSSGraph = pd.DataFrame.from_dict(ArkansasUSSDict, orient='index')
    st.bar_chart(arkansasUSSGraph)

if radio == "📕 Documentation":
    st.image('/Users/nolens1\Downloads/usecasegraphic (3).png')
    st.markdown("___")
    st.title("📉 Arkansas Expansion Cost : ")
    st.write("""
    The cost of expanding the Arkansas Mill is *$247,122,938*. We found this number by computing Net Profit for Arkansas
    in 2021 using the Average Growth per Year formula. We took np/365 to find how much money the company is profiting
     per day (np_per_day). We then had to find the opportunity cost for the mill operating at half production. 
     We decided to find out how much money the mill would be producing in that time under 
      normal production and divided that by 2. 
        We added that number to physical expansion cost, which was $188,500,000.
        *overall_expansion_cost = (np_per_day x number_of_days) / 2) + switching_cost*.
         We didn't think that this cost was worth the
        time, money, or resources compared to some other options.  
    """)
    st.markdown("___")

    st.title("📈 Switch Costs : ")
    st.write("""
    We found switch cost by computing Net Profit for a mill for 2021 using 
    the Average Growth per Year formula. We took np/365 to find how much money 
    is being made per day (np_per_day). Every mill has a certain time period for which they would not be able 
    to produce (down_time), and took np_per_day x down_time to find the opportunity cost for the mill
    not being in production. We added that number to physical switching cost.
    *overall_switching_cost = (np_per_day x down_time) + switching_cost *  
    """)
    st.title(" Arkansas switch cost is 💲17,662,058.14")
    st.title(" Wisconsin switch cost is 💲23,538,969.86")
    st.title(" Oregon switch cost is 💲13,620,309.04")
    st.write("")
    st.write("")
    st.write("""
    The switch cost associated with every mill is significantly cheaper than the expansion cost. We also saw that the 
    return on investment is much higher with switching rather than expanding. For simplicity purposes, 
    we kept the switch cost equation out of the algorithm.
     If we were to include it, there are many other 
    market factors that would make it more complex. (Payback periods, etc)  
    """)
    st.markdown("___")
    st.title("ℹ️ Algorithm Explanation")
    st.write("""

    The first step was to identify the static variables - the numbers given in the case study packet and 
    understanding that they won't change.
    In the real world, we know that costs and prices will change over time, but for this situation, they were set to 
    static. 
    We needed to find demand (d) for year (n) based on the growth rate (g).
    The goal was to calculate net profit for all mills and return them in a bar graph. 
    """)
    st.write("""
    The non static variable that was used (User input) was the year that the user wants to calculate for (n).
    That can be seen as:""")
    st.latex(r'''n = userInput - 2020''')

    st.write("""
    We only used 1 growth rate option - Avg Growth Rate per Year. 
    That can be seen as """)
    st.latex(r'''(((Demand2 - Demand1)/(Demand1)) + (Demand3 - Demand2)/(Demand 2)) / 2''')
    st.write("""
    We contemplated trying out multiple growth rates, such as Compound Annual Growth Rate,
    but decided against it to keep things simple. *It is important to understand that by using this growth rate, 
    we can potentially get unrealistically high returns.* We then needed to find demand (d) for the year (n) using the 
    growth 
    rate (g).

    """)
    st.write("Demand was calculated using this formula:")
    st.latex(r''' d = (demandFor2020 * (g ^ n))''')
    st.write("The rest of the formulas used are with static numbers : ")
    st.latex(r'''Revenue (r) = d * revenuePerCase''')
    st.latex(r''' shippingCost (sc) = d * shippingCostForRegion''')
    st.latex(r'''productionCost (pc) = d * productionCostForMill''')
    st.latex(r'''Cost (c) = sc + pc''')
    st.latex(r''' netProfit(np) = r - c ''')
if radio == "🗃 Work Cited":
    st.image('/Users/nolens1\Downloads\workcited.png', caption=None,
             width=None, use_column_width=None, clamp=False, channels='RGB',
             output_format='auto')
oldDataDict = {
    "Wisconsin": 181000000,
    "Oregon": 73000000,
    "Arkansas": 109000000
    }
newDataDict = {
    "Wisconsin": 213000000,
    "Oregon": 132000000,
    "Arkansas": 120000000
}
if radio == "📅 Implementation Plan":
    st.title("📑 Steps for solution")
    st.write("")
    st.write("""
    The first step is to develop a budget for the project. The total switch cost is approximately $42,000,000.00. 
    
    The second step is to identify affected roles. Jack Cobalt, Vice President of Operations, has experience
    with the Wisconsin mill. It would be in the best interest of the company if he were able to temporarally 
    oversee the switch since
    Wisconsin is the most profitable of all the mills. Jason Allen, Marketing and Sales Manager, should switch to 
    oversee the Ultra Plush industry. Jason has extended knowledge in the sales space and his competitive advantage 
    would
    be to support the marketing and sales of this new product. Olivia Kennedy should be promoted to oversee the
    marketing and sales of Ultra Soft & Strong. Nick Jones will continue oversee the Oregon mill and its capability to
     meet
    demand in an additional region. He is motivated by his mill and believes in his product. Emily Green will
    oversee the Arkansas mill switch from one product to another. Emily's performance will speak for her. Everybody else 
    will stay in their role while being flexible to help those around them. 
    
    The next step is to identify required resources. We believe that there will be a need for mill management and 
    project management personnel. We will also need production specialists in both Ultra Plush and Ultra Soft & Strong
    allocated to the proper mills. We need to identify if production resources (if any) need to be 
    reallocated to the proper mill. 
    
    The last step is to develop a timeline with key milestones for this project. The physical switch of production
    capabilities should all take within 50 days. Reallocation of mill production instruments should take within 90 days.
    We think that the reallocation of personnel should be completed within
    the year. 
    
    Accomplish these deliverables! 
    
    
    """)
    st.title("If nothing changes : ")
    st.write("")
    st.write("Wisconsin will still be producing Ultra Soft & Strong in the East, Oregon will still be producing Ultra "
             "Soft & Strong in the West, and Arkansas will still be producing Ultra Plush in every region.")
    st.write("")
    oldData = pd.DataFrame.from_dict(oldDataDict, orient='index')
    st.bar_chart(oldData)
    st.title("Our solution : ")
    st.write("Wisconsin will switch to producing Ultra Plush in the West, Oregon will add the Midwest region, and "
             "Arkansas will switch to producing Ultra Soft & Strong in the South.")
    newData = pd.DataFrame.from_dict(newDataDict, orient='index')
    st.bar_chart(newData)

if radio == "👍 Success or Failure?":
    st.title("Within 4 years (2024) :")
    st.markdown("___")
    st.write("Is the project at or under budget?")
    st.markdown("___")
    st.write("Has the project been completed on time?")
    st.markdown("___")
    st.write("Did the project deliver on the requirements?")
    st.markdown("___")
    st.write("Did the mills productivity realistically mirror our forecasted data?")
    st.markdown("___")
    st.write("Did the quality of work for the mills stay consistent?")


if radio == "💻 View Source Code Here":
    st.write("Github link: ", "https://github.com/nolen4242/UseCaseProject")
    st.markdown("![Alt Text](https://media2.giphy.com/media/TgV7fAvYIZMHOed0Rg/giphy.gif?cid"
                "=ecf05e47m9g6neabvrv5pst2qvg3lbahs1xtppdh45rvha3y&rid=giphy.gif&ct=g)")
