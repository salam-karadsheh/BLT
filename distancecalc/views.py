from django.shortcuts import render
import pandas as pd

#This view function handles the intra-asia route calculator
def search_intra_asia(request):
    #Load the entire dataset from distance.csv file
    df = pd.read_csv('https://raw.githubusercontent.com/salam-karadsheh/BLT/master/distances.csv')
    df['Distance'] = df['Distance'].astype(int)
    
    #Filter the dataset to only include intra-Asia routes involving the following countries
    include_countries = ['Thailand', 'Indonesia', 'Singapore', 'South Korea', 'Hong Kong', 'Malaysia', 'Sarawak', 'Taiwan', 'China', 'Japan', 'Vietnam', 'Philippines']
    pattern = '|'.join(include_countries)
    df = df[(df['From'].str.contains(pattern)) & (df['To'].str.contains(pattern))]
    all_countries = ['Thailand', 'Indonesia', 'Singapore', 'South Korea', 'Hong Kong', 'Malaysia', 'Sarawak', 'Taiwan', 'China', 'Japan', 'Vietnam', 'Philippines']
    all_countries.sort()

    #Request handling
    starting_country = request.GET.get('starting_country')
    ending_country = request.GET.get('ending_country')
    within_range = request.GET.get('within_range')
    
    #This boolean variable is True if any results were found and False otherwise
    found = False
    temp = ""
    temp_two = ""
    
    #Handles the case when the Ending Country is not specified
    if (ending_country == "") | (ending_country == None):
        #Handles the case when the range is not specified
        if (within_range == "") | (within_range == None):
            distance_df = df[(df['From'].str.contains(str(starting_country), case = False))].sort_values(['From', 'To'])
        #Handles the case when the range is specified
        else:
            distance_df = df[(df['From'].str.contains(str(starting_country), case = False)) & (df['To'].str.contains(str(ending_country), case = False)) & (df['Distance'] <= float(within_range))].sort_values(['From', 'To'])
            #String to display the specified range
            temp_two = " within " + str(within_range) + " NM"
    #Handles the case when the Ending Country is specified 
    else: 
        #Handles the case when the range is not specified
        if (within_range == "") | (within_range == None):
            distance_df = df[(df['From'].str.contains(str(starting_country), case = False)) & (df['To'].str.contains(str(ending_country), case = False))].sort_values(['From', 'To'])
        #Handles the case when the range is specified
        else:
            distance_df = df[(df['From'].str.contains(str(starting_country), case = False)) & (df['To'].str.contains(str(ending_country), case = False)) & (df['Distance'] <= float(within_range))].sort_values(['From', 'To'])
            #String to display the specified range
            temp_two = " within " + str(within_range) + " NM"
        #String to display the specified Ending Country
        temp = " to " + str(ending_country).title()
    
    #Handles the case when there are no routes found
    if distance_df.empty:
        routes_found = []
    #Handles the case when there are routes found
    else:
        found = True
        #Calls the function to retrieve all the calculations necessary to be displayed
        routes_found = all_calculations(distance_df)
    #String to display the full route
    route = str(starting_country).title() + temp + temp_two
    return render(request, 'asia.html', {'countries' : all_countries, 'routes_found' : routes_found, 'found' : found, 'route' : route})

