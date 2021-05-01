import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.balls_dict = dict()
        self.contents = list()
        self.balls_dict.update(kwargs)
        if self.balls_dict == {} or sum(self.balls_dict.values() ) < 1:
            print('Must enter at least one ball.')
        else:
            for k,v in self.balls_dict.items():
                while v > 0:
                    self.contents.append(k)
                    v -= 1

    def draw(self, x):
        random.shuffle(self.contents)
        self.draw_contents = self.contents[:x]
        self.contents = self.contents[x:]
        return self.draw_contents

hat0=Hat(red=3, blue=5)

# print(hat0.draw(3))

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_list0 = list()
    for k, v in expected_balls.items():
        while v > 0:
            expected_list0.append(k)
            v -= 1
    count = 0
    while num_experiments > 0:
        expected_list1 = copy.deepcopy(expected_list0)
        expected_list2 = copy.deepcopy(expected_list1)
        drawn_list0 = hat.draw(num_balls_drawn)
        for x in expected_list1:
            for y in drawn_list0:
                if x == y:
                    expected_list2.remove(x)
                    drawn_list0.remove(y)
                    if len(expected_list2) < 1:
                        count += 1
        num_experiments -= 1
    return count

print(experiment(hat0, {'red': 1}, 1, 20))

#maybe try converting to dictionaries and comparing