from pyrogram import Client, Filters
from pyrogram.errors import FloodWait
import time
app = Client("mnnn",bot_token="958014530:AAHC4DFWQBoe_VwnoPrsgrFy2zFed-DI4jE",api_id=768402,api_hash="f6420bf67303614279049d48d3e670f6")
bullet = -1001378725482
ferrari = -1001274887387
@app.on_message(Filters.chat(bullet) & ~ Filters.edited)
def main(client, message):
 file = open("bullet.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  p = line.split()
  for s in p:
   try:
    mes = client.send_message( int(s), "**" + message.text + "**" )
    fie = open(str(s)+".txt","a")
    fie.write(" " + str(message.message_id) + " " + str(mes.message_id))
    fie.close()
   except:
    continue
@app.on_message(Filters.chat(ferrari) & ~ Filters.edited)
def main(client, message):
 file = open("ferrari.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  p = line.split()
  for r in p: 
   try:
    mes = client.send_message( int(r), "**" + message.text + "**" )
    fie = open(str(r)+".txt","a")
    fie.write(" " + str(message.message_id) + " " + str(mes.message_id))
    fie.close()
   except:
    continue
@app.on_message(Filters.chat(ferrari) & Filters.edited)
def main(client, message):
 file = open("ferrari.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  t = line.split()
  for m in t:
   files = open(str(m)+".txt" , "r")
   d = files.readlines()
   files.close()
   for c in d:
    x = c.split()
    id = str(message.message_id)
    if id in x:
     try:
      if message.text == ".":
       client.delete_messages(int(m),int(x[x.index(id)+1]))
      else:
       client.edit_message_text(int(m),int(x[x.index(id)+1]), "**" + message.text + "**" )
     except FloodWait as e:
       time.sleep(e.x)
@app.on_message(Filters.chat(bullet) & Filters.edited)
def main(client, message):
 file = open("bullet.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  b = line.split()
  for a in b:
   files = open(str(a)+".txt" , "r")
   d = files.readlines()
   files.close()
   for c in d:
    x = c.split()
    id = str(message.message_id)
    if id in x:
     try:
      if message.text == ".":
       client.delete_messages(int(a),int(x[x.index(id)+1]))
      else:
       client.edit_message_text(int(a),int(x[x.index(id)+1]), "**" + message.text + "**" )
     except FloodWait as e:
      time.sleep(e.x)

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
@app.on_message(Filters.command('clear') & Filters.user(491634139))
def forward(client, message):
    file = open(message.text.split(" ")[1] + ".txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
     p = line.split()
     for x in p:
        fie = open(str(x)+".txt","w")
        fie.write("001 002")
        fie.close()
        message.reply("☢️ Done, Editing data cleared ✅✅")
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


@app.on_message(Filters.command("start"))
def forward(client, message):
 if message.from_user.id == 491634139:
   message.reply("♻️ Welcome to your LineBot . ✅✅")
 else:
   message.reply("♻️ You need admins permission to use my functions. ✅✅")
@app.on_message(Filters.private)
def forward(client, message):
 if not message.from_user.id == 491634139:
   message.reply("♻️ You need admins permission to use my functions. ✅✅")
app.run()
