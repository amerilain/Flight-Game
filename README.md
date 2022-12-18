# Flight-Game, Requirement Specification Document

## Group One: Amir Ghari, Aleksi Merilainen, Chad Clusker, Arina Vasileva


The folder v.2 contains all the project files
 

### Chapter 1
###### Introduction:

    This document describes the purpose and functionality of Group one's flight
    simulator game from the player’s perspective. In this document, we will describe
    what the user can do with the game and outline the game's goals and implementation.
    
    This document is written for two audiences: first, it is intended as a reference for our
    group to use during project implementation/futre impovements and second, it is for the 
    player to better understand the purpose of the game and how they can interact 
    with it.

    Here we explain the game's current state, the purpose of the game, how it works, how
    it's played, and how the game is expected to perfom.

### Chapter 2:
###### Current State

    In its current state, Alien Weather  is an interactive, web browser-based game which uses 
    Leaflet maps and OpenWeather API as external data sources and the course’s flight_game 
    relational database. 

    The front end is implemented using HTML, CSS, and JavaScript for the
    necessary browser functionality. 

    Game operation logic is implemented as a Python-based backend service that provides an API
    for the browser, handles JSON responses, utilizes the language’s object oriented 
    functionality and takes sustainable development practices into account

    Alien Weather is appropriate for all ages, has concrete goals and provides a clear and 
    enjoyable gaming experience.

### Chapter 3:

###### vision of the game - what the purpose of the game is and how it works

    The purpose of the game is  to travel between different airports around the world,
    each of which have randomly generated weather conditions in order to reach goals
    from the goal table of the flight_game database.

    Players begin in Helsinki Vantaa airport with a CO2 budget of fifteen thousand credits.
    Each "flight" will deduct CO2 from the player's budget based on the number of kilometers
    travelled (1 km equals to one CO2 point). Players can fly to any airport in the world as
    long as they have enough budgeted CO2 for the trip.

    Then, as soon as players enter the username they are presented a list of options and should
    make their first move: check their current location, view goals, search by continent to show
    selected airports, check their CO2 budget and travel to a new airport. 

    After each flight, they are informed of their new location, the local weather conditions,
    the goals which those conditions unlock, and are presented again with the game options.

    When players achieve all the eight weather goals, they win the game.
    
    ![image](https://user-images.githubusercontent.com/111734550/208272624-4152f23a-8e73-4979-9961-2a30fe0307db.png)

### Chapter 4:

###### Functional requirements – what the user can do with the game and how they interact with it

    Alien Weather has been designed in order to be intuitive for the player. Indeed, after entering their 
    name, the player will be faced with different information bars such as the game status which represents 
    the co2-consumed and co2-budget, the weather at different airports, and lastly distinctive goals that 
    the player needs to achieve.

    To interact with the game in an optimized way, the player first needs to enter the continent where they 
    want to travel, afterwards, airports of that specific continent will be shown on the map. According to 
    the remaining goals and the weather status of each airport which is accessible by clicking on the 
    airport markers, the player will decide in which airport they want to land.

    The major challenge of the game is to achieve the goals while not exceeding the co2 budget threshold 
    which is 15000 kg. Otherwise, the game will be over and the player has to start from the beginning.
### Chapter 5:

###### Quality requirements – how the game must perform and what the user experience must entail

    We set out with two requirements in mind, a fast and responsive user experience and a product with 
    no major bugs. 
    
    Our first hurdle was to make the map usage fast and for it to work on older browsers / devices. This 
    was mainly due to having such a large database of airports where the player could fly to. We fixed 
    this issue by limiting the airports to only large ones. That helped, but not enough. We added a form 
    where you could limit the amount of visible airports to only the ones from one continent. That made 
    sure there could always be a low amount of markers on screen even if you were on older devices.
    
    The second hurdle was getting the live weather data to show up on the markers in the map when you 
    clicked on them. At first it was too slow because the app was calling the weather data for all airports 
    simultaneously. This was fixed by having the API call done when the marker was clicked, meaning that 
    there would be only one call at a time making the experience quick and low latency. 
    
    Due to our tweaks and additional features we have satisfied our two requirements and made the experience 
    as good as we wanted it to be.


 

 
 