#This view function handles all the routes
def search_global(request):
    #Load the entire dataset from distance.csv file
    df = pd.read_csv('https://raw.githubusercontent.com/salam-karadsheh/BLT/master/distances.csv')
    df['Distance'] = df['Distance'].astype(int)

    #List of all the countries in the dataset (parsed) to display in the dropdown search bars
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

    #Request handling
    starting_country = request.GET.get('starting_country')
    ending_country = request.GET.get('ending_country')
    within_range = request.GET.get('within_range')
    
    #This boolean variable is True if any results were found and False otherwise
    found = False
    temp = ""
    temp_two = ""
    
    #Handles the case when the Ending Country is not specified
    if (ending_country == "") | (ending_country == None):
        #Handles the case when the range is not specified
        if (within_range == "") | (within_range == None):
            distance_df = df[(df['From'].str.contains(str(starting_country), case = False))].sort_values(['From', 'To'])
        #Handles the case when the range is specified
        else:
            distance_df = df[(df['From'].str.contains(str(starting_country), case = False)) & (df['To'].str.contains(str(ending_country), case = False)) & (df['Distance'] <= float(within_range))].sort_values(['From', 'To'])
            #String to display the specified range
            temp_two = " within " + str(within_range) + " NM"
    #Handles the case when the Ending Country is specified
    else: 
        #Handles the case when the range is not specified
        if (within_range == "") | (within_range == None):
            distance_df = df[(df['From'].str.contains(str(starting_country), case = False)) & (df['To'].str.contains(str(ending_country), case = False))].sort_values(['From', 'To'])
        #Handles the case when the range is specified
        else:
            distance_df = df[(df['From'].str.contains(str(starting_country), case = False)) & (df['To'].str.contains(str(ending_country), case = False)) & (df['Distance'] <= float(within_range))].sort_values(['From', 'To'])
            #String to display the specified range
            temp_two = " within " + str(within_range) + " NM"
        #String to display the specified Ending Country
        temp = " to " + str(ending_country).title()
    
    #Handles the case when there are no routes found
    if distance_df.empty:
        routes_found = []
    #Handles the case when there are routes found
    else:
        found = True
        #Calls the function to retrieve all the calculations necessary to be displayed
        routes_found = all_calculations(distance_df)
    #String to display the full route
    route = str(starting_country).title() + temp + temp_two
    return render(request, 'global.html', {'countries' : all_countries, 'routes_found' : routes_found, 'found' : found, 'route' : route})

#This view function handles the 'all routes within a given range' tool
def routes(request):
    #Load the entire dataset from distance.csv file
    df = pd.read_csv('https://raw.githubusercontent.com/salam-karadsheh/BLT/master/distances.csv')
    df['Distance'] = df['Distance'].astype(int)
    #Get all the unique origins for the dropdown search bar options
    all_countries = df['From'].unique()
    all_countries.sort()
    
    #Request handling
    country_from = request.GET.get('country_from')
    within_range = request.GET.get('within_range')
    
    #This boolean variable is True if any results were found and False otherwise
    found = False
    temp = ""
    
    #Handles the case when the range is not specified
    if (within_range == "") | (within_range == None):
        distance_df = df[(df['From'].str.contains(str(country_from), case = False))].sort_values('Distance')
    #Handles the case when the range is specified
    else: 
        distance_df = df[(df['From'].str.contains(str(country_from), case = False)) & (df['Distance'] <= float(within_range))].sort_values('Distance')
        #String to display the specified range
        temp = " within " + str(within_range) + " NM"
    
    #Handles the case when there are no routes found
    if distance_df.empty:
        routes_found = []
    #Handles the case when there are routes found
    else:
        found = True
        routes_found = distance_df.values.tolist
    #String to display the full route
    route = str(country_from).title() + temp
    return render(request, 'routes.html', {'countries' : all_countries, 'routes_found' : routes_found, 'found' : found, 'route' : route})

