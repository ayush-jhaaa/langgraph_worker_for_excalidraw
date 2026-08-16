from langchain.output_parsers import PydanticOutputParser




test_cases = [
    {"type": "rectangle", "label": {"text": "Rectangle Label"}},
    {"type": "arrow", "label": {"text": "Arrow Label"}},
    {"type": "ellipse", "label": {"text": "Ellipse Label"}},
    {"type": "diamond", "label": {"text": "Diamond Label"}},
    {"type": "rectangle"},
    {"type": "arrow"},
    {"type": "ellipse"},
    {"type": "diamond"},
    {"type": "line"},
    {"type": "text"},
]

def sentinel(state):
    generated_json = state["generated_json"]






    # for idx,json in enumerate(json_array):
    #     try:
    #         model_class = validator_selector(json)
    #         validated_obj = model_class.model_validate(json)
    #         validated_json.append(json)

    #     except ValidationError as e:
    #         validation_errors[idx] = e.errors()


    #     if validation_errors:
    #         state["is_valid"] = False
    #     else:
    #         state["is_valid"] = True
    #         state["validated_json"] = json_array
            
    #     state["validation_errors"] = []


    print('node 2 running')
    return state


init_state = {
    "generated_json" : test_cases
}
if __name__ == "__main__":
    sentinel(init_state)
