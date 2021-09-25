close all
clear all
clc

alpha = 1.1;
beta = 0.4;
delta = 0.1;
gamma = 0.4;

params = [alpha; beta; delta; gamma];


y0 = [10; 1];

tspan = [0 50];


[t, y] = ode45(@(t,y)myODE(t,y,params), tspan, y0);


subplot(2,1,1);
plot(t,y(:,1));
xlabel('Time')
ylabel('Prey');

subplot(2,1,2);
plot(t,y(:,2));
xlabel('Time')
ylabel('Predators');









function dy = myODE(t,y,params)

    alpha = params(1);
    beta = params(2);
    delta = params(3);
    gamma = params(4);
    
    X = y(1);
    Y = y(2);
    
    dy = zeros(2,1);
    
    dy(1) = alpha * X - beta * X * Y;
    dy(2) = delta * X * Y - gamma * Y;
end