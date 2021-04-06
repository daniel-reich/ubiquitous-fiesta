
staircase=lambda n,k=1:'#'*k if n==k else'_'*(n-k)+'#'*k+'\n'+staircase(n,k+1)if n>0else'_'*(k-1)+'#'if n==-k else'_'*(k-1)+'#'*(-n-k+1)+'\n'+staircase(n,k+1)

