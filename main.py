import warnings
from langchain_core._api.deprecation import LangChainPendingDeprecationWarning
warnings.filterwarnings("ignore", category=LangChainPendingDeprecationWarning)
    
import asyncio

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()


llm = ChatOpenAI()

stdio_server_params = StdioServerParameters(
    command="python",
    args=[r"C:\Users\Bruna\Desktop\Estudos\Udemy\LangChain and LangGraph\mcp-crash-course\servers\math_server.py"]
)

async def main():
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":    
    asyncio.run(main())
