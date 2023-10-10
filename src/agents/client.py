from uagents import Agent,Context, Model, Bureau
import Scripts.APICall as ac
import time
from uagents.setup import fund_agent_if_low
import sys
from termcolor import colored
#Below we are defining a client agent, with an endpoint http://127.0.0.1:8000/submit. We are using this agent to send the Value of current temperature to the agent in src/agents/Alert.py
client_agent = Agent(name = "Bob",port = 8000,seed = "Bob secret phase",endpoint=["http://127.0.0.1:8000/submit"])
RECIPIENT_ADDRESS = "agent1q2kxet3vh0scsf0sm7y2erzz33cve6tv5uk63x64upw5g68kr0chkv7hw50"
class Message(Model):
    message: str
fund_agent_if_low(client_agent.wallet.address())
@client_agent.on_message(model = Message)
async def send_details(ctx:Context, sender:str, msg = Message):
    ctx.logger.info("Recieved message "+msg.message)
    City,Tmax,Tmin = msg.message.split(",")
    Val=ac.getTemp(City)
    log_msg = colored("Gathering temperature data for, "+City+"\n","yellow")
    for i in log_msg:
        sys.stdout.write(i)
        time.sleep(0.02)
        sys.stdout.flush()
    await ctx.send(RECIPIENT_ADDRESS, Message(message = Tmax+","+Tmin+","+Val))
if __name__ == "__main__":
    client_agent.run()
