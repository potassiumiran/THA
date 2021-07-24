from telegram.ext import Updater,MessageHandler,Filters


def lighton(bot,update):
  chat_id=bot.message.chat_id
  path='https://cdn.pixabay.com/photo/2019/09/29/22/06/light-bulb-4514505_1280.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("the light is on")
  val=1
  from Adafruit_IO import Client
  aio = Client('kirran', 'aio_CAWg83fKkth1jp4SjMy5q9dT8SsY')


  aio.send('light', val)


  data = aio.receive('light')
  print('Received value: {0}'.format(data.value))
  

def lightoff(bot,update):
  chat_id=bot.message.chat_id
  path='https://cdn5.vectorstock.com/i/1000x1000/70/44/3d-realistic-off-light-bulb-icon-closeup-vector-27407044.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("the light is off")
  val=0
  from Adafruit_IO import Client
  aio = Client('kirran', 'aio_CAWg83fKkth1jp4SjMy5q9dT8SsY')


  aio.send('light', val)


  data = aio.receive('light')
  print('Received value: {0}'.format(data.value))

def fanon(bot,update):
  chat_id=bot.message.chat_id
  path='https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/decorative-ceiling-fan-in-motion-b-john-myers.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("the fan is on")
  val=1
  from Adafruit_IO import Client
  aio = Client('kirran', 'aio_CAWg83fKkth1jp4SjMy5q9dT8SsY')


  aio.send('fan', val)


  data = aio.receive('fan')
  print('Received value: {0}'.format(data.value))


def fanoff(bot,update):
  chat_id=bot.message.chat_id
  path='https://5.imimg.com/data5/PN/HR/MY-8054528/pooja-meghdoot-high-speed-ceiling-fan-500x500.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("the fan is off")
  val=0
  from Adafruit_IO import Client
  aio = Client('kirran', 'aio_CAWg83fKkth1jp4SjMy5q9dT8SsY')


  aio.send('fan', val)


  data = aio.receive('fan')
  print('Received value: {0}'.format(data.value))




def accept(bot,update):

  mark=False

  a=bot.message.text.lower()


  b=a.split()

  for i in b:
    if i=="light":
      for j in b:
        if j=="on":
          lighton(bot,update)
        elif j=="off":
          lightoff(bot,update)
  
    


  for i in b:

    if i=="fan":
      for j in b:
        if j=="on":
          fanon(bot,update)
        elif j=="off":
          fanoff(bot,update)

  for i in b:
    if i == "light" or i == "fan":
      mark=True
      break

  if mark==False:
     bot.message.reply_text("invalid command, specify the device and function to be performed together")
  elif mark==True:
    mark=False

  
      

     
    


 

  




  







BOT_TOKEN='1924859836:AAFTOIeoH_Twbc2KjeWIsXh2AwxHvOcu61g'
u=Updater(BOT_TOKEN,use_context=True)
dp=u.dispatcher
dp.add_handler(MessageHandler(Filters.text,accept))
u.start_polling()
u.idle()

