import json


def load_candidates():
    with open('candidates.json', 'r', encoding='UTF-8') as load_files:
        return json.load(load_files)


def get_candidate(candidate_id):
    """
    :param candidate_id:
    :return:dict
    Находит нужного кандидата по запрошенному ID, возвращает словарь с данными по кандидату
    """
    candidates = load_candidates()
    for candidate in candidates:
        if candidate_id == candidate.get('id'):
            return candidate


def get_candidates_by_name(candidate_name):
    """
    :param candidate_name:
    :return:dict
    Находит кандидатов, содержащих в имени запрошенные данные, возвращает словарь с данными кандидатов
    """
    candidates = load_candidates()
    candidate = [i for i in candidates if candidate_name.lower() in i.get("name").lower()]
    return candidate


def get_candidates_by_skill(skill_name):
    """
    :param skill_name:
    :return:dict
    Находит кандидатов, обладающих запрошенными навыками, возвращает словарь с данными кандидатов
    """
    candidates = load_candidates()
    candidates_skill = [i for i in candidates if skill_name.lower() in i.get("skills").lower().split(', ')]
    return candidates_skill
