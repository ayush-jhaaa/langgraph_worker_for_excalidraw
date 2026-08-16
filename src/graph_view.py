from src.graph_contoller import graph
from src.graph_contoller import plan

app = graph.compile()

initial_state = plan(user_input = "give all possible text types",
                     generated_json = [],
                     validation_errors = {},
                     is_valid = False,
                     valid_json = [],
                     invalid_json = [],
                     retry_count = 0,
                     max_retries = 3,
                     coming_from = "initialization")
final_state = app.invoke(initial_state)

print(f"{i}\n" for i in final_state)
