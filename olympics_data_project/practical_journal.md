# Beginning of Project Diary

## 27/05/25
- Answered questions and worked further with pandas

## 30/05/25
- Answered more questions and completing activities A

# Questions

## Activities A

1. Each column represents these things: ID (ID), Name (Name), Sex (Biological Gender), Age (Age), Height (Height), Weight (Weight), Team (Their team in the olympics), NOC (Their team's country), Games (Which olympics games they played in), Year (The year the games were played in), Season (Summer or Winter olympics), City (Olympics City), Sport (The sport they played), Event (The event they were in), Medal (The medal they won).
2. Inputs:
- ID, Name, Sex, Age, Height, Weight, Team, NOC, Year
3. Outputs:
- Games, Season, City, Sport, Event, Medal
4. We could explore questions about the ability of people based on class (weight, age, etc...) and how that has changed through time.
5. Find and describe six real-life data examples (Example, Source, Why It’s Collected, Who Uses It):
- Student Arrival Time, School App, Check for constant tardiness, Schools & Parents
- Nutritional Info, Nutrition Label, Plan for health in meals, Parents & Chefs
- Character Stats for a game, Game code, create guides and builds, Players
- Population, Head count, create census data, government
- Local Plant Health, plant monitors, to help plants who need it, ecologists
- Endangered Animal Count, head count & cameras, to help them survive & keep safe, ecologists
6. What’s one real-world benefit of analysing data?
- To create ideas of problems and how they can be solved
7. What’s one thing you didn’t realise was data until now?
- Social Media statistics
8. If you could collect data on anything, what would it be and why?
- Future Stock Market trends (yes future)

## Activities B & C

1. How many columns are in the dataset?
15
2. Name 3 of them and explain what they represent.
- Name; Competitor name
- Sex; Biological Gender
- Age; THEIR AGE
3. What do the first 5 rows show?
- The results for these competitors in their individual sports: A Dijiang, A Lamusi, Gunnar Nielsen Aaby, Edgar Lindenau Aabye, Christine Jacoba Aaftink
4. What are the top 5 sports?
- Athletics, Gymnastics, Swimming, Shooting, Cycling
5. How many male vs female athletes?
- M; 196594, F; 74522

6. What’s the average age?
- 25.5 yrs old
7. What’s the oldest and youngest athlete?
- 10-97 yrs old
8. Are there any columns with missing or strange values?
- someone being 25kg. someone being 97 yrs old.
9. Research what three of the lesser-known codes stand for:
- MRI; Mauritius...SAM; Samoa...TOG; Togo

## Activities D

1. What do these filters do?
- These filters create 2 new dataframes, 1 for female people only, the other for people over 35 yrs old.
2. How many rows were returned?
- female_athletes; 74522...older_athletes; 16384
3. Write a filter for athletes from Australia in Swimming
- australian_swimmers = df[(df['Team'] == 'Australia') & (df['Sport'] == 'Swimming')]
4. Sort by Height then Weight and display top 10.
- Sorting by weight would negate the whole height sort? But here:
- sorted_by_height = df.sort_values(by='height', ascending=False)
- sorted_by_weight = sorted_by_height.sort_values(by='weight', ascending=False)
- print(sorted_by_weight['Name'].head(10))
5. Which sport had the most female participants?
- Athletics

## Activities E

1. Create a new group that shows average weight by Sex and Sport
- 