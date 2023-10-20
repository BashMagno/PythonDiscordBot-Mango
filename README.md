# Welcome to MangoBot!

This is a discord bot created by me (***BashMagno / Mango***). 
Developed 100% in **python** with usage of a **personalized 'database'** created by me as well.
While in 2023 this bot is going to be in beta:

 1. October 2023 - **v0.1**
 2. November 2023 - **v0.5**
 3. December 2023 - **v0.9**
 4. Future 2024 - **v1.0**

# Commands:

As i said this bot is going to be in beta until **2024** so, until then, the commands are going to be very **basic and specific**.

## Prefix ($)

The prefix used in this bot, for now it´s going to be:

>  `$<command> <parameters>`


## Send embed

Allow you announcements to be more 'cool' or special using discord embeds.


Syntax:




 - If you want to insert an embed **without** image:
 

> `$announce "<title>" "<description>"`

![Embed without image](https://i.ibb.co/wcfGLcD/imagen-2023-10-20-015714812.png)
 - If you want to insert an embed **with** image:
 
> `$announce2 "<title>" "<description>" "<image url>"`

![enter image description here](https://i.ibb.co/xqW7cyc/imagen-2023-10-20-021038450.png)


## Ping

Garbage command, it´s default, just to verify bot is working correctly at that precise moment.

Syntax:

> `$ping`
> Expected output: `Pong!`


## Timer

With this command you can set a timer for as much time as you want. This helps with community events, pick and bans in tourneys, giveaways, countdowns, etc etc...

|Measure| Command |Graphic example |
|---------|--| --
|    Minutes     | `$timer <minutes> minutes` |![minutes](https://i.ibb.co/2FYZnF2/imagen-2023-10-20-023648089.png)
|    Seconds     |  `$timer <seconds> seconds`|![seconds](https://i.ibb.co/2c8xxKy/imagen-2023-10-20-023029377.png)


Example:
> `$timer 10 seconds`
> Expected output: `Timer of 10 second/s started.`
> After 10 seconds: `Time ended! 10 second/s passed.`

# Admin rights commands (in progress...)

In order to run the following commands you must be included in the Admin or SuperAdmin list. 
I am still working on this cause im having problems to update the database while the free hosting is running so i have to code some git push / pulls as well in order to this work at fully.
But if you want to add / remove any admin please contact me through discord and i will add / remove him/her manually.
I expect this to be finished by v1.0 even v0.9.

 - QA


> A) How do i know if i am in the list or not?
> B) On the one hand, try to execute a command with admin rights and you will get an answer by the bot executing it correctly, on the other hand,  if u are not in the list, you will get an error explaining it.


# AddAdmin - RemoveAdmin

This command (AddAdmin) will let you add a new admin to the list, this new admin will have the same privileges as an Admin, but not as a SuperAdmin.
As well, the command RemoveAdmin will remove the admin we are looking for if it exists in the list.
*Exceptions: *You cant remove 'magno1337' as admin cause its me and you will get an error.**

Syntax:

 - AddAdmin command

> `$addAdmin <discordName>`

 - RemoveAdmin command

> `$removeAdmin <discordName>`

Example: 

![+perms](https://i.ibb.co/LkV832v/addAdmin.png)

 - Now user 'Juan' **can** execute admin rights commands.

![-perms](https://i.ibb.co/QmPs68R/imagen-2023-10-20-025201467.png)

 - Now user 'Juan' **can`t** execute admin rights commands.

**Quick tip:**

 

 - The name of the user **must** be exactly the one below the nickname after clicking the profile. Example: 
![idproperly](https://i.ibb.co/PGcJgFC/imagen-2023-10-20-030104489.png)
In this case, the name we should use is the one in smaller font-size (magno1337) which is the **unique username** by discord.


# Delete past messages
This command has two variants.
|| First Variant | Second Variant|
|--|--|--
| Syntax | `$delete` | `$delete <msg.id>`
| Output| This command deletes **every last 100 messages** of the channel from the same message the command has been sent | This command deletes every message exactly the same as the other one, but **it doesn´t delete the message with the id you included** as parameter
| Example:![beforedelete](https://i.ibb.co/phGyPXT/deletemessages.png)| After using this command![delete](https://i.ibb.co/g4MpQbm/afetdeletemessages.png) | After using this command![iddelete](https://i.ibb.co/Hnr5cBr/afterdeletemsgid.png)

 - How to properly do the second variant:

First we **right click** at the message we want to save and **NOT** delete after using the command and we press '**Copy Message ID**'.
After copying the message id, we type `$delete ` and we **paste** the message ID.

![copyid](https://i.ibb.co/VTRSqf9/copymsgid.png)

 - The result:

 The bot deletes last 100 messages in the chat history, **except** the one with the ID you have provided
 ![iddelete](https://i.ibb.co/Hnr5cBr/afterdeletemsgid.png)
