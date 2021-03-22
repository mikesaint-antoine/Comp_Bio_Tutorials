

close all
clear all
clc



tend = 1000;

k_1 = 2;
gamma_1 = 0.1;
k_2 = 2;
gamma_2 = 0.1;
k_3 = 2;
gamma_3 = 0.1;
n = 9;
c = 1;

t(1) = 0;
G1(1) = 0;
G2(1) = 0;
G3(1) = 0;


i = 1;


while t(end) < tend
    
    rates = zeros(1,6);
    
    rates(1) = (c^n / (c^n + G3(i)^n)) * k_1;
    rates(2) = gamma_1 * G1(i);
    
    rates(3) = (G1(i)^n / (c^n + G2(i)^n)) * k_2;
    rates(4) = gamma_2 * G2(i);
    
    rates(5) = (G2(i)^n / (c^n + G2(i)^n)) * k_3;
    rates(6) = gamma_3 * G3(i);
    
    
    rate_sum = sum(rates);
    
    
    r1 = rand(1);
    tau = (1/rate_sum) * log(1/r1);
    
    
    t(i+1) = t(i) + tau;
    
    
    r2 = rand(1);
    
    if r2*rate_sum <= rates(1)
        G1(i+1) = G1(i) + 1;
        G2(i+1) = G2(i);
        G3(i+1) = G3(i);
      
    elseif r2 * rate_sum > rates(1) && r2 * rate_sum <= rates(1) + rates(2)
        G1(i+1) = G1(i) - 1;
        G2(i+1) = G2(i);
        G3(i+1) = G3(i);            
        
    elseif r2 * rate_sum > rates(1) + rates(2) && r2 * rate_sum <= rates(1) + rates(2) + rates(3)
            G1(i+1) = G1(i);
            G2(i+1) = G2(i) + 1;
            G3(i+1) = G3(i);            
       
    elseif r2 * rate_sum > rates(1) + rates(2) + rates(3) && r2 * rate_sum <= rates(1) + rates(2) + rates(3) + rates(4)
        G1(i+1) = G1(i);
        G2(i+1) = G2(i) - 1;
        G3(i+1) = G3(i);            
 
        
    elseif r2 * rate_sum > rates(1) + rates(2) + rates(3) + rates(4) && r2 * rate_sum <= rates(1) + rates(2) + rates(3) + rates(4) + rates(5)
        G1(i+1) = G1(i);
        G2(i+1) = G2(i);        
        G3(i+1) = G3(i) + 1;
        
        
    elseif r2 * rate_sum > rates(1) + rates(2) + rates(3) + rates(4) + rates(5) && r2 * rate_sum <= rates(1) + rates(2) + rates(3) + rates(4) + rates(5) + rates(6)
        G1(i+1) = G1(i);
        G2(i+1) = G2(i);             
        G3(i+1) = G3(i) - 1;
        
        
        
    end
    
   
    i = i + 1;
    
    
    
end


subplot(3,1,1);
plot(t,G1)

subplot(3,1,2);
plot(t,G2)

subplot(3,1,3);
plot(t,G3)






