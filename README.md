# kqdrafter
## For Killer Queen
A good draft tournament seeks to split teams as evenly as possible in order to provide the best experience for all players. Often the problem with team creation for draft or pick up teams for killer queen is that it's a labor intensive, highly subjective process. This project is a command line tool for creating killer queen teams for a draft tournament according to arbitrary scoring. It depends a lot on subjective scoring and constants. Future goals for this project is that we machine learn these constants.

# Basics
Killer queen is a five v five arcade game. Each time starts with four drones and a queen. The queen is a special player in that one of the win conditions of the game depends on her.  There are three ways to win the game: kill the opposing queen three times, gather all the berries, ride the snail into the goal.

Drones are the only players who can gather berries or ride the snail or turn into warriors. Though important, drones are lower in skill floor and ceiling. Warriors however are a staple of any team with a high skill ceiling and fairly high skill floor. In addition, warriors can add speed to their repitoire making them even more important and vulnerable.

At the current moment, the game is played on two maps with one in beta. The first is the day map. The meta for day map as of time of writing is 3 warriors and 1 snail rider (fairly constant across scenes). On the other hand the meta for the night map is a little more fluid. Two warriors, two berry workers works well, as does three one snail, as does 3 berry workers and one warrior. I know nothing of dusk map strategies.

# Designing a Team
First we must posit that every player must be able to be scored on a 1-5 point scale. In the simple model, a player receives a role and a score. A more complex model involves detailing every role a player could possibly play and scoring each of them.

The theory behind killer queen teams is complex and thus difficult to model. The team is very dependant on each other. So let's explain the model.

Queens are the backbone of the team: they are required to exert influence on the map and they are the best fighters. However they are also vulnerable to being surrounded and killed. A good queen has a multiplying effect on the rest of her team. A bad one can have a net negative effect on her team. Therefore it is fair to both score the queen and give her a multiplier for the rest of her team.

Warriors are the next most important piece of the team. Good warriors cover for their queen, help secure the map and objectives, and fight to eliminate threats on the board. Therefore, a warrior should get full use of their scores.

Finally drones. Drones are the simplest to play, but no less important. A good drone helps acheive a win condition. But otherwise they have limited influence over the map. The best drones and the worst drones are not as far apart as the best warriors and the worst warriors. They have a multiplier for themselves that lowers their overall impact.

Finally there is a team synergy multiplier. Players who often play together are more likely to do well then players who are not. Thus those on the same team should receive some sort of multiplier to their cumulative score.

# Algorithm
This design calls for three parts. There is a tournament builder, a team builder, and a player pool.

The player pool is the simplest part. Give the format of a playerbase, take those players and put them into a pool.

The team builder is greedy. It will look at the options, scan through the players in the player pool, try to fill slots with the best option available.

The tournament builder keeps track of the order which the team builder picks. It sorts the team by lowest score and then lets that team pick its best options.
