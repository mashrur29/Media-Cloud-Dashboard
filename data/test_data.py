# far_left -> mostly_left
# somewhat_left -> somewhat_left
# center
# somewhat_right -> somewhat_right
# right -> mostly_right

clusters = {
    "week 1": [
        {
            "name": "Donald Trump second term would be 'worse than first', warns former ambassador",
            "article_counts": 5,
            "articles": [
                {"title": "Donald Trump second term would be 'worse than first', warns former ambassador",
                 "url": "http://example.com/0", "collection": "somewhat_right"},
                {"title": "Biden’s State of the Union speech to take place in March", "url": "http://example.com/1",
                 "collection": "center"},
                {"title": "Biden attacks Trump as threat to democracy, warns against his re-election",
                 "url": "http://example.com/2", "collection": "mostly_right"},
                {"title": "Anti-Defamation League staff decry ‘dishonest’ campaign against Israel critics",
                 "url": "http://example.com/3", "collection": "mostly_right"},
                {"title": "Haley campaign announces $24 million haul in 4th quarter", "url": "http://example.com/4",
                 "collection": "mostly_left"}
            ]
        },
        {
            "name": "How Key Right-Wing Media Figures Rewrote The History Of January 6",
            "article_counts": 5,
            "articles": [
                {"title": "How Key Right-Wing Media Figures Rewrote The History Of January 6",
                 "url": "http://example.com/0", "collection": "somewhat_right"},
                {"title": "Donald Trump omits context on Nikki Haley’s comments about US retirement age being too low",
                 "url": "http://example.com/1", "collection": "mostly_left"},
                {
                    "title": "Joe Biden’s Valley Forge Speech About Trump’s ‘Threat to Our Democracy’ Was as Awful as You’d Expect",
                    "url": "http://example.com/2", "collection": "somewhat_left"},
                {"title": "Many Republicans who blamed Trump for Capitol riot now endorse him",
                 "url": "http://example.com/3", "collection": "somewhat_right"},
                {"title": "Three years later, beware dangerous revisionism of Jan. 6", "url": "http://example.com/4",
                 "collection": "center"}
            ]
        },
        {
            "name": "WATCH: Barely Coherent Nancy Pelosi Says States Can Overrule Constitution, Ban Trump From the Ballot",
            "article_counts": 5,
            "articles": [
                {
                    "title": "WATCH: Barely Coherent Nancy Pelosi Says States Can Overrule Constitution, Ban Trump From the Ballot",
                    "url": "http://example.com/0", "collection": "somewhat_left"},
                {
                    "title": "Robert F. Kennedy Jr. files as presidential candidate in Utah, the first state to grant him access",
                    "url": "http://example.com/1", "collection": "somewhat_right"},
                {"title": "House speaker demands hard-line policies during border visit", "url": "http://example.com/2",
                 "collection": "mostly_right"},
                {"title": "Rise in Americans citing foreign policy as a top issue", "url": "http://example.com/3",
                 "collection": "somewhat_right"},
                {"title": "MORRISEY: As Political Persecution Ramps Up, West Virginia Has Trump’s Back",
                 "url": "http://example.com/4", "collection": "somewhat_right"}
            ]
        },
        {
            "name": "VICTOR JOECKS: Biden’s priority is power, not democracy",
            "article_counts": 5,
            "articles": [
                {"title": "VICTOR JOECKS: Biden’s priority is power, not democracy", "url": "http://example.com/0",
                 "collection": "somewhat_right"},
                {"title": "Donald Trump and Republicans want to downplay Jan. 6. It's going to be a big issue anyway.",
                 "url": "http://example.com/1", "collection": "somewhat_left"},
                {
                    "title": "Trump appeals Maine ruling barring him from ballot under the Constitution’s insurrection clause",
                    "url": "http://example.com/2", "collection": "mostly_right"},
                {"title": "Colorado voters call on U.S. Supreme Court to determine Donald Trump’s ballot eligibility",
                 "url": "http://example.com/3", "collection": "somewhat_right"},
                {"title": "Stuart Varney: The voters who put Biden in the White House are turning on him",
                 "url": "http://example.com/4", "collection": "somewhat_left"}
            ]
        },
        {
            "name": "MSNBC host grows emotional, draws tissue on Jan. 6 riot anniversary",
            "article_counts": 5,
            "articles": [
                {"title": "MSNBC host grows emotional, draws tissue on Jan. 6 riot anniversary",
                 "url": "http://example.com/0", "collection": "somewhat_right"},
                {"title": "Are presidential elections good or bad for California’s economy?",
                 "url": "http://example.com/1", "collection": "somewhat_left"},
                {"title": "Supreme Court allows Idaho to enforce its strict abortion ban, even in medical emergencies",
                 "url": "http://example.com/2", "collection": "center"},
                {"title": "'Rip us limb from limb': House Dem releases footage of 'close encounter' with J6 rioters",
                 "url": "http://example.com/3", "collection": "center"},
                {
                    "title": "NH Gov. Chris Sununu predicts Haley primary win, ‘strong second’ in Iowa as race for GOP nom heats up",
                    "url": "http://example.com/4", "collection": "mostly_left"}
            ]
        },
        {
            "name": "Trump barely mentions Jan. 6 on third anniversary of assault on the Capitol",
            "article_counts": 5,
            "articles": [
                {"title": "Trump barely mentions Jan. 6 on third anniversary of assault on the Capitol",
                 "url": "http://example.com/0", "collection": "center"},
                {"title": "Only DeSantis and Haley Will Face Off at Next GOP Debate as Rankings Flip",
                 "url": "http://example.com/1", "collection": "mostly_right"},
                {"title": "Biden and Trump Face-Off in Jan. 6 Anniversary Rally Cries", "url": "http://example.com/2",
                 "collection": "mostly_right"},
                {"title": "RUBEN NAVARRETTE JR.: By hiring migrants, Americans made a mess at the border",
                 "url": "http://example.com/3", "collection": "somewhat_left"},
                {"title": "GOP contenders spend a hectic weekend in Iowa as caucuses draw near",
                 "url": "http://example.com/4", "collection": "mostly_left"}
            ]
        },
        {
            "name": "Supreme Court allows Idaho to enforce its strict abortion ban",
            "article_counts": 5,
            "articles": [
                {"title": "Supreme Court allows Idaho to enforce its strict abortion ban",
                 "url": "http://example.com/0", "collection": "mostly_left"},
                {"title": "Donald Trump returns to Iowa with big lead in caucus polls", "url": "http://example.com/1",
                 "collection": "mostly_right"},
                {"title": "Congressional leaders say they've reached agreement on government funding",
                 "url": "http://example.com/2", "collection": "mostly_right"},
                {"title": "Newly released Jan 6 video from Capitol attack shows GOP lawmakers scolding rioters",
                 "url": "http://example.com/3", "collection": "center"},
                {"title": "Ron DeSantis says Jan. 6 wouldn’t have happened if he were President",
                 "url": "http://example.com/4", "collection": "somewhat_left"}
            ]
        },
        {
            "name": "Potential rematch between Biden and Trump in 2024 could shake up American politics",
            "article_counts": 5,
            "articles": [
                {"title": "VICTOR JOECKS: Biden’s priority is power, not democracy", "url": "http://example.com/0",
                 "collection": "mostly_right"},
                {"title": "Not a Good Week for Nikki Haley", "url": "http://example.com/1", "collection": "center"},
                {"title": "Potential rematch between Biden and Trump in 2024 could shake up American politics",
                 "url": "http://example.com/2", "collection": "somewhat_left"},
                {"title": "Trump cannot legally qualify for Nevada’s 2024 primary ballot",
                 "url": "http://example.com/3", "collection": "mostly_right"},
                {
                    "title": "She's a school board 'warrior'. He chairs the Florida GOP. A threesome revelation and rape claim threaten their futures",
                    "url": "http://example.com/4", "collection": "mostly_left"}
            ]
        },
        {
            "name": "New January 6 footage shows tense exchange between GOP congressmen and Capitol rioters",
            "article_counts": 5,
            "articles": [
                {"title": "New January 6 footage shows tense exchange between GOP congressmen and Capitol rioters",
                 "url": "http://example.com/0", "collection": "mostly_right"},
                {"title": "Congressional leaders announce funding deal to avoid government shutdown",
                 "url": "http://example.com/1", "collection": "mostly_left"},
                {"title": "JOHNSON FAVOR: Was the State of the Union scheduled to help Trump?",
                 "url": "http://example.com/2", "collection": "somewhat_right"},
                {"title": "Can Democrats bounce back in North Carolina after 2023 'gut punch'?",
                 "url": "http://example.com/3", "collection": "somewhat_right"},
                {"title": "Things to know about a school shooting in the small Iowa town of Perry",
                 "url": "http://example.com/4", "collection": "mostly_right"}
            ]
        },
        {
            "name": "The Jan. 6 Capitol riot gave ‘new courage to white supremacists,’ activists say",
            "article_counts": 5,
            "articles": [
                {"title": "The Jan. 6 Capitol riot gave ‘new courage to white supremacists,’ activists say",
                 "url": "http://example.com/0", "collection": "somewhat_right"},
                {"title": "Trump Signals an Election Year Full of Falsehoods on Jan. 6 and Democracy",
                 "url": "http://example.com/1", "collection": "center"},
                {"title": "Ramaswamy defends endorser, former U.S. Rep. Steve King", "url": "http://example.com/2",
                 "collection": "somewhat_right"},
                {"title": "Florida to be first state allowed to import prescription drugs from Canada",
                 "url": "http://example.com/3", "collection": "somewhat_left"},
                {"title": "\"This Is Not A Time For Us To Have A Mentally-Challenged President\"",
                 "url": "http://example.com/4", "collection": "mostly_right"}
            ]
        }
    ],
    "week 2": [
        {
            "name": "Over 4 Million Americans Roll Up Sleeves For Omicron-Targeted COVID Boosters",
            "article_counts": 10,
            "distribution": {"mostly_left": 2, "somewhat_left": 2, "center": 2, "somewhat_right": 2, "mostly_right": 2},
            "articles": [
                {"title": "Article 1", "url": "http://example.com/1", "collection": "mostly_left"},
                {"title": "Article 2", "url": "http://example.com/2", "collection": "somewhat_left"},
                {"title": "Article 3", "url": "http://example.com/3", "collection": "center"},
                {"title": "Article 4", "url": "http://example.com/4", "collection": "somewhat_right"},
                {"title": "Article 5", "url": "http://example.com/5", "collection": "mostly_right"},
                {"title": "Article 6", "url": "http://example.com/6", "collection": "mostly_left"},
                {"title": "Article 7", "url": "http://example.com/7", "collection": "somewhat_left"},
                {"title": "Article 8", "url": "http://example.com/8", "collection": "center"},
                {"title": "Article 9", "url": "http://example.com/9", "collection": "somewhat_right"},
                {"title": "Article 10", "url": "http://example.com/10", "collection": "mostly_right"}
            ]
        },
        {
            "name": "American Airlines Flyer Charged, Banned For Life After Punching Flight Attendant On Video",
            "article_counts": 20,
            "articles": [
                {"title": "Article 1", "url": "http://example.com/1", "collection": "mostly_left"},
                {"title": "Article 2", "url": "http://example.com/2", "collection": "somewhat_left"},
                {"title": "Article 3", "url": "http://example.com/3", "collection": "center"},
                {"title": "Article 4", "url": "http://example.com/4", "collection": "somewhat_right"},
                {"title": "Article 5", "url": "http://example.com/5", "collection": "mostly_right"},
                {"title": "Article 6", "url": "http://example.com/6", "collection": "mostly_left"},
                {"title": "Article 7", "url": "http://example.com/7", "collection": "somewhat_left"},
                {"title": "Article 8", "url": "http://example.com/8", "collection": "center"},
                {"title": "Article 9", "url": "http://example.com/9", "collection": "somewhat_right"},
                {"title": "Article 10", "url": "http://example.com/10", "collection": "mostly_right"},
                {"title": "Article 11", "url": "http://example.com/11", "collection": "mostly_left"},
                {"title": "Article 12", "url": "http://example.com/12", "collection": "somewhat_left"},
                {"title": "Article 13", "url": "http://example.com/13", "collection": "center"},
                {"title": "Article 14", "url": "http://example.com/14", "collection": "somewhat_right"},
                {"title": "Article 15", "url": "http://example.com/15", "collection": "mostly_right"},
                {"title": "Article 16", "url": "http://example.com/16", "collection": "mostly_left"},
                {"title": "Article 17", "url": "http://example.com/17", "collection": "somewhat_left"},
                {"title": "Article 18", "url": "http://example.com/18", "collection": "center"},
                {"title": "Article 19", "url": "http://example.com/19", "collection": "somewhat_right"},
                {"title": "Article 20", "url": "http://example.com/20", "collection": "mostly_right"}
            ]
        },
        {
            "name": "23 Of The Funniest Tweets About Cats And Dogs This Week (Sept. 17-23)",
            "article_counts": 15,
            "articles": [
                {"title": "Article 1", "url": "http://example.com/1", "collection": "mostly_left"},
                {"title": "Article 2", "url": "http://example.com/2", "collection": "somewhat_left"},
                {"title": "Article 3", "url": "http://example.com/3", "collection": "center"},
                {"title": "Article 4", "url": "http://example.com/4", "collection": "somewhat_right"},
                {"title": "Article 5", "url": "http://example.com/5", "collection": "mostly_right"},
                {"title": "Article 6", "url": "http://example.com/6", "collection": "mostly_left"},
                {"title": "Article 7", "url": "http://example.com/7", "collection": "somewhat_left"},
                {"title": "Article 8", "url": "http://example.com/8", "collection": "center"},
                {"title": "Article 9", "url": "http://example.com/9", "collection": "somewhat_right"},
                {"title": "Article 10", "url": "http://example.com/10", "collection": "mostly_right"},
                {"title": "Article 11", "url": "http://example.com/11", "collection": "mostly_left"},
                {"title": "Article 12", "url": "http://example.com/12", "collection": "somewhat_left"},
                {"title": "Article 13", "url": "http://example.com/13", "collection": "center"},
                {"title": "Article 14", "url": "http://example.com/14", "collection": "somewhat_right"},
                {"title": "Article 15", "url": "http://example.com/15", "collection": "mostly_right"}
            ]
        },
        {
            "name": "Woman Who Called Cops On Black Bird-Watcher Loses Lawsuit Against Ex-Employer",
            "article_counts": 12,
            "articles": [
                {"title": "Article 1", "url": "http://example.com/1", "collection": "mostly_left"},
                {"title": "Article 2", "url": "http://example.com/2", "collection": "somewhat_left"},
                {"title": "Article 3", "url": "http://example.com/3", "collection": "center"},
                {"title": "Article 4", "url": "http://example.com/4", "collection": "somewhat_right"},
                {"title": "Article 5", "url": "http://example.com/5", "collection": "mostly_right"},
                {"title": "Article 6", "url": "http://example.com/6", "collection": "mostly_left"},
                {"title": "Article 7", "url": "http://example.com/7", "collection": "somewhat_left"},
                {"title": "Article 8", "url": "http://example.com/8", "collection": "center"},
                {"title": "Article 9", "url": "http://example.com/9", "collection": "somewhat_right"},
                {"title": "Article 10", "url": "http://example.com/10", "collection": "mostly_right"},
                {"title": "Article 11", "url": "http://example.com/11", "collection": "mostly_left"},
                {"title": "Article 12", "url": "http://example.com/12", "collection": "somewhat_left"}
            ]
        },
        {
            "name": "Cleaner Was Dead In Belk Bathroom For 4 Days Before Body Found: Police",
            "article_counts": 18,
            "articles": [
                {"title": "Article 1", "url": "http://example.com/1", "collection": "mostly_left"},
                {"title": "Article 2", "url": "http://example.com/2", "collection": "somewhat_left"},
                {"title": "Article 3", "url": "http://example.com/3", "collection": "center"},
                {"title": "Article 4", "url": "http://example.com/4", "collection": "somewhat_right"},
                {"title": "Article 5", "url": "http://example.com/5", "collection": "mostly_right"},
                {"title": "Article 6", "url": "http://example.com/6", "collection": "mostly_left"},
                {"title": "Article 7", "url": "http://example.com/7", "collection": "somewhat_left"},
                {"title": "Article 8", "url": "http://example.com/8", "collection": "center"},
                {"title": "Article 9", "url": "http://example.com/9", "collection": "somewhat_right"},
                {"title": "Article 10", "url": "http://example.com/10", "collection": "mostly_right"},
                {"title": "Article 11", "url": "http://example.com/11", "collection": "mostly_left"},
                {"title": "Article 12", "url": "http://example.com/12", "collection": "somewhat_left"},
                {"title": "Article 13", "url": "http://example.com/13", "collection": "center"},
                {"title": "Article 14", "url": "http://example.com/14", "collection": "somewhat_right"},
                {"title": "Article 15", "url": "http://example.com/15", "collection": "mostly_right"},
                {"title": "Article 16", "url": "http://example.com/16", "collection": "mostly_left"},
                {"title": "Article 17", "url": "http://example.com/17", "collection": "somewhat_left"},
                {"title": "Article 18", "url": "http://example.com/18", "collection": "center"}
            ]
        },
        {
            "name": "Reporter Gets Adorable Surprise From Her Mom While Live On TV",
            "article_counts": 16,
            "articles": [
                {"title": "Article 1", "url": "http://example.com/1", "collection": "mostly_left"},
                {"title": "Article 2", "url": "http://example.com/2", "collection": "somewhat_left"},
                {"title": "Article 3", "url": "http://example.com/3", "collection": "center"},
                {"title": "Article 4", "url": "http://example.com/4", "collection": "somewhat_right"},
                {"title": "Article 5", "url": "http://example.com/5", "collection": "mostly_right"},
                {"title": "Article 6", "url": "http://example.com/6", "collection": "mostly_left"},
                {"title": "Article 7", "url": "http://example.com/7", "collection": "somewhat_left"},
                {"title": "Article 8", "url": "http://example.com/8", "collection": "center"},
                {"title": "Article 9", "url": "http://example.com/9", "collection": "somewhat_right"},
                {"title": "Article 10", "url": "http://example.com/10", "collection": "mostly_right"},
                {"title": "Article 11", "url": "http://example.com/11", "collection": "mostly_left"},
                {"title": "Article 12", "url": "http://example.com/12", "collection": "somewhat_left"},
                {"title": "Article 13", "url": "http://example.com/13", "collection": "center"},
                {"title": "Article 14", "url": "http://example.com/14", "collection": "somewhat_right"},
                {"title": "Article 15", "url": "http://example.com/15", "collection": "mostly_right"},
                {"title": "Article 16", "url": "http://example.com/16", "collection": "mostly_left"}
            ]
        },
        {
            "name": "How A New Documentary Captures The Complexity Of Being A Child Of Immigrants",
            "article_counts": 14,
            "articles": [
                {"title": "Article 1", "url": "http://example.com/1", "collection": "mostly_left"},
                {"title": "Article 2", "url": "http://example.com/2", "collection": "somewhat_left"},
                {"title": "Article 3", "url": "http://example.com/3", "collection": "center"},
                {"title": "Article 4", "url": "http://example.com/4", "collection": "somewhat_right"},
                {"title": "Article 5", "url": "http://example.com/5", "collection": "mostly_right"},
                {"title": "Article 6", "url": "http://example.com/6", "collection": "mostly_left"},
                {"title": "Article 7", "url": "http://example.com/7", "collection": "somewhat_left"},
                {"title": "Article 8", "url": "http://example.com/8", "collection": "center"},
                {"title": "Article 9", "url": "http://example.com/9", "collection": "somewhat_right"},
                {"title": "Article 10", "url": "http://example.com/10", "collection": "mostly_right"},
                {"title": "Article 11", "url": "http://example.com/11", "collection": "mostly_left"},
                {"title": "Article 12", "url": "http://example.com/12", "collection": "somewhat_left"},
                {"title": "Article 13", "url": "http://example.com/13", "collection": "center"},
                {"title": "Article 14", "url": "http://example.com/14", "collection": "somewhat_right"}
            ]
        },
        {
            "name": "Biden At UN To Call Russian War An Affront To Body's Charter",
            "article_counts": 11,
            "articles": [
                {"title": "Article 1", "url": "http://example.com/1", "collection": "mostly_left"},
                {"title": "Article 2", "url": "http://example.com/2", "collection": "somewhat_left"},
                {"title": "Article 3", "url": "http://example.com/3", "collection": "center"},
                {"title": "Article 4", "url": "http://example.com/4", "collection": "somewhat_right"},
                {"title": "Article 5", "url": "http://example.com/5", "collection": "mostly_right"},
                {"title": "Article 6", "url": "http://example.com/6", "collection": "mostly_left"},
                {"title": "Article 7", "url": "http://example.com/7", "collection": "somewhat_left"},
                {"title": "Article 8", "url": "http://example.com/8", "collection": "center"},
                {"title": "Article 9", "url": "http://example.com/9", "collection": "somewhat_right"},
                {"title": "Article 10", "url": "http://example.com/10", "collection": "mostly_right"},
                {"title": "Article 11", "url": "http://example.com/11", "collection": "mostly_left"}
            ]
        },
        {
            "name": "World Cup Captains Want To Wear Rainbow Armbands In Qatar",
            "article_counts": 17,
            "articles": [
                {"title": "Article 1", "url": "http://example.com/1", "collection": "mostly_left"},
                {"title": "Article 2", "url": "http://example.com/2", "collection": "somewhat_left"},
                {"title": "Article 3", "url": "http://example.com/3", "collection": "center"},
                {"title": "Article 4", "url": "http://example.com/4", "collection": "somewhat_right"},
                {"title": "Article 5", "url": "http://example.com/5", "collection": "mostly_right"},
                {"title": "Article 6", "url": "http://example.com/6", "collection": "mostly_left"},
                {"title": "Article 7", "url": "http://example.com/7", "collection": "somewhat_left"},
                {"title": "Article 8", "url": "http://example.com/8", "collection": "center"},
                {"title": "Article 9", "url": "http://example.com/9", "collection": "somewhat_right"},
                {"title": "Article 10", "url": "http://example.com/10", "collection": "mostly_right"},
                {"title": "Article 11", "url": "http://example.com/11", "collection": "mostly_left"},
                {"title": "Article 12", "url": "http://example.com/12", "collection": "somewhat_left"},
                {"title": "Article 13", "url": "http://example.com/13", "collection": "center"},
                {"title": "Article 14", "url": "http://example.com/14", "collection": "somewhat_right"},
                {"title": "Article 15", "url": "http://example.com/15", "collection": "mostly_right"},
                {"title": "Article 16", "url": "http://example.com/16", "collection": "mostly_left"},
                {"title": "Article 17", "url": "http://example.com/17", "collection": "somewhat_left"}
            ]
        },
        {
            "name": "Man Sets Himself On Fire In Apparent Protest Of Funeral For Japan's Abe",
            "article_counts": 13,
            "articles": [
                {"title": "Article 1", "url": "http://example.com/1", "collection": "mostly_left"},
                {"title": "Article 2", "url": "http://example.com/2", "collection": "somewhat_left"},
                {"title": "Article 3", "url": "http://example.com/3", "collection": "center"},
                {"title": "Article 4", "url": "http://example.com/4", "collection": "somewhat_right"},
                {"title": "Article 5", "url": "http://example.com/5", "collection": "mostly_right"},
                {"title": "Article 6", "url": "http://example.com/6", "collection": "mostly_left"},
                {"title": "Article 7", "url": "http://example.com/7", "collection": "somewhat_left"},
                {"title": "Article 8", "url": "http://example.com/8", "collection": "center"},
                {"title": "Article 9", "url": "http://example.com/9", "collection": "somewhat_right"},
                {"title": "Article 10", "url": "http://example.com/10", "collection": "mostly_right"},
                {"title": "Article 11", "url": "http://example.com/11", "collection": "mostly_left"},
                {"title": "Article 12", "url": "http://example.com/12", "collection": "somewhat_left"},
                {"title": "Article 13", "url": "http://example.com/13", "collection": "center"}
            ]
        }
    ]
}


group_colors = {
    "mostly left": "#4E79A7",
    "somewhat left": "#5FA2CE",
    "center": "#9467BD",
    "somewhat right": "#FF9D9A",
    "mostly right": "#E15759"
}