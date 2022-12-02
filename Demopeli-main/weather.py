import requests
import config

class Weather:

    def kelvin_to_celsius(self, kelvin):
        return int (kelvin - 273.15)

    def check_weather_goals(self, game):

        for goal in game.goals:
            if goal.target=="TEMP":
                # temperature rule
                if self.temp>=goal.target_minvalue and self.temp<=goal.target_maxvalue:
                    self.meets_goals.append(goal.goalid)
            elif goal.target=="WEATHER":
                # weather type rule
                if self.main==goal.target_text:
                    self.meets_goals.append(goal.goalid)
            elif goal.target=="WIND":
                # wind rule
                if self.wind["speed"]>=goal.target_minvalue and self.wind["speed"]<=goal.target_maxvalue:
                    self.meets_goals.append(goal.goalid)

        for goal in game.goals:
            if goal.reached==False and goal.goalid in self.meets_goals:
                # new goal
                sql = "INSERT INTO GoalReached VALUES ('" + game.status["id"] + "', '" + str(goal.goalid)  + "')"
                print(sql)
                cur = config.conn.cursor()
                cur.execute(sql)
                goal.reached = True
        return


    def __init__(self, location, game):
        apikey = "860bb330bc46d74511f5ed55ff8b4cf0"

        request = "https://api.openweathermap.org/data/2.5/weather?lat=" + \
                  str(location.latitude) + "&lon=" + str(location.longitude) + "&appid=" + apikey
        answer = requests.get(request).json()
        self.main = answer["weather"][0]["main"]
        self.description = answer["weather"][0]["description"]
        self.icon = "https://openweathermap.org/img/wn/" + answer["weather"][0]["icon"] + ".png"
        self.temp = self.kelvin_to_celsius(answer["main"]["temp"])
        self.humidity = answer["main"]["humidity"]
        self.wind = {
            "speed": answer["wind"]["speed"],
            "deg": answer["wind"]["deg"]
        }

        self.meets_goals = []
        self.check_weather_goals(game)
