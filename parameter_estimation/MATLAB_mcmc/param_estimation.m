
%% read in CSV data

exp_data = csvread('cell_count_data.csv',1,0);

% plot(exp_data(:,1), exp_data(:,2))

%% MCMC

% first guess for params
params0 = [1;100];

% first loglikelihood
ll_init = ll_function(exp_data, params0);


% keeping track of params and LLs
paraset = [];
paraset = [paraset params0];

loglikelihoodset = [];
loglikelihoodset = [loglikelihoodset ll_init];

all_guesses = [];
all_guesses = [all_guesses params0];



run_num = 1000000;

for i = 2:run_num

    % keep track of progress
    if rem(i,100)==0
        i/run_num
    end


    paramtest = [random('Uniform',0,2); random('Uniform', 0,10000)];

    ll_test = ll_function(exp_data, paramtest);


    % Metropolis - Hastings
    if ll_test >= loglikelihoodset(end) + log(random('Uniform',0,1))
        loglikelihoodset = [loglikelihoodset ll_test];
        paraset = [paraset paramtest];
        all_guesses = [all_guesses paramtest];

    else
        loglikelihoodset = [loglikelihoodset loglikelihoodset(end)];
        paraset = [paraset paraset(:,end)];
        all_guesses = [all_guesses paramtest];        

    end

end

%% plots


figure
subplot(2,1,1);
histogram(all_guesses(1,:));
title('r Prior Distribution');

subplot(2,1,2);
histogram(paraset(1,:));
title('r Posterior Distribution');
xlabel('Parameter Value') ;
ylabel('Occurences'); 



figure
subplot(2,1,1);
histogram(all_guesses(2,:));
title('K Prior Distribution');

subplot(2,1,2);
histogram(paraset(2,:));
title('K Posterior Distribution');
xlabel('Parameter Value') ;
ylabel('Occurences'); 



%% functions to use

function [dxdt] = sim(t,x,theta)
% variable for cell counts
X = x(1);

r = theta(1); 
K = theta(2); 

dXdt = r*X * (1 - X/K);
dxdt = [dXdt];
end

function [out] = datagen(timepoints,theta)
[t,y] = ode23s(@sim, timepoints, [1],[],theta);

out = [t,sum(y,2)];
end




function [loglikelihood] = ll_function(data,theta)


[testdata] = datagen(data(:,1),theta);

loglikelihood = sum(log(pdf('Normal', data(:,2), testdata(:,2), 1000)));

end

