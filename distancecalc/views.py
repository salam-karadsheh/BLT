from django.shortcuts import render
import pandas as pd

# Create your views here.
# request handle - action

def search_intra_asia(request):
    #Intra-Asia Routes
    df = pd.read_csv('/static/distances.csv')
    df['Distance'] = df['Distance'].astype(int)
    include_countries = ['Thailand', 'Indonesia', 'Singapore', 'South Korea', 'Hong Kong', 'Malaysia', 'Sarawak', 'Taiwan', 'China', 'Japan', 'Vietnam', 'Philippines', 'Brunei', 'Myanmar']
    pattern = '|'.join(include_countries)
    df = df[(df['From'].str.contains(pattern)) & (df['To'].str.contains(pattern)) & (df['Distance'] <= 1500)]
    all_countries = ['Thailand', 'Indonesia', 'Singapore', 'South Korea', 'Hong Kong', 'Malaysia', 'Sarawak', 'Taiwan', 'China', 'Japan', 'Vietnam', 'Philippines']
    all_countries.sort()

    #request handling
    starting_country = request.GET.get('starting_country')
    ending_country = request.GET.get('ending_country')
    within_range = request.GET.get('within_range')

    found = False
    temp = ""
    temp_two = ""
    if (ending_country == "") | (ending_country == None):
        if (within_range == "") | (within_range == None):
            distance_df = df[(df['From'].str.contains(str(starting_country), case = False))].sort_values(['From', 'To'])
        else:
            distance_df = df[(df['From'].str.contains(str(starting_country), case = False)) & (df['To'].str.contains(str(ending_country), case = False)) & (df['Distance'] <= float(within_range))].sort_values(['From', 'To'])
            temp_two = " within " + str(within_range) + " NM"
    else: 
        if (within_range == "") | (within_range == None):
            distance_df = df[(df['From'].str.contains(str(starting_country), case = False)) & (df['To'].str.contains(str(ending_country), case = False))].sort_values(['From', 'To'])
        else:
            distance_df = df[(df['From'].str.contains(str(starting_country), case = False)) & (df['To'].str.contains(str(ending_country), case = False)) & (df['Distance'] <= float(within_range))].sort_values(['From', 'To'])
            temp_two = " within " + str(within_range) + " NM"
        temp = " to " + str(ending_country).title()
    if distance_df.empty:
        routes_found = []
    else:
        found = True
        routes_found = all_calculations(distance_df)
    route = str(starting_country).title() + temp + temp_two
    return render(request, 'asia.html', {'countries' : all_countries, 'routes_found' : routes_found, 'found' : found, 'route' : route})

