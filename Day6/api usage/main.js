const { Client, MessageEmbed } = require("discord.js");
const fetch = require("node-fetch");
const client = new Client({ intents: ["GUILDS", "GUILD_MESSAGES"] });
const config = require('dotenv').config();

const botToken = process.env.TOKEN;
const movieToken = process.env.TMDB;
const BASE_URL = "https://api.themoviedb.org/3";
const BASE_IMAGE_URL = "https://image.tmdb.org/t/p/w500";

const getMovie = async (value) => {
    const response = await fetch(`${BASE_URL}/search/movie?api_key=${movieToken}&query=${value}`);
    const data = await response.json();
    const actual = data.results[0];

    return [BASE_IMAGE_URL + actual.poster_path, actual.original_title, actual.overview, actual.release_date, actual.vote_average];
}

client.on("ready", () => {
    console.log(`Logged in as : ${client.user.tag}`)
});

client.on("message", async (msg) => {
    if(msg.author.bot) return;

    /* msg.channel.send() //for no tag */

    if((msg.content).search("movie") !== -1 && (msg.content).startsWith("$")){
        cont = (msg.content).split("$movie");
        const data = await getMovie(cont[1]);


        const exampleEmbed = new MessageEmbed()
	        .setColor('#0099ff')
	        .setTitle(`${data[1]}`)
            .setImage(data[0])
	        .addFields(
	        	{ name: 'Synopsis', value: `${data[2]}`},
	        	{ name: 'Release Date', value: `${data[3]}`},
	        	{ name: 'IMDb Rating', value: `${data[4] === 0 ? "-" : data[4]}`},
	        )
	        .setTimestamp()

            msg.channel.send({ embeds: [exampleEmbed] });
    }
    
}) ;

client.login(botToken);