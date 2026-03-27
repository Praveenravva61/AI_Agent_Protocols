# Expose: Turn A2A agent in an A2A service.
from google.adk.a2a.utils.agent_to_a2a import to_a2a
app= to_a2a(pricing_agent, port= 8001)



# Discover: Resolve a Agent card and create client - just url
from a2a.client.client_factory import ClientFactory
client= await ClientFactory.connect("https://pricing_agent:8001")
card = await client.get_card()

print(f" {card.name} - {card.description}")

# Pricing_Agent ->check's today wholesale market prices


# call: send a message via the A2A Protocol
from a2a.client.helpers import create_text_message_object
msg= create_text_message_object(content= "what is chicken price in hyderabad.")

async for response in client.send_message(msg)