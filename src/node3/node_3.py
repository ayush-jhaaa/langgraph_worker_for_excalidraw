# This is for geometric correction and all
def node_3_corrector(state):
    state["corrected_json"] = "NODE_3"

    print(state.get("validated_json"))
    return state