def test(request):
    #All Routes
    df = pd.read_csv('/static/distances.csv')
    df['Distance'] = df['Distance'].astype(int)

    all_countries = ['Alaska','Albania','Algeria','American Samoa','Andaman Islands','Angola','Antigua','Argentina','Aruba','Ascension Island','Australia','Azores',
    'Bahamas','Bahrain','Baker Island','Balearic Islands','Bangladesh','Barbados','Belgium','Belize','Benin','Bermuda','Bjornoya Island','Bonaire','Bonin Islands',
    'Brazil','British Honduras','Bulgaria','Burma','Cabinda','Cambodia','Cameroon','Canada','Canary Islands','Cape Verde Islands','Caroline Islands','Cayman Islands',
    'Celebes','Chagos Archipelago','Chile','China','Christmas Island','Cocos Islands','Colombia','Congo','Cook Islands','Corsica','Costa Rica','Croatia','Cuba','Curacao',
    'Cyprus','Dahomey','Denmark','Djibouti','Dominica','Dominican Republic','Easter Island','Ecuador','Egypt','El Salvador','England','Equatorial Guinea','Estonia',
    'Ethiopia','Falkland Islands','Fanning Island','Faroe Islands','Fernando De Noronha','Fiji Islands','Finland','France','French Polynesia','Gabon','Gambia','Georgia',
    'Germany','Ghana','Gibraltar','Gilbert Islands','Grand Bahamas','Grand Banks South','Grand Cayman','Grand Turk Island','Great Inagua Island','Greece','Greenland',
    'Grenada','Guadeloupe','Guam','Guatemala','Guinea','Guinea-Bissau','Gulf Of Guinea','Guyana','Haiti','Honduras','Hong Kong','Honshu Japan','Howland Island','Iceland',
    'Iles Tuamotu','India','Indonesia','Iran','Iraq','Ireland','Isla De Vieques','Islas Juan Fernandez','Isle Of Man','Israel','Italy','Ivory Coast','Jamaica','Japan',
    'Jarvis Island','Johnston Island','Jordan','Kalimantan','Kenya','Kermadec Islands','Kiribati','Kriti','Kuwait','Latvia','Lebanon','Liberia','Libya','Line Islands',
    'Lithuania','Madagascar','Madeira Island','Malaysia','Malta','Mariana Islands','Marie Galante','Marquesa Islands','Marshall Islands','Martinique','Mauritania',
    'Mauritius','Mexico','Midway Island','Monaco','Montenegro','Montserrat','Morocco','Mozambique','Namibia','Netherlands','New Caledonia','New Guinea','New Zealand',
    'Newcaledonia','Nicaragua','Nigeria','Nord-Ostsee-Kanal','North Korea','Northern Ireland','Norway','Ocean Island','Oman','Outer Bar','Pakistan','Palau Islands',
    'Panama','Papua New Guinea','Patrai Greece','Peru','Philippines','Phoenix Islands','Poland','Port Sudan','Portugal','Puerto Bolivar','Puerto Rico','Qatar',
    'Reunion Islands','Romania','Russia','Ryukyu Islands','Sabah','Saint Kitts And Nevis','Samoa','Sao Tome','Sarawak','Sardinia','Saudi Arabia','Scotland','Senegal',
    'Seychelles','Sicily','Sierra Leone','Singapore','Slovenia','Solomon Islands','Somalia','South Africa','South Korea','Spain','Sri Lanka','St. Croix','St. Eustatius',
    'St. Helena Island','St. Lucia','St. Vincent','Strait Of Gibraltar','Sudan','Sulawesi','Suriname','Svalbard','Sweden','Syria','Taiwan','Tanzania','Tasmania','Thailand',
    'Togo','Tonga Islands','Trinidad','Tunisia','Turkey','Tuvalu','United States','Ukraine','United Arab Emirates','United Kingdom','Uruguay','Vanuatu','Venezuela','Vietnam',
    'Virgin Islands','Wake Island','Wales','Western Sahara','Yemen','Yucatan Channel']
    all_countries.sort()

    #request handling
    starting_country = request.GET.get('starting_country')
    ending_country = request.GET.get('ending_country')
    within_range = request.GET.get('within_range')
    found = False
    temp = ""
    temp_two = ""
    if (ending_country == "") | (ending_country == None):
        if (within_range == "") | (within_range == None):
            distance_df = df[(df['From'].str.contains(str(starting_country), case = False))].sort_values(['From', 'To'])
        else:
            distance_df = df[(df['From'].str.contains(str(starting_country), case = False)) & (df['To'].str.contains(str(ending_country), case = False)) & (df['Distance'] <= float(within_range))].sort_values(['From', 'To'])
            temp_two = " within " + str(within_range) + " NM"
    else: 
        if (within_range == "") | (within_range == None):
            distance_df = df[(df['From'].str.contains(str(starting_country), case = False)) & (df['To'].str.contains(str(ending_country), case = False))].sort_values(['From', 'To'])
        else:
            distance_df = df[(df['From'].str.contains(str(starting_country), case = False)) & (df['To'].str.contains(str(ending_country), case = False)) & (df['Distance'] <= float(within_range))].sort_values(['From', 'To'])
            temp_two = " within " + str(within_range) + " NM"
        temp = " to " + str(ending_country).title()
    if distance_df.empty:
        routes_found = []
    else:
        found = True
        routes_found = all_calculations(distance_df)
    route = str(starting_country).title() + temp + temp_two
    return render(request, 'test.html', {'countries' : all_countries, 'routes_found' : routes_found, 'found' : found, 'route' : route})

def routes(request):
    df = pd.read_csv('/static/distances.csv')
    df['Distance'] = df['Distance'].astype(int)
    all_countries = df['From'].unique()
    all_countries.sort()
    country_from = request.GET.get('country_from')
    within_range = request.GET.get('within_range')
    found = False
    temp = ""
    if (within_range == "") | (within_range == None):
        distance_df = df[(df['From'].str.contains(str(country_from), case = False))].sort_values('Distance')
    else: 
        distance_df = df[(df['From'].str.contains(str(country_from), case = False)) & (df['Distance'] <= float(within_range))].sort_values('Distance')
        temp = " within " + str(within_range) + " NM"
    if distance_df.empty:
        routes_found = []
    else:
        found = True
        routes_found = distance_df.values.tolist
    route = str(country_from).title() + temp
    return render(request, 'routes.html', {'countries' : all_countries, 'routes_found' : routes_found, 'found' : found, 'route' : route})

