
## Udacity DAND Data Visualization Project in Tableau

[Link to the Tableau Story early version](https://public.tableau.com/profile/christopher.ivan#!/vizhome/Pisa2012_1/Story1)

[Link to the Tableau Story FINAL version](https://public.tableau.com/profile/christopher.ivan#!/vizhome/Top-scoringAsiancitiesinthePISAdatasetFinalversion/Story1)


### Dataset: PISA 2012 educational dataset

#### by Christopher Ivanovich, 2017

#### Summation of Visualization
The aim of my visualization is to tell the story of what makes the 3 "Asian tiger" cities of Shanghai, Taipei, and Hong Kong distinct from other countries and cities in the PISA 2012 educational dataset. After release of the PISA survey data, media outlets all over the world hailed these three cities (Shanghai in particular) as beating the rest of the world in educational achievement. Doing data by data comparisons of these top cities with the more than 60 participating countries makes little sense, but that didn't stop the media or the home countries of these cities from gushing with excitment. I seek to show that these three cities have factors in common that differentiate them from the other geographic units in the dataset (including the nations to which these cities belong), as they have (especially within their countries) distinct characteristics apart from good scores, some of which we can infer to be cultural in nature (regarding the all-importance of test scores in the student social hierarchy and as a source of familial pride).

#### Design
I sought to tell a logically linear story about what I found to be an interesting feature of the PISA 2012 data set--the inclusion of a handful of cities in an otherwise national-level education study, and the fact that these cities almost all happen to be global top-performers in standardized testing. It struck me as additionally odd that three of the four cities in the entire data set (the top performings ones) are all held or claimed by China. The only other city, Perm, Russia, seemed strange and interesting as well, but because it breaks the pattern I opted to leave it for a possible separate analysis.

I decided to focus on the phenomenon of these cities' high test scores in relation to other features, in part because they famously received much applaud for those scores, and because Shanghai's performance in particular instigated a lot of hand-wringing and self-doubt among educational leaders in the West (the "What are we doing wrong? What can we learn from Shanghai's success?" self-questioning that received a great deal of coverage in the news). I looked for variables that seemed to distinguish these cities from other participants, such as number of hours spent in and out of class, wealth as the data set defines it (relative ownership of non-essentials like washing machines and cellphones), and the presence or absence of parents in the home--variables that might reasonably have some explanatory power for these scores. I also emphasize the fact that these cities are not proper representatives of their home countries, as they are all top economic powerhouses and enjoy concentrations of capital and educated citizens unmatched in other parts of their countries.

My first challenge was simply to highlight the cities as being distinct and separate from the bulk of the political units in the survey. I chose to open the Story with a map of participating locations, which visually clarifies that Shanghai, Taipei, and Hong Kong are just cities, being represented alongside entire countries. 

Then, for the presentation of my simple analysis, I sought to keep the distinction between these cities and all the other locations clear in the graphs with coloring and by creating distinct subsets, and then doing my subsequent analyses while maintaining that distinction as clearly as possible.

#### Feedback
- After receiving feedback about it being difficult to identify the cities of interest, I decided to center the map on that part of the world, zoomed in, and to state clearly in the text for that slide that Taipei and Shanghai are represented as circles in otherwise unrepresented countries, and to note the curiousness of only these cities being represented as well as the importance of their labelling in the data as belonging to China or the requirement that they in some way be labelled as Chinese when China itself is not in the data.
- The single most important feedback I received was that my story didn't seem to have much of a focus, so I sought to craft one as clearly as I could with the limited data (non-numeric survey items went mostly unanswered by this massive cohort, giving these items little power for drawing cross-border comparisons). This guided me towards the selection and creation of variables related to time spent inside and outside of the classroom studying, and time (and money, though it's only implicit) spent on extracurricular learning, particularly by limiting the creation of a summation variable of EC activities to only those that we can safely infer require money, such as attendance at a cram school, having a private tutor, and so on.
- More minor changes I've addressed in the final version after receiving feedback from a friend with a keen eye include:
    - The OECD/non-OECD variable was failing to display as a shape feature.
    - The text boxes overran the pages in the browser view of the published workbook. I changed them to caption slides to make for less distracting text.
    - Inaccurate description of an axis as representing the size of a class rather than as classes per week. I opted to include two charts in the same slide exploring both of these variables, as both are unusually high in the cities and generally track increasing scores well.
- Changes I've made of my own initiative include:
    - Inclusion of trend lines where useful.
    - Removal of Perm from the data, as the inclusion of another city not included in the cities group weakens city/country comparisons.

#### Resources
Most importantly, I spent a great deal of time consulting the PISA codebook to select and properly interpret the variables that were of interest to me. I also made of the [PISA Programme for International Student Assessment (PISA) PISA 2000 Technical Report: PISA 2000 Technical Report](https://books.google.com/books?id=IVdo5jhkgx4C&pg=RA1-PA66&lpg=RA1-PA66&dq=wealth+pisa+negative&source=bl&ots=UY98cTubXw&sig=vnTb7adUe41eVsBm-V_jc4eDzY8&hl=en&sa=X&ved=0ahUKEwjigdfvrbPOAhUKTSYKHRkiA2cQ6AEIHjAA#v=onepage&q=wealth%20pisa%20negative&f=false) (by Adams, Ray and Wu, Margaret: OECD Publishing, Jan 24, 2003). Though dated, this provided a clear explanation of the meaning and usefulness of the WEALTH variable in the dataset, which was not explained in the variable codebook. 

