from pyrogram import Client, Filters
from pyrogram.errors import FloodWait
import time
app = Client(session_name="4send",api_id=728044,api_hash="a41ddadc9696482aff94a4b37221574a")
bullet = -1001360119073
ferrari = -1001396702215
@app.on_message(Filters.chat(bullet) & ~ Filters.edited)
def main(client, message):
 f = False
 words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','line','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
 for word in words:
  if word.casefold() in message.text.casefold():
   f = True
 if not f:
  file = open("bullet.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   p = line.split()
   for s in p:
    try:
     client.send_message( int(s), "**" + message.text + "**" )
    except:
     continue
@app.on_message(Filters.chat(ferrari) & ~ Filters.edited)
def main(client, message):
 f = False
 words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','line','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
 for word in words:
  if word.casefold() in message.text.casefold():
   f = True
 if not f:
  file = open("ferrari.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   p = line.split()
   for r in p: 
    try:
     client.send_message( int(r), "**" + message.text + "**" )
    except:
     continue
@app.on_message(Filters.command('add') & Filters.user(491634139) )
def forward(client, message):
 if len(message.text.split(' ')) > 2:
  if len(message.text.split(' ')[1]) == 14:
   with open(message.text.split(" ")[2] + ".txt" , "r") as file:
    lines = file.readlines()
    file.close()
    for line in lines:
     files = open(message.text.split(" ")[2] + ".txt" , "w") 
     files.write(line + " " + message.text.split(' ')[1])
     files.close()
     with open(message.text.split(' ')[1]+".txt" , "w") as g:
       g.write("001 002")
       g.close()
     message.reply("💾 Done, The chat_id  ```" + message.text.split(' ')[1] +"```🌐 has been added to my database. ✅✅")
  else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")
 else:
   message.reply("💼 Please write a valid chat id. ✅✅ ")
@app.on_message(Filters.command('remove') & Filters.user(491634139))
def forward(client, message):
 if len(message.text.split(' ')) > 2:
  if len(message.text.split(' ')[1]) == 14:
   file = open(message.text.split(" ")[2] + ".txt" , "r")
   u = file.readlines()
   file.close()
   for v in u:
     lines = v.split() 
     del lines[lines.index(message.text.split(' ')[1])]
     y = " ".join(str(x) for x in lines)
     files = open(message.text.split(" ")[2] + ".txt" , "w") 
     files.write(y)
     files.close()
     message.reply("💾 Done, The chat_id  ```" + message.text.split(' ')[1] +"```🌐 has been removed to my database. ✅✅")
  else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")
 else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")
@app.on_message(Filters.command('list') & Filters.user(491634139))
def forward(client, message):
  file = open(message.text.split(" ")[1] + ".txt" , "r")
  u = file.readlines()
  file.close()
  for v in u :
   message.reply("🏘️ List of Chat_ids in my database are ```" + str(v) + "```. Its can be change. ✅✅")
@app.on_message(Filters.command('get') & Filters.user(491634139) )
def forward(client, message):
 if len(message.text.split(' ')) > 1:
  if len(message.text.split(' ')[1]) == 14:
   x = client.get_chat(int(message.text.split(' ')[1])).title
   message.reply("📶 This chat name is - "+str(x)+" ✅")
  else:
   message.reply("💼 Please write a valid chat id. ✅✅ ")
 else:
  message.reply("💼 Please write a valid chat id. ✅✅ ")

@app.on_message(Filters.command('reset') & Filters.user(491634139))
def forward(client, message):
 with open("ferrari.txt" , "w") as g:
  g.write("-1001353340635")
  g.close()
 with open("bullet.txt" , "w") as g:
  g.write("-1001353340635")
  g.close()
 with open("ids.txt" , "w") as g:
  g.write("-1001353340635")
  g.close()
 message.reply("done")
app.run()
