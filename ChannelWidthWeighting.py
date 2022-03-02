import warnings


def weightEst2(x1, x2, SEP1, SEP2, r12):
    #x1, x2 are input estimates in log units
	#SEP1, SEP2 are input SEPs in log units
	#r12 is correlation between the methods

    #Sanity checks
    if((SEP1 <= 0) | (SEP2 <= 0)):
        raise ValueError("All SEP values must be greater than zero")
    
    if(abs(r12) > 1):
        raise ValueError("Correlation coefficient values must be between -1 and 1")

    S12 = r12*(SEP1*SEP2) 

    a1 = (SEP2**2 - S12) / (SEP1**2 + SEP2**2 - 2*S12)
    a2 = 1-a1

    Z = a1*x1 + a2*x2 #EQ 11
    SEPZ = ((SEP1**2*SEP2**2 - S12**2) / (SEP1**2 + SEP2**2 - 2*S12))**0.5 #EQ 12

    #Check for estimate outside input bounds
    if ((Z < min(x1, x2)) | (Z > max(x1, x2))):
        warnings.warn("Weighted value is outside the range of input values. This can occur when the input estimates are highly correlated.")

    return((Z, SEPZ)) #Returns weighted estimate Z, and associated SEP


def weightEst3(x1, x2, x3, SEP1, SEP2, SEP3, r12, r13, r23):
    #x1, x2, x3 are input estimates in log units
	#SEP1, SEP2, SEP3 are input SEPs in log units
	#r12, r13, r23 are correlations between the methods

    #Sanity checks
    if((SEP1 <= 0) | (SEP2 <= 0) | (SEP3 <= 0)):
        raise ValueError("All SEP values must be greater than zero")

    if((abs(r12) > 1) | (abs(r12) > 1) | (abs(r12) > 1)):
        raise ValueError("Correlation coefficient values must be between -1 and 1")

    S12 = r12*(SEP1*SEP2) 
    S13 = r13*(SEP1*SEP3)
    S23 = r23*(SEP2*SEP3)

    A = SEP1**2 + SEP3**2 - 2*S13
    B = SEP3**2 + S12 - S13 - S23
    C = SEP2**2 + SEP3**2 - 2*S23

    a1 = (C*(SEP3**2 - S13) - B*(SEP3**2 - S23)) / (A*C - B**2) #EQ 6
    a2 = (A*(SEP3**2 - S23) - B*(SEP3**2 - S13)) / (A*C - B**2) #EQ 7
    a3 = 1 - a1 - a2 #EQ 8

    Z = a1*x1 + a2*x2 + a3*x3 #EQ 5

    #Check for estimate outside input bounds
    if ((Z < min(x1, x2, x3)) | (Z > max(x1, x2, x3))):
        warnings.warn("Weighted value is outside the range of input values. This can occur when the input estimates are highly correlated.")
                                
    SEPZ = ((a1*SEP1)**2 + (a2*SEP2)**2 + (a3*SEP3)**2 + 2*a1*a2*S12 + 2*a1*a3*S13 + 2*a2*a3*S23)**0.5 #EQ 10

    return((Z, SEPZ)) #Returns weighted estimate Z, and associated SEP