def search_two(request):
    df = pd.read_csv('/static/distances.csv')
    df['Distance'] = df['Distance'].astype(int)
    all_countries = df['From'].unique()
    starting_point = request.GET.get('starting_point')
    ending_point = request.GET.get('ending_point')
    avg_speed = request.GET.get('avg_speed')
    if (request.GET.get('starting_point') is None) & (request.GET.get('ending_point') is None):
        route = ""
        distance = ""
        ptp_time = ""
        dtd_time = ""
    else:
        distance_df = df['Distance'][(df['From'].str.contains(str(starting_point))) & (df['To'].str.contains(str(ending_point)))]
        if distance_df.empty:
            distance = 'Route Not Available'
            ptp_time = 'Route Not Available'
            dtd_time = 'Route Not Available'
        else:
            distance = distance_df.values[0]
            if avg_speed == "":
                ptp_time = "Enter Speed"
                dtd_time = "Enter Speed"
            else:
                ptp_time = (round(float(distance) / float(avg_speed), 1))
                dtd_time = ptp_time + 24
                if ptp_time > 23.9:
                    ptp_time = str(round(ptp_time / 24.0, 1)) + " Days"
                else:
                    ptp_time = str(round(ptp_time, 1)) + " Hours"
                if dtd_time > 23.9:
                    dtd_time = str(round(dtd_time / 24.0, 1)) + " Days"
                else:
                    dtd_time = str(round(dtd_time, 1)) + " Hours"
        route = str(starting_point) + " to " + str(ending_point)

    return render(request, 'search.html', {'countries' : all_countries, 'distance' : distance, 
                                            'route' : route, 'ptp_time' : ptp_time, 'dtd_time' : dtd_time})

def all_calculations(df_temp):
    new_list = []    

    for index, row in df_temp.iterrows():
        route = str(row['From']) + " - " + str(row['To'])
        distance = row['Distance']
        remaining_distance = distance
        ptp_time = 0.0
        #Port-to-Port transit time handling
        #Routes involving Singapore should take into account speed limit of 12 knots for 7 NM
        if (row['From'] == 'Singapore') | (row['To'] == 'Singapore'):
            speed_limit_distance = 7.0
            speed_limit = 12.0
            ptp_time = ptp_time + round((speed_limit_distance / speed_limit), 1)
            remaining_distance = remaining_distance - speed_limit_distance
            if distance >= 150:
                slow_distance = 3.0
                slow_speed = 5.0
                ptp_time = ptp_time + round((slow_distance / slow_speed), 1)
                remaining_distance = remaining_distance - slow_distance
            else:
                slow_distance = 1.5
                slow_speed = 5.0
                ptp_time = ptp_time + round((slow_distance / slow_speed), 1)
                remaining_distance = remaining_distance - slow_distance
        #Routes not involving Singapore
        else: 
            if distance >= 150:
                slow_distance = 3.0 * 2.0
                slow_speed = 5.0
                ptp_time = ptp_time + round((slow_distance / slow_speed), 1)
                remaining_distance = remaining_distance - slow_distance
            else:
                slow_distance = 1.5 * 2.0
                slow_speed = 5.0
                ptp_time = ptp_time + round((slow_distance / slow_speed), 1)
                remaining_distance = remaining_distance - slow_distance
        ptp_time = ptp_time + round((remaining_distance / 40.0), 1)
        #Door-to-Door transit time handling
        dtd_time = 0.0
        num_containers_loaded = 20
        num_containers_unloaded = 20
        #mins
        docking = 20
        #mins
        undocking = 20
        #mins
        load_one_container = 1.5
        #mins
        unload_one_container = 1.5
        #mins
        loading = num_containers_loaded * load_one_container
        #mins
        unloading = num_containers_unloaded * unload_one_container
        #trucking
        to_port = 3
        from_port = 3
        #wait time at port
        port_wait = 2.5
        dtd_time = ((loading + unloading + docking + undocking) / 60.0) + ptp_time + to_port + from_port + port_wait
        
        #Turn transit times into days
        ptp_time = ptp_time / 24.0
        dtd_time = dtd_time / 24.0

        #######
        #Fuel consumption per day in kgs
        fuel_consumption_per_day = 15000.0
        #fuel consumption per trip in kgs
        fuel_consumption = fuel_consumption_per_day * ptp_time
        #15 tons a day - 24 hours

        #######
        #price of hydrogen per kg
        h2_price_per_kg = 4.0
        variable_cost = h2_price_per_kg * fuel_consumption
        #place holder
        fixed_cost = 1000.0
        #in kgs
        payload = 200000.0
        cost_per_kg = (variable_cost + fixed_cost) / payload
        price_margin = 0.4
        price_per_kg = cost_per_kg * (1 + price_margin)

        #Formatting
        fuel_consumption = int(fuel_consumption)
        cost_per_kg = round(cost_per_kg, 2)
        price_per_kg = round(price_per_kg, 2)
        if ptp_time > 1.0:
            ptp_time = str(round(ptp_time, 1)) + " Days"
        else:
            ptp_time = str(round(ptp_time * 24.0, 1)) + " Hours"
        if dtd_time > 1.0:
            dtd_time = str(round(dtd_time, 1)) + " Days"
        else:
            dtd_time = str(round(dtd_time * 24.0, 1 )) + " Hours"

        new_list.append([route, distance, ptp_time, dtd_time, fuel_consumption, cost_per_kg, price_per_kg])
    return new_list
