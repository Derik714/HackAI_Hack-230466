from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low
from termcolor import colored
import sys,time

CLIENT_RECIPIENT_ADDRESS = "agent1qw39gza344t8zdegf6ws0qpj5u5pvmgny2xsy8htmndhukhm5634swj6am7" #Address of the client_agent
start_agent = Agent(name="John",port=7999,seed="John secret phrase",endpoint=["http://127.0.0.1:7999/submit"])#Similar to client_agent and the alert agent, we are defining another agent here
fund_agent_if_low(start_agent.wallet.address())

class Message(Model):
    message:str
@start_agent.on_interval(period = 8) #This function iterates the below starter function after every 8 seconds
async def starter(ctx:Context):
    #Introducing an attractive log message by displaying it in a typing animation form
    log_message = colored("Enter your location details and temperature details below\n","blue")
    for i in log_message:
        sys.stdout.write(i)
        time.sleep(0.02)
        sys.stdout.flush()
    City = input("Enter the name of the city") #Taking input of City name from the user
    Tmax = input("Enter the maximum temperature") #Taking input of Maximum Temperature from the user
    Tmin = input("Enter the minimum temperature") #Taking input of Minimum Temperature from the user
    msg= City + ","+str(Tmax)+","+str(Tmin) #Structuring the values into a comma-separated message
    await ctx.send(CLIENT_RECIPIENT_ADDRESS,Message(message=msg))#Sending the comma-separated message to the Client address
@start_agent.on_message(model=Message) #Recieving the result message from Alert.py agent
async def output(ctx:Context, sender:str, msg:Message): 
    if "lesser" in msg.message or "greater" in msg.message: #Using a Warning if the result string contains "lesser" or "greater" in it
        ctx.logger.warning(msg.message)
    else:
        ctx.logger.info(msg.message) #Else normally printing the values
if __name__ == "__main__":
    start_agent.run()
    
