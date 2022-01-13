%% simple_portfolio_data
n=20;
rng(5,'v5uniform');
pbar = ones(n,1)*.03+[rand(n-1,1); 0]*.12;
rng(5,'v5normal');
S = randn(n,n);
S = S'*S;
S = S/max(abs(diag(S)))*.2;
S(:,n) = zeros(n,1);
S(n,:) = zeros(n,1)';
x_unif = ones(n,1)/n;

%% writematrix(S,'S.txt')



rng(0,'v5uniform');
n=100;
m=300;
A=rand(m,n);
b=A*ones(n,1)/2;
c=-rand(n,1);
writematrix(A,'A.txt')

writematrix(b,'b.txt')

writematrix(c,'c.txt')