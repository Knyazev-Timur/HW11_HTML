from flask import Flask, request, render_template
import utils

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/all/')
def all_candidates():
    items = utils.load_candidates()
    return render_template('list.html', items=items)


@app.route('/candidate/<int:pk>')
def profile(pk):
    candidate_id = utils.get_candidate(pk)
    return render_template('card.html', item=candidate_id)


@app.route('/search/<candidate_name>')
def search_candidates(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', items=candidates, len_items=f'Найдено кандидатов: {len(candidates)}')


@app.route('/search/', methods=['GET'])
def search():
    error = None
    candidate_name = request.args.get('candidate_name')
    # проверяем, передается ли параметр в URL-адресе
    if candidate_name and candidate_name != '':
        candidates = utils.get_candidates_by_name(candidate_name)
        return render_template('search.html', items=candidates, message=f'Найдено кандидатов: {len(candidates)}')
    else:
        error = 'Не введен запрос!'
        return render_template('search.html', error=error)


@app.route('/skill/<skill_name>')
def search_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', items=candidates,
                           message=f'Найдено кандидатов со скиллом "{skill_name}": {len(candidates)}')


@app.route("/skill/", methods=['GET'])
def get_search_skill():
    error = None
    skill_name = request.args.get('skill_name')
    # проверяем, передается ли параметр в URL-адресе
    if skill_name and skill_name != '':
        candidates = utils.get_candidates_by_skill(skill_name)
        return render_template('skill.html', items=candidates,
                               message=f'Найдено кандидатов со скиллом "{skill_name}": {len(candidates)}')
    else:
        error = 'Не введен запрос!'
        return render_template('skill.html', error=error)


app.run()
