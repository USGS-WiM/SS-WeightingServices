import warnings
import math
from coefficient_table import crossCorrelationCoefficientTable
from hydrologic_region_table import hydrologicRegionsTable

#Returns cross-correlation coefficients between residuals for combinations of different estimation methods
#Values come from Table 6 https://pubs.usgs.gov/sir/2020/5142/sir20205142.pdf
def getCrossCorrelationCoefficient(regressionRegionCode, code1, code2):
    #regressionRegionCode is the string code for the Regression Region, ex. "GC1829"
    #code1, code2 ares the string codes that describes the flow statistic for the estimation methods, ex. "ACPK0_2AEP", which represents "Active Channel Width 0.2-percent AEP flood"

    if code1 == code2:
        raise Exception("code1 and code2 must be different")

    #Determine hydrologic region that contains this Regression Region
    hydrologicRegionName = None
    for hydrologicRegion, regressionRegionCodes in hydrologicRegionsTable.items():
        if regressionRegionCode in regressionRegionCodes:
            hydrologicRegionName = hydrologicRegion
    if hydrologicRegionName == None:
        raise Exception("Regression region code not valid")

    #Determine method for each code: "BC" (basin characteristic), "AC" (active channel), "BF" (bankfull width), or "RS" (remote sensing)
    methodCode1 = code1[:2]
    methodCode2 = code2[:2]
    if methodCode1 == "PK":
        methodCode1 = "BC"
    if methodCode2 == "PK":
        methodCode2 = "BC"
    validMethodCodes = ["BC", "AC", "BF", "RS"]
    if methodCode1 not in validMethodCodes :
        raise Exception("Method in code1 not valid")
    if methodCode2 not in validMethodCodes:
        raise Exception("Method in code2 not valid")
    if methodCode1 == methodCode2:
        raise Exception("Method codes must be different")

    #Determine AEP: a string to describe the peak-flow discharge with annual exceedance probability, ex. "Q42.9"
    isDigitsCode1 = [x.isdigit() for x in code1]
    firstDigitIndexCode1 = isDigitsCode1.index(True)
    lastDigitIndexCode1 = len(isDigitsCode1) - isDigitsCode1[::-1].index(True) - 1
    
    isDigitsCode2 = [x.isdigit() for x in code2]
    firstDigitIndexCode2 = isDigitsCode2.index(True)
    lastDigitIndexCode2 = len(isDigitsCode2) - isDigitsCode2[::-1].index(True) - 1

    if code1[firstDigitIndexCode1:lastDigitIndexCode1+1] == code2[firstDigitIndexCode2:lastDigitIndexCode2+1]:
        AEP = "Q" + code1[firstDigitIndexCode1:lastDigitIndexCode1+1].replace("_", ".") 
    else:
        raise Exception("AEP value must be the same for both flow statistics")

    #Return the coefficient from the table
    try:
        coefficient = crossCorrelationCoefficientTable[hydrologicRegionName][methodCode1 + "," + methodCode2][AEP]
    except:
        try:
            coefficient = crossCorrelationCoefficientTable[hydrologicRegionName][methodCode2 + "," + methodCode1][AEP]
        except:
            raise Exception("Coefficient could not be determined")
    finally: 
        return coefficient

def weightEst2(x1, x2, SEP1, SEP2, regressionRegionCode, code1, code2):
    #x1, x2 are input estimates
	#SEP1, SEP2 are input SEPs
	#regressionRegionCode is the string code for the Regression Region, ex. "GC1829"
    #code1, code2 ares the string codes that describes the flow statistic for the estimation methods, ex. "ACPK0_2AEP", which represents "Active Channel Width 0.2-percent AEP flood"

    x1 = math.log10(x1)
    x2 = math.log10(x2)
    SEP1 = math.log10(SEP1)
    SEP2 = math.log10(SEP2)

    r12 = getCrossCorrelationCoefficient(regressionRegionCode, code1, code2)

    #Sanity checks
    if((SEP1 <= 0) | (SEP2 <= 0)):
        raise ValueError("All SEP values must be greater than zero")

    S12 = r12*(SEP1*SEP2) 

    a1 = (SEP2**2 - S12) / (SEP1**2 + SEP2**2 - 2*S12)
    a2 = 1-a1

    Z = 10 ** (a1*x1 + a2*x2) #EQ 11
    SEPZ = 10 ** (((SEP1**2*SEP2**2 - S12**2) / (SEP1**2 + SEP2**2 - 2*S12))**0.5) #EQ 12

    #Check for estimate outside input bounds
    if ((Z < min(x1, x2)) | (Z > max(x1, x2))):
        warnings.warn("Weighted value is outside the range of input values. This can occur when the input estimates are highly correlated.")

    return((Z, SEPZ)) #Returns weighted estimate Z, and associated SEP


def weightEst3(x1, x2, x3, SEP1, SEP2, SEP3, regressionRegionCode, code1, code2, code3):
    #x1, x2, x3 are input estimates
	#SEP1, SEP2, SEP3 are input SEPs
    #regressionRegionCode is the string code for the Regression Region, ex. "GC1829"
    #code1, code2, code3 ares the string codes that describes the flow statistic for the estimation methods, ex. "ACPK0_2AEP", which represents "Active Channel Width 0.2-percent AEP flood"

    x1 = math.log10(x1)
    x2 = math.log10(x2)
    x3 = math.log10(x3)
    SEP1 = math.log10(SEP1)
    SEP2 = math.log10(SEP2)
    SEP3 = math.log10(SEP3)

    r12 = getCrossCorrelationCoefficient(regressionRegionCode, code1, code2)
    r13 = getCrossCorrelationCoefficient(regressionRegionCode, code1, code3)
    r23 = getCrossCorrelationCoefficient(regressionRegionCode, code2, code3)

    #Sanity checks
    if((SEP1 <= 0) | (SEP2 <= 0) | (SEP3 <= 0)):
        raise ValueError("All SEP values must be greater than zero")

    S12 = r12*(SEP1*SEP2) 
    S13 = r13*(SEP1*SEP3)
    S23 = r23*(SEP2*SEP3)

    A = SEP1**2 + SEP3**2 - 2*S13
    B = SEP3**2 + S12 - S13 - S23
    C = SEP2**2 + SEP3**2 - 2*S23

    a1 = (C*(SEP3**2 - S13) - B*(SEP3**2 - S23)) / (A*C - B**2) #EQ 6
    a2 = (A*(SEP3**2 - S23) - B*(SEP3**2 - S13)) / (A*C - B**2) #EQ 7
    a3 = 1 - a1 - a2 #EQ 8

    Z = 10 ** (a1*x1 + a2*x2 + a3*x3) #EQ 5

    #Check for estimate outside input bounds
    if ((Z < min(x1, x2, x3)) | (Z > max(x1, x2, x3))):
        warnings.warn("Weighted value is outside the range of input values. This can occur when the input estimates are highly correlated.")
                                
    SEPZ = 10 ** (((a1*SEP1)**2 + (a2*SEP2)**2 + (a3*SEP3)**2 + 2*a1*a2*S12 + 2*a1*a3*S13 + 2*a2*a3*S23)**0.5) #EQ 10

    return((Z, SEPZ)) #Returns weighted estimate Z, and associated SEP
