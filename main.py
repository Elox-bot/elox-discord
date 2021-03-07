import discord
from discord.ext import commands, tasks
import random

bot = commands.Bot(command_prefix = "e!", description = "Elox by LEN", help_command=None)
status = ["My prefix is e!",
        "I look your server",
        "Made in Belgium",
        "Full english",
        "My creator is LƎN"]

@bot.event
async def on_ready():
	print("Ready !")
	changeStatus.start()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "<@813824566110584913>" in message.content.lower():
        await message.channel.send(f"> **Hello {message.author} i'am Elox.**\n> **My prefix is e! , for have a help enter the following commands : e!help**", delete_after = 20)
    else:
         pass
    await bot.process_commands(message)

@bot.command
async def server_info_nr(ctx):
	server = ctx.guild
	serverName = server.name

@bot.command()
async def namecreator(ctx):
	embed = discord.Embed(title = "**The name on creator is : LƎN#2021 .**", color = 0x4cd10)
	await ctx.send(embed = embed, delete_after = 5)
	await ctx.message.delete()


@bot.event
async def on_command_error(ctx , error):
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title = "Please enter one number !", color = 0xff0000)
		await ctx.send(embed = embed, delete_after = 3)
	elif isinstance(error, commands.MissingPermissions):
		embedtwo = discord.Embed(title = "You dont have the required permissions !", color = 0xff0000, delete_after = 5)
		await ctx.send(embed = embedtwo, delete_after = 5)

#clear

@bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, nombre : int):
	await ctx.channel.purge(limit = nombre + 1)
	embed = discord.Embed(title = "The messages has been deleted !", color = 0xffffff)
	await ctx.send(embed = embed, delete_after = 2)
	await ctx.message.delete()

#kick

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	embed = discord.Embed(title = f"The user {user} has been kick on the server , for the following reason : {reason}  !", color=0xff0000)
	await ctx.send(embed = embed)
	await ctx.message.delete()

#name 

@bot.command(name='name', aliases=['nam', 'NAME'])
async def name(ctx, user: discord.Member):
    embed = discord.Embed(title = f"Your name is {user}", url = "https://discord.gg/uvsG8A9kXa", color=0x4cd10)
    embed.set_image(url=f"{user.avatar_url}")
    await ctx.send(embed = embed)
    await ctx.message.delete()
 
@name.error
async def avatar_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        embed = discord.Embed(title = f"Your name is {ctx.author}", color =0xff0000)
        embed.set_image(url = f"{ctx.author.avatar_url}")
        await ctx.send(embed = embed)
        await ctx.message.delete()

#ban

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.Member, *, reason = "No reason was given"):
 if user.top_role >= ctx.author.top_role:
    await ctx.send("You can't banish people underneath or who have the same roles as you !")
    return
 else:
        await ctx.guild.ban(user, reason = reason)
        embed = discord.Embed(title = "**Banning**", description = "A moderator has banned a member!", color=0xff0000)
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.add_field(name = "Banned member", value = user.name, inline = False)
        embed.add_field(name = "Reason", value = reason)
                
        await ctx.send(embed = embed)



#unban

@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, user, *, reason = "No reason was given"):
    reason = " ".join(reason)
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    embed = discord.Embed(title = f"The user was unbaned !", color = 0xff0000)
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason = reason)
            await ctx.send(embed = embed)
            return
    # not found
    await ctx.send(f"**The user {user} was not found in banned list .**")

#warn
@bot.command()
@commands.has_permissions(kick_members = True)
async def warn(ctx, user: discord.Member, *, reason = "No reason was given"):
	name = user.mention

	embed = discord.Embed(title = "Warned", description = f"**The user {user} has been warned ! Please follow the rules !**", color = 0x4deeea)
	embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
	embed.add_field(name = "Reason", value = reason)
	await ctx.message.delete()
	await ctx.send(embed = embed)
    
#help
@bot.command(name ='help', aliases=['hel', 'HELP'])
async def help(ctx):
    embed = discord.Embed(title = "Here are the commands ...", description = f"**e!help**\n**e!name**\n**e!Administrator**\n**e!namecreator**\n**e!fakeban**", color=0x74ee15)
    await ctx.send(embed = embed, delete_after = 30)
    await ctx.message.delete()

@bot.command(name = 'Administrator', aliases=['admin'])
@commands.has_permissions(kick_members = True)
async def Administrator(ctx):
	embed = discord.Embed(title = "Administrator", description = f"**e!clear (count)**\n**e!ban @(just for admin or have permission to ban)**\n**e!kick @(username)**\n**e!unban (name and #)**\n**e!warn @(username)**", color =0x74ee15)
	await ctx.send(embed = embed, delete_after = 30)
	await ctx.message.delete()

@tasks.loop(seconds = 5)
async def changeStatus():
	game = discord.Game(random.choice(status))
	await bot.change_presence(status = discord.Status.dnd, activity = game)

#fakeban

@bot.command()
async def fakeban(ctx, user : discord.Member, *, reason = "No reason was given"):
        embed = discord.Embed(title = "**Banning**", description = "A moderator has banned a member!", color=0xee8899)
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.add_field(name = "Banned member", value = user.name, inline = False)
        embed.add_field(name = "Reason", value = reason)
                
        await ctx.send(embed = embed)





#démmarage du bot

bot.run("ODEzODI0NTY2MTEwNTg0OTEz.YDU7MA.vXxj67WvidPHsb0P9PAkYWiokE0")

