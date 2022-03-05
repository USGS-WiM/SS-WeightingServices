import warnings
from coefficient_table import crossCorrelationCoefficientTable
from hydrologic_region_table import hydrologicRegionsTable

#Returns cross-correlation coefficients between residuals for combinations of different estimation methods
#Values come from Table 6 https://pubs.usgs.gov/sir/2020/5142/sir20205142.pdf
def getCrossCorrelationCoefficient(regressionRegionCode, method, AEP):
    #regressionRegionCode is the string code for the Regression Region, ex. "GC1829"
    #method is a string to describe the combination of estimation methods, ex. "rBC,Wac"
    #AEP is a string to describe the peak-flow discharge with annual exceedance probability, ex. "Q42.9"

    #Find the hydrologic region that contains this Regression Region
    hydrologicRegionName = None
    for hydrologicRegion, regressionRegionCodes in hydrologicRegionsTable.items():
        if regressionRegionCode in regressionRegionCodes:
            hydrologicRegionName = hydrologicRegion

    return(crossCorrelationCoefficientTable[hydrologicRegionName][method][AEP])

def weightEst2(x1, x2, SEP1, SEP2, regressionRegionCode, method, AEP):
    #x1, x2 are input estimates in log units
	#SEP1, SEP2 are input SEPs in log units
	#regressionRegionCode is the string code for the Regression Region, ex. "GC1829"
    #method is a string to describe the combination of estimation methods, ex. "rBC,Wac"
    #AEP is a string to describe the peak-flow discharge with annual exceedance probability, ex. "Q42.9"

    r12 = crossCorrelationCoefficientTable[regressionRegionCode][method][AEP] 

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


def weightEst3(x1, x2, x3, SEP1, SEP2, SEP3, regressionRegionCode, method1, method2, method3, AEP):
    #x1, x2, x3 are input estimates in log units
	#SEP1, SEP2, SEP3 are input SEPs in log units
	#regressionRegionCode is the string code for the Regression Region, ex. "GC1829"
    #method1, method2, method3 are strings to describe the combination of estimation methods, ex. "rBC,Wac"
    #AEP is a string to describe the peak-flow discharge with annual exceedance probability, ex. "Q42.9"

    r12 = crossCorrelationCoefficientTable[regressionRegionCode][method1][AEP] 
    r13 = crossCorrelationCoefficientTable[regressionRegionCode][method2][AEP] 
    r23 = crossCorrelationCoefficientTable[regressionRegionCode][method3][AEP] 

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
