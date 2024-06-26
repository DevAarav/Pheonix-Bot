from typing import cast
import wavelink
from discord.ext import commands
import discord

class Nightcore(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.nightcore_on = False

    @commands.command()
    async def nightcore(self, ctx: commands.Context, mode: str = None) -> None:
        """Set the filter to a nightcore style."""
        player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
        if not player:
            return

        if mode is None:
            embedVar = discord.Embed(
                title="Nightcore Command",
                description="Use ``p!nightcore on`` to turn on nightcore mode or ``p!nightcore off`` to turn it off.",
                color=discord.Color.blue()
            )
            await ctx.send(embed=embedVar)
            return

        if mode.lower() == "on":
            self.nightcore_on = True
            filters: wavelink.Filters = player.filters
            filters.timescale.set(pitch=1.2, speed=1.2, rate=1)
            await player.set_filters(filters)
            await ctx.send("Nightcore mode is now on.")
        elif mode.lower() == "off":
            self.nightcore_on = False
            filters: wavelink.Filters = player.filters
            filters.timescale.set(pitch=1.0, speed=1.0, rate=1)
            await player.set_filters(filters)
            await ctx.send("Nightcore mode is now off.")
        else:
            await ctx.send("Invalid mode. Please use '?nightcore on' or '?nightcore off'.")

        await ctx.message.add_reaction("\u2705")

async def setup(bot):
    await bot.add_cog(Nightcore(bot))
    print("Music: Nightcore Loaded")
