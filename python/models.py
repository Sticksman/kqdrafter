import math

DEFAULT_ROLE = 'berry'


class Player(object):
    '''
        Role_scores is a dictionary of the following
        key: role (queen, speed, warrior, berry, snail)
        value:
          score: numeric 1-5
          main: boolean true false
    '''
    def __init__(self, name, role_scores):
        self.name = name
        self.role_scores = role_scores

    def derive_score_by_name(self, score):
        main_role = self.get_main_role()
        cls_by_names = cls_by_name_dict()
        klass = cls_by_names[main_role]
        derivation_table = klass.derivation_table()
        return derivation_table[main_role](score)

    def get_main_role(self):
        for role, scores in self.role_scores.iteritems():
            if scores['main']:
                return role, scores['score']

        return DEFAULT_ROLE, 1

    def _get_score(self, name):
        score = self.role_scores.get(name)
        if score:
            return score
        return self.derive_score_by_name(name)

    def get_queen_score(self):
        return self._get_score('queen')

    def get_speed_score(self):
        return self._get_score('speed')

    def get_warrior_score(self):
        return self._get_score('warrior')

    def get_berry_score(self):
        return self._get_score('berry')

    def get_snail_score(self):
        return self._get_score('snail')


def cls_by_name_dict():
    roles = Role.__subclasses__()
    return dict([(cls.name(), cls) for cls in roles])


class Role(object):
    @classmethod
    def derivation_table(cls):
        raise NotImplementedError("Please implement the role's derivation table")

    @classmethod
    def name(cls):
        raise NotImplementedError("Please implement the role's name")

    def __init__(self, score):
        self.score = score

    def team_modifier(self):
        return 1

    def self_modifier(self):
        return 1


class Queen(Role):
    @classmethod
    def derivation_table(cls):
        return {
            'speed': lambda score: score * 0.9,
            'warrior': lambda score: score * 0.85,
            'berry': lambda score: max(score - 2, 0),
            'snail': lambda score: max(score - 3, 0),
        }

    @classmethod
    def name(cls):
        return 'queen'

    def team_modifier(self):
        score = math.floor(self.score)
        if score == 5:
            return 1.75
        elif score == 4:
            return 1.25
        elif score == 3:
            return 1
        elif score == 2:
            return 0.75
        elif score == 1:
            return 0.5
        return 0.1


class Speed(Role):
    @classmethod
    def derivation_table(cls):
        return {
            'queen': lambda score: score * 0.9,
            'warrior': lambda score: score * 0.8,
            'berry': lambda score: max(score - 2, 0),
            'snail': lambda score: max(score - 3, 0),
        }

    @classmethod
    def name(cls):
        return 'speed'


class Warrior(Role):
    @classmethod
    def derivation_table(cls):
        return {
            'speed': lambda score: score * 1.2,
            'queen': lambda score: score * 1.1,
            'berry': lambda score: max(score - 1, 0),
            'snail': lambda score: max(score - 2, 0),
        }

    @classmethod
    def name(cls):
        return 'warrior'


class Berry(Role):
    @classmethod
    def derivation_table(cls):
        return {
            'queen': lambda score: min(score + 2, 5),
            'speed': lambda score: min(score + 2, 5),
            'warrior': lambda score: min(score + 2, 5),
            'snail': lambda score: score * 0.9
        }

    @classmethod
    def name(cls):
        return 'berry'

    def self_modifier(self):
        score = math.floor(score)
        if score == 5:
            return 0.8
        elif score == 4:
            return 0.64
        elif score == 3:
            return 0.48
        elif score == 2:
            return 0.32
        return 0.16


class Snail(Role):
    @classmethod
    def derivation_table(cls):
        return {
            'queen': lambda score: min(score + 3, 5),
            'speed': lambda score: min(score + 3, 5),
            'warrior': lambda score: min(score + 3, 5),
            'berry': lambda score: score * 1.1
        }

    @classmethod
    def name(cls):
        return 'snail'

    def self_modifier(self):
        score = math.floor(score)
        if score == 5:
            return 0.75
        elif score == 4:
            return 0.60
        elif score == 3:
            return 0.45
        elif score == 2:
            return 0.3
        return 0.15

