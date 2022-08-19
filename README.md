# BLT Shipping Route Calculator
This web application was developed for Boundary Layer Technologies to present details on a selection of sea routes from a scraped database of 30,000 sea distances. The tools provide specific information regarding the distance, port-to-port transit time, door-to-door transit time, fuel consumption, and freight rate estimates for their hydrogen-powered cargo ship - ARGO - on a given route. 

Instructions for how to navigate the web application are provided below:
- Tool #1 "All Routes": Provides a list of available routes from a specified country to another with the option to filter routes within a certain range. Simply select the country endpoints from the dropdown list of the search bars, and click search to display the routes. If no routes are displayed, then there are no such routes in the database for the set of countries provided. Once the routes are displayed, you can click on any of the routes to present a dropdown of the route details. If you want to display all the routes starting or ending at a certain point, leave the corresponding search bar input empty. 

- Tool #2 "Intra-Asia Routes": Provides a list of available routes from a specified country to another with the option to filter routes within a certain range, only for intra-Asia routes. 

- Tool #3 "Routes within a Range": Provides a list of available routes from a specified origin point with the option to filter routes within a certain range. Simply type in the origin point and click search to display a table of all the routes starting from this origin point including their distances. 

Assumptions: 
- Breakdown of Port-to-Port transit time calculations:
  - All routes involving Singapore must take into account the 12 knots speed limit for 7 NM within the Singaporean Strait.
  - All routes under [150] NM must take into account 'slow speed zones' in which the vessel travels at an average speed of [5] knots for [6] NM.
  - All routes over [150] NM must take into account 'slow speed zones' in which the vessel travels at an average speed of [5] knots for [3] NM. 
  - The vessel is assumed to travel at its cruise speed of 40 knots for the remainder of the trip. 

- Breakdown of Door-to-Door transit time calculations:
  - Loading [20] TEU containers takes [1.5] mins each. 
  - Unloading [20] TEU containers takes [1.5] mins each. 
  - Docking takes [20] mins. 
  - Undocking takes [20] mins.
  - Trucking time to origin port takes [3] hours.
  - Trucking time from destination port take [3] hours.
  - Additional wait time of [2.5] hours at each port.
