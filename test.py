import re
import json

transcript_text = """
Speaker 1: (00:01)
Summer was going so well for the president, the White House threw a party last week with a concert by James Taylor. Mr. Biden’s streak began in June when he signed a bipartisan gun safety law. Then in August, over Republican objections, he signed the largest investment ever on climate change, a minimum tax on corporations, a law to lower prescription drug prices and student loan forgiveness. But Tuesday, as James Taylor sang Fire and Rain, it seemed like both descended on the President’s party, the Dow plummeted nearly 1,300 points after a dismal inflation report. At the White House on Thursday, we spoke to President Biden about the economy, Ukraine, those top secret documents in Donald Trump’s home and whether Mr. Biden will run again. The President made news and will ignite a few controversies. This the story will continue in a moment.
Speaker 1: (01:08)
Mr. President, as you know, last Tuesday, the annual inflation rate came in at 8.3%, the stock market nosedived, people are shocked by their grocery bills. What can you do better and faster?
President Joe Biden: (01:24)
Well, first of all, let’s put this in perspective. Inflation rate month to month is just up an inch, hardly at all.
Speaker 1: (01:31)
You’re not arguing that 8.3 is good news?
President Joe Biden: (01:34)
No, I’m not saying it is good news, but it was 8.2 before. I mean, it’s not… I can make it sound like all of a sudden, “My God, it went to 8.2%.” It’s been-
Speaker 1: (01:44)
It’s the highest inflation rate, Mr. President, in 40 years.
President Joe Biden: (01:47)
I got that. But guess what we are, we’re in a position where for the last several months it hasn’t spiked, it has just barely… It’s been basically even. And in the meantime, we created all these jobs and prices have gone up, but they’ve come down for energy. The fact is that we’ve created 10 million new jobs since we came to office. We’re in a situation where the unemployment rate is about 3.7%, one of the lowest in history. We’re in a situation where manufacturing is coming back to the United States in a big way. And look down the road, we have massive investments being made in computer chips and employment. So look, this is a process, this is a process.
Speaker 1: (02:33)
Is the economy going to get worse before it gets better?
President Joe Biden: (02:36)
No, I don’t think so. We hope we can have what they say, a soft landing, a transition to a place where we don’t lose the gains that I ran to make in the first place for middle class folks, being able to generate good paying jobs and expansion. And at the same time, make sure that we are able to continue to grow.
Speaker 1: (03:01)
And you would tell the American people that inflation is going to continue to decline?
President Joe Biden: (03:06)
No, I’m telling the American people that we’re going to get control of inflation, and their prescription drug prices are going to be a hell of a lot lower, their healthcare costs are going to be a lot lower, their basic costs for everybody. Their energy prices are going to be lower. They’re going to be in a situation where they begin to gain control again. I’m more optimistic than I’ve been in a long time.
Speaker 1: (03:25)
Sir, with the Federal Reserve rapidly raising interest rates, what can you do to prevent a recession?
President Joe Biden: (03:33)
Continue to grow the economy, and we’re growing the economy. It’s growing in a way that it hasn’t in years and years.
Speaker 1: (03:41)
How so?
President Joe Biden: (03:42)
We’re growing entire new industries. We’re at 695, I think it is, or 85,000 new manufacturing jobs just since I’ve become president of the United States. Continue to grow the economy and continue to give hard working people a break in terms of, we pay the highest drug prices in the world of any industrialized nation, making sure that Medicare can negotiate down those prices. By the way, we’ve also reduced the debt and reduced the deficit by 350 billion dollars my first year. This year, it’s going to be over $1.5 trillion dollars reduced the debt. So, to continue to put people in a position to be able to make a decent living and grow, and grow, and increase their capacity to grow.
Speaker 1: (04:28)
[inaudible 00:04:28]. To see what he means we went with Mr. Biden to the Detroit Auto Show last Wednesday.
President Joe Biden: (04:34)
[inaudible 00:04:34].
Speaker 1: (04:34)
He celebrated his new funding of a network of charging stations for electric vehicles. But the newly crowded convention center brought a different question to mind. Mr. President, the first Detroit Auto Show in three years, is the pandemic over?
President Joe Biden: (04:52)
The pandemic is over. We still have a problem with COVID, we’re still doing a lot of work on it, but the pandemic is over. If you noticed, no one’s wearing masks, everybody seems to be in pretty good shape. And so I think it’s changing, and I think this is a perfect example of it.
Speaker 1: (05:10)
The car show was a reminder that gasoline prices hit a historic high last June, in part because Russia cut fuel supplies in its war on Ukraine. Mr. President, the price of gasoline is down about 26% from the $5 high, what can you do to keep that price down while Vladimir Putin is throttling energy supply?
President Joe Biden: (05:33)
Well, there’s a couple things we’ve done. For example, remember I got some criticisms for releasing a million barrels of oil a day from the Strategic Petroleum Reserve, and then along came the industry saying they’d produce another million barrels a day by the spring. So I think we’re in relatively good shape.
Speaker 1: (05:49)
Vladimir Putin is going to try to break your will on Ukraine and use energy prices to do it.
President Joe Biden: (05:56)
Sure he is, but we, the United States, are in a much better shape than anyone else is, and relative to Russia, particularly. But he’s been trying that for a while, he’s not going to succeed. Anybody want to go to Washington, jump in.
Speaker 1: (06:12)
But at this very moment that Mr. Biden steered for the future, a 19th century form of transport threatened to wreck the economy. A deadline for a national rail strike was two days away. The White House brokered a deal Thursday after a 20 hour marathon of negotiations.
President Joe Biden: (06:34)
One of the things that happens in negotiations, particularly if they’ve been elongated like these have, is people say and do things where their pride gets engaged as well, and it’s awful hard to back off of some of these things. They both sat down, in my view, and they were in the office today saying, “Well, we finally figured it out. This is fair on both sides.” And it took that time to focus. And the alternative was just not thinkable.
Speaker 1: (07:03)
What do you mean?
President Joe Biden: (07:04)
If, in fact, they’d gone on a strike, the supply chains in this country would’ve come to a screeching halt. We would’ve seen a real economic crisis.
Speaker 1: (07:12)
The other crisis on the president’s desk, Ukraine was also improving last week as Ukrainian forces recaptured, about 3,000 square miles from the Russian invasion. Is Ukraine winning the war?
President Joe Biden: (07:26)
Ukraine, through their… With significant help we and our allies are giving them, and the incredible bravery, and the incredible determination of the Ukrainian people, are not losing a war, and they’re making gains in certain areas. Winning the war in Ukraine is to get Russia out of Ukraine completely and recognizing their sovereignty. They’re defeating Russia. Russia’s turning out not to be as competent and capable as many people thought they were gonna be. But winning the war? The damage it’s doing, and the citizens, and the innocent people are being killed, it’s awful hard to count that as winning.
Speaker 1: (08:10)
After the horrors of seven months of war, President Biden has called Russian President, Vladimir Putin, a war criminal.
President Joe Biden: (08:18)
It has been barbaric, what he’s done. His attacks on civilian, everything from civilian hospitals, to old-age homes, to neighborhoods where just ordinary people live-
Speaker 1: (08:33)
Schools.
President Joe Biden: (08:34)
And schools, it’s just outrageous. So the price the Ukrainian people are paying for this war is extremely high. But we’re gonna stay with them as long as they need our help.
Speaker 1: (08:48)
You’re already north of $15 billion in terms of those commitments. How far do you go?
President Joe Biden: (08:53)
As long as it takes.
Speaker 1: (08:55)
Ironclad commitment?
President Joe Biden: (08:56)
Yes.
Speaker 1: (08:58)
As Ukraine succeeds on the battlefield, Vladimir Putin is becoming embarrassed and pushed into a corner. And I wonder Mr. President, what you would say to him, if he is considering using chemical or tactical nuclear weapons.
President Joe Biden: (09:15)
Don’t. Don’t. Don’t. It will change the face of war unlike anything since World War II.
Speaker 1: (09:26)
And the consequences of that would be what?
President Joe Biden: (09:28)
I am not going to speculate-
Speaker 1: (09:29)
What would the US response be?
President Joe Biden: (09:31)
You think I would tell you if I knew exactly what it would be? Of course, I’m not going to tell you, but it’ll be consequential. They’ll become more of a pariah in the world than they ever have been, and depending on the extent of what they do will determine what response would occur. [inaudible 00:09:45].
Speaker 1: (09:45)
On the same day, we spoke to the President, Putin met with China’s leader, Xi Jingling. There’s concern that Russia’s attempt to force reunification with Ukraine could inspire China to attack the island of Taiwan. US policy since 1979 has been to recognize Taiwan as part of China, but remain silent on whether the US military would defend the democratic government there. This is among the places where our interview runs into controversy. What should Chinese President Xi know about your commitment to Taiwan?
President Joe Biden: (10:28)
We agree with what we signed onto a long time ago. And that there’s a one China policy, and Taiwan makes their own judgments about their independence. We are not moving, we’re not encouraging their being independent. That’s their decision,
Speaker 1: (10:43)
But would US forces defend the island?
President Joe Biden: (10:45)
Yes, if in fact there was an unprecedented attack [inaudible 00:10:49]-
Speaker 1: (10:48)
After our interview a White House official told us U.S. policy has not changed. Officially, the U.S. will not say whether American forces would defend Taiwan, but the commander-in-chief had a view of his own.
President Joe Biden: (11:05)
[inaudible 00:11:05].
Speaker 1: (11:05)
So unlike Ukraine, to be clear, sir, U.S. Forces, U.S. men and women, would defend Taiwan in the event of a Chinese invasion?
President Joe Biden: (11:13)
Yes.
Speaker 1: (11:16)
For the first time Mr. Biden spoke about the classified documents that the FBI found in former President Trump’s home. The Justice Department has opened a criminal investigation. Have you been brief, sir, on the top secret documents that were found at Mar-a-Lago?
President Joe Biden: (11:33)
No.
Speaker 1: (11:34)
No one has come to you to warn you that important national security secrets were revealed by the storage of those documents at the former president’s home?
President Joe Biden: (11:45)
I have not personally spoken to anyone in that regard. I’m sure, my administration is aware of all of that and so is the National Security Council, but I have not.
Speaker 1: (11:55)
Were you notified of the FBI’s execution of a search warrant at Mar-a-Lago?
President Joe Biden: (12:01)
No, not ahead of time.
Speaker 1: (12:04)
The FBI spread the documents out on a floor to make a record of what was found. When you saw the photograph of the top-secret documents laid out on the floor at Mar-a-Lago, what did you think to yourself looking at that image?
President Joe Biden: (12:22)
How that could possibly happen? How anyone could be that irresponsible. And I thought, what data was in there that may compromise sources and methods? By that I mean, names of people who helped, or et cetera. And it’s just totally irresponsible.
Speaker 1: (12:41)
And you don’t know what was in those documents?
President Joe Biden: (12:44)
I have not asked for the specifics of those documents because I don’t want to get myself in the middle of whether or not the Justice Department should move or not move on certain actions they can take. I agreed I would not tell them what to do, and not, in fact, engage in telling them how to prosecute or not.
Speaker 1: (13:05)
When we come back a surprising answer to the question of whether President Biden will run for a second term.
Speaker 1: (13:20)
At the White House last Thursday, President Biden told us he hopes to retain control of the House and the Senate in the midterm election in November, but given the president’s job approval rating of around 40%, that remains to be seen. For his part, Mr. Biden has said he plans to run again in 2024, but here is another place where our interview may cause controversy.
Speaker 1: (13:48)
The story will continue in a moment.
Speaker 1: (13:53)
Sir, are you committed to running again? Or are there certain conditions that have to be right?
President Joe Biden: (13:59)
Look, if I were to say to you, “I’m running again,” all of the sudden a whole range of things come into play, requirements I have to change and move and do.
Speaker 1: (14:07)
In terms of election laws?
President Joe Biden: (14:08)
In terms of election laws. And it’s much too early to make that kind of decision. I’m a great respecter of fate. And so what I’m doing is I’m doing my job, I’m going to do that job and within the timeframe that makes sense, after this next election cycle here, going into next year, make a judgment of what to do.
Speaker 1: (14:27)
You say that it’s much too early to make that decision. I take it the decision has not been made in your own head?
President Joe Biden: (14:34)
Look, my intention, as I said to began with, is that I would run again, but it’s just an intention. But is it a firm decision that I run again, that remains to be seen.
Speaker 1: (14:46)
Mr. President, you are the oldest president ever-
President Joe Biden: (14:50)
Pretty good shape, huh?
Speaker 1: (14:52)
Which leads to my next question, you are more aware of this than anyone, some people ask whether you are fit for the job. And when you hear that, I wonder what you think.
President Joe Biden: (15:05)
Watch me. And honest to God, that’s what I think. Watch me. If you think I don’t have the energy level or the mental acuity, then that’s one thing. But it’s another thing to just watch and keep my schedule, do what I’m doing. I think that… I don’t, when I sit down with our NATO allies and keep them together, I don’t have them saying, “Wait a minute, how old are you? What do you say?” I mean, it’s a matter of that old expression, the proof of the pudding’s in the eating. I mean, I respect the fact that people would say, “You’re old.” But I think it relates to how much energy you have and whether or not the job you’re doing is one consistent with what any person of any age would be able to do.
Speaker 1: (15:55)
How would you say your mental focus is?
President Joe Biden: (15:58)
Oh, it’s focused. Look, I have trouble even mentioning, even saying to myself in my own head the number of years. I no more think of myself as being as old as I am than fly. I mean, it’s just not… I haven’t observed anything in terms of… There’s not things I don’t do now that I did before, whether it’s physical or mental or anything else.
Speaker 1: (16:26)
You have had a string of legislative successes recently-
President Joe Biden: (16:32)
How’s an old guy do that?
Speaker 1: (16:34)
But your approval rating in the country is well below 50%, and I wonder why you think that is?
President Joe Biden: (16:44)
This is a really difficult time. We’re at an inflection point in the history of this country. We’re going to make decisions, and we’re making decisions now, that are going to determine what we’re going to look like in the next 10 years from now.
President Joe Biden: (16:57)
I think you’d agree that the impact on the psyche of the American people, as a consequence of the pandemic, is profound. Think of how that has changed everything, people’s attitudes about themselves, their families, about the state of the nation, about the state of their communities. And so there’s a lot of uncertainty out there, a great deal of uncertainty. And we lost a million people, a million people to COVID. When I got in office, when I got elected, only two million people had been vaccinated, I got 220 million… My point is, it takes time. We were left in a very difficult situation. It’s been a very difficult time, very difficult.
Speaker 1: (17:43)
And a difficult life for the president. In 1972 he lost his wife and daughter in a car accident. He lost his son, Beau, to cancer in 2015 at the age of 46. And his son, Hunter, has been a lightning rod for suspicion. Hunter Biden’s former addiction to crack cocaine led to a life he describes as nonstop depravity. He has also acknowledged a federal investigation into his taxes. Congress investigated Hunter Biden’s job with a Ukrainian company at the time that his father ran Ukrainian policy in the Obama administration. A Republican investigation, however, uncovered no wrongdoing by then Vice President Biden.
Speaker 1: (18:32)
Mr. President, if you run again, Republicans are most likely to go after your son, Hunter, once again. And I wonder what you would like to say about your son and whether any of his troubles have caused conflicts for you or for the United States.
President Joe Biden: (18:56)
I love my son, number one. He fought an addiction problem. He overcame it, he wrote about it. And no, there’s not a single thing that I’ve observed at all that would affect me or the United States relative to my son, Hunter.
Speaker 1: (19:15)
Republican investigations are likely to resume if Mr. Biden loses either the House or the Senate, and history shows that presidents usually lose seats in Congress in a midterm election. If so, the president’s remaining ambitions may be beyond his reach.
President Joe Biden: (19:33)
For example, we passed the most extensive gun legislation in 30 years, although I’m not gonna rest till we get assault weapons banned, which I did once before when I was a senator.
Speaker 1: (19:42)
Assault weapons banned?
President Joe Biden: (19:44)
Assault weapons banned. There’s no rationale. Deer aren’t running through the woods wearing Kevlar vests.
Speaker 1: (19:51)
Somebody came in and told you about Uvalde when it happened, and I wonder what you thought.
President Joe Biden: (20:00)
Again, I’ve gone to every one of those places. And in Uvalde, I spent time with every sing… Four hours, four hours in the pain, the pain, and it’s just so, so unnecessary. So wrong. Who the hell… Don’t get me going. But I met with every one of those families and the extended families for four hours. Look, our kids should be learning how to read and write, not duck and cover. Think about that. Think of the mental impact on these kids going back to school. We saw it. It’s wrong. It’s wrong. It’s not who we are. And we’ve gotta stop it. We’ve got to stop it. And the NRA continuing to push the sale of assault and semiautomatic weapons is bizarre.
Speaker 1: (20:59)
The much more modest bi-partisan gun law that passed this summer may be the best example of the President’s legislative breakthroughs that no one thought possible. “How’d an old guy do that?” He asked us earlier. We have a theory. Joe Biden is among the longest-serving politicians in Washington. If there is less bounce in the step than there once was, if the words don’t flow like they used to, maybe there’s something to be said for knowhow, five decades on the Hill and in the Oval.
Speaker 1: (21:35)
Concerning politics, Mr. President, you were elected to the Senate in 1972, you were 29 years old. And in those days, it seemed that the parties worked together to move the country forward. And I think many Americans feel that that no longer happens, and, in fact, may be impossible now.
President Joe Biden: (22:01)
Well, I don’t think it’s impossible, but it’s changed. What we do today, think about it, it’s all personal attacks. It’s about motive. It’s not about, I disagree with you on the subject matter. And secondly, I think it’s fair to say that we’ve not had a president like the last president, who has made all of it so personal. I’ve had six Republican senators, I promised I’d never say their names, and I won’t, come up to me in the last two years and say, “Joe, I agree with you, but if I vote this way they’re going to primary me and I’m going to lose an election.” It didn’t used to be that way, but it’s coming back a little bit. It’s coming back.
Speaker 1: (22:44)
Do you see it? It seems to me, Mr. President, that when you first came to the Senate the other guy had a bad idea, and now the other guy is a bad guy. And I don’t know how you get back to that.
President Joe Biden: (22:58)
Well, I’ll tell you what I think about this. We were able to get a bipartisan $1.2 trillion package done for dealing with the whole question of rebuilding the country, the roads and the highways. The fact of the matter is we’ve gotten a lot of things done bi-partisanly, when everybody said, “We’re not gonna do anything, don’t let Biden have any successes,” et cetera. So it’s still a way to go, but I think we’re making some progress.
Speaker 1: (23:24)
You have lived a long life of triumph and tragedy. In November, you’ll be 80. And I wonder what it is that keeps you in the arena.
President Joe Biden: (23:37)
Well, look, I’ve had tragedies. I lost part of my soul when I lost my son Beau, and I lost my wife and my daughter in an accident. I think of all the people who’ve gone through what I’ve gone through and a lot more without what I had. I have had incredibly supportive family. There’s so many, literally, heroes getting up every day putting one foot in front of the other with no help, I constantly think, what would Beau want me to do? What would… And this gets me a long way, this rosary.
Speaker 1: (24:16)
Catholic and devout, he keeps a rosary in his pocket. And he showed us his other inspiration in a cartoon that his father had framed. In it, the Viking, Hagar, confronts God after a lighting strike, a blow like those endured by the president. [inaudible 00:24:35].
President Joe Biden: (24:35)
And he’s looking up, and what’s he say? He says, “Why me, God?” And the next scene, a voice from heaven, “Why not?” That’s my dad. “Why not, Joey? Why not you? Why not? What makes you so different? Just get up.” My mom’s expression was, “Just get up. Get up. Get up.”
Speaker 1: (24:56)
And you feel you have more to give?
President Joe Biden: (24:58)
A lot more to give, a lot more to give.
"""

