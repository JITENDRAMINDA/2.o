from pyrogram import Client, Filters
app = Client("mnnn",bot_token="956760634:AAHv51MMd2qdXbwWJU24QxsI9_It70djzeI",api_id=768402,api_hash="f6420bf67303614279049d48d3e670f6")
bullet = -1001289914295
ferrari = -1001103958201
@app.on_message(Filters.chat(bullet) & ~ Filters.edited)
def main(client, message):
 file = open("bullet.txt" , "r")
 lines = str(file.readlines()).replace("['",'').replace("']",'').replace(' ','',1).split(' ')
 file.close()
 for s in lines:
   try:
    mes = client.send_message(int('-100' + s),message.text.markdown)
   except:
    continue
@app.on_message(Filters.chat(ferrari) & ~ Filters.edited)
def main(client, message):
 file = open("ferrari.txt" , "r")
 lines = str(file.readlines()).replace("['",'').replace("']",'').replace(' ','',1).split(' ')
 file.close()
 for s in lines:
   try:
    mes = client.send_message(int('-100' + s),message.text.markdown)
   except:
    continue
@app.on_message(Filters.command('add') & Filters.user(491634139) )
def forward(client, message):
 if len(message.text.split(' ')) > 2:
  if len(message.text.split(' ')[1]) == 10:
   files = open(message.text.split(" ")[2] + ".txt" , "a") 
   files.write(line + " " + message.text.split(' ')[1])
   files.close()
   message.reply("💾 Done, The chat_id  ```" + message.text.split(' ')[1] +"```🌐 has been added to my database. ✅✅")
  else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")
 else:
   message.reply("💼 Please write a valid chat id. ✅✅ ")
@app.on_message(Filters.command('remove') & Filters.user(491634139))
def forward(client, message):
 if len(message.text.split(' ')) > 2:
  if len(message.text.split(' ')[1]) == 10:
   file = open(message.text.split(" ")[2] + ".txt" , "r")
   u = str(file.readlines()).replace("['",'').replace("']",'').replace(' ','',1).split(' ')
   file.close() 
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
      y = client.export_chat_invite_link(int(message.text.split(' ')[1]))
      message.reply(y)
  else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")
 else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")
app.run()
