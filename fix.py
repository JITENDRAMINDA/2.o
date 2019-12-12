from pyrogram import Client, Filters
import nltk
app = Client("mnnn",bot_token="1052551256:AAFnTOgC5ENmBDpWpMVhCWa7WKAE2xkgjiw",api_id=768402,api_hash="f6420bf67303614279049d48d3e670f6")
bullet = -1001289914295
ferrari = -1001453099412
@app.on_message(Filters.chat(bullet) & ~ Filters.edited)
def main(client, message):
 file = open("bullet.txt" , "r")
 lines = nltk.word_tokenize.file.readlines()
 file.close()
 for s in lines:
   try:
    mes = client.send_message( -100 + int(s),message.text.markdown)
   except:
    continue
@app.on_message(Filters.chat(ferrari) & ~ Filters.edited)
def main(client, message):
 file = open("ferrari.txt" , "r")
 lines = nltk.word_tokenize.file.readlines()
 file.close()
 for s in lines:
   try:
    mes = client.send_message( -100 + int(s),message.text.markdown)
   except:
    continue
@app.on_message(Filters.command('add') & Filters.user(491634139) )
def forward(client, message):
 if len(message.text.split(' ')) > 2:
  if len(message.text.split(' ')[1]) == 11:
   with open(message.text.split(" ")[2] + ".txt" , "r") as file:
    lines = file.readlines()
    file.close()
    for line in lines:
     files = open(message.text.split(" ")[2] + ".txt" , "w") 
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
  if len(message.text.split(' ')[1]) == 11:
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
  if len(message.text.split(' ')[1]) == 11:
      x = client.get_chat(int(message.text.split(' ')[1])).title 
      message.reply("📶 This chat name is - "+str(x)+" ✅")
      y = client.export_chat_invite_link(int(message.text.split(' ')[1]))
      message.reply(y)
  else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")
 else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")
app.run()
