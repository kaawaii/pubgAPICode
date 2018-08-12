# importações essenciais para o funcionamento do código da API.
import requests
import discord
prefixo = "!" # Coloque seu prefixo aqui

client = discord.Client()
## importação sem importância para o funcionamento do código Pubg Official Api
import asyncio

@client.event
async def on_ready():
	print('{}'.format(str('-')*10))
	print('O {} foi iniciado...'.format(client.user.name))
	print('Servidores conectado {}'.format(str(len(client.servers))))
	print('Todos os membros do servidor(es) {}'.format(str(len(set(client.get_all_members())))))
	print('ID: {}'.format(client.user.id))
	print('{}'.format(str('-')*10))
	kawaii = await client.get_user_info(user_id="356225453733838848")
	print('Developed by: Emanuel\nNickname discord: {}'.format(kawaii))
	loop = 1
	while loop == 1:
		await client.change_presence(game=discord.Game(name="Bot name: {}".format(client.user.name)))
		await asyncio.sleep(5)
		await client.change_presence(game=discord.Game(name="Command desenvolvido por {}".format(kawaii.name)))
		await asyncio.sleep(5)
		await client.change_presence(game=discord.Game(name="Em {} servidores".format(str(len(client.servers)))))
		await asyncio.sleep(5)
		await client.change_presence(game=discord.Game(name="Atendendo {} Membros".format(str(len(set(client.get_all_members()))))))
		await asyncio.sleep(5)
@client.event
async def on_message(message):
	if message.content.lower().startswith(prefixo + "pubg"): # Ex de como usar : !pubg JJota solo
		#############################  Modos de jogo: solo,solo-fpp,duo,duo-fpp,squad,squad-fpp
		try:# caso queira muda o nome do comando tera que muda a variavel co2
############# coloque o número de letras do nome do seu comando ex: pubg tem 4
			co = len(prefixo)
			co2 = co + 1 + 4 # coloque aqui o números de letras
			cont2 = str(message.content[co2:]).split()
			api_key = "" # Coloque aqui a APi Key Site para conseguir API KEY: "https://documentation.playbattlegrounds.com/en/api-keys.html"
			header = {
				"Authorization": "Bearer {}".format(api_key),
				"Accept": "application/vnd.api+json"
			}
			url = "https://api.pubg.com/shards/pc-sa/players?filter[playerNames]={}".format(cont2[0])
			response = requests.get(url, headers=header)
			js = response.json()
			js3 = js['data'][0]['id']
			link2 = 'https://api.pubg.com/shards/pc-na/players/{}/seasons/division.bro.official.2018-08'.format(js3)
# division.bro.official.2018-08 é a id da season, na hora que estou escrevendo essas explicações esta na season 8
# Bem a season no pubg muda direto, não consegui fazer a api pega o id das seasons novas, ou seja as proximas seasons
# Eu poderia ter feito isto mais meu intuito não é dar comandos totalmentes prontos e fabulosos, meu intuito é fazer você aprender e ter menos
# dificuldade para mexer na API, ou seja quero que você melhore o que já esta feito.
			response3 = requests.get(link2, headers=header)
			json1 = response3.json()
			json3 = json1['data']['attributes']['gameModeStats']
			json2 = json3['{}'.format(cont2[1])] ## aqui é a variavel dos modos de jogos
			EmbedPu = discord.Embed(title="Playerunknown's Battlegrounds",
									description="**══════════════════**\n"
									            "**[Player:](https://i2.wp.com/)** **{}**\n"
												"**══════════════════**".format(cont2[0]),
									colour=0x9b00ff
									)
			EmbedPu.set_thumbnail(
				url="https://i2.wp.com/gamerfocus.co/wp-content/uploads/2017/12/PUBG.jpg%27"
			)
			d = await client.get_user_info(user_id="356225453733838848")
			EmbedPu.set_footer(text="Developed by: {}".format(d))
			EmbedPu.add_field(
				name="Modo de Jogo: {}".format(str(cont2[1]).capitalize()),
				value="**Partida(s): [{}](https://i2.wp.com/)\nAssitencias: [{}](https://i2.wp.com/)\nKills Total: [{}](https://i2.wp.com/)\nRecord Kills em partida: [{}](https://i2.wp.com/)\n"
					  "Kills por Headshot: [{}](https://i2.wp.com/)\nTop 10s: [{}](https://i2.wp.com/)\nVitórias: [{}](https://i2.wp.com/)\nPontos por mata: [{}](https://i2.wp.com/)\nPontos por vitorias: [{}](https://i2.wp.com/)**".format(json2['roundsPlayed'],json2['kills'],json2['assists'],json2['roundMostKills'],json2['headshotKills'],json2['top10s'],json2['wins'],json2['killPoints'],json2['winPoints'])
			)
			EmbedPu.set_author(name=message.author.name, icon_url=message.author.avatar_url)
			await client.send_message(message.channel, embed=EmbedPu)
		except KeyError:
			await client.send_message(message.channel, "{} você digitou seu nick ou modo de jogo errado!".format(message.author.mention))
		except IndexError:
			await client.send_message(message.channel, "{} você não digitou o comando completo".format(message.author.mention))
# Como falei "melhore o que já esta feito", você está totalmente livre para mudar o que quiser neste comando.
# Link da documentação da API "https://documentation.playbattlegrounds.com/en/introduction.html"


client.run("Token do bot")
