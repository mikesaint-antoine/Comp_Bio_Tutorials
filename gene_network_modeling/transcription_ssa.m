

close all
clear all
clc


tend = 100;

k = 2;
gamma = 0.1;


t(1) = 0;
X(1) = 0;
i = 1;


while t(end)< tend
   
    rates = zeros(1,2);
    rates(1) = k;
    rates(2) = gamma * X(i);
    
    rate_sum = sum(rates);
    
    
    r1 = rand(1);
    tau = (1/rate_sum)*log(1/r1);
    
    t(i+1) = t(i) + tau;
    
    
    r2 = rand(1);
    
    if r2*rate_sum <= rates(1)
        X(i+1) = X(i) + 1;
        
    else if r2 * rate_sum > rates(1) && r2 * rate_sum <= rates(1) + rates(2)
            X(i+1) = X(i) - 1;
        end 
    end
    
    
    
    i = i + 1;
    
    
end


plot(t,X)

