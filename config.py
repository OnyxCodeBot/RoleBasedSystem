
# types: -----
# 0 -> One time effect over multiple turns
# 1 -> effect triggers each turn

effects = {
    "effect_rand": {
        "shown_name": "Afterschocks",
        "affected_attribute": "ap",
        "effect": "reduce",
        "value": 5,
        "duration": 3,
        "type": 0,
        "can_be_cleared": 1,
        "description": "A random effect"
    },
    "effect_2": {
        "shown_name": "Erosion",
        "affected_attribute": "current_hp",
        "effect": "reduce",
        "value": 1,
        "duration": 999,
        "type": 1,
        "can_be_cleared": 0,
        "description": "Another random effect"
    },
    "effect3": {
        "shown_name": "Erosion",
        "affected_attribute": "current_hp",
        "effect": "reduce",
        "value": 0,
        "duration": 9,
        "type": 0,
        "probability": 0.8,
        "can_be_cleared": 0,
        "description": "Trait"
    }

}


skills = {
    "s1": {
        "name": "Flüchten",
        "required_for_activation": [],
        "affectedAttr": ['current_hp', 'ap'],
        "effect": ['add', 'add'],
        "values": [200, 20],
        "duration": [3, 3],
        "cooldown": 6
    }
}



pU = {
    "Unit1": {
        "name": "Lukas",
        "max_hp": 200,
        "current_hp": 200,
        "ap": 5,
        "defense": 2,
        "can_act": 1,
        "skill": ["s1"]
    },
    "Unit2": {
        "name": "Lulu",
        "max_hp": 100,
        "current_hp": 100,
        "ap": 30,
        "defense": 2,
        "can_act": 1,
        "skill": []
    }
}


eEntity = {
    "e001":{
        "name": "Verärgerter Kunde",
        "max_hp": 400,
        "current_hp": 400,
        "ap": 33,
        "defense": 0,
        "resistence": 0.04,
        "can_act": 1,
        "skill": []
}
}