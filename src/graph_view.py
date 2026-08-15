from src.graph_contoller import graph
from src.graph_contoller import plan

app = graph.compile()

initial_state = plan(user_input = "give all possible text types",
                     max_retries = 3)
final_state = app.invoke(initial_state)

print(f"{i}\n" for i in final_state)
