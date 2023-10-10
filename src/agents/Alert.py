from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
from termcolor import colored
import sys,time
import Scripts.Temp_alert as TA
class Message(Model): # A basic message model which represents that if the agent uses this message model then the messages would be of String format.
    message: str
 #Below, we are defining an Agent called Bob with a defined endpoint of http://127.0.0.1:8001/submit. Endpoint ensures that the agent is able to send and receive messages
bob = Agent( 
    name="bob",
    port=8001,
    seed="bob secret phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)
 
fund_agent_if_low(bob.wallet.address()) #This makes sure the agent registers on the Almanac server. If the agent lacks funds to do so, this function provides the required funds
start_address = "agent1qtegd7lf58rpldn3qe4x8lrk6swlj0ypd53zgy4rf4xcrzewx72xzm8lj9u" #The address of the agent defined in src/starter.py
@bob.on_message(model=Message) #This defines an condition where if bob receives a message on its endpoint, the below asynchronous function "message_handler" would be executed
async def message_handler(ctx: Context, sender: str, msg: Message):
        ctx.logger.info("Recieved message "+msg.message)
        Tmax,Tmin,Val = msg.message.split(',')
        coloured_message = colored(TA.verify_temp(float(Tmax), float(Tmin), float(Val))+"\n", "green")#Adding a color to the messsage for clarity
        await ctx.send(start_address, Message(message=coloured_message))#sending the message to the starter agent
if __name__ == "__main__":
    bob.run()
