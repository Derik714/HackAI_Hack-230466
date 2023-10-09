from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
from termcolor import colored
import sys,time
import Scripts.Temp_alert as TA
class Message(Model):
    message: str
 
bob = Agent(
    name="bob",
    port=8001,
    seed="bob secret phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)
 
fund_agent_if_low(bob.wallet.address())
start_address = "agent1qtegd7lf58rpldn3qe4x8lrk6swlj0ypd53zgy4rf4xcrzewx72xzm8lj9u"
@bob.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
        ctx.logger.info("Recieved message "+msg.message)
        Tmax,Tmin,Val = msg.message.split(',')
        coloured_message = colored(TA.verify_temp(float(Tmax), float(Tmin), float(Val))+"\n", "green")
        await ctx.send(start_address, Message(message=coloured_message))
if __name__ == "__main__":
    bob.run()