import re
import json

def convert_transcript(transcript_text):
    # Remove timestamps from transcript
    transcript_text = re.sub(r'\(\d+:\d+\)', '', transcript_text)

    # Split the text by speaker
    split_text = re.split(r'((?:Speaker \d+|President Joe Biden):)', transcript_text)

    # Ensure no empty strings and strip white spaces
    split_text = [segment.strip() for segment in split_text if segment.strip()]

    # Initialize an empty list for storing the segments
    data = []

    # Initialize a variable to keep track of the last speaker
    last_speaker = None

    for i in range(len(split_text)):
        if "Speaker" in split_text[i]:
            data.append({
                "role": "user",
                "content": split_text[i+1]
            })
            last_speaker = "user"

        elif "President Joe Biden" in split_text[i]:
            data.append({
                "role": "assistant",
                "content": split_text[i+1]
            })
            last_speaker = "assistant"

    # Convert the pairs list to json
    json_transcript = json.dumps({"messages": data}, indent=2)

    return json_transcript

json_transcript = convert_transcript(transcript_text)
print(json_transcript)

desktop_path = "/Users/samwirth/Desktop/perrincorp/"  # For MacOS

# Write the JSON data to a file on your desktop
with open(desktop_path + 'updated_biden.json', 'w') as f:
    f.write(json_transcript)