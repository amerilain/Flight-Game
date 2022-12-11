for (let airport of airports) {
      const marker = L.marker([airport.latitude, airport.longitude]).addTo(map);
      if (airport.active) {
        showWeather(airport);
        //check game over is true or false
        /*if (gameData['gameover'] == true) {
          document.querySelector('.dark-background').classList.remove('hide');
          document.querySelector('.goal').classList.add('hide');
          document.querySelector('.gameover').classList.remove('hide');
          // console.log('game over');
          return false;

        }
        */
        //flash image
        //return
        checkGoals(airport.weather.meets_goals);
        marker.bindPopup(`You are here: <b>${airport.name}</b>`);
        marker.openPopup();
        marker.setIcon(greenIcon);
      } else {
        marker.setIcon(blueIcon);
        const popupContent = document.createElement('div');
        const h4 = document.createElement('h4');
        h4.innerHTML = airport.name;
        popupContent.append(h4);
        const goButton = document.createElement('button');
        goButton.classList.add('button');
        goButton.innerHTML = 'Fly here';
        popupContent.append(goButton);
        const p = document.createElement('p');
        marker.addEventListener('click', async function() {
          const weatherdata = await getData(
              weatherapiurl + 'lat=' + airport.latitude + '&lon=' +
              airport.longitude + '&appid=' + apikey + '&units=metric');
          console.log(weatherdata);
          p.innerHTML = `Distance: ${airport.distance} km <br /> Temperature: ${weatherdata.main.temp}°C <br /> Conditions: ${weatherdata.weather[0].description}<br /> Wind: ${weatherdata.wind.speed}m/s`;
        });
        // console.log(`${apiUrl}getweather?EFHK`);
        popupContent.append(p);
        marker.bindPopup(popupContent);
        /*goButton.addEventListener('click', async function() {
          gameSetup(
              `${apiUrl}flyto?game=${gameData.status.id}&dest=${airport.ident}&consumption=${airport.co2_consumption}`);
        });*/

      }
    }
updateGoals(gameData.goals);
