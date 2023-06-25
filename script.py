import random

class Player:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        self.name = name
        self.bowling = bowling
        self.batting = batting
        self.fielding = fielding
        self.running = running
        self.experience = experience

class Teams:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = []
        self.current_batsmen = []

    def select_captain(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.captain = player
                break

    def set_batting_order(self, player_names):
        for name in player_names:
            for player in self.players:
                if player.name == name:
                    self.batting_order.append(player)
                    break

    def send_next_batsman(self):
        if self.current_batsmen:
            return self.current_batsmen.pop(0)
        else:
            return self.batting_order[0]

class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage

class Umpire:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.scores = {team1.name: 0, team2.name: 0}
        self.wickets = {team1.name: 0, team2.name: 0}
        self.overs = {team1.name: 0, team2.name: 0}

    def predict_outcome(self, batsman, bowler):
        # Logic to predict the outcome of a ball based on player stats and field conditions
        batting_skill = batsman.batting * random.uniform(0.9, 1.1)
        bowling_skill = bowler.bowling * random.uniform(0.9, 1.1)
        run_chance = batting_skill - bowling_skill
        return run_chance

    def update_score(self, team_name, runs):
        self.scores[team_name] += runs

    def update_wickets(self, team_name):
        self.wickets[team_name] += 1

    def update_overs(self, team_name):
        self.overs[team_name] += 0.1

class Commentator:
    def __init__(self, umpire):
        self.umpire = umpire

    def provide_commentary(self, batsman, bowler, runs_scored):
        # Logic to provide commentary based on the match events
        print(f"{batsman.name} scored {runs_scored} runs against {bowler.name}.")

class Match:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = Umpire(team1, team2, field)
        self.commentator = Commentator(self.umpire)

    def start_match(self):
        self.umpire.scores = {self.team1.name: 0, self.team2.name: 0}
        self.umpire.wickets = {self.team1.name: 0, self.team2.name: 0}
        self.umpire.overs = {self.team1.name: 0, self.team2.name: 0}
        self.play_innings(self.team1, self.team2)
        self.play_innings(self.team2, self.team1)

    def play_innings(self, batting_team, bowling_team):
        self.umpire.update_overs(batting_team.name)
        batsman = batting_team.send_next_batsman()
        self.commentator.provide_commentary(batsman, None, 0)
        while True:
            bowler = random.choice(bowling_team.players)
            run_chance = self.umpire.predict_outcome(batsman, bowler)
            runs_scored = 0
            if run_chance > 0.5:
                runs_scored = random.randint(0, 6)
                self.umpire.update_score(batting_team.name, runs_scored)
            else:
                self.umpire.update_wickets(batting_team.name)
                if self.umpire.wickets[batting_team.name] == len(batting_team.batting_order):
                    break
            self.commentator.provide_commentary(batsman, bowler, runs_scored)
            batsman = batting_team.send_next_batsman()

        print(f"{batting_team.name} innings ended with a score of {self.umpire.scores[batting_team.name]}")

# Example usage
player1 = Player("MS Dhoni", 0.2, 0.8, 0.99, 0.8, 0.9)
player2 = Player("Virat Kohli", 0.1, 0.9, 0.95, 0.7, 0.95)
player3 = Player("Rohit Sharma", 0.05, 0.85, 0.92, 0.75, 0.9)
team1 = Teams("Team 1", [player1, player2, player3])
team1.select_captain("MS Dhoni")
team1.set_batting_order(["MS Dhoni", "Virat Kohli", "Rohit Sharma"])

player4 = Player("Kane Williamson", 0.15, 0.85, 0.96, 0.8, 0.95)
player5 = Player("David Warner", 0.1, 0.88, 0.94, 0.78, 0.9)
player6 = Player("Steve Smith", 0.08, 0.82, 0.91, 0.77, 0.85)
team2 = Teams("Team 2", [player4, player5, player6])
team2.select_captain("Kane Williamson")
team2.set_batting_order(["Kane Williamson", "David Warner", "Steve Smith"])

field = Field("Large", 0.8, "Dry", 0.1)

match = Match(team1, team2, field)
match.start_match()
