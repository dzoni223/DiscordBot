import discord
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
TOKEN = 'OTg2Njc3NzQzNzQxNzAyMjI0.GLFGXu.ZLoSJaIl5FG8vyvIwqnepZxhMHOMAiGJ4ELdxQ'

client = discord.Client()

@client.event
async def on_ready():
  print('{0.user} is online'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$hello'):
    await message.channel.send('Hello!')

  if msg.startswith('$ping'):
    split = msg.split()
    if len(split) != 3:
      await message.channel.send("Wrong number of arguments")
      return
    url = "https://" + split[1] + ".op.gg/summoners/" + split[1] + "/" + split[2]
    driver.get(url)
    if driver.find_element(By.XPATH, '//*[@id="content-header"]/div[1]/div/div[1]/div[2]/div[4]/button[1]').is_enabled():
      driver.find_element(By.XPATH, '//*[@id="content-header"]/div[1]/div/div[1]/div[2]/div[4]/button[1]').click()
      await message.channel.send('Updated information:')
    else:
      text = driver.find_element(By.XPATH, '//*[@id="content-header"]/div[1]/div/div[1]/div[2]/div[5]').text
      await message.channel.send(text)
      return
    tier = driver.find_element(By.XPATH, '//*[@id="content-container"]/div[1]/div[1]/div[2]/div[2]/div[1]').text
    lp = driver.find_element(By.XPATH, '//*[@id="content-container"]/div[1]/div[1]/div[2]/div[2]/div[2]').text
    winLose = driver.find_element(By.XPATH, '//*[@id="content-container"]/div[1]/div[1]/div[2]/div[3]/div[1]').text
    ratio = driver.find_element(By.XPATH, '//*[@id="content-container"]/div[1]/div[1]/div[2]/div[3]/div[2]').text
    await message.channel.send(split[2] +': ' + tier + " " + lp + " | " + winLose + " | " + ratio)
    
client.run(TOKEN)
