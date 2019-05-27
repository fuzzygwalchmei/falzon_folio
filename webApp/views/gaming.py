import random
import re

from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

gaming_blueprint = Blueprint('gaming', __name__)

page_config = {"colour": "#6699FF", "icon":"gaming.png", "title": "Falzon Folio: Gaming",
               "links": {"diceroller": "./diceroller", "characters": "#"}}

diceRegex = "[\d?]d[\d]"
modRegex = "[+-]\s?\d\b"
dataToRender = {}
dataDict = {}


class frmDiceRoll(FlaskForm):
    dicefield = StringField("Dice Field")
    submit = SubmitField("Click to Roll")


def getItems(diceInput):
    """
    Function to strip a string down to dice components (number of dice, type of dice and modifiers)
    :param diceInput:
    :return:
    """
    diceInput = diceInput.lower()
    diceInput = diceInput.replace(" ", "")
    myDice = re.findall(diceRegex, diceInput)
    myMods = re.findall(modRegex, diceInput)
    rolls = []
    mods = []

    for each in myDice:
        numDice,typeDice = re.split('d', each)
        rolls.append(diceRoll(int(numDice), int(typeDice)))

    for each in myMods:
        mods.append(int(each))
    print("Rolls: ", rolls) #, sum(rolls)
    print("Mods: ", mods) #, sum(mods)
    sumRolls = sum(list(map(sum, rolls)))
    sumMods = sum(mods)
    dataDict['myString'] = diceInput
    dataDict['myDice'] = myDice
    dataDict['myMods'] = myMods
    dataDict['indRolls'] = rolls
    dataDict['totalRolls'] = sumRolls
    dataDict['totalMods'] = sumMods
    dataDict['total'] = sumRolls+sumMods

    print(sumRolls + sumMods)
    return dataDict


def diceRoll(numDice, typeDice):
    """
    Function to take in the number and type of dice and return the rolls generated
    :param numDice:
    :param typeDice:
    :return:
    """
    rolls = []
    for each in range(numDice):
        rolls.append(random.randint(1, typeDice))
    return rolls


@gaming_blueprint.route('/')
def index():
    return render_template('gaming/index.html', page_config=page_config)

@gaming_blueprint.route('/diceroller', methods=['GET','POST'])
def diceroller():
    form = frmDiceRoll()
    if request.method == 'POST':
        myDice = form.dicefield.data
        dataToRender = getItems(myDice)
        return render_template('gaming/results.html', form=form, page_config=page_config, dataToRender=dataToRender)
    if request.method == "GET":
        return render_template('gaming/diceroller.html', form=form, page_config=page_config)