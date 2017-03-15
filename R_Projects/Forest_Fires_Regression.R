#import libraries dplyr and e1071

library(dplyr)
library(e1071)

#import data set forest fires to daa 

daa <- read.csv("forestfires.csv")
attach(daa)

#cleaning and transforming the data

dat <- daa[,-13:-17]
y <- c()
fun <- function(x)
{
  y <- c(y,ceiling(x))
}
ar <- lapply(area, fun)
ar <- as.numeric(ar)
ar <- as.factor(ar)
daa <- cbind(daa,ar)
daa = daa[,-13]
rm(ar)


#using svm for regression

s <- svm(ar~.,data=daa,cost=0.1,kernel="linear",scale = FALSE)


#predicting values of area

p <- predict(s,daa)


#plotting the graph for predicted and actual values 

plot(p,area,ylim=c(0,100))


#tuning the model for better predictions  

tun <- tune(svm,ar~.,data=daa,kernel="linear",scale=FALSE,ranges = list(cost=c(1.1,10,11.1)))
summary(tun)


#predicting with best model

pre <- predict(tun$best.model,daa)


#plotting the predicted and actual vaslues of area

plot(pre,area,ylim=c(0,100))


#add the predicted values to data set daa

daa <- cbind(daa,pre)



