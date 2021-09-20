//lancement du bot//
const Discord = require('discord.js');
const bot = new Discord.Client();
const token = require("./token.json")
const bdd =require("./token.json")

bot.on("ready", async () => {
    console.log("le bot à démarrer")
    bot.user.setStatus("online")
    bot.user.setActivity("Développement du bot en cour", {type:'COMPETING'})//ce que le bot a comme activité
    bot.channels.cache.get('839923844952883260').send('Bot vient de démarer !')
})

//quand un menbre arrive su le serveur
bot.on("guildMemberAdd", menber => { 
    bot.channels.cache.get('839944518291685376').send('Bienvenue sur le serveur de la coms ${member}!')

})




bot.login(token.token); //key du bot dans token.josen #