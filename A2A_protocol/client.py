import asyncio
from a2a.client.client_factory import ClientFactory
from a2a.client.helpers import create_text_message_object

async def main():
    # conncect to agent
    client = await ClientFactory.connect("http://localhost:8001")
    
    # get agent card
    card= await client.get_card()
    print(f'connected to:{card.name} , \n descreption: {card.description}')
    
    
    # create message
    msg = create_text_message_object(content= "what is chicken price.")
    
    print("sending request..........\n")
    
    #stream response
    async for response in client.send_message(msg):
        print("RAW RESPONSE:", response) 
        if getattr(response, "content", None):
            print("Agent:", response.content)

         # Task-based response
        if getattr(response, "artifacts", None):
            for artifact in response.artifacts:
                if getattr(artifact, "content", None):
                    print("Agent:", artifact.content)
            
            
if __name__ == '__main__':
    asyncio.run(main())
        
        
    
