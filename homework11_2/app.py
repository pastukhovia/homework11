from flask import Flask, render_template
import utils


app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = utils.load_candidates_from_json()
    return render_template('list.html', items=candidates)


@app.route('/candidate/<x>')
def page_candidate(x):
    candidate = utils.get_candidate(x)
    return render_template('card.html', item=candidate)


@app.route('/search/<candidate_name>')
def page_search(candidate_name):
    candidate = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', items=candidate, name=candidate_name)


@app.route('/skill/<skill_name>')
def page_skill(skill_name):
    candidate = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', items=candidate, skill=skill_name)


if __name__ == '__main__':
    app.run()
