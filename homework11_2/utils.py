import json


def load_candidates_from_json():
    with open('candidates.json', encoding='utf-8') as file:
        file_content = json.loads(file.read())
    return file_content


def get_candidate(candidate_id):
    '''Возвращает кандидата по его номеру в списке'''

    file_content = load_candidates_from_json()

    for item in file_content:
        if int(candidate_id) == item['id']:
            return item

    return False


def get_candidates_by_skill(skill_name):
    '''Возвращает кандидатов по их навыкам'''

    file_content = load_candidates_from_json()
    candidates_list = []

    for item in file_content:
        # нужный навык и навык кандидата переводятся в нижний регистр
        if skill_name.lower() in [x.lower() for x in item['skills'].split(', ')]:
            candidates_list.append(item)

    if candidates_list:
        return candidates_list
    else:
        return False


def get_candidates_by_name(candidate_name):
    '''Возвращает кандидатов по имени'''

    file_content = load_candidates_from_json()
    candidates_list = []

    for item in file_content:
        if candidate_name.lower() in item['name'].lower():
            candidates_list.append(item)

    if candidates_list:
        return candidates_list
    else:
        return False
