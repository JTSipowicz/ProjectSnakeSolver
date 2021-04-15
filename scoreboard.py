import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.isPlayer = True
        self.isAI = False
        self.high_scores = []
    
    def increase_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    def update(self):
        if self.isPlayer:
            score_type = 'Player'
        elif self.isAI:
            score_type = 'AI'
        assert score_type == 'Player' or score_type == 'AI'
        assert self.score >= 0
        temp_score = {
                "Place": 0,
                "Type": score_type,
                "Score": self.score
            }
        # Add current score to the high scores
        self.high_scores.append(temp_score)
        # Sort high scores with the new added score
        self.high_scores = sorted(self.high_scores, key= lambda i: i['Score'], reverse=True)
        # Pop the smallest score
        self.high_scores.pop()
        # Move all places by one since score was given place 0
        temp_var = 0
        for element in self.high_scores:
            element['Place'] = 0 + temp_var
            temp_var += 1

    def load_scores(self):
        # Reset high scores
        self.high_scores = []
        temp = []
        with open(os.path.join(__location__,"scores.txt"), mode="r") as file:
            for lines in file:
                temp.append(lines.rstrip('\n'))
        # Scores are in format "Place|Type|Score"
        for element in temp:
            separate = element.split('|')
            temp_score = {
                "Place": int(separate[0]),
                "Type": separate[1],
                "Score": int(separate[2])
            }
            self.high_scores.append(temp_score)

    def save_scores(self):
        text = ''
        for element in self.high_scores:
            text += str(element["Place"]) + '|' + element["Type"] + '|' + str(element["Score"]) + '\n'
        #Remove last \n
        text = text[:-1]
        
        with open(os.path.join(__location__,"scores.txt"), mode="w") as file:
            file.truncate()
            file.write(text)

    def get_score(self):
        return self.score

    def get_high_scores(self, index):
        return self.high_scores[index]
        
    def set_type_AI(self):
        self.isAI = True
        self.isPlayer = False
    
    def set_type_Player(self):
        self.isPlayer = True
        self.isAI = False
