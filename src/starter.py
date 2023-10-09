from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low
from termcolor import colored
import sys,time

client_path = "C:/Users/HRITHIMAN GUHA/Desktop/IITB_Final/src/agents/client.py"
CLIENT_RECIPIENT_ADDRESS = "agent1qw39gza344t8zdegf6ws0qpj5u5pvmgny2xsy8htmndhukhm5634swj6am7"
start_agent = Agent(name="John",port=7999,seed="John secret phrase",endpoint=["http://127.0.0.1:7999/submit"])
fund_agent_if_low(start_agent.wallet.address())

class Message(Model):
    message:str
@start_agent.on_interval(period = 8)
async def starter(ctx:Context):
    log_message = colored("Enter your location details and temperature details below\n","blue")
    for i in log_message:
        sys.stdout.write(i)
        time.sleep(0.02)
        sys.stdout.flush()
    City = input("Enter the name of the city")
    Tmax = input("Enter the maximum temperature")
    Tmin = input("Enter the minimum temperature")
    msg= City + ","+str(Tmax)+","+str(Tmin)
    await ctx.send(CLIENT_RECIPIENT_ADDRESS,Message(message=msg))
@start_agent.on_message(model=Message)
async def output(ctx:Context, sender:str, msg:Message): 
    if "lesser" in msg.message or "greater" in msg.message:
        ctx.logger.warning(msg.message)
    else:
        ctx.logger.info(msg.message)
if __name__ == "__main__":
    start_agent.run()
    