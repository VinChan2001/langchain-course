# langchain-agents-lab

Experiments with LLM agents in Python: tool calling, agent loops, structured output, and tracing. I build each idea twice when I can. First with LangChain, then without it, so I can see what the framework does for me.

## Branches

| Branch | What it covers |
|--------|----------------|
| `my/hello-world` | Environment setup and a first LangChain chain |
| `my/search-agent` | A web search agent with `create_agent`, a Tavily search tool, and Pydantic structured output (answer + source URLs) |
| `my/under_the_hood` | Tool-calling agent loops written by hand, with LangSmith tracing |

### `my/under_the_hood`

| File | What it shows |
|------|---------------|
| `1_agent_loop_tc.py` | Agent loop with LangChain `@tool` and `init_chat_model`. The loop sends messages, runs the tool the model asks for, and adds the result to the history until the model gives a final answer. |
| `2_agent_loop_raw_tc.py` | The same loop with no LangChain. It calls `ollama.chat` directly, defines the JSON tool schemas by hand, and adds LangSmith tracing with `@traceable`. |

Both loops have a maximum number of iterations, and both fail loudly if the model asks for a tool that does not exist.

## Run it

You need Python 3.10+, [uv](https://docs.astral.sh/uv/), and [Ollama](https://ollama.com) with the model pulled:

```bash
ollama pull qwen3:1.7b
git checkout my/under_the_hood
uv sync
uv run python 2_agent_loop_raw_tc.py
```

For LangSmith tracing, put `LANGSMITH_API_KEY` and `LANGSMITH_TRACING=true` in a `.env` file. The search agent also needs `OPENAI_API_KEY` and `TAVILY_API_KEY`.

## Checks

GitHub Actions imports every script on each push and pull request. Run the same check locally:

```bash
uv run --locked python -m unittest discover -s tests
```

## Credits

The project structure follows Eden Marco's [LangChain course](https://github.com/emarco177/langchain-course) (Apache-2.0, see `LICENSE`).
