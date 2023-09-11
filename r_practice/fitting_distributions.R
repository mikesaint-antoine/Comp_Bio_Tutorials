
rm(list=ls()) 

library(MASS)




########################################################################################
########################################################################################
# Normal Distribution


data <- read.csv("data/diner_quality.csv",header=0)


data <- unlist(as.vector(data))


fit <- fitdistr(data, "normal")

mean_fit <- fit$estimate["mean"]
sd_fit <- fit$estimate["sd"]



hist(data, breaks = 20, col = "lightblue", main = "Histogram of Data",
     xlab = "Data", ylab = "Frequency")

x <- seq(min(data), max(data), length = 100)
normal_curve <- dnorm(x, mean = mean_fit, sd = sd_fit)
normal_density <- dnorm(x, mean = mean_fit, sd = sd_fit)
scaled_density <- normal_density * length(data) * diff(hist(data, breaks = 20)$breaks[1:2])
lines(x, scaled_density, col = "red", lwd = 2)



########################################################################################
########################################################################################
# Log-Normal Distribution

data <- read.csv("data/pizza_shop_quality.csv",header=0)

data <- unlist(as.vector(data))

fit <- fitdistr(data, "lognormal")

meanlog_fit <- fit$estimate["meanlog"]
sdlog_fit <- fit$estimate["sdlog"]

hist(data, breaks = 100, col = "lightblue", main = "Histogram of Data",
     xlab = "Data", ylab = "Frequency")


x <- seq(min(data), max(data), length = 100)
lognormal_density <- dlnorm(x, meanlog = meanlog_fit, sdlog = sdlog_fit)
scaled_density <- lognormal_density * length(data) * diff(hist(data, breaks=100)$breaks[1:2])
lines(x, scaled_density, col = "red", lwd = 2)


########################################################################################
########################################################################################
# Poisson Distribution

data <- read.csv("data/customers_per_day.csv",header=0)

data <- unlist(as.vector(data))

fit <- fitdistr(data, "Poisson")


lambda_fit <- fit$estimate["lambda"]


hist(data, breaks = 20, col = "lightblue", main = "Histogram of Data",
     xlab = "Data", ylab = "Frequency")


x_pmf <- 0:max(data)
poisson_pmf <- dpois(x_pmf, lambda = lambda_fit)
points(x_pmf, poisson_pmf * length(data), col = "red", pch = 19)


