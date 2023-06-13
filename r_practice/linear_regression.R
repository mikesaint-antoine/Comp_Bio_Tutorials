
## clear all
rm(list=ls()) 



# read in data
data <- read.csv("data/basketball_skills.csv")





# plot data
plot(x = data$height,y = data$basketball_skill,
     xlab = "Height (inches)",
     ylab = "Basketball Skill",
     xlim = c(min(data$height),max(data$height)),
     main = "Height vs Basketball Skill"
)


## easy way

model <- lm(data$basketball_skill ~ data$height)

fit_b <- model$coefficients[1]
fit_m <- model$coefficients[2]


fit_x <- seq(min(data$height),max(data$height),by=0.1)
fit_y <- fit_m * fit_x + fit_b

lines(fit_x, fit_y, col = "blue")


########################################################################


## loss function

loss_function <- function(m,b,xdata,ydata){
  loss <- 0
  
  for(i in 1:length(xdata)){
    
    predicted_y <- m * xdata[i] + b
    
    squared_res <- (predicted_y - ydata[i])**2
    
    loss <- loss + squared_res
    
  }
  
  return(loss)
  
}



# minimize loss function

for(count in 1:500000){
  
  m_guess <- runif(n=1, min=-20, max=20)
  b_guess <- runif(n=1, min=-20, max=20)
  
  current_loss <- loss_function(m=m_guess, b=b_guess, xdata=data$height, ydata=data$basketball_skill)
  
  if(count==1){
    best_loss <- current_loss
    best_m <- m_guess
    best_b <- b_guess
  }else if(current_loss < best_loss){
    best_loss <- current_loss
    best_m <- m_guess
    best_b <- b_guess
  }
  
}



## plot line
fit_x <- seq(min(data$height),max(data$height),by=0.1)
fit_y <- best_m * fit_x + best_b
lines(fit_x, fit_y, col = "red")


###

base_model_loss <- loss_function(m=0, b=mean(data$basketball_skill), xdata=data$height, ydata=data$basketball_skill)


r_squared <- 1 - (best_loss/base_model_loss)

