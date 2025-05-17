from smolagents import CodeAgent, LiteLLMModel, Tool, FinalAnswerTool
from search import shortest_path, format_route

class FindRouteTool(Tool):
    name = "find_route"
    description = "This tool must be used when you want to find the route or path between two places, locations or points."

    inputs = {
        "source": {
            "type": "string",
            "description": "The source location. It can be an address, a place, a street name, etc."
        },
        "target": {
            "type": "string",
            "description": "The target location. It can be an address, a place, a street name, etc."
        }
    }
    output_type = "string"

    def forward(self, source, target):
        route = shortest_path(source, target)
        return format_route(route)


model = LiteLLMModel(
    model_id="ollama/qwen3:4b",
    api_base="http://localhost:11434",
    max_ctx=8192,
)

agent = CodeAgent(tools=[FindRouteTool()], model=model, add_base_tools=False)
agent.run("How can I go from Praça Sete to Praça da Liberdade")