#This helper function handles all the calculations needed to be displayed
def all_calculations(df_temp):
    new_list = []    
    #Iterate through each row in the specified dataset
    for index, row in df_temp.iterrows():
        #String to display the route on each button
        route = str(row['From']) + " - " + str(row['To'])
        #Gets the route distance
        distance = row['Distance']
        
        #######################################
        #Port-to-Port Transit Time Calculations
        remaining_distance = distance
        ptp_time = 0.0
        #Routes involving Singapore should take into account speed limit of 12 knots for 7 NM
        if (row['From'] == 'Singapore') | (row['To'] == 'Singapore'):
            #Total distance for complying with the speed limit (NM)
            speed_limit_distance = 7.0
            #Speed limit (knots)
            speed_limit = 12.0
            #Factoring in the time under which the vessel must comply with speed limit
            ptp_time = ptp_time + (speed_limit_distance / speed_limit)
            remaining_distance = remaining_distance - speed_limit_distance
            #Factoring in the transit time for the remaining distance on routes over [150 NM]
            if distance >= 150:
                #Total distance for which the vessel is going at a slow speed (NM)
                slow_distance = 3.0
                #Slow speed (knots)
                slow_speed = 5.0
                ptp_time = ptp_time + (slow_distance / slow_speed)
                remaining_distance = remaining_distance - slow_distance
            #Factoring in the transit time for the remaining distance on routes under [150 NM]
            else:
                #Total distance for which the vessel is going at a slow speed (NM)
                slow_distance = 1.5
                #Slow speed (knots)
                slow_speed = 5.0
                ptp_time = ptp_time + (slow_distance / slow_speed)
                remaining_distance = remaining_distance - slow_distance
        #Routes not involving Singapore
        else: 
            #Routes over [150 NM]
            if distance >= 150:
                #Total distance for which the vessel is going at a slow speed (NM) (twice that of earlier)
                slow_distance = 3.0 * 2.0
                #Slow speed (knots)
                slow_speed = 5.0
                ptp_time = ptp_time + (slow_distance / slow_speed)
                remaining_distance = remaining_distance - slow_distance
            else:
                #Total distance for which the vessel is going at a slow speed (NM) (twice that of earlier)
                slow_distance = 1.5 * 2.0
                #Slow speed (knots)
                slow_speed = 5.0
                ptp_time = ptp_time + (slow_distance / slow_speed)
                remaining_distance = remaining_distance - slow_distance
        #Vessel travels at a speed of [40.0 knots] for the remaining distance of the trip
        ptp_time = ptp_time + (remaining_distance / 40.0)
        
        #######################################
        #Door-to-Door Transit Time Calculations
        dtd_time = 0.0
        #Number of containers loaded and unloaded from vessel
        num_containers_loaded = 20
        num_containers_unloaded = 20
        #Docking time (mins)
        docking = 20
        #Undocking time (mins)
        undocking = 20
        #Time needed to load one container (mins)
        load_one_container = 1.5
        #Time needed to unload one container (mins)
        unload_one_container = 1.5
        #Total time taken to load all the containers (mins)
        loading = num_containers_loaded * load_one_container
        #Total time taken to unload all the containers (mins)
        unloading = num_containers_unloaded * unload_one_container
        #Trucking time to port (hrs)
        to_port = 3
        #Trucking time from port (hrs)
        from_port = 3
        #Additional wait time at ports (hrs)
        port_wait = 2.5
        
        #Final calculation
        dtd_time = ((loading + unloading + docking + undocking) / 60.0) + ptp_time + to_port + from_port + (port_wait * 2.0)
        
        #Turn transit times into days
        ptp_time_days = ptp_time / 24.0
        dtd_time_days = dtd_time / 24.0

        ##############################
        #Fuel Consumption Calculations
        fuel_consumption = 0.0
        #Fuel consumption per day (tons)
        fuel_consumption_per_day = 15.0
        #Total fuel consumption per trip (tons)
        fuel_consumption = fuel_consumption_per_day * ptp_time_days

        #####################################
        #ARGO Freight Cost/Price Calculations
        #Price of hydrogen per ton ($ / ton)
        h2_price_per_ton = 4000.0
        #Fixed cost per trip accounting for crew salaries, depreciation... ($)
        fixed_cost_per_trip = (3500000.0 / 300.0 / 24.0) * ((ptp_time + 6.0))
        #Fuel cost per trip ($)
        fuel_costs = h2_price_per_ton * fuel_consumption
        #Cargo handling costs ($)
        cargo_handling = 4000.0
        #Port costs ($)
        port_costs = 1000.0
        #Payload (kg)
        payload = 200000.0
        
        #ARGO freight cost per kg ($ / kg)
        freight_cost_per_kg = (fixed_cost_per_trip + fuel_costs + cargo_handling + port_costs) / payload
        
        #ARGO freight price per kg ($ / kg)
        freight_price_per_kg = freight_cost_per_kg / 0.6

        #Formatting
        fuel_consumption = round(fuel_consumption, 1)
        freight_cost_per_kg = round(freight_cost_per_kg, 2)
        freight_price_per_kg = round(freight_price_per_kg, 2)
        #Displaying transit time in days vs hours
        if ptp_time_days > 1.0:
            ptp_time = str(round(ptp_time_days, 1)) + " Days"
        else:
            ptp_time = str(round(ptp_time, 1)) + " Hours"
        if dtd_time_days > 1.0:
            dtd_time = str(round(dtd_time_days, 1)) + " Days"
        else:
            dtd_time = str(round(dtd_time, 1 )) + " Hours"

        new_list.append([route, distance, ptp_time, dtd_time, fuel_consumption, freight_cost_per_kg, freight_price_per_kg])
    return new_list
