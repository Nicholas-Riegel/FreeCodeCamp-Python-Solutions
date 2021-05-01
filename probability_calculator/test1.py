import random


class Hat:
    def __init__(self, **kwargs):
        self.balls_dict = dict()
        self.contents = list()
        self.balls_dict.update(kwargs)
        if self.balls_dict == {} or sum(self.balls_dict.values()) < 1:
            print('Must enter at least one ball.')
        else:
            for k, v in self.balls_dict.items():
                while v > 0:
                    self.contents.append(k)
                    v -= 1

    def draw(self, x):
        random.shuffle(self.contents)
        self.draw_contents = self.contents[:x]
        # self.contents = self.contents[x:]
        return self.draw_contents


hat0 = Hat(red=3, blue=5)

# print(hat0.draw(3))


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    # seems num_balls_drawn has to be >= expected_balls, no?

    num_experiments0 = num_experiments
    match = 0
    while num_experiments0 > 0:
        
        drawn_balls_dict = dict()
        drawn_balls_list = hat.draw(num_balls_drawn)
        for x in drawn_balls_list:
            if x in drawn_balls_dict.keys():
                drawn_balls_dict[x] += 1
            else:
                drawn_balls_dict[x] = 1
        
        count = 0
        for k, v in expected_balls.items():
            if k in drawn_balls_dict.keys() and drawn_balls_dict[k] >= v:
                count += 1
            if count == len(expected_balls.items()):
                match += 1
        num_experiments0 -= 1
    
    return 'Expected balls: ' + str(expected_balls) + '\nDrawn balls: ' + str(drawn_balls_dict) + '\nMatch: ' + str(match) + '\nProbability: ' + str(match/num_experiments)


print(experiment(hat0, {'red': 3}, 3, 2000))
