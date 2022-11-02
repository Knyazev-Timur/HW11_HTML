from flask import Flask, request, render_template
import utils
import logging


logging.basicConfig(level=logging.INFO)
#new_logger = logging.getLogger()

#logging.basicConfig(level=logging.INFO)

logger_file = logging.getLogger('one')
# logging.basicConfig()Config(filename="log.ini", level=logging.ERROR, encoding='UTF-8')
file_handler = logging.FileHandler("log.ini", encoding='UTF-8')
formatter_one = logging.Formatter("%(asctime)s : %(levelname)s : %(funcName)s : %(message)s")
# asctime - время записи, pathname - путь, funcName - название функции,levelname -уровень записи, message Текст записи
file_handler.setFormatter(formatter_one)
logger_file.addHandler(file_handler)

consol_loger = logging.getLogger('two')
# logging.basicConfig(level=logging.INFO)
console_handler = logging.StreamHandler()
formatter_one = logging.Formatter("%(asctime)s : %(levelname)s : %(funcName)s : %(message)s")
# # asctime - время записи, pathname - путь, funcName - название функции,levelname -уровень записи, message Текст записи
console_handler.setFormatter(formatter_one)
consol_loger.addHandler(console_handler)

app = Flask(__name__)


@app.route('/')
def home():
    logging.info("запрошен INDEX")
    return render_template('index.html')


@app.route('/all/')
def all_candidates():
    logging.info("запрошен LIST")
    #logging.ERROR("ERROR!!!")

    logger_file.warning("Запись для логгера один")
    consol_loger.warning("Запись для логгера два")

    items = utils.load_candidates()
    return render_template('list.html', items=items)


@app.route('/candidate/<int:pk>')
def profile(pk):
    logging.info(f"PK :  {pk}")
    candidate_id = utils.get_candidate(pk)
    return render_template('card.html', item=candidate_id)


@app.route('/search/<candidate_name>')
def search_candidates(candidate_name):
    logging.info("запрошен SERCH из адресной строки")
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', items=candidates, len_items=f'Найдено кандидатов: {len(candidates)}')


@app.route('/search/', methods=['GET'])
def search():
    error = None
    candidate_name = request.args.get('candidate_name')
    # проверяем, передается ли параметр в URL-адресе
    logging.info(f"search : {candidate_name}")
    if candidate_name and candidate_name != '':
        candidates = utils.get_candidates_by_name(candidate_name)
        return render_template('search.html', items=candidates, message=f'Найдено кандидатов: {len(candidates)}')
    else:
        error = 'Не введен запрос!'
        return render_template('search.html', error=error)


@app.route('/skill/<skill_name>')
def search_skill(skill_name):
    logging.info("запрошен SKILL из адресной строки")
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', items=candidates,
                           message=f'Найдено кандидатов со скиллом "{skill_name}": {len(candidates)}')


@app.route("/skill/", methods=['GET'])
def get_search_skill():
    error = None
    skill_name = request.args.get('skill_name')
    # проверяем, передается ли параметр в URL-адресе
    logging.info(f"SKILL : {skill_name}")
    if skill_name and skill_name != '':
        candidates = utils.get_candidates_by_skill(skill_name)
        return render_template('skill.html', items=candidates,
                               message=f'Найдено кандидатов со скиллом "{skill_name}": {len(candidates)}')
    else:
        error = 'Не введен запрос!'
        return render_template('skill.html', error=error)


app.run(host="127.0.0.1", port=8080)
