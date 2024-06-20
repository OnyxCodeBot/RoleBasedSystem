
effects = {
    "effect_rand": {
        "shown_name": "Afterschocks",
        "affected_attribute": "ap",
        "effect": "reduce",
        "value": 5,
        "duration": 3,
        "can_be_cleared": 1,
        "description": "A random effect"
    },
    "effect_2": {
        "shown_name": "Erosion",
        "affected_attribute": "current_hp",
        "effect": "reduce",
        "value": 1,
        "duration": 999,
        "can_be_cleared": 0,
        "description": "Another random effect"
    }

}


skills = {
    "s1": {
        "affectedAttr": ['current_hp', 'ap'],
        "effect": ['add', 'add'],
        "values": [200, 20],
        "duration": [3, 3],
        "cooldown": 6


    }
}