from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import random

education_blueprint = Blueprint('education', __name__)

page_config = {"colour": "#339966", "icon": "educate.png", "title": "Falzon Folio: Education", "links": {
    "cards": "./pick_a_card", "highest": "#"}}

dataToRender={}
SUITS={"H": "Hearts", "D": "Diamonds", "C": "Clubs", "S": "Spades"}
CARDS={"A": "Ace", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight",
       "9": "Nine", "10": "Ten", "J": "Jack", "Q": "Queen", "K": "King"}


class frmPickaCard(FlaskForm):
    submit = SubmitField("Click for Card")

# App to display a random playing card


def change_card():
    """
    Function to pick a random card from a deck
    :return:
    """
    card_suit = random.choice(list(SUITS.keys()))
    card_number = random.choice(list(CARDS.keys()))
    img_text = CARDS[card_number]+" of "+SUITS[card_suit]
    img_card = card_number+card_suit+".jpg"
    return {"image": img_text, "card": img_card}


@education_blueprint.route('/')
def index():
    return render_template('education/index.html', page_config=page_config)


@education_blueprint.route('/pick_a_card', methods=['GET','POST'])
def education():
    form=frmPickaCard()
    if request.method == 'POST':
        card_value=change_card()
        return render_template('education/card_show.html', form=form, page_config=page_config, cardValue=card_value)
    if request.method == 'GET':
        return render_template('education/pick_a_card.html', form=form, page_config=page_config)