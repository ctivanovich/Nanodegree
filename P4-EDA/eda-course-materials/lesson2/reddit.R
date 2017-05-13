setwd("C:/Users/Christopher/OneDrive/Nanodegree/P4-EDA/eda-course-materials/lesson2")
reddit <- read.csv(file = "reddit.csv")
table(reddit$gender)
summary(reddit)
nrow(reddit)
str(reddit$age.range)


library("ggplot2")
levels <- c("Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 or Above")
reddit$age.range <- factor(reddit$age.range,levels = levels, ordered = TRUE)
qplot(data=reddit, x=age.range)
