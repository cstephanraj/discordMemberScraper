import discum
import os
from datetime import datetime

def get_input_details():
    global token, guild_id, channel_id
    tokenFile = os.path.join(os.getcwd(), 'input.txt')
    print(tokenFile)
    with open(tokenFile) as f:
        data = f.read()
        token = data.split(',')[0].split('token:')[1].strip()
        guild_id = data.split(',')[1].split('guild_id:')[1].strip()
        channel_id = data.split(',')[2].split('channel_id:')[1].strip()
#here

get_input_details()

bot = discum.Client(token= token, log=True)

bot.gateway.fetchMembers(guild_id, channel_id, keep=['username','discriminator'], method='overlap',wait=1)
@bot.gateway.command
def memberTest(resp):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched)+' members fetched')
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()

bot.gateway.run()

output_file = "userName" + str(guild_id) + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + ".txt"
f = open(output_file, "a", encoding="utf-8")
for memberID in bot.gateway.session.guild(guild_id).members:
    print(bot.gateway.session.guild(guild_id).members[memberID]['username'])
    print(bot.gateway.session.guild(guild_id).members[memberID]['discriminator'])
    f.write(str(bot.gateway.session.guild(guild_id).members[memberID]['username']) + "#" + str(bot.gateway.session.guild(guild_id).members[memberID]['discriminator']) + '\n')
f.close()