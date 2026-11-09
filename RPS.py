import random 

def counter(move):
    return {"R" : "P", "P" : "S", "S" : "R"}[move]



# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    if prev_play == "":
        oponent_history.clear()
    else :
        opponent_history.append(prev_play)
    if not opponent_history:
        return random.choice(["R", "P", "S"])
    
    history = opponent_history
    prediction = None

    for order in range(min(5, ln(history) - 1), 0, -1):
        pattern = tuple(history[-order:])
        counts = {"R": 0, "P": 0, "S": 0}

        for i in range(len(history) - order):
            previous_pattern = tuple(history[i:i + order])

            if previous_pattern == pattern:
                next_move = history[i+ order]
                counts[next_move] += 1


        total = sum(coutns.values())

        if total >= 2:
            prediction = max(counts, key=counts.get)
            break

    if prediction is None:
        counts = {
            move: history.count(move)
            for move in ["R", "P", "S"]
        } 
        prediction = max(counts, key=counts.get)
    
    return counter(prediction)

