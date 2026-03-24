from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.adk.tools.toolbox_toolset import ToolboxToolset
from mcp import StdioServerParameters

# 1. Inventory Databases for mcp Toolbox for Database (PostgreSql, SQLite, etc..)
Inventory_data= ToolboxToolset(server_url= TOOLBOX_URL)

# 2. KITCHEN SOPS AND RECIPES - NATION_MCP((read menus, ingredient lists, supplier contacts)
notion_tool= McpToolset(
    connection_params= StdioConnectionParams(
        server_params= StdioServerParameters(
            command= "npx",
            args= ['y', '@notionhq/notion-mcp-server'],
            env= {"NOTION_TOKEN": NOTION_TOKEN}
        ), timeout= 30
    )
)

mailgun= McpToolset(
    connection_params=StdioConnectionParams(
        server_params= StdioServerParameters(
            command= "npx",
            args= ['y', '@mailgun/mcp-server'],\
            env= {'MAILGUN_API_KEY': MAILGUN_API_KEY}
            
        ), timeout= 30
    )
)


kitchen_agent= Agent(
    name= "kitchen_manager",
    model= 'gemini-3-flash-preview',
    instructions= """ 
    You manage a restraurant kitchen. Check inventory, lookup recipes, and email suppliers
    """,
    tools= [Inventory_data, notion_tool, mailgun],
)