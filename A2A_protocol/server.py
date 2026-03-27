from google.adk.agents import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a

#-----------------------------------------------------
# 1. Simple Price Agent
#-----------------------------------------------------

class PriceAgent(Agent):
    async def handle_message(self, message, context):  # ✅ FIXED
        user_text = message.content.lower()

        if "salmon" in user_text:
            price = "1200/kg"
        elif "chicken" in user_text:
            price = "220/kg"
        else:
            price = "100/kg"

        return {
            "type": "message",
            "content": f"Today wholesale price is {price}"
        }

pricing_agent = PriceAgent(
    name="pricing_agent",
    description="Check today market wholesale market prices for foods."
)

# convert to A2A service
app = to_a2a(pricing_agent, port=8001)

# run server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)