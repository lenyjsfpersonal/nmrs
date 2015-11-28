#This script automates calculation of reliability rate in the NMRS (N-Modular Redudancy with Spares) design

import math
N=3
S=4
T=17520
failure = (2.37266/1000000)
R = 0.959283
n=(N-1)/2
#print n

#power(R,N)
rpowern = math.pow(R,N)
#print rpowern

#for 1st part of summation in the curly bracket
##=============================================
i1=0
result_1st_part = 0
for i1 in range(i1,S):
    result_1st_part+= math.pow(N*failure*T,i1)/math.factorial(i1)
#print result_1st_part

#for 2nd part of summation in the curly bracket
##=============================================
temp01 = (2*n)-n
two_n_n = math.factorial(2*n)/math.factorial(n)*math.factorial(temp01)
#print two_n_n 

result_2nd_part = round(math.pow(N*failure*T,S)*math.pow(-1,N)/math.factorial(S)*two_n_n,6)
#print result_2nd_part

#for 3rd part of summation in the curly bracket
#================================================
#---3a
N_power_s = math.pow(N,S)
#print N_power_s
##---3b
i2=1
total_i_series = 0
for i2 in range(i2,n+1):
    N_minus_i = N - i2
    #print N_minus_i
    N_i = math.factorial(N)/(math.factorial(i2)*math.factorial(N_minus_i))
    #print N_i
    
    j1=1
    total_j_series=0
    for j1 in range(j1,i2+1):
        #*       
        i2_minus_j1 = i2 - j1
        i2_j1 = math.factorial(i2)/(math.factorial(j1)*math.factorial(i2_minus_j1))
        #print i2_j1
        
        #*
        power_i2_j1 = math.pow(-1,(i2-j1))
        #print power_i2_j1
        
        #*
        l1=1
        l_result=0
        for l1 in range(l1,S):
            l_result += math.pow((failure*T),l1)/math.factorial(l1)*math.pow(j1,S-l1)
        #print l_result
        super_long_result = 0   
        super_long_result = round((1/math.pow(j1,S))*(1/math.pow(R,j1)-1),6)-round(l_result,6)
        #print super_long_result
        
        total_j_series += i2_j1*power_i2_j1*super_long_result
        #print total_j_series
        
    total_i_series += total_j_series*N_i
    #print total_i_series

result_3rd_part = N_power_s*total_i_series

total_result = rpowern*(result_1st_part+result_2nd_part+result_3rd_part)

print 'N: %s,S: %d, T: %s, R:%r' %(N,S,T,total_result)


    

