My plan for my project is to make a program that allows for people to type in exactly what they want a minecraft commands to do and having it
automagicly put together the syntax for the NBT. This removes a lot of the human error NBT syntaxing usually undergoes. Let me give you an example of 
the potential of this project. Let's say you want to make a command that summons a Zombie with full diamond armor. You would first tell the program you
want to spawn a entity, then you would specify a Zombie, then you would tell it you wanted it to wear full diamond armor. It would evaluate each request
and put together something like this: /summon Zombie ~ ~1 ~ {Equipment:[{},{id:diamond_helmet},{id:diamond_chestplate},{id:diamond_leggings},{id:diamond_boots}]}
The possiblities are endless.