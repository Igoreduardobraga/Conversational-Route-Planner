from smolagents import CodeAgent, LiteLLMModel, Tool, FinalAnswerTool
from search import shortest_path, format_route, plot_routes

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
        bfs_route, a_star_route = shortest_path(source, target)
        plot_routes(bfs_route, a_star_route)
        
        bfs_str = format_route(bfs_route)
        a_star_str = format_route(a_star_route)

        return f"BFS Route:\n{bfs_str}\n\nA* Route:\n{a_star_str}"


model = LiteLLMModel(
    model_id="ollama/qwen3:4b",
    api_base="http://localhost:11434",
    max_ctx=8192,
)

agent = CodeAgent(tools=[FindRouteTool()], model=model, add_base_tools=False)
agent.run("How can I go from Xapuri to Maria das Tranças")
