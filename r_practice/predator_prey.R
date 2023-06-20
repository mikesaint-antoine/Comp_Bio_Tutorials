
## clear all
rm(list=ls()) 


X_init <- 10

Y_init <- 1

tend <- 50


a <- 1.1
b <- 0.4
c <- 0.1
h <- 0.4



X <- c(X_init)
Y <- c(Y_init)
t <- c(0)

delta_t <- 0.01


while(t[length(t)] < tend)
{
  
  current_X <- X[length(X)]
  current_Y <- Y[length(Y)]
  current_t <- t[length(t)]
  
  delta_X <- (a * current_X - b * current_X * current_Y) * delta_t
  next_X <- current_X + delta_X
  
  delta_Y <- (c * current_X * current_Y - h * current_Y) * delta_t
  next_Y <- current_Y + delta_Y
  
  
  next_t <- current_t + delta_t
  
  
  X <- append(X,next_X)
  Y <- append(Y,next_Y)
  t <- append(t,next_t)
  
  
}



par(mfrow = c(2, 1))
plot(x = t, y = X,
     xlab = "Time",
     ylab = "Prey"
)

plot(x = t, y = Y,
     xlab = "Time",
     ylab = "Predator"
)



#Phase space plot
par(mfrow = c(1, 1))
plot(x = X, y = Y,
     xlab = "Prey",
     ylab = "Predator"
)





