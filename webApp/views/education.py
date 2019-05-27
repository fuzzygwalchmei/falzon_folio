from flask import Blueprint, render_template, request

education_blueprint = Blueprint('education', __name__)

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import random

dataToRender={}
SUITS={"H":"Hearts","D":"Diamonds","C":"Clubs","S":"Spades"}
CARDS={"A":"Ace","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine","10":"Ten","J":"Jack","Q":"Queen","K":"King"}


class frmPickaCard(FlaskForm):
    submit = SubmitField("Click for Card")

# App to display a random playing card


def change_card():
    card_suit = random.choice(list(SUITS.keys()))
    card_number = random.choice(list(CARDS.keys()))
    imgText=CARDS[card_number]+" of "+SUITS[card_suit]
    imgCard = card_number+card_suit+".jpg"
    return {"image": imgText, "card": imgCard}

page_config = {"colour": "green", "icon": "educate.png", "title": "Falzon Folio: Education", "links": {
    "cards": "./pick_a_card", "highest": "https://google.com"}}

@education_blueprint.route('/')
def index():
    return render_template('education/index.html', page_config=page_config)

@education_blueprint.route('/pick_a_card', methods=['GET','POST'])
def education():
    form=frmPickaCard()
    if request.method=='POST':
        cardValue=change_card()
        return render_template('education/card_show.html', form=form, page_config=page_config, cardValue=cardValue)
    if request.method=='GET':
        return render_template('education/pick_a_card.html', form=form, page_config=page_config)