library(datasets)
library(ggplot2)
data("diamonds")
ggplot(data=diamonds, aes(x=log(price))) +
  geom_histogram(aes(color=cut)) +
  facet_wrap(~color)

ggplot(data=diamonds, aes(x=table,y=price)) +
  geom_point(aes(color=cut)) +
  scale_color_brewer(type = 'qual')

#note: graph naming conventions are Y vs X or dept vs indept
#so the above is price vs table

# Create a scatterplot of diamond price vs.
# volume (x * y * z) and color the points by
# the clarity of diamonds. Use scale on the y-axis
# to take the log10 of price. You should also
# omit the top 1% of diamond volumes from the plot.

diamonds$volume <- diamonds$x*diamonds$y*diamonds$z
ggplot(data=subset(diamonds, volume < quantile(diamonds$volume, .99)), 
       aes(x=volume, y=price)) +
  geom_point(aes(color=clarity)) +
  scale_y_log10() +
  scale_color_brewer(type = 'qual')

library(dplyr, tidyr)

setwd("C:/Users/Christopher/Desktop/Nanodegree/P4-EDA/eda-course-materials/")

pf <- read.csv("pseudo_facebook.tsv", sep = "\t")

pf$prop_initiated <- pf$friendships_initiated/pf$friend_count
# Create a line graph of the median proportion of
# friendships initiated ('prop_initiated') vs.
# tenure and color the line segment by
# year_joined.bucket.

# Recall, we created year_joined.bucket in Lesson 5
# by first creating year_joined from the variable tenure.
# Then, we used the cut function on year_joined to create
# four bins or cohorts of users.
ggplot(data=pf, aes(x=tenure, y=prop_initiated)) + 
  geom_line(aes(color=year_joined.bucket), 
            stat="summary", fun.y=median) + 
  geom_smooth()


group_by(subset(pf, !is.na(prop_initiated)), year_joined.bucket) %>% 
  summarize(mean_prop = mean(as.numeric(prop_initiated)))

# Create a scatter plot of the price/carat ratio
# of diamonds. The variable x should be
# assigned to cut. The points should be colored
# by diamond color, and the plot should be
# faceted by clarity.
ggplot(data=diamonds, aes(x=cut, y=price/carat)) + 
  geom_point(aes(color=color)) + 
  facet_wrap(~clarity) + 
  scale_color_brewer(type='div')


