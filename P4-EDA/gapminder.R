library(dplyr)
library(tidyr)
library(ggplot2)
library(gridExtra)
getwd()
setwd("C:/Users/Christopher/Desktop/Nanodegree/P4-EDA")

billionaires <- read.csv("billionaires.csv",header = T)
extdebt <- read.csv('External Debt.csv', header=T)

colnames(billionaires)[1] <- "countries"
colnames(extdebt)[1] <- "countries"

df <- left_join(x=billionaires, 
            y=extdebt[,c("countries","X2004", "X2005", "X2006", "X2007")], 
            by="countries")

df2006 <- filter(df, X2006.x !=0 & !is.na(X2006.y))

p1 <- ggplot(data=df2006, aes(x=X2006.x, y=X2006.y)) +
  xlab("Billionaires per million 2006") +
  ylab("% External Debt") +
  geom_point() + xlim(c(0,1.1))

df2007 <- filter(df, X2007.x !=0 & !is.na(X2007.y))

p2 <- ggplot(data=df2007, aes(x=X2007.x, y=X2007.y)) +
  xlab("Billionaires per million 2007") +
  ylab("% External Debt") +
  geom_point() +
  xlim(c(0,1.1))

grid.arrange(p1,p2, nrow=1)

ggsave("billionaires per million vs external national debt.jpeg")
library(dplyr)
library(tidyr)
library(ggplot2)
library(gridExtra)
getwd()
setwd("C:/Users/Christopher/Desktop/Nanodegree/P4-EDA")

billionaires <- read.csv("billionaires.csv",header = T)
extdebt <- read.csv('External Debt.csv', header=T)

colnames(billionaires)[1] <- "countries"
colnames(extdebt)[1] <- "countries"

df <- left_join(x=billionaires, 
                y=extdebt[,c("countries","X2004", "X2005", "X2006", "X2007")], 
                by="countries")

df2006 <- filter(df, X2006.x !=0 & !is.na(X2006.y))

p1 <- ggplot(data=df2006, aes(x=X2006.x, y=X2006.y)) +
  xlab("Billionaires per million 2006") +
  ylab("% External Debt") +
  geom_point() + xlim(c(0,1.1))

df2007 <- filter(df, X2007.x !=0 & !is.na(X2007.y))

 
p2 <- ggplot(data=df2007, aes(x=X2007.x, y=X2007.y)) +
  xlab("Billionaires per million 2007") +
  ylab("% External Debt") +
  geom_point() + 
  #geom_text(aes(label=countries))
  xlim(c(0,1.1))

g <- arrangeGrob(p1, p2, nrow=1)

ggsave("billionaires per million vs external national debt.jpeg", g)

cor.test(df2006$X2006.x, df2006$X2006.y)
cor.test(df2007$X2007.x, df2007$X2007.y